### Laboratorio 2: Cifrado y Hash


#### Integrantes

- Sebastian Allende
- Gian Franco Astorga

#### Fecha de Entrega

- 19 de septiembre

#### Instrucciones de uso

- Para ejecutar el programa de cifrado, se debe ejecutar el siguiente comando:
``` 

```

#### Dependencias

- Python 3.11
- pipenv (contiene las dependencias necesarias para ejecutar el programa)

#### Descripción del problema

Se le solicita crear un programa que envie un mensaje seguro, asegurando la integridad de este sin que este sea modificado.
Cifrar ocupando cualquier red de sustitucion que usted defina y generar un hash de un archivo de texto llamado mensajedeentrada.txt generando un nuevo archivo llamado mensajeseguro.txt.
Con un segundo programa generar la operacion a la inversa, generando el mismo mensaje original con el adicional de poder detectar si el mensaje ha sido modificado o no.

#### Función del código

- Lee el contenido de un archivo llamado "mensajedeentrada.txt" como texto sin formato.

- Calcula el valor hash SHA-1 del texto sin formato.

- Encripta el mensaje utilizando un cifrado Feistel, donde realiza sustitución y permutación en varias rondas.

- Escribe el mensaje cifrado en un archivo llamado "mensajeseguro.txt", agregando el valor hash calculado al final.

- Lee el contenido del archivo cifrado y lo intenta desencriptar.

- Verifica la integridad del mensaje comparando el valor hash recibido con el valor hash calculado del mensaje desencriptado.
