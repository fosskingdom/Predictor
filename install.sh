#!/bin/bash -e

# https://github.com/TomSchimansky/CustomTkinter/wiki/Packaging#windows-pyinstaller-auto-py-to-exe

clear;

echo "> sudo apt update;";
sudo apt update;
echo;

apt list --upgradable -a;
echo;

echo "> sudo apt install gnuplot python3 xtitle -y;";
sudo apt install gnuplot python3 xtitle -y;
echo;

echo "> sudo apt autoremove -y;";
sudo apt autoremove -y;
echo;

if [ -f "./requirements.txt" ]; then
    python3 -m pip install -r requirements.txt;
    echo;
fi

echo "Identifying outdated modules...";
python3 -m pip list --outdated;
echo "Done...";
echo;

if [ -f "./checksums.txt" ]; then
    echo "Calculating checksums, Please wait..."
    sha256sum -c ./checksums.txt;
    echo;
fi

if [ -f "./constants.py" ]; then
    python3 -m isort ./constants.py;
    python3 -m black ./constants.py;
    python3 -m pylint ./constants.py;
fi

if [ -f "./__main__.py" ]; then
    python3 -m isort ./__main__.py;
    python3 -m black ./__main__.py;
    echo;
    python3 -m pylint ./__main__.py;
    pyinstaller ./__main__.py -n "Predictor" --add-data="./checksums.txt:./" --add-data="./mp3/*:./mp3/" --add-data="./docs/*:./docs/" --add-data="./assets/*:./assets/" --add-data="./venv/lib/python3.*/site-packages/customtkinter:./customtkinter" --add-data="./venv/lib/python3.*/site-packages/pyfiglet/fonts/*:./pyfiglet/fonts/" --hidden-import="PIL._tkinter_finder" --hidden-import="sklearn.metrics._pairwise_distances_reduction._datasets_pair" --hidden-import="sklearn.metrics._pairwise_distances_reduction._middle_term_computer" -Fy;
    echo;
fi

if [ -d "./build" ]; then
    rm -rv ./build;
    echo;
fi

if [ -d "./__pycache__" ]; then
    rm -rv ./__pycache__;
    echo;
fi

if [ -f "./Predictor.spec" ]; then
    rm -fv ./Predictor.spec;
    echo;
fi

if [ -f "./dist/Predictor" ]; then
    cd ./dist/
    sha256sum ./Predictor > ./Predictor.sha256
    strings ./Predictor > ./strings.txt
    echo "Installation Completed Successfully..."
    notify-send "Predictor, Installation Completed Successfully..."
fi

exit;
