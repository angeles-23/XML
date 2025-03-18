import os
os.system('cls')


def introducir_frutas_lista():
    frutas = []

    for i in range(5):
        fruta = input(f'Fruta {i+1}: ')
        frutas.append(fruta)
    
    return frutas


def crear_fichero(frutas):
    f = open('./02_Guardar_y_leer_una_lista_en_un_archivo_de_texto/frutas.txt', 'w')
    
    for fruta in frutas:
        f.writelines(f'{fruta}\n')
    f.close()


def leer_frutas():
    f = open('./02_Guardar_y_leer_una_lista_en_un_archivo_de_texto/frutas.txt', 'r')
    contenido = f.read()
    print(contenido)
    f.close()


def frutas_desde_el_final():
    f = open('./02_Guardar_y_leer_una_lista_en_un_archivo_de_texto/frutas.txt', 'r')

    frutas = f.readlines()
    
    lista_inversa = []

    for fruta in range(len(frutas)-1, -1, -1):
        lista_inversa.append(frutas[fruta])
    
    return lista_inversa


def anadir_lista_inversa(lista_inversa):
    f = open('./02_Guardar_y_leer_una_lista_en_un_archivo_de_texto/frutas.txt', 'a')

    for fruta in lista_inversa:
        f.write(f'{fruta}')
    f.close()



if __name__ == '__main__':
    listado_frutas = introducir_frutas_lista()
    crear_fichero(listado_frutas)
    leer_frutas()
    frutas_del_reves = frutas_desde_el_final()
    
    anadir_lista_inversa(frutas_del_reves)
    