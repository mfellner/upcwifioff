import re
import time
from os import path
from tqdm import tqdm
from splinter import Browser

host = 'http://192.168.0.1'

urls = {
    'login_page': host + '/',
    'login_form': host + '/goform/login'
}

login = {
    'user': 'admin',
    'pass': 'admin'
}


def run_splinter(browser, pbar, set_wifi=0):
    tqdm.write('Load login page...')
    browser.visit(urls['login_page'])
    pbar.update(1)

    tqdm.write('Log in...')
    browser.fill_form({
        'loginUsername': login['user'],
        'loginPassword': login['pass']
    })
    login_button = [b for b in browser.find_by_tag('button')
                    if b['type'] == 'submit'][0]
    login_button.click()
    pbar.update(1)
    time.sleep(0.25)
    pbar.update(1)

    if re.match('.*/login\.asp$', browser.url):
        tqdm.write('Force login...')
        login_button = [b for b in browser.find_by_tag('button')
                        if b['onclick'] and re.match('^userForceLogoff', b['onclick'])][0]
        login_button.click()

    pbar.update(1)
    if browser.is_element_not_present_by_css('a[href="/wireless/radio.asp"]', 1):
        raise Exception('Unable to identify login page.')
    pbar.update(1)

    tqdm.write('Navigate to wireless page...')
    wifi_button = browser.find_by_css('a[href="/wireless/radio.asp"]').first
    wifi_button.click()
    pbar.update(1)

    if browser.is_element_not_present_by_id('WirelessEnable', 0):
        raise Exception('Unable to identify wireless page.')
    pbar.update(1)

    tqdm.write('Turning WiFi %s...' % ('on' if set_wifi else 'off'))
    browser.select('WirelessEnable', str(set_wifi))
    save_button = browser.find_by_id('CommitRadioSubmit').first
    save_button.click()
    pbar.update(1)
    time.sleep(0.25)
    pbar.update(1)

    tqdm.write('Log out...')
    logout_button = browser.find_by_css('a[href="/logout.asp"]').first
    logout_button.click()
    pbar.update(1)

    tqdm.write('Done!')


def main(driver_path):
    browser = Browser('phantomjs', executable_path=driver_path)
    try:
        with tqdm(total=10) as pbar:
            run_splinter(browser, pbar)
    except Exception as e:
        print e
    finally:
        browser.quit()
