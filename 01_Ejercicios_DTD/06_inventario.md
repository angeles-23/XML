# Ejercicio VI DTD
Un mayorista de productos de librería desea tener un formato de almacenamiento de datos para reflejar la información de su inventario.

- El elemento raíz debe ser `<inventario>`
- Dentro de inventario pueden ir elementos `<lapiz>`, `<cuaderno>` o `<boligrafo>` repetidos y en cualquier orden.
- Todo `<lapiz>` puede tener un elemento `<dureza>`
- Todo cuaderno debe llevar dos elementos: `<numhojas>` y `<estilo>`
- Todo boligrafo lleva un `<precio>` y puede o no llevar un elemento `<color>`
El siguiente fichero debería ser validado por la DTD:

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
```
