# Suministros médicos (DTD)
En un centro médico se desea almacenar la información sobre el inventario usando XML. Se ha llegado a un acuerdo para almacenar la información en este formato

- El elemento raíz se llama «suministrosmedicos». Dentro de él hay lo siguiente:

  - Primero hay uno o muchos elementos «antibiotico». Todo antibiotico lleva dentro un elemento «nombre». Puede llevar o no un elemento llamado «nombrecomercial».
  - Despues hay uno o muchos elementos «analgesico». El analgesico puede llevar dentro o no un elemento «fechadecaducidad» y despues siempre un elemento nombre. El analgesico siempre lleva un atributo llamado «pvp».
  -  Despues puede haber 0 o muchos elementos «antitusivo». Todo antitusivo lleva dentro dos elementos QUE PUEDEN IR EN CUALQUIER ORDEN: elemento «tiporeceta» y el elemento «presentacion». La presentacion siempre lleva un atributo «dosisrecomendada»

A continuación se da un ejemplo de fichero:
```xml
<suministrosmedicos>
    <antibiotico>
        <nombre>Penicilina</nombre>
    </antibiotico>
    <antibiotico>
        <nombre>Penicilina</nombre>
        <nombrecomercial>Zitromax</nombrecomercial>
    </antibiotico>
    <antibiotico>
        <nombre>Amoxicilina</nombre>
    </antibiotico>
    <analgesico pvp="14.80 euros">
        <nombre>Paracetamol</nombre>
    </analgesico>
    <analgesico pvp="14.80 euros">
        <fechadecaducidad>15-02-2026</fechadecaducidad>
        <nombre>Apiretal</nombre>
    </analgesico>
    <antitusivo>
        <tiporeceta>Innecesaria</tiporeceta>
        <presentacion  dosisrecomendada="1-1-1">Jarabe</presentacion>
    </antitusivo>
    <antitusivo>
        <presentacion  dosisrecomendada="1-1-1">Jarabe</presentacion>
        <tiporeceta>Atencion primaria</tiporeceta>
    </antitusivo>
    <antitusivo>
        <tiporeceta>Atencion primaria</tiporeceta>
        <presentacion dosisrecomendada="0-0-1">Pastillas</presentacion>
    </antitusivo>
</suministrosmedicos>
```