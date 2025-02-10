# Ejercicio III
Se desea crear una gramática para ficheros de datos en los que se ha decidido contemplar lo siguiente:

- El fichero debe llevar una raíz `<productos>`
- Dentro debe haber uno o más elementos `<producto>`
- Dentro de productos debe haber alguno de estos `<producto>` , `<raton>` , `<teclado>` o `<monitor>`
- Todo ratón, teclado o monitor tiene siempre un código.
- Todo ratón, teclado o monitor puede llevar un nombre.
- Todo ratón, teclado o monitor puede llevar una descripción.

``` xml
<productos>
    <producto>
        <raton>
            <codigo>27A</codigo>
        </raton>
    </producto>
    <producto>
        <teclado>
            <codigo>28D</codigo>
            <descripcion>Teclado en Español</descripcion>
        </teclado>
    </producto>
</productos>
```