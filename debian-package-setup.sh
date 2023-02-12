#!/bin/bash
if [ "$EUID" -ne 0 ]
  then echo "Please run as root"
  exit
fi
echo "Installing the following packages via apt: libffi-dev libnacl-dev python3-dev"
echo "Press Ctrl+C if you don't want these packages"
sleep 5
apt install -y libffi-dev libnacl-dev python3-dev