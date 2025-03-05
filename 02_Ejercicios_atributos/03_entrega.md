# Ejercicio 3
Un mayorista informático necesita especificar las reglas de los elementos permitidos en las aplicaciones que utiliza en sus empresas, para ello ha indicado los siguientes requisitos:

- Una entrega consta de uno o más lotes.
- Un lote tiene uno o más palés
- Todo palé tiene una serie de elementos: número de cajas, contenido y peso y forma de manipulación.
- El contenido consta de una serie de elementos: nombre del componente, procedencia (puede aparecer 0, 1 o más países), número de serie del componente, peso del componente individual y unidad de peso que puede aparecer o no.
  

#### SOLUCIÓN
``` xml
<?xml version="1.0" encoding="UTF-8"?>

<!DOCTYPE entrega [

    <!ELEMENT entrega (lotes)>
    <!ELEMENT lotes (lote+)>
    <!ELEMENT lote (pale+)>
    <!ELEMENT pale (numCajas, contenidoPeso, formaManipulacion)>
    <!ELEMENT contenidoPeso (nombreComponente, procedencia?, numSerie, peso, unidadPeso?)>
    <!ELEMENT numCajas (#PCDATA)>
    <!ELEMENT nombreComponente (#PCDATA)>
    <!ELEMENT procedencia (#PCDATA)>
    <!ELEMENT numSerie (#PCDATA)>
    <!ELEMENT peso (#PCDATA)>
    <!ELEMENT unidadPeso (#PCDATA)>
    <!ELEMENT formaManipulacion (#PCDATA)>
]>

<entrega>
    <lotes> <!-- + -->
        <lote>
            <pale> <!-- + -->
                <numCajas></numCajas>
                <contenidoPeso>
                    <nombreComponente></nombreComponente>
                    <procedencia></procedencia> <!-- ? + -->
                    <numSerie></numSerie>
                    <peso></peso>
                    <unidadPeso></unidadPeso> <!-- ? -->
                </contenidoPeso>
                <formaManipulacion></formaManipulacion>
            </pale> 
        </lote>
    </lotes>
</entrega>
```