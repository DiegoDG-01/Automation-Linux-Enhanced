<p align="center">
  <a href="" rel="noopener">
 <img width=150px height=150px src="https://image.flaticon.com/icons/svg/311/311329.svg" alt="Project logo"></a>
</p>

<h1 align="center">Automation Linux Enhanced</h1>

<div align="center">

[![](https://img.shields.io/badge/status-active-success.svg)]()

</div>

---

<p align="center"> Permitir un manejo mas ágil, así como una ayuda a nuevos usuarios en sistemas operativos linux.
    <br> 
</p>

## 📝 Tabla de contenido

- [Acerca de](#about)
- [Comandos funcionales](#functionality)
- [Comenzando](#getting_started)
- [Despliegue](#deployment)
- [Uso](#usage)
- [Construido usando](#built_using)
- [Autor](#authors)
- [Agradecimientos](#acknowledgement)

## 🧐 Acerca de <a name = "about"></a>

Ayudar a toda persona que inicie su cambio a una plataforma abierta linux, brindándole una herramienta para que su transición sea mas agradable.

## Comandos funcionales <a name = "functionality"></a>

* APT
    - [x] Update.
    - [x] Upgrade.
    - [x] Update & Upgrade.
* CP
    - [x] Copy file.
    - [x] Copy folder.
* PIP
    - [x] Install package.
    - [ ] Uninstall package.
* Web Server
    - [ ] Inicializar servidor.
    - [ ] Detener servidor.


## 🏁 Comenzando <a name = "getting_started"></a>

Estas instrucciones le proporcionarán una copia del proyecto en funcionamiento en su máquina local para fines de desarrollo y prueba. Consulte la [implementacion](#deployment) para obtener notas sobre cómo implementar el proyecto en un sistema.

### Prerequisitos

* Python3. <img height="30" src="https://image.flaticon.com/icons/svg/2/2181.svg">
* Sistema operativo linux (debian o derivados). <img height="30" src="https://image.flaticon.com/icons/svg/25/25719.svg">


## Instalacion

Para su instalación solo basta con clonar el repositorio en la ruta deseada, se recomienda ubicar el sistema en la raíz de la carpeta del usuario.

Pued hacer uso del comando: ***cp -r Basic-Automatication-for-linux/ $HOME/***

## 🎈 Uso <a name="usage"></a>

El uso del script se puede llevar a cabo ejecutándolo directamente y siguiendo los pasos que te muestra el script o en su defecto hacer uso de argumentos al momento de ejecutarlo.


### Uso de argumentos

El uso de los argumentos permite mayor rapidez para la ejecución de los comandos, omitiendo la
espera de la presentación del menú y ejecutando los comando directamente.

```
Python3 'NOMBRE_SCRIPT' -r 'PASSWORD' -s 'SECUENCIA'
```
Actualmente los argumentos disponibles son:
- **-r**: Designa la contraseña del usuario para tareas que así lo requieran 

- **-s**: Es la secuencia para la ejecución del comando a utilizar

```
Python3 'ALE.py' -r contraseña_de_ejemplo -s 13
```

El primer término de la secuencia corresponde el comando a utilizar:

* 1.- **APT**
* 2.- **CP**
* 3.- **PIP**

El segundo término corresponde al submenú del comando seleccionado, por ejemplo:
* **APT**
    - 1.- Update
    - 2.- Upgrade
    - 3.- Update & Upgrade

## 🚀 Despliegue <a name = "deployment"></a>


* Se recomiendo mantener el script en la raíz de la carpeta del usuario.

* Generar un alias al script, de tal forma que no sea necesario escribir la ruta del script, para ello modificaremos el siguiente archivo.
    * Escribiremos el siguiente comando en la terminal ***sudo nano  $HOME/.bashrc***

    * Nos ubicaremos al final del archivo.

    * Escribimos el siguiente comando:  
    **alias ale='python3 (RUTA DE LA CARPETA)/ALE.py**

    ***Ejemplo:***
    
    *alias ale='python3 /home/diego/Proyects/Python/Basic-Automatication-for-linux/ALE.py*


## ⛏️ Construido usando <a name = "built_using"></a>

- [Python](https://www.python.org/) - Lenguage de programacion
- [Debian](https://www.debian.org/) - Sistema operativo


## ✍️ Autor <a name = "authors"></a>

- [@DiegoDG-01](https://github.com/DiegoDG-01)


## 🎉 Agradecimientos <a name = "acknowledgement"></a>

- Mrth GM
- Ale AR
- Freepik (Icono)
