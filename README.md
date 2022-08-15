# Analizador Semántico

## Creadores:
|      Nombre     | # Carnet |
|:---------------:|:--------:|
| André Rodríguez |   18332  |
|  Sara Zaravala  |   18893  |

## Requerimientos del sistema:
- Python 3.10 o más reciente
- Node 16.14.2 o version más actual
- Git versión más actual

## Instalación
### Repositorio
Clonar el Repositorio donde se desee:
HTTPS: 
```
git clone https://github.com/andro095/Compilers_2.git
```

SSH:
```
git clone git@github.com:andro095/Compilers_2.git
```

GithubCLI (tener instalado la herramienta para poder usar esta opción):
```
gh repo clone andro095/Compilers_2
```

Luego se ingresa a la carpeta clonada:
```
cd Compilers_2
```
### Mac o Linux:
```
bash proyect_setup.sh
```
### Windows:

```
& ./proyect_setup.ps1
```
### Manual
### Backend
#### Venv (Opcional):
Creamos un ambiente venv:
```
python -m venv venv 
```

Activamos el venv:
Windows: 
```
& venv/bin/activate
```

Mac o Linux:
```
source venv/bin/activate
```

#### Paquetes
Instalamos los paquetes necesarios:
```
pip install -r requirements.txt
```

Si creamos un venv:
```
deactivate
```

### Frontend
Ingresamos a la carpeta de frontend:
```
cd Frontend
```

Instalamos los paquetes:
```
npm install
```

## Inicio del programa
Nos ubicamos en en la carpeta donde está el programa
```
cd path/to/Compilers_2
```

### Backend
#### Mac o Linux
```
bash server_init.sh
```
#### Windows
```
& ./server_init.ps1
```

### Manual
#### Venv (si lo creamos)
#### Mac o Linux
```
source venv/bin/activate
```

#### Windows
Si creamos un venv lo activamos:
```
& venv/bin/activate
```

#### Iniciar el servidor
Ingresamos a la carpeta backend:
```
cd backend
```

Activamos el servidor:
```
uvicorn main:app --reload
```

### Frontend
Iniciamos otra ventana o pestaña de la terminal. Nos vamos a la carpeta del frontend:
```
cd path/to/Compilers_2/frontend
```

Corremos el frontend
```
npm start
```

Nos dirigimos al [localhost:3000](http://localhost:3000)