# Ejercicio V DTD
En un departamento se ha decidido la siguiente estructura para ficheros de datos que se tengan que mover de unos software a otros.

La raíz debe ser el elemento `<listacompras>`

Dentro de `<listacompras>` debe haber uno o más elementos `<venta>`

Una venta puede llevar dentro uno de dos: `<ventaacredito>` o `<ventainmediata>`

Un elemento `<ventacredito>` consta de : un elemento <fechafinpago> que es optativo y un elemento `<cantidad>` que es obligatorio.

Un elemento `<ventainmediata>` lleva dentro dos cosas: un elemento `<cantidad>` que es obligatorio y un elemento `<divisa>` que también es obligatorio.