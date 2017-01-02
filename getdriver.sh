#!/usr/bin/env bash

readonly VERSION="2.1.1"
readonly ARTIFACT="phantomjs-$VERSION-macosx"
readonly ARCHIVE="$ARTIFACT.zip"
readonly URL="https://bitbucket.org/ariya/phantomjs/downloads/$ARCHIVE"
readonly DOWNLOAD_DIR="$PWD/driver"

mkdir -p ${DOWNLOAD_DIR}

if [ ! -f "$DOWNLOAD_DIR/$ARCHIVE" ]; then
  wget -P ${DOWNLOAD_DIR} ${URL}
else
  echo "Already downloaded $ARCHIVE"
fi

if [ ! -d "$DOWNLOAD_DIR/$ARTIFACT" ]; then
  unzip -d ${DOWNLOAD_DIR} ${DOWNLOAD_DIR}/${ARCHIVE}
else
  echo "Already unpacked $ARCHIVE"
fi
