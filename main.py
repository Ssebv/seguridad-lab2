### Laboratorio 2 - Seguridad Informática ###
import hashlib
import time
from cryptography.fernet import Fernet

def read_txt(filename):
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError: 
        return "ERROR: No se encontro el archivo"

def write_txt(filename, content):
    try:
        with open(filename, 'wb') as file: # wb = write binary
            file.write(content)
    except IOError: # Input/Output error
        return "ERROR: No se pudo escribir el archivo"

def get_hash(text):
    hash_object = hashlib.sha256(text.encode()) # sha1, sha256, sha512, md5 aqui puedes cambiar el algoritmo de hash
    return hash_object.hexdigest()

def generate_key():
    return Fernet.generate_key()

def encrypt(text, key):
    f = Fernet(key)
    return f.encrypt(text.encode())

def decrypt(ciphertext, key):
    try:
        f = Fernet(key)
        decrypted = f.decrypt(ciphertext.encode()).decode()
        return decrypted
    except:
        return "ERROR: No se pudo descifrar el texto"

def main():
    
    input_file = "mensajedeentrada.txt"
    output_file = "mensajeseguro.txt"
    plaintext = read_txt(input_file)
    
    print("----------------------------------------")
    print("[+] Texto plano:", plaintext)
    
    if plaintext is not None:
        key = generate_key()
        print("[+] Llave generada:", key)
        
        hash_original = get_hash(plaintext).encode()  # Convertir el hash a bytes
        ciphertext = encrypt(plaintext, key)
        print("[+] Texto cifrado:", ciphertext)
        write_txt(output_file, ciphertext + b'\n' + hash_original) 

        print("[+] Archivo cifrado guardado en:", output_file)
        print("----------------------------------------")
        print("Descifrando mensaje...")
        time.sleep(1)
        
        current_ciphertext = read_txt(output_file) 
        print("[+] Texto cifrado:", current_ciphertext)
        
        decrypted = decrypt(current_ciphertext, key)
        print("[+] Texto descifrado:", decrypted)
        
        print("\n----------------------------------------")
        print("[+] Prueba de integridad del archivo cifrado:")

        stored_hash = current_ciphertext.split('\n')[-1]  # Obtenemos el último hash almacenado
        current_hash = get_hash(decrypted)  # Calculamos el hash del texto descifrado

        if current_hash == stored_hash:
            print("      No se detectaron modificaciones en el archivo cifrado")
        else:
            print("      Se detectó una modificación en el archivo cifrado")

        
if __name__ == "__main__":
    main()
    
    