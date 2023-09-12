import hashlib
import time

def read_txt(filename):
    try:
        with open(filename, 'r') as file:
            return file.readlines()
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{filename}'")
        return []

def write_txt(filename, content):
    try:
        with open(filename, 'w') as file:
            file.write(content)
    except IOError:
        print(f"Error al escribir en el archivo '{filename}'")


def get_hash(text):
    hash_object = hashlib.sha1(text.encode()) # sha1, sha256, sha512, md5 aqui puedes cambiar el algoritmo de hash
    return hash_object.hexdigest()

def encrypt(text): # Feistel, AES, DES,

    pass


def decrypt(ciphertext):

    pass


def main():

    plaintext = ''.join(read_txt("mensajedeentrada.txt"))
    hash_original = get_hash(plaintext)
    ciphertext = encrypt(plaintext + '\n' + hash_original)
    write_txt("mensajeseguro.txt", ciphertext)

    decrypted_text = decrypt(''.join(read_txt("mensajeseguro.txt")))
    decrypted_lines = decrypted_text.split('\n')
    decrypted_message = '\n'.join(decrypted_lines[:-1])
    received_hash = decrypted_lines[-1]

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
    decrypted_text = decrypt(''.join(read_txt("mensajeseguro.txt")))
    if "ERROR" in decrypted_text:
        print("La modificación del archivo cifrado ha sido detectada.")
    else:
        print("El archivo cifrado modificado no ha sido detectado.")
