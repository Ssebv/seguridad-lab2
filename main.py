import hashlib
import time
import random

# Definimos la tabla de sustitución como variable global

substitute_table = {
        'a': 'x',
        'b': 'y',
        'c': 'z',
        'd': 'm',
        'e': 'n',
        'f': 'o',
        'g': 'p',
        'h': 'q',
        'i': 'r',
        'j': 's',
        'k': 't',
        'l': 'u',
        'm': 'v',
        'n': 'w',
        'o': 'a',
        'p': 'b',
        'q': 'c',
        'r': 'd',
        's': 'e',
        't': 'f',
        'u': 'g',
        'v': 'h',
        'w': 'i',
        'x': 'j',
        'y': 'k',
        'z': 'l',
        ' ': ' ',
        '\n': '\n'
    }

def read_txt(filename):
    try:
        with open(filename, 'r+') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{filename}'")
        return []

def write_txt(filename, content):
    try:
        with open(filename, 'w+') as file:
            file.write(content)
    except IOError:
        print(f"Error al escribir en el archivo '{filename}'")

def get_hash(text):
    hash_object = hashlib.sha1(text.encode()) # sha1, sha256, sha512, md5 aqui puedes cambiar el algoritmo de hash
    return hash_object.hexdigest()

def substitute(text, substitution_table):
    substitution_text = ''.join([substitution_table[char] if char in substitution_table else char for char in text])
    return substitution_text

def permute(text, permutation_seed):
    random.seed(permutation_seed)
    text_list = list(text)
    random.shuffle(text_list)
    return ''.join(text_list)

def encrypt(text): # Feistel
    key = "MiClaveSecreta" # Aqui puedes cambiar la clave segura

    num_ronds = 5 # Aqui puedes cambiar el numero de rondas que se necesiten
    ciphertext = text

    for round in range(num_ronds):
        # Sustitución
        ciphertext = substitute(ciphertext, substitute_table)
        # Permutación
        ciphertext = permute(ciphertext, key)
    
    ciphertext = ''.join([chr(ord(c) ^ ord(k)) for c, k in zip(ciphertext, key)]) # Operación XOR
    
    return ciphertext

def decrypt(ciphertext):

    key = "MiClaveSecreta" # Debe ser la misma clave utilizada para cifrar
    num_ronds = 5 # Debe ser el mismo número de rondas utilizado para cifrar
    plaintext = ciphertext

    # Deshacer la operación XOR
    

    for round in reversed(range(num_ronds)):
        # Deshacer la permutación
        plaintext = permute(plaintext, key)
        # Deshacer la sustitución
        plaintext = substitute(plaintext, substitute_table)

    return plaintext

def main():
    plaintext = ''.join(read_txt("mensajedeentrada.txt")) # Leemos todo el contenido en una cadena
    print(plaintext)
    hash_original = get_hash(plaintext)
    ciphertext = encrypt(plaintext + '\n' + hash_original)
    write_txt("mensajeseguro.txt", ciphertext)
    print(ciphertext)

    decrypted_text = decrypt(''.join(read_txt("mensajeseguro.txt"))) # Leemos todo el contenido en una cadena
    decrypted_lines = decrypted_text.split('\n')
    decrypted_message = '\n'.join(decrypted_lines[:-1])
    received_hash = decrypted_lines[-1]
    print(received_hash)

    calculated_hash = get_hash(decrypted_message)
    if received_hash == calculated_hash:
        print("La integridad del mensaje es válida.")
    else:
        print("Error: La integridad del mensaje ha sido comprometida.")

if __name__ == "__main__":
    main()
    time.sleep(1)
    
    print("\n\n")
    print("Prueba de modificación del archivo cifrado:")
    modified_text = ""
    write_txt("mensajeseguro.txt", modified_text)
    # Intenta descifrar el archivo modificado
    decrypted_text = decrypt(read_txt("mensajeseguro.txt"))
    if "ERROR" in decrypted_text:
        print("La modificación del archivo cifrado ha sido detectada.")
    else:
        print("El archivo cifrado modificado no ha sido detectado.")
