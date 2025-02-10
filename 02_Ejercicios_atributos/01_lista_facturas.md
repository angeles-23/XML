# Ejercicio (con atributos)
Unos programadores necesitan estructurar la información que intercambiarán los ficheros de sus aplicaciones para lo cual han determinado los requisitos siguientes.

- Los ficheros deben tener un elemento `<listafacturas>`
- Dentro de la lista debe haber una o más facturas.
- Las facturas tienen un atributo fecha que es optativo.
- Toda factura tiene un emisor, que es un elemento obligatorio y que debe tener un atributo cif que es obligatorio. Dentro de emisor debe haber un elemento nombre, que es obligatorio y puede o no haber un elemento volumenventas.
- Toda factura debe tener un elemento pagador, el cual tiene exactamente la misma estructura que emisor.
- Toda factura tiene un elemento importe.