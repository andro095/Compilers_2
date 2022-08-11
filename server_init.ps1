& venv/bin/Activate.ps1
Set-Location backend
uvicorn main:app --reload