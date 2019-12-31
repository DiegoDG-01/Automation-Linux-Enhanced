# <img height="60" src="https://image.flaticon.com/icons/svg/311/311329.svg"> Automatication for linux <img height="60" src="https://image.flaticon.com/icons/svg/311/311329.svg">

'Automatication for linux' automatiza el uso de los comandos que son usados más frecuentemente por los usuarios, todo ello a través de la terminal del sistema.

## Comandos funcionales

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


## Requisitos <img height="25" src="https://github.githubassets.com/images/icons/emoji/unicode/1f4cb.png">
* Python3. <img height="30" src="https://image.flaticon.com/icons/svg/2/2181.svg">
* Sistema linux (debian o derivadas). <img height="30" src="https://image.flaticon.com/icons/svg/25/25719.svg">



## Ejemplos <img height="30" src="https://github.githubassets.com/images/icons/emoji/unicode/2699.png">

El uso del script se puede llevar a cabo ejecutandolo directamente y siguiendo los pasos que te muestra el script o en su defecto hacer uso de argumentos al momento de ejecutarlo.

#### Uso de argumentos

El uso de los argumentos permite mayor rapidez para la ejecución de los comandos, omitiendo la espera de la presentación del menú y ejecutando los comando directamente.

    Python3 'NOMBRE_SCRIPT' -r 'PASSWORD' -s 'SECUENCIA'

Actualmente los argumentos disponibles son:
**-r**: Designa la contraseña del usuario para tareas que así lo requieran
**-s**: Es la secuencia para la ejecución del comando a utilizar

    Python3 'NOMBRE_SCRIPT' -r contraseña_de_ejemplo -s 13

El primer término de la secuencia corresponde el comando a utilizar:

* 1.- **APT**
* 2.- **CP**
* 3.- **PIP**

El segundo término corresponde al submenú del comando seleccionado, por ejemplo:
* **APT**
    - 1.- Update
    - 2.- Upgrade
    - 3.- Update & Upgrade


## Autores

* DiegoDG.
