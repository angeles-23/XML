# Ejercicio VI DTD
Un mayorista de productos de librería desea tener un formato de almacenamiento de datos para reflejar la información de su inventario.

- El elemento raíz debe ser `<inventario>`
- Dentro de inventario pueden ir elementos `<lapiz>`, `<cuaderno>` o `<boligrafo>` repetidos y en cualquier orden.
- Todo `<lapiz>` puede tener un elemento `<dureza>`
- Todo cuaderno debe llevar dos elementos: `<numhojas>` y `<estilo>`
- Todo boligrafo lleva un `<precio>` y puede o no llevar un elemento `<color>`


``` xml
<inventario>
    <lapiz></lapiz>
    <lapiz>
        <dureza>H2</dureza>
    </lapiz>
    <cuaderno>
        <numhojas>80</numhojas>
        <estilo>2 rayas</estilo>
    </cuaderno>
    <boligrafo>
        <precio>0.80</precio>
    </boligrafo>
    <cuaderno>
        <numhojas>100</numhojas>
        <estilo>Cuadriculado</estilo>
    </cuaderno>
    <boligrafo>
        <precio>0.80</precio>
        <color>Rojo</color>
    </boligrafo>
</inventario>



<?xml version="1.0" encoding="UTF-8"?>

<!DOCTYPE inventario [
    <!ELEMENT inventario (lapiz|cuaderno|boligrafo)+>
    <!ELEMENT lapiz (dureza?)>
    <!ELEMENT cuaderno (numhojas, estilo)>
    <!ELEMENT boligrafo (precio, color?)>
    <!ELEMENT dureza (#PCDATA)>
    <!ELEMENT numhojas (#PCDATA)>
    <!ELEMENT estilo (#PCDATA)>
    <!ELEMENT precio (#PCDATA)>
    <!ELEMENT color (#PCDATA)>
]>


<inventario>
    <lapiz> <!-- <lapiz>, <cuaderno> o <boligrafo> repetidos en cualquier orden-->
        <dureza>mucho</dureza> <!-- ? -->
    </lapiz>
    <cuaderno>
        <numhojas>165</numhojas>
        <estilo>minimalista</estilo>
    </cuaderno>
    <boligrafo>
        <precio>16.3</precio>
        <color>rojo</color> <!-- ? -->
    </boligrafo>
</inventario>
```
