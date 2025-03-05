# Ejercicio 2
Un instituto necesita registrar los cursos y alumnos que estudian en él y necesita una DTD para comprobar los documentos XML de los programas que utiliza:

- Tiene que haber un elemento raíz listacursos. Tiene que haber uno o más cursos.
- Un curso tiene uno o más alumnos
- Todo alumno tiene un DNI, un nombre y un apellido, puede que tenga segundo apellido o no.
- Un alumno escoge una lista de asignaturas donde habrá una o más asignaturas. Toda asignatura tiene un nombre, un atributo código y un profesor.
- Un profesor tiene un NRP (Número de Registro Personal), un nombre y un apellido (también puede tener o no un segundo apellido).

#### SOLUCIÓN
``` xml
<?xml version="1.0" encoding="UTF-8"?>

<!DOCTYPE listaCursos [
    <!ELEMENT listaCursos (curso+)>
    <!ELEMENT curso (alumno+)>
    <!ELEMENT alumno (dni, nombre,apellido1, apellido2?, listaAsignaturas)>
    <!ELEMENT listaAsignaturas (asignatura+)>
    <!ATTLIST asignatura codigo CDATA #REQUIRED>
    <!ELEMENT asignatura (nombre, profesor)>
    <!ELEMENT profesor (NRP, nombre, apellido1, apellido2?)>
    <!ELEMENT dni (#PCDATA)>
    <!ELEMENT nombre (#PCDATA)>
    <!ELEMENT apellido1 (#PCDATA)>
    <!ELEMENT apellido2 (#PCDATA)>
    <!ELEMENT NRP (#PCDATA)>
]>



<listaCursos>
    <curso> <!-- + -->
        <alumno> <!-- + -->
            <dni>165498</dni>
            <nombre>Carol</nombre>
            <apellido1>Kimenez</apellido1>
            <apellido2>Gonzalez</apellido2> <!-- ? -->
            <listaAsignaturas>
                <asignatura codigo="123"> <!-- +, #R -->
                    <nombre>Pedro</nombre>
                    <profesor>
                        <NRP>1564596485</NRP>
                        <nombre>Santiago</nombre>
                        <apellido1>Bernabeu</apellido1>
                    </profesor>
                </asignatura>
            </listaAsignaturas>
        </alumno>
    </curso>
</listaCursos>
```