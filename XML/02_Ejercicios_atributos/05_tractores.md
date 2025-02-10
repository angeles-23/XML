# Ejercicio: fabricante de tractores
Un fabricante de tractores desea unificar el formato XML de sus proveedores y para ello ha indicado que necesita que los archivos XML cumplan las siguientes restricciones:

- Un pedido consta de uno o más tractores.

- Un tractor consta de uno o más componentes.

- Un componente tiene los siguientes elementos: nombre del fabricante (atributo obligatorio), fecha de entrega (si es posible, aunque puede que no aparezca, si aparece el dia es optativo, pero el mes y el año son obligatorios). También se necesita saber del componente si es frágil o no. También debe aparecer un elemento peso del componente y dicho elemento peso tiene un atributo unidad del peso (kilos o gramos), un elemento número de serie y puede que aparezca o no un elemento kmmaximos indicando que el componente debe sustituirse tras un cierto número de kilómetros.

Un posible fichero de ejemplo que podría validar sería este:
``` xml
<pedido>
    <tractor>
        <componente nombrefabricante="Ebro">
            <fechaentrega>
                <mes>2018</mes> <anio>2018</anio>
            </fechaentrega>
            <fragil/>
            <peso unidad="kg">12</peso>
            <numserie>00A</numserie>
        </componente>
        <componente nombrefabricante="Avia">
            <fechaentrega>
                <dia>12</dia><mes>1</mes><anio>2019</anio>
            </fechaentrega>
            <nofragil/>
            <peso unidad="g">1450</peso>
            <numserie>00D</numserie>
            <kmmaximos>25000</kmmaximos>
        </componente>
    </tractor>
    <tractor>
        <componente nombrefabricante="John Deere">
            <fragil/>
            <peso unidad="g">770</peso>
            <numserie>43Z</numserie>
        </componente>
    </tractor>
</pedido>
```
