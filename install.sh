#!/bin/bash


curl -O https://raw.githubusercontent.com/gwimtux/fraction-killer/main/main.py
mv main.py fractionkiller
chmod +x fractionkiller
sudo mv fractionkiller /usr/bin
