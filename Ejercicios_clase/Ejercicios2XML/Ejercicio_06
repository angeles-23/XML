<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE operaciones [ 
  <!ELEMENT operaciones (ventacoche | compracoche)+>
  <!ELEMENT compracoche (vehiculo, precio, cliente)>
  <!ELEMENT ventacoche (vehiculo, precio, cliente)>
  <!ELEMENT vehiculo (marca, modelo, anio)>
  <!ATTLIST compracoche 
    id ID  #REQUIRED
    fecha CDATA #REQUIRED
    estado CDATA #IMPLIED
  >
  <!ATTLIST ventacoche
    id ID #REQUIRED 
    fecha CDATA #REQUIRED
    estado CDATA #IMPLIED
  >
  <!ELEMENT marca (#PCDATA)>
  <!ELEMENT modelo (#PCDATA)>
  <!ELEMENT anio (#PCDATA)>
  <!ELEMENT precio (#PCDATA)>
  <!ELEMENT cliente (#PCDATA)>
]>

<operaciones>
    <ventacoche id="v1" fecha="2024-01-15" estado="completada">
        <vehiculo>
            <marca>Ford</marca>
            <modelo>Focus</modelo>
            <anio>2018</anio>
        </vehiculo>
        <precio>12000</precio>
        <cliente>Juan Pérez</cliente>
    </ventacoche>
    <compracoche id="c1" fecha="2024-01-16">
        <vehiculo>
            <marca>Honda</marca>
            <modelo>Civic</modelo>
            <anio>2020</anio>
        </vehiculo>
        <precio>15000</precio>
        <cliente>Ana López</cliente>
    </compracoche>
    <ventacoche id="v2" fecha="2024-01-20">
        <vehiculo>
            <marca>BMW</marca>
            <modelo>X3</modelo>
            <anio>2019</anio>
        </vehiculo>
        <precio>35000</precio>
        <cliente>Carlos García</cliente>
    </ventacoche>
</operaciones>