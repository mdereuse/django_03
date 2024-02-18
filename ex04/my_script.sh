#!/bin/bash

BASH_FILEPATH="/bin/bash"
VENV_DIRPATH="django_venv"
VENV_ACTIVATION_FILEPATH=$VENV_DIRPATH"/bin/activate"

virtualenv $VENV_DIRPATH --always-copy
. $VENV_ACTIVATION_FILEPATH
python3 -m pip install -r requirement.txt
$BASH_FILEPATH -c ". $VENV_ACTIVATION_FILEPATH; exec $BASH_FILEPATH -i"
