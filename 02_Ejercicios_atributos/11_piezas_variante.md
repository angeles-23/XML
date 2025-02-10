# Inventario de piezas (variante)
Se desea almacenar nombres de piezas y para ello se ha llegado a este acuerdo:

- El elemento raíz se va a llamar «listapiezas».

- Dentro de «listapiezas» va a haber uno o muchos elementos «pieza»

- Dentro de «pieza» hay tres elementos:

  - Un elemento llamado «peso» que contiene datos. NO ES OBLIGATORIO QUE ESTÉ

  - Un elemento llamado «nombre» que contiene datos

  - Un elemento llamado fabricante que contiene datos.

    - El fabricante PUEDE LLEVAR un atributo llamado pais que indica el pais.

Ejemplo de fichero válido
```xml
<listapiezas>
    <pieza>
        <!--No hay peso, pero no debe importar, debe darse como bueno-->
        <nombre>Pistón</nombre>
        <fabricante pais="China"> Asia Electronics</fabricante>
    </pieza>
    <pieza>
        <peso>15</peso>
        <nombre>Cilindro</nombre>
        <!--No hay atributo pais, pero no debe pasar nada-->
        <fabricante>Toyota Motors</fabricante>
    </pieza>
</listapiezas>
```