#!/usr/bin/env bash

readonly DRIVER="chromedriver_mac64.zip"
readonly VERSION="2.27"

if [ ! -f "$DRIVER" ]; then
  wget https://chromedriver.storage.googleapis.com/${VERSION}/${DRIVER}
else
  echo "Already downloaded $DRIVER"
fi

if [ ! -f "driver/chromedriver" ]; then
  mkdir -p driver
  unzip -d driver ${DRIVER}
else
  echo "Already unpacked $DRIVER"
fi
