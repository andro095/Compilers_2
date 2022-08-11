#!/bin/bash
python_command=''

if command -v python &> /dev/null
then
    python_command='python'
elif command -v python3 &> /dev/null
then
    python_command='python3'
else
    echo "Python no está instalado en el sistema. Por favor, instale Python 3.10 o superior."
    exit 1
fi

python_ver=$($python_command --version)

search='.'

rest=${python_ver#*$search}

prefix=${rest%%$search*}

version=$((0+$prefix))

if [[ $version -lt 10 ]]; then
    echo "Tu version es 3.$version. Por favor, instale Python 3.10 o superior."
    exit 1
fi

$python_command -m venv venv

source venv/bin/activate

pip install -r requirements.txt

deactivate

cd frontend

npm install