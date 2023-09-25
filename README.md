### Laboratorio 2: Cifrado y Hash


#### Integrantes

- Sebastian Allende
- Gian Franco Astorga

#### Fecha de Entrega

- 19 de septiembre

#### Instrucciones de uso

- Para ejecutar el programa de cifrado, se debe ejecutar el siguiente comando:
``` 
python3 main.py
```

#### Dependencias

- Python 3.11
- pipenv (contiene las dependencias necesarias para ejecutar el programa)
- pipenv shell (para activar el entorno virtual)
- Recordar seleccionar el interprete de python 3.11 en el entorno virtual que se crea al ejecutar el comando pipenv shell

#### Descripción del problema

Se le solicita crear un programa que envie un mensaje seguro, asegurando la integridad de este sin que este sea modificado.
Cifrar ocupando cualquier red de sustitucion que usted defina y generar un hash de un archivo de texto llamado mensajedeentrada.txt generando un nuevo archivo llamado mensajeseguro.txt.
Con un segundo programa generar la operacion a la inversa, generando el mismo mensaje original con el adicional de poder detectar si el mensaje ha sido modificado o no.

#### Función del código

- Lee el contenido de un archivo llamado "mensajedeentrada.txt" como texto sin formato.

- Genera una clave de cifrado aleatoria.

- Calcula el valor hash SHA-256 del texto sin formato.

- Cifra el texto sin formato usando la clave de cifrado generada.

- Guarda el texto cifrado en un archivo llamado "mensajeseguro.txt". El archivo contiene el texto cifrado y el valor hash calculado.

- Verifica la integridad del mensaje cifrado.
