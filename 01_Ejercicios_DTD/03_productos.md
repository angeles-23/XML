# Ejercicio III
Se desea crear una gramática para ficheros de datos en los que se ha decidido contemplar lo siguiente:

- El fichero debe llevar una raíz `<productos>`
- Dentro debe haber uno o más elementos `<producto>`
- Dentro de productos debe haber alguno de estos `<producto>` , `<raton>` , `<teclado>` o `<monitor>`
- Todo ratón, teclado o monitor tiene siempre un código.
- Todo ratón, teclado o monitor puede llevar un nombre.
- Todo ratón, teclado o monitor puede llevar una descripción.


#### SOLUCIÓN

``` xml
<?xml version="1.0" encoding="UTF-8"?>

<!DOCTYPE productos[
    <!ELEMENT productos (producto+)>
    <!ELEMENT producto (teclado|raton|monitor)>
    <!ELEMENT teclado (codigo, nombre?, descripcion?)>
    <!ELEMENT raton (codigo, nombre?, descripcion?)>
    <!ELEMENT monitor (codigo, nombre?, descripcion?)>
    <!ELEMENT nombre (#PCDATA)>
    <!ELEMENT codigo (#PCDATA)>
    <!ELEMENT descripcion (#PCDATA)>
]>


<productos>
    <producto> <!-- + -->
        <teclado> <!-- <raton> , <teclado> o <monitor> -->
            <codigo>1654</codigo>
            <descripcion>Muy potente</descripcion>
        </teclado>     
    </producto>
    <producto> <!-- + -->
        <teclado> <!-- <raton> , <teclado> o <monitor> -->
            <codigo>1954</codigo>
            <nombre>Ratón pP65</nombre>
        </teclado>     
    </producto>
</productos>
```