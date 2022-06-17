#! /bin/bash

echo "Installing setuptools..."
python3 -m pip install --user --upgrade setuptools wheel twine
echo "Installed setuptools, wheel and twine!"

echo "Removing dist files..."
rm -r dist/*
echo "Done!"

echo "Generating the distribution files..."
python3 setup.py sdist bdist_wheel
echo "Done!"

echo "Publishing the package to the TestPyPi..."
python3 -m twine upload --repository testpypi dist/* --verbose
echo "Published!"
