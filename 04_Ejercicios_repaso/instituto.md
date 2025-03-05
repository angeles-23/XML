# 📌 Enunciado del Ejercicio: Creación de un Esquema XSD para un Instituto

## 🎯 Objetivo
El objetivo de este ejercicio es que los estudiantes diseñen un esquema **XSD (XML Schema Definition)** que valide un archivo XML que modela la estructura de un instituto. El esquema debe incluir restricciones específicas sobre los datos para garantizar la coherencia y validez del XML.

---

## 📖 Enunciado
Se proporciona la estructura de un instituto en XML que contiene **cursos, asignaturas, departamentos y alumnos**. Tu tarea consiste en diseñar un esquema **XSD** que valide este XML, aplicando las siguientes restricciones:

### 📌 Requisitos del Esquema XSD

### 1️⃣ Estructura General
- El elemento raíz debe ser `<instituto>`, que contendrá los elementos `<cursos>`, `<asignaturas>`, `<departamentos>` y `<alumnos>`.

### 2️⃣ Cursos
- `<cursos>` debe dividirse en `<secundaria>` y `<formacion_profesional>`.
- En **secundaria**, debe haber `<ano>` con un atributo obligatorio `id` que solo puede tomar valores **"1ESO", "2ESO", "3ESO" o "4ESO"**.
- Dentro de cada `<ano>`, debe haber al menos una `<letra>` con un atributo `id` que solo puede ser **"A", "B" o "C"**. Dentro de `<letra>` viene la información del número de alumnos matriculados (máximo 30 alumnos por letra)
- En **formación profesional**, se deben definir las ramas `<GEA>`, `<DAW>` y `<ASIR>`, cada una con `<curso>` que tenga un atributo `id` con valores **"GEA1", "GEA2", "DAW1", "DAW2", "ASIR1", "ASIR2"**. Dentro de cada `<curso>` viene la información del número de alumnos matriculados (máximo 25 alumnos por curso)

### 3️⃣ Asignaturas
- Cada `<asignatura>` debe tener los siguientes atributos:
  - `id` (obligatorio y único).
  - `nombre` (obligatorio y de tipo string).
  - `imparten` (referencia a uno o más cursos válidos mediante `keyref`).
  - Ej: `<asignatura id="FIS1" nombre="Física y Química" imparten="3ESO 4ESO"/>`

### 4️⃣ Departamentos
- Cada `<departamento>` debe tener un atributo `id` y al menos **tres `<profesor>`**.
- Cada `<profesor>` debe tener los atributos:
  - `id` (obligatorio y único).
  - `nombre` (cadena de al menos 3 caracteres y máximo 50).
- Ej:
```xml
<departamento id="MAT">
            <profesor id="P001" nombre="Antonio García"/>
            <profesor id="P002" nombre="María López"/>
            <profesor id="P003" nombre="Carlos Fernández"/>
        </departamento>
```

### 5️⃣ Alumnos
- Cada `<alumno>` debe contener los atributos:
  - `id` (obligatorio y único). Sigue el formato de `A577841` donde "A" significa alumno y el numero es el de murciaeduca. 
  - `curso` (referencia a un curso válido).
  - `letra` (opcional, solo si el curso es de secundaria, y su valor puede ser "A", "B" o "C").
  - `edad` (entero, entre **12 y 20 años**).
  - `repetidor` (valor "S" o "N" únicamente).
  - Informacion con el nombre completo del alumno: "Joaquín Reyes Amador"

### 6️⃣ Restricciones Adicionales
- Se debe utilizar **key/keyref** para garantizar la integridad referencial en los cursos y asignaturas.
- El orden de los elementos dentro de `<instituto>` debe respetarse: **cursos → asignaturas → departamentos → alumnos**.

---

## 📌 Entrega
- Archivo **XSD** con las validaciones y restricciones indicadas.
- Archivo **DTD** con validaciones y restricciones.
- Archivo **XML** de prueba validado con tu esquema.
- **Informe en formato MarkDown** explicando la estructura del XSD y las validaciones implementadas.

⚠️ **Importante**: Si el XML no cumple con las restricciones definidas en el XSD, se considerará incorrecto.



