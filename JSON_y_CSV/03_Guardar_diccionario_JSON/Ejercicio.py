import os, json
os.system('cls')

def recibir_datos():
    nombre = input('Nombre: ')

    try:
        edad = int(input('Edad: '))
        if edad < 0 and edad > 100:
            print('Edad correcta')
    except Exception:
        print('Valor incorrecto')
    email = input('Email: ')

    return nombre, edad, email


def es_edad_correcta():
    ...

def es_email_correcto():
    ...


if __name__ == '__main__':
    recibir_datos()