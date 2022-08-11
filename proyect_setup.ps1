$python_command = ''


if (Get-Command python -errorAction SilentlyContinue)
{
    $python_command = 'python'
} elseif (Get-Command python3 -errorAction SilentlyContinue) {
    $python_command = 'python3'
} else {
    Write-Error "Python no está instalado en el sistema. Por favor, instale Python 3.10 o superior."
    exit 1
}

$python_ver = & $python_command --version

$start = $python_ver.IndexOf(".")
$end = $python_ver.LastIndexOf(".")

$version = $python_ver.Substring($start+1, $end-$start-1)

$version = [int]$version

if ($version -lt 10)
{
    Write-Error "Tu version es 3.$version. Por favor, instale Python 3.10 o superior."
    exit 1
}

& $python_command -m venv venv

& venv/bin/activate

pip install -r requirements.txt

deactivate

cd frontend

npm install