### XSD
```xml
<xsd:schema xmlns:xsd="http://www.w3.org/2001/XMLSchema">

  <xsd:element name="instituto">
    <xsd:complexType>
      <xsd:sequence>
        <xsd:element name="cursos" type="cursosType"/>
        <xsd:element name="asignaturas" type="asignaturasType"/>
        <xsd:element name="departamentos" type="departamentosType"/>
        <xsd:element name="alumnos" type="alumnosType"/>
      </xsd:sequence>
    </xsd:complexType>
  
    <xsd:key name="claveAsignatura">
      <xsd:selector xpath="asignaturas/asignatura"/>
      <xsd:field xpath="@id"/>
    </xsd:key>
    
    <xsd:key name="claveDepartamento">
      <xsd:selector xpath="departamentos/departamento"/>
      <xsd:field xpath="@id"/>
    </xsd:key>
    
    <xsd:key name="claveAlumno">
      <xsd:selector xpath="alumnos/alumno"/>
      <xsd:field xpath="@id"/>
    </xsd:key>
    
    <xsd:key name="claveCursoSecundaria">
      <xsd:selector xpath="cursos/secundaria/ano"/>
      <xsd:field xpath="@id"/>
    </xsd:key>
    
    <xsd:key name="claveCursoFP">
      <xsd:selector xpath="cursos/formacion_profesional/*/curso"/>
      <xsd:field xpath="@id"/>
    </xsd:key>
    
    <xsd:keyref name="claveImpartenRefSecundaria" refer="claveCursoSecundaria">
      <xsd:selector xpath="asignaturas/asignatura"/>
      <xsd:field xpath="@imparten"/>
    </xsd:keyref>
    
    <xsd:keyref name="claveImpartenRefFP" refer="claveCursoFP">
      <xsd:selector xpath="asignaturas/asignatura"/>
      <xsd:field xpath="@imparten"/>
    </xsd:keyref>
  </xsd:element>
  
  <xsd:complexType name="cursosType">
    <xsd:sequence>
      <xsd:element name="secundaria" type="secundariaType"/>
      <xsd:element name="formacion_profesional" type="fpType"/>
    </xsd:sequence>
  </xsd:complexType>
  
  <xsd:complexType name="secundariaType">
    <xsd:sequence>
      <xsd:element name="ano" type="anoType" maxOccurs="unbounded"/>
    </xsd:sequence>
  </xsd:complexType>

  <xsd:complexType name="anoType">
    <xsd:sequence>
      <xsd:element name="letra" type="letraType" minOccurs="1" maxOccurs="unbounded"/>
    </xsd:sequence>
    <xsd:attribute name="id" type="idAnoType" use="required"/>
  </xsd:complexType>
  
  <xsd:simpleType name="idAnoType">
    <xsd:restriction base="xsd:string">
      <xsd:enumeration value="1ESO"/>
      <xsd:enumeration value="2ESO"/>
      <xsd:enumeration value="3ESO"/>
      <xsd:enumeration value="4ESO"/>
    </xsd:restriction>
  </xsd:simpleType>
  
  <xsd:complexType name="letraType">
    <xsd:simpleContent>
      <xsd:extension base="letraRestriccionType">
        <xsd:attribute name="id" type="idLetraType" use="required"/>
      </xsd:extension>
    </xsd:simpleContent>
  </xsd:complexType>

  <xsd:simpleType name="idLetraType">
    <xsd:restriction base="xsd:string">
      <xsd:enumeration value="A"/>
      <xsd:enumeration value="B"/>
      <xsd:enumeration value="C"/>
    </xsd:restriction>
  </xsd:simpleType>

  <xsd:simpleType name="letraRestriccionType">
    <xsd:restriction base="xsd:integer">
      <xsd:minInclusive value="0"/>
      <xsd:maxInclusive value="30"/>
    </xsd:restriction>
  </xsd:simpleType>

  <xsd:complexType name="fpType">
    <xsd:sequence>
      <xsd:element name="GEA" type="gradoType" maxOccurs="2"/>
      <xsd:element name="DAW" type="gradoType" maxOccurs="2"/>
      <xsd:element name="ASIR" type="gradoType" maxOccurs="2"/>
    </xsd:sequence>
  </xsd:complexType>

  <xsd:complexType name="gradoType">
    <xsd:sequence>
      <xsd:element name="curso" type="cursoType" maxOccurs="2"/>
    </xsd:sequence>
  </xsd:complexType>
  
  <xsd:complexType name="cursoType">
    <xsd:simpleContent>
      <xsd:extension base="cursoGradoType">
        <xsd:attribute name="id" type="idCursoType" use="required"/>
      </xsd:extension>
    </xsd:simpleContent>
  </xsd:complexType>
  
  <xsd:simpleType name="cursoGradoType">
    <xsd:restriction base="xsd:integer">
      <xsd:minInclusive value="0"/>
      <xsd:maxInclusive value="25"/>
    </xsd:restriction>
  </xsd:simpleType>
  
  <xsd:simpleType name="idCursoType">
    <xsd:restriction base="xsd:string">
      <xsd:enumeration value="GEA1"/>
      <xsd:enumeration value="GEA2"/>
      <xsd:enumeration value="DAW1"/>
      <xsd:enumeration value="DAW2"/>
      <xsd:enumeration value="ASIR1"/>
      <xsd:enumeration value="ASIR2"/>
    </xsd:restriction>
  </xsd:simpleType>

  <xsd:complexType name="asignaturasType">
    <xsd:sequence>
      <xsd:element name="asignatura" type="asignaturaType" maxOccurs="unbounded"/>
    </xsd:sequence>
  </xsd:complexType>
  
  <xsd:complexType name="asignaturaType">
    <xsd:attribute name="id" type="xsd:string" use="required"/>
    <xsd:attribute name="nombre" type="xsd:string" use="required"/>
    <xsd:attribute name="imparten" type="xsd:string"/>
  </xsd:complexType>
  
  <xsd:complexType name="departamentosType">
    <xsd:sequence>
      <xsd:element name="departamento" type="departamentoType" maxOccurs="unbounded"/>
    </xsd:sequence>
  </xsd:complexType>
  
  <xsd:complexType name="departamentoType">
    <xsd:sequence>
      <xsd:element name="profesor" type="profesorType" minOccurs="3" maxOccurs="unbounded"/>
    </xsd:sequence>
    <xsd:attribute name="id" type="idDepartamentoType" use="required"/>
  </xsd:complexType>
  
  <xsd:simpleType name="idDepartamentoType">
    <xsd:restriction base="xsd:string">
      <xsd:pattern value="[A-Z]{3}"/>
    </xsd:restriction>
  </xsd:simpleType>  
  
  <xsd:complexType name="profesorType">
    <xsd:attribute name="id" type="idProfesorType" use="required"/>
    <xsd:attribute name="nombre" type="nombreProfesorType" use="required"/>
  </xsd:complexType>
  
  <xsd:simpleType name="idProfesorType">
    <xsd:restriction base="xsd:string">
      <xsd:pattern value="P[0-9]{3}"/>
    </xsd:restriction>
  </xsd:simpleType>
  
  <xsd:simpleType name="nombreProfesorType">
    <xsd:restriction base="xsd:string">
      <xsd:minLength value="3"/>
      <xsd:maxLength value="50"/>
    </xsd:restriction>
  </xsd:simpleType>
  
  <xsd:complexType name="alumnosType">
    <xsd:sequence>
      <xsd:element name="alumno" type="alumnoType" maxOccurs="unbounded"/>
    </xsd:sequence>
  </xsd:complexType>
  
  <xsd:complexType name="alumnoType">
    <xsd:simpleContent>
      <xsd:extension base="xsd:string">
        <xsd:attribute name="id" type="idAlumnoType" use="required"/>
        <xsd:attribute name="curso" type="idCursoType" use="required"/>
        <xsd:attribute name="letra" type="idLetraType" use="optional"/>
        <xsd:attribute name="edad" type="edadType" use="required"/>
        <xsd:attribute name="repetidor" type="repetidorType" use="required"/>
      </xsd:extension>
    </xsd:simpleContent>
  </xsd:complexType>
  
  <xsd:simpleType name="idAlumnoType">
    <xsd:restriction base="xsd:string">
      <xsd:pattern value="A[0-9]{6}"/>
    </xsd:restriction>
  </xsd:simpleType>
  
  <xsd:simpleType name="edadType">
    <xsd:restriction base="xsd:integer">
      <xsd:minInclusive value="12"/>
      <xsd:maxInclusive value="20"/>
    </xsd:restriction>
  </xsd:simpleType>
  
  <xsd:simpleType name="repetidorType">
    <xsd:restriction base="xsd:string">
      <xsd:enumeration value="S"/>
      <xsd:enumeration value="N"/>
    </xsd:restriction>
  </xsd:simpleType>
  
</xsd:schema>
```


