# Ejercicio II (DTD)
Crear un XML de ejemplo y la DTD asociada para unos programadores que programan una aplicación de pedidos donde hay una lista de pedidos con 0 o más pedidos. Cada pedido tiene un número de serie, una cantidad y un peso que puede ser opcional.


#### SOLUCIÓN 
``` xml
<?xml version="1.0" encoding="UTF-8"?>

<!DOCTYPE pedidos [
    <!ELEMENT pedidos (pedido*)>
    <!ELEMENT pedido (numeroSerie, cantidad, peso?)>
    <!ELEMENT numeroSerie (#PCDATA)>
    <!ELEMENT cantidad (#PCDATA)>
    <!ELEMENT peso (#PCDATA)>
]>

<pedidos>
    <pedido>
        <numeroSerie>123456</numeroSerie>
        <cantidad>6</cantidad>
        <peso>9.3</peso>
    </pedido>
    <pedido>
        <numeroSerie>15948</numeroSerie>
        <cantidad>3</cantidad>
    </pedido>
</pedidos>
```