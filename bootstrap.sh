#!/usr/bin/env bash

echo 'TODO: build project'
python -m pip install --upgrade pip
python -m pip install --upgrade pip setuptools wheel pip-tools bpython coverage isort autoflake yapf
sudo apt-get install lynx direnv tor torsocks -y
python -m pip install --upgrade -r requirements.txt

# python -m pip install --upgrade pip requests httpx bs4 
# python -m pip install --upgrade 'requests[socks]'
# python -m pip install --upgrade 'httpx[socks]'

# python -m pip freeze > requirements.in
# pip-compile
   