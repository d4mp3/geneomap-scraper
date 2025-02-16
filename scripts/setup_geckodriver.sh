#!/bin/bash

wget https://github.com/mozilla/geckodriver/releases/download/v0.32.0/geckodriver-v0.32.0-linux64.tar.gz
tar xzvf geckodriver-v0.32.0-linux64.tar.gz
sudo mv geckodriver /usr/local/bin
sudo chmod +x /usr/local/bin/geckodriver
export TMPDIR=$HOME/snap/firefox/common/tmp
