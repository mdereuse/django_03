#!/bin/bash
VENV_DIRPATH="./local_lib"
VENV_ACTIVATION_FILEPATH=$VENV_DIRPATH"/bin/activate"
DEP_URL="https://github.com/jaraco/path.git"
LOG_FILEPATH="local_lib_install.log"


virtualenv $VENV_DIRPATH --always-copy
. $VENV_ACTIVATION_FILEPATH
python3 -m pip --version
python3 -m pip install --log $LOG_FILEPATH --force-reinstall git+$DEP_URL && python3 my_program.py
