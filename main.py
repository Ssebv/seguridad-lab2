### Laboratorio 2 - Seguridad Informática ##

import hashlib
import time
from cryptography.fernet import Fernet

def read_txt(filename):  # Función para leer un archivo de texto
    try:
        with open(filename, 'r') as file: # r = read
            return file.read()
    except FileNotFoundError: 
        return "ERROR: No se encontro el archivo"

def write_txt(filename, content): # Función para escribir un archivo de texto
    try:
        with open(filename, 'wb') as file: # wb = write binary
            file.write(content)
    except IOError: # Input/Output error
        return "ERROR: No se pudo escribir el archivo"

def get_hash(text): # Función para obtener el hash de un texto
    hash_object = hashlib.sha256(text.encode()) # sha1, sha256, sha512 aqui puedes cambiar el algoritmo de hash
    return hash_object.hexdigest() # Convertir el hash a hexadecimal

def generate_key(): # Función para generar una llave aleatoria
    clave = Fernet.generate_key()
    return clave # Generar una llave aleatoria

def encrypt(text, key): # Función para cifrar un texto
    try:
        f = Fernet(key) # Crear un objeto Fernet de cifrado simétrico
        return f.encrypt(text.encode()) # Cifrar a los bytes del texto plano
    except:
        return "ERROR: No se pudo cifrar el texto"

def decrypt(ciphertext, key): # Función para descifrar un texto
    try:
        f = Fernet(key) # Crear un objeto Fernet
        decrypted = f.decrypt(ciphertext.encode()).decode() # Descifrar el texto cifrado y convertirlo a texto plano con decode()
        return decrypted # Retornar el texto descifrado
    except:
        return "ERROR: No se pudo descifrar el texto"

def main(): # Función principal
    
    input_file = "mensajedeentrada.txt" # Nombre del archivo de entrada
    output_file = "mensajeseguro.txt" # Nombre del archivo de salida
    plaintext = read_txt(input_file)
    
    print("----------------------------------------")
    print("[+] Texto plano:", plaintext)
    
    if plaintext is not None: # Si el archivo no está vacío
        key = generate_key() # Generar una llave aleatoria 
        print("[+] Llave generada:", key)
        
        hash_original = get_hash(plaintext).encode()  # Convertir el hash a bytes
        ciphertext = encrypt(plaintext, key)  # Cifrar el texto plano
        print("[+] Texto cifrado:", ciphertext)  
        write_txt(output_file, ciphertext + b'\n' + hash_original) # Escribir el texto cifrado en un archivo

        print("[+] Archivo cifrado guardado en:", output_file)
        print("----------------------------------------")
        print("Descifrando mensaje...")
        time.sleep(1) # Esperar 1 segundo
        
        current_ciphertext = read_txt(output_file) # Leer el archivo cifrado 
        print("[+] Texto cifrado:", current_ciphertext) 
        
        decrypted = decrypt(current_ciphertext, key) # Descifrar el texto cifrado
        print("[+] Texto descifrado:", decrypted)
        
        print("\n----------------------------------------")
        print("[+] Prueba de integridad del archivo cifrado:")

        stored_hash = current_ciphertext.split('\n')[-1]  # Obtenemos el último hash almacenado
        current_hash = get_hash(decrypted)  # Calculamos el hash del texto descifrado

        if current_hash == stored_hash: # Comparamos los hashes
            print("      No se detectaron modificaciones en el archivo cifrado")
        else:
            print("      Se detectó una modificación en el archivo cifrado")

        print("----------------------------------------")
        
if __name__ == "__main__": # Función para ejecutar el programa
    main()
    
    