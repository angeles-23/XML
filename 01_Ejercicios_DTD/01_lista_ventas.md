# Ejercicio I (DTD)
Unos programadores necesitan un formato de fichero para que sus distintos programas intercambien información sobre ventas. El acuerdo al que han llegado es que su XML debería tener esta estructura:

- El elemento raíz será `<listaventas>`
- Toda `<listaventas>` tiene una o más ventas.
- Toda `<venta>` tiene los siguientes datos:
  - Importe.
  - Comprador.
  - Vendedor.
  - Fecha (optativa).
  - Un codigo de factura.
  

#### SOLUCION
``` xml
<?xml version="1.0" encoding="UTF-8"?>

<!DOCTYPE listaventas[
    <!ELEMENT listaventas (venta+)>
    <!ELEMENT venta (importe, comprador, vendedor, fecha?, codigoFactura)>
    <!ELEMENT importe (#PCDATA)>
    <!ELEMENT comprador (#PCDATA)>
    <!ELEMENT vendedor (#PCDATA)>
    <!ELEMENT fecha (#PCDATA)>
    <!ELEMENT codigoFactura (#PCDATA)>
]>


<listaventas>
    <venta>
        <importe>15€</importe>
        <comprador>Manuel</comprador>
        <vendedor>Juan</vendedor>
        <fecha>2020-11-16</fecha> <!-- ? -->
        <codigoFactura>13526</codigoFactura>
    </venta>
    <venta>
        <importe>15€</importe>
        <comprador>Manuel</comprador>
        <vendedor>Juan</vendedor>
        <fecha>2020-11-16</fecha> <!-- ? -->
        <codigoFactura>13526</codigoFactura>
    </venta>
</listaventas>
```