### XML
```xml
<?xml version="1.0" encoding="UTF-8"?>

<instituto>
    <cursos>
        <secundaria>
            <ano id="1ESO"> <!-- "1ESO", "2ESO", "3ESO" o "4ESO" -->
                <letra id="A">25</letra><!-- "A", "B" o "C" -->
                <letra id="B">30</letra><!-- "A", "B" o "C" -->
            </ano> 
            <ano id="2ESO"> <!-- "1ESO", "2ESO", "3ESO" o "4ESO" -->
                <letra id="B">28</letra><!-- "A", "B" o "C" -->
            </ano> 
        </secundaria>
        <formacion_profesional>
            <GEA>
                <curso id="GEA1">20</curso> <!--  "GEA1", "GEA2" -->
                <curso id="GEA2">22</curso> 
            </GEA>
            <DAW>
                <curso id="DAW1">18</curso> <!--  "DAW1", "DAW2" -->
                <curso id="DAW2">19</curso> 
            </DAW>
            <ASIR>
                <curso id="ASIR1">21</curso> <!--  "ASIRA", "ASIR2" -->
                <curso id="ASIR2">20</curso>
            </ASIR>
        </formacion_profesional>
    </cursos>
  
    <asignaturas>
        <asignatura id="FIS1" nombre="Física y Química" imparten="1ESO 2ESO"/>
        <asignatura id="MAT1" nombre="Matemáticas" imparten="GEA1 DAW1"/>
    </asignaturas>
    
    <departamentos>
        <departamento id="MAT">
        <profesor id="P001" nombre="Antonio García"/>
        <profesor id="P002" nombre="María López"/>
        <profesor id="P003" nombre="Carlos Fernández"/>
        </departamento>
    </departamentos>
    
    <alumnos>
        <alumno id="A577841" curso="GEA1" letra="A" edad="15" repetidor="N">Joaquín Reyes Amador</alumno>
        <alumno id="A577842" curso="2ESO" letra="C" edad="15" repetidor="S">María Jiménez Torres</alumno>
        <alumno id="A577843" curso="DAW1" letra="GEA1" edad="17" repetidor="N">Santiago Pérez Casas</alumno>
    </alumnos>
  
</instituto>
```

