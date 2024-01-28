#!/bin/sh
VENV_DIRPATH="./local_lib"
VENV_ACTIVATION_FILEPATH=$VENV_DIRPATH"/bin/activate"
DEP_URL="https://github.com/jaraco/path.git"
LOG_FILEPATH="venv_install.log"


python3 -m pip --version
python3 -m venv $VENV_DIRPATH
. $VENV_ACTIVATION_FILEPATH
python3 -m pip install --log $LOG_FILEPATH --force-reinstall git+$DEP_URL

python3 my_program.py
