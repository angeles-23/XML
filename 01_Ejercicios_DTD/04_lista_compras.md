# Ejercicio V DTD
En un departamento se ha decidido la siguiente estructura para ficheros de datos que se tengan que mover de unos software a otros.

La raíz debe ser el elemento `<listacompras>`

Dentro de `<listacompras>` debe haber uno o más elementos `<venta>`

Una venta puede llevar dentro uno de dos: `<ventaacredito>` o `<ventainmediata>`

Un elemento `<ventacredito>` consta de : un elemento <fechafinpago> que es optativo y un elemento `<cantidad>` que es obligatorio.

Un elemento `<ventainmediata>` lleva dentro dos cosas: un elemento `<cantidad>` que es obligatorio y un elemento `<divisa>` que también es obligatorio.

#### SOLUCIÓN
``` xml
<?xml version="1.0" encoding="UTF-8"?>

<!DOCTYPE listacompras [
    <!ELEMENT listacompras (venta+)>
    <!ELEMENT venta (ventacredito | ventainmediata)>
    <!ELEMENT ventacredito (fechafinpago?, cantidad)>
    <!ELEMENT ventainmediata (cantidad?, divisa)>
    <!ELEMENT fechafinpago (#PCDATA)>
    <!ELEMENT cantidad (#PCDATA)>
    <!ELEMENT divisa (#PCDATA)>
]>

<listacompras>
    <venta> <!-- + -->
        <ventacredito> <!-- <ventaacredito> o <ventainmediata> -->
            <fechafinpago>2025-12-03</fechafinpago> <!-- ? -->
            <cantidad>9</cantidad>
        </ventacredito> 
    </venta>
    <venta> <!-- + -->
        <ventainmediata> <!-- <ventaacredito> o <ventainmediata> -->
            <cantidad>4</cantidad>
            <divisa>1652645</divisa> 
        </ventainmediata> 
    </venta>
</listacompras>
```