### DTD
```xml
<!DOCTYPE instituto [
  <!ELEMENT instituto (cursos, asignaturas, departamentos, alumnos)>
  <!ELEMENT cursos (secundaria, formacion_profesional)>
  <!ELEMENT secundaria (ano+)>
  <!ELEMENT ano (letra?)>
  <!ATTLIST ano
    id (1ESO|2ESO|3ESO|4ESO) #REQUIRED
  >
  <!ATTLIST letra
    id (A|B|C) #REQUIRED
  >
  <!ELEMENT formacion_profesional (GEA, DAW, ASIR)+>
  <!ELEMENT GEA (curso+)>
  <!ELEMENT DAW (curso+)>
  <!ELEMENT ASIR (curso+)>
  <!ATTLIST curso
    id CDATA #REQUIRED
  >
  <!ELEMENT asignaturas (asignatura+)>
  <!ATTLIST asignatura
    id ID #REQUIRED
    nombre CDATA #REQUIRED
    imparten IDREF #REQUIRED
  >
  <!ELEMENT departamentos (departamento+)>
  <!ELEMENT departamento (profesor+)>
  <!ATTLIST departamento
    id ID #REQUIRED
  >
  <!ATTLIST profesor
    id ID #REQUIRED
    nombre CDATA #REQUIRED
  >
  <!ELEMENT alumnos (alumno+)>
  <!ATTLIST alumno
    id ID #REQUIRED
    curso IDREF #REQUIRED
    letra IDRED #REQUIRED
    repetidor CDATA #REQUIRED
  >
  <!ELEMENT asignatura EMPTY>
  <!ELEMENT departamento EMPTY>
  <!ELEMENT letra (#PCDATA)>
  <!ELEMENT curso (#PCDATA)>
  <!ELEMENT alumno (#PCDATA)>
]>
```