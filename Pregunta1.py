def char_to_int(char, modulo):
    if modulo == 27:
        # Función para convertir un carácter en su valor numérico en módulo 27 (alfabeto español)
        if 'A' <= char <= 'Z':
            return ord(char) - ord('A')
        elif 'a' <= char <= 'z':
            return ord(char) - ord('a')
        elif char == 'Ñ':
            return 14  # Representamos la letra "Ñ" como 14 en el alfabeto español
        else:
            # Otros caracteres (espacio, signos de puntuación, etc.)
            return 27  # Puedes asignar 27 a otros caracteres si es necesario
    elif modulo == 191:
        # Función para convertir un carácter en su valor numérico en módulo 191 (ASCII extendido)
        return ord(char)

def int_to_char(num, modulo):
    if modulo == 27:
        # Función para convertir un valor numérico en módulo 27 en un carácter (alfabeto español)
        if 0 <= num <= 25:
            return chr(num + ord('A'))
        elif num == 14:
            return 'Ñ'  # Representamos 14 como la letra "Ñ" en el alfabeto español
        else:
            # Otros caracteres (espacio, signos de puntuación, etc.)
            return ' '  # Puedes asignar un espacio u otros caracteres si es necesario
    elif modulo == 191:
        # Función para convertir un valor numérico en módulo 191 en un carácter (ASCII extendido)
        return chr(num)

def vigenere_cipher(texto, clave, modulo):
    resultado = ""
    for i in range(len(texto)):
        char_texto = char_to_int(texto[i], modulo)
        char_clave = char_to_int(clave[i % len(clave)], modulo)
        if char_texto < modulo:
            resultado += int_to_char((char_texto + char_clave) % modulo, modulo)
        else:
            # Mantener otros caracteres sin cambios
            resultado += texto[i]
    return resultado

# Solicitar al usuario el módulo a utilizar (27 o 191)
modulo = int(input("Ingrese el módulo a utilizar (27 para alfabeto español, 191 para ASCII): "))

# Leer el archivo de entrada
nombre_archivo = input("Ingrese el nombre del archivo de texto claro (por ejemplo, texto.txt): ")
with open(nombre_archivo, 'r', encoding='utf-8') as archivo_entrada:
    texto_claro = archivo_entrada.read()

# Solicitar la clave
clave = input("Ingrese la clave: ")

# Cifrar el texto claro
texto_cifrado = vigenere_cipher(texto_claro, clave, modulo)

# Guardar el resultado en un archivo de salida
nombre_salida = input("Ingrese el nombre del archivo de salida (por ejemplo, cifra.txt): ")
with open(nombre_salida, 'w', encoding='utf-8') as archivo_salida:
    archivo_salida.write(texto_cifrado)

print("Cifrado de Vigenère completado. El resultado se ha guardado en", nombre_salida)
