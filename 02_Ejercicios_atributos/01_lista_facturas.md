# Ejercicio (con atributos)
Unos programadores necesitan estructurar la información que intercambiarán los ficheros de sus aplicaciones para lo cual han determinado los requisitos siguientes.

- Los ficheros deben tener un elemento `<listafacturas>`
- Dentro de la lista debe haber una o más facturas.
- Las facturas tienen un atributo fecha que es optativo.
- Toda factura tiene un emisor, que es un elemento obligatorio y que debe tener un atributo cif que es obligatorio. Dentro de emisor debe haber un elemento nombre, que es obligatorio y puede o no haber un elemento volumenventas.
- Toda factura debe tener un elemento pagador, el cual tiene exactamente la misma estructura que emisor.
- Toda factura tiene un elemento importe.


#### SOLUCIÓN
```xml
<?xml version="1.0" encoding="UTF-8"?>

<!DOCTYPE listafacturas [
    <!ELEMENT listafacturas (factura+)>
    <!ATTLIST factura fecha CDATA #IMPLIED>
    <!ELEMENT factura (emisor, pagador, importe)>
    <!ATTLIST emisor cif CDATA #REQUIRED>
    <!ELEMENT emisor (nombre, volumenventas?)>
    <!ATTLIST pagador cif CDATA #REQUIRED>
    <!ELEMENT pagador (nombre, volumenventas?)>
    <!ELEMENT nombre (#PCDATA)>
    <!ELEMENT volumenventas (#PCDATA)>
    <!ELEMENT importe (#PCDATA)>
]>

<listafacturas>
    <factura fecha="13-06-2024"> <!-- + , #I -->
        <emisor cif="123"> <!-- #R-->
            <nombre>Juan</nombre>
            <volumenventas>9</volumenventas> <!-- ? -->
        </emisor>
        <pagador cif="456"> <!-- #R-->
            <nombre>Manuel</nombre>
            <volumenventas>954</volumenventas> <!-- ? -->
        </pagador>
        <importe>165.32</importe>
    </factura>
</listafacturas>

```