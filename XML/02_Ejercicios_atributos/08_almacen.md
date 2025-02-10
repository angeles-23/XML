Almacén de repuestos
Una empresa de repuestos desea almacenar en XML la información de su inventario:

- El elemento raíz debe ser «repuestos»

- Dentro de «repuestos» debe haber uno o más «repuesto».

- Dentro de «repuesto» debe haber una de estas dos cosas: «tornillo» o «tuerca»
  -   Tornillo: lleva siempre un atributo «peso». Lleva dentro un elemento llamado «descripcion» 
  -   Tuerca: puede llevar un atributo «peso». Lleva dentro siempre un elemento llamado «material»

Ejemplo de fichero válido
``` xml
<repuestos>
    <repuesto>
        <tornillo peso="5g">
            <descripcion>Tornillo para ensamblajes metálicos</descripcion>
        </tornillo>
    </repuesto>
    <repuesto>
        <tuerca>
            <material>Acero</material>
        </tuerca>
    </repuesto>
    <repuesto>
        <tuerca peso="12 mg">
            <material>Aleación</material>
        </tuerca>
    </repuesto>
</repuestos>
```