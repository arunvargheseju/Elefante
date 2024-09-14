#!/bin/bash
trap ctrl_c INT

function ctrl_c() {
	clear
        exit
}

if ! [ -x "$(command -v figlet)" ]; then
  echo 'Error: figlet is not installed.'
  echo 'Installing figlet'
  sudo apt-get install figlet
  clear
fi
if ! [ -x "$(command -v lolcat)" ]; then
  echo 'Error: lolcat is not installed.'
  echo 'Installing lolcat'
  sudo apt-get install lolcat
  clear
fi
if ! [ -x "$(command -v gnome-terminal)" ]; then
  echo 'Error: GNOME terminal is not installed.'
  echo 'Install and try again !'
  exit
fi
if ! [ -x "$(command -v pip)" ]; then
  echo 'Error: pip is not installed or not in path.'
  echo 'Install pip and try again !'
  exit
fi
pip install -r requirements.txt