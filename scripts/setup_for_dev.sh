#!/usr/bin/env bash

pip install virtualenv

echo "-> Creating virtualenv..."
virtualenv --setuptools --no-site-packages --prompt="(${PWD##*/}) " -p python .venv

echo "-> Activating virtualenv..."
source .venv/scripts/activate

echo "Upgrading and installing pip dependencies..."
pip install --upgrade setuptools
pip install --upgrade --requirement requirements/requirement.txt

deactivate
echo "-> Pip dependencies install complete!"

echo "Done!"