#!/usr/bin/env python

import re
import time
from os import path
from splinter import Browser

host = 'http://192.168.0.1'
selenium_driver = path.join(path.dirname(__file__), 'driver/chromedriver')

urls = {
    'login_page': host + '/',
    'login_form': host + '/goform/login'
}

login = {
    'user': 'admin',
    'pass': 'admin'
}


def run_splinter(browser):
    'Load login page...'
    browser.visit(urls['login_page'])
    browser.fill_form({
        'loginUsername': login['user'],
        'loginPassword': login['pass']
    })

    print 'Log in...'
    login_button = [b for b in browser.find_by_tag('button')
                    if b['type'] == 'submit'][0]
    login_button.click()
    time.sleep(0.25)

    if re.match('.*/login\.asp$', browser.url):
        print 'Force login...'
        login_button = [b for b in browser.find_by_tag('button')
                        if b['onclick'] and re.match('^userForceLogoff', b['onclick'])][0]
        login_button.click()

    if browser.is_element_not_present_by_css('a[href="/wireless/radio.asp"]', 1):
        raise Exception('Unable to identify login page.')

    print 'Navigate to wireless page...'
    wifi_button = browser.find_by_css('a[href="/wireless/radio.asp"]').first
    wifi_button.click()

    if browser.is_element_not_present_by_id('WirelessEnable', 1):
        raise Exception('Unable to identify wireless page.')

    print 'Turning off WiFi...'
    browser.select('WirelessEnable', '0')
    save_button = browser.find_by_id('CommitRadioSubmit').first
    save_button.click()
    time.sleep(0.25)

    print 'Log out...'
    logout_button = browser.find_by_css('a[href="/logout.asp"]').first
    logout_button.click()

    print 'Done!'
    browser.quit()


def main():
    browser = Browser('chrome', executable_path=selenium_driver)
    try:
        run_splinter(browser)
    except Exception as e:
        print e
    finally:
        browser.quit()

main()
