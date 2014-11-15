#!/bin/bash

apt-get update
apt-get -y install build-essential libssl-dev openssl libsqlite3-dev
wget python.org/ftp/python/3.4.1/Python-3.4.1.tgz
tar -xzvf Python-3.4.1.tgz
cd Python-3.4.1/
./configure
make
make install
pip3.4 install -r /vagrant/requirements.txt