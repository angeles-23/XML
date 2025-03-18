import os
os.system('cls')


def ingresar_texto():
    texto = input('Introduce un mensaje: ')
    return texto


def escribir_archivo(texto):
    f = open('./01_Escribir_y_leer_un_archivo_simple/mensaje.txt', 'w')
    f.write(texto)
    f.close()


def leer_contenido():
    f = open('./01_Escribir_y_leer_un_archivo_simple/mensaje.txt', 'r')
    contenido = f.read()
    print(f'Contenido del archivo: {contenido}')
    f.close()


if __name__ == '__main__':
    texto = ingresar_texto()
    escribir_archivo(texto)
    leer_contenido()