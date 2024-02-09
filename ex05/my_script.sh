#!/bin/bash

PYTHON_FILEPATH="/usr/bin/python3"
VENV_DIRPATH="django_venv"
VENV_ACTIVATION_FILEPATH=$VENV_DIRPATH"/bin/activate"

$PYTHON_FILEPATH -m venv $VENV_DIRPATH
. $VENV_ACTIVATION_FILEPATH
python3 -m pip install -r requirement.txt
