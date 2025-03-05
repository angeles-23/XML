### Tarea: Crear un XML, DTD y XSD para la Gestión de una Biblioteca Digital

### Instrucciones Generales:

Deberás crear tres documentos:
1. **XML**: Contiene la información de una biblioteca digital (autores, libros y usuarios) basada en los datos proporcionados en el **JSON** adjunto.
2. **DTD**: Define las reglas para validar la estructura del XML.
3. **XSD**: Define las reglas avanzadas de validación, incluyendo restricciones para los atributos y elementos.

---

### Especificaciones del XML:

#### **Estructura General del XML:**
- El documento XML tiene un elemento raíz llamado `<biblioteca>`.
- El elemento `<biblioteca>` contiene tres secciones:
  - `<autores>`: Lista de autores registrados.
  - `<libros>`: Lista de libros disponibles.
  - `<usuarios>`: Lista de usuarios registrados en la biblioteca.

#### **Datos del XML:**
El contenido del XML **debe basarse en la información proporcionada en el siguiente JSON**:

```json
{
    "biblioteca": {
        "autores": [
            {
                "id": "A1",
                "nombre": "Gabriel García Márquez",
                "nacionalidad": "Colombiana",
                "fechaNacimiento": "1927-03-06"
            },
            {
                "id": "A2",
                "nombre": "Jane Austen",
                "nacionalidad": "Británica",
                "fechaNacimiento": "1775-12-16"
            },
            {
                "id": "A3",
                "nombre": "Isaac Asimov",
                "nacionalidad": "Rusa",
                "fechaNacimiento": "1920-01-02"
            },
            {
                "id": "A4",
                "nombre": "Haruki Murakami",
                "nacionalidad": "Japonesa",
                "fechaNacimiento": "1949-01-12"
            },
            {
                "id": "A5",
                "nombre": "J.K. Rowling",
                "nacionalidad": "Británica",
                "fechaNacimiento": "1965-07-31"
            }
        ],
        "libros": [
            {
                "isbn": "978-3-16-148410-0",
                "autorId": "A1",
                "titulo": "Cien Años de Soledad",
                "genero": "Novela",
                "anioPublicacion": 1967,
                "disponibilidad": {
                    "estado": "Disponible",
                    "usuario": null
                }
            },
            {
                "isbn": "978-0-19-953556-9",
                "autorId": "A2",
                "titulo": "Orgullo y Prejuicio",
                "genero": "Romance",
                "anioPublicacion": 1813,
                "disponibilidad": {
                    "estado": "Prestado",
                    "usuario": "Usuario 3"
                }
            },
            {
                "isbn": "978-0-345-38644-0",
                "autorId": "A3",
                "titulo": "Fundación",
                "genero": "Ciencia Ficción",
                "anioPublicacion": 1951,
                "disponibilidad": {
                    "estado": "Reservado",
                    "usuario": "Usuario 2"
                }
            },
            {
                "isbn": "978-1-101-90694-2",
                "autorId": "A4",
                "titulo": "Kafka en la Orilla",
                "genero": "Ficción",
                "anioPublicacion": 2002,
                "disponibilidad": {
                    "estado": "Disponible",
                    "usuario": null
                }
            },
            {
                "isbn": "978-0-7475-3269-9",
                "autorId": "A5",
                "titulo": "Harry Potter y la Piedra Filosofal",
                "genero": "Fantasía",
                "anioPublicacion": 1997,
                "disponibilidad": {
                    "estado": "Prestado",
                    "usuario": "Usuario 5"
                }
            }
        ],
        "usuarios": [
            {
                "id": "U1",
                "nombre": "Juan Pérez",
                "email": "juan.perez@example.com",
                "librosPrestados": [
                    "978-0-19-953556-9"
                ]
            },
            {
                "id": "U2",
                "nombre": "Ana García",
                "email": "ana.garcia@example.com",
                "librosPrestados": [
                    "978-0-345-38644-0"
                ]
            },
            {
                "id": "U3",
                "nombre": "Carlos Ruiz",
                "email": "carlos.ruiz@example.com",
                "librosPrestados": [
                    "978-0-7475-3269-9"
                ]
            },
            {
                "id": "U4",
                "nombre": "María López",
                "email": "maria.lopez@example.com",
                "librosPrestados": []
            },
            {
                "id": "U5",
                "nombre": "Sofía Fernández",
                "email": "sofia.fernandez@example.com",
                "librosPrestados": []
            }
        ]
    }
}
```

### Especificaciones del DTD:

1. **Define los elementos:**
   - `<biblioteca>` es el elemento raíz.
   - `<autores>`, `<libros>` y `<usuarios>` son hijos directos de `<biblioteca>`.
   - `<autor>`, `<libro>` y `<usuario>` son hijos de `<autores>`, `<libros>` y `<usuarios>`, respectivamente.

2. **Define los atributos:**
   - Los autores y usuarios tienen un atributo obligatorio `id` (único).
   - Los libros tienen un atributo `isbn` (único) y `autorId` para referenciar a un autor.
   - `<disponibilidad>` tiene un atributo `estado` con valores enumerados `"Disponible"`, `"Prestado"` o `"Reservado"`.

---

### Especificaciones del XSD:

1. **Define las claves (`ID` y `IDREF`):**
   - El atributo `id` de `<autor>` y `<usuario>`, así como el atributo `isbn` de `<libro>`, deben ser únicos.
   - El atributo `autorId` de `<libro>` debe referenciar un `id` de la lista de autores.

2. **Define restricciones avanzadas:**
   - Los años de publicación deben ser un número entero de 4 dígitos.
   - Los correos electrónicos deben cumplir con un patrón válido.
   - Las referencias (`autorId`, `usuario`) deben ser consistentes con los elementos definidos en el XML.

---

### Entregables:

1. **XML**: Archivo basado en el JSON proporcionado.
2. **DTD**: Define la estructura básica del XML.
3. **XSD**: Incluye restricciones avanzadas.


#### SOLUCIÓN XML
``` xml
<biblioteca>
    <autores>
        <autor id="A1"> <!-- id obligatorio y único-->
            <nombre>Gabriel García Márquez</nombre>
            <nacionalidad>Colombiana</nacionalidad>
            <fechaNacimiento>1927-03-06</fechaNacimiento>
        </autor>
        <autor id="A2">
            <nombre>Jane Austen</nombre>
            <nacionalidad>Británica</nacionalidad>
            <fechaNacimiento>1775-12-16</fechaNacimiento>
        </autor>
        <autor id="A3">
            <nombre>Isaac Asimov</nombre>
            <nacionalidad>Rusa</nacionalidad>
            <fechaNacimiento>1920-01-02</fechaNacimiento>
        </autor>
        <autor id="A4">
            <nombre>Haruki Murakami</nombre>
            <nacionalidad>Japonesa</nacionalidad>
            <fechaNacimiento>1949-01-12</fechaNacimiento>
        </autor>
        <autor id="A5"> 
            <nombre>J.K. Rowling</nombre>
            <nacionalidad>Británica</nacionalidad>
            <fechaNacimiento>1965-07-31</fechaNacimiento>
        </autor>
    </autores>
    
    <libros>
        <libro isbn="978-3-16-148410-0" autorId="A1">  <!--  isbn único y obligatorio,  autorId referencia al id de autor -->
            <titulo>Cien Años de Soledad</titulo>
            <genero>Novela</genero>
            <anioPublicacion>1967</anioPublicacion>  <!-- año: nº enteros de 4 dígitos -->
            <disponibilidad estado="Disponible">  <!-- "Disponible"|"Prestado"|"Reservado" -->
                <usuario>null</usuario>
            </disponibilidad>
        </libro>
        <libro isbn="978-0-19-953556-9" autorId="A2"> 
            <titulo>Orgullo y Prejuicio</titulo>
            <genero>Romance</genero>
            <anioPublicacion>1813</anioPublicacion>
            <disponibilidad estado="Prestado"> 
                <usuario>Usuario 3</usuario>
            </disponibilidad>
        </libro>
        <libro isbn="978-0-345-38644-0" autorId="A3">
            <titulo>Fundación</titulo>
            <genero>Ciencia Ficción</genero>
            <anioPublicacion>1951</anioPublicacion> 
            <disponibilidad estado="Reservado">
                <usuario>Usuario 2</usuario>
            </disponibilidad>
        </libro>
        <libro isbn="978-1-101-90694-2" autorId="A4"> 
            <titulo>Kafka en la Orilla</titulo>
            <genero>Ficción</genero>
            <anioPublicacion>2002</anioPublicacion>
            <disponibilidad estado="Disponible"> 
                <usuario>null</usuario>
            </disponibilidad>
        </libro>
        <libro isbn="978-0-7475-3269-9" autorId="A5"> 
            <titulo>Harry Potter y la Piedra Filosofal</titulo>
            <genero>Fantasía</genero>
            <anioPublicacion>1997</anioPublicacion>
            <disponibilidad estado="Prestado"> 
                <usuario>Usuario 5</usuario>
            </disponibilidad>
        </libro>
        
    </libros>
    
    <usuarios>
        <usuario id="U1"> <!-- id obligatorio y único-->
            <nombre>Juan Pérez</nombre>
            <email>juan.perez@example.com</email> <!-- Formato válido -->
            <librosPrestados>978-0-19-953556-9</librosPrestados>
        </usuario>
        <usuario id="U2">
            <nombre>Ana García</nombre>
            <email>ana.garcia@example.com</email>
            <librosPrestados>978-0-345-38644-0</librosPrestados>
        </usuario>
        <usuario id="U3">
            <nombre>Carlos Ruiz</nombre>
            <email>carlos.ruiz@example.com</email>
            <librosPrestados>978-0-7475-3269-9</librosPrestados>
        </usuario>
        <usuario id="U4">
            <nombre>María López</nombre>
            <email>maria.lopez@example.com</email>
            <librosPrestados></librosPrestados>
        </usuario>
        <usuario id="U5">
            <nombre>Sofía Fernández</nombre>
            <email>sofia.fernandez@example.com</email>
            <librosPrestados></librosPrestados>
        </usuario>
    </usuarios>
</biblioteca>
```

#### SOLUCIÓN DTD
``` xml
<!DOCTYPE biblioteca [
  <!ELEMENT biblioteca (autores, libros, usuarios)>
  <!ELEMENT autores (autor+)>
  <!ATTLIST autor
    id ID #REQUIRED
  >
  <!ELEMENT autor (nombre, nacionalidad, fechaNacimiento)>
  <!ELEMENT libros (libro+)>
  <!ATTLIST libro 
    isbn ID #REQUIRED
    autorId IDREF #REQUIRED
  >
  <!ELEMENT libro (titulo, genero, anioPublicacion, disponibilidad)>
  <!ATTLIST disponibilidad
    estado (Disponible|Prestado|Reservado) #REQUIRED
  >
  <!ELEMENT disponibilidad (usuario)>
  <!ELEMENT usuarios (usuario+)>
  <!ATTLIST usuario
    id ID #REQUIRED
  >
  <!ELEMENT usuario (nombre, email, librosPrestados)>
  <!ELEMENT nombre (#PCDATA)>
  <!ELEMENT nacionalidad (#PCDATA)>
  <!ELEMENT fechaNacimiento (#PCDATA)>
  <!ELEMENT titulo (#PCDATA)>
  <!ELEMENT genero (#PCDATA)>
  <!ELEMENT anioPublicacion (#PCDATA)>
  <!ELEMENT usuario (#PCDATA)>
  <!ELEMENT email (#PCDATA)>
  <!ELEMENT librosPrestados (#PCDATA)>

]>
```

#### SOLUCIÓN XSD
``` xml
<?xml version="1.0" encoding="UTF-8"?>
<xsd:schema xmlns:xsd="http://www.w3.org/2001/XMLSchema">

  <xsd:element name="biblioteca">
    <xsd:complexType>
      <xsd:sequence>
        <xsd:element name="autores" type="autoresType"/>
        <xsd:element name="libros" type="librosType"/>
        <xsd:element name="usuarios" type="usuariosType"/>
      </xsd:sequence>
    </xsd:complexType>
    
    <xsd:key name="claveIDAutor">
      <xsd:selector xpath="autores/autor"/>
      <xsd:field xpath="@id"/>
    </xsd:key>
    
    <xsd:key name="claveIDLibro">
      <xsd:selector xpath="libros/libro"/>
      <xsd:field xpath="@isbn"/>
    </xsd:key>
    
    <xsd:keyref name="claveAutorIDRef" refer="claveIDAutor">
      <xsd:selector xpath="libros/libro"/>
      <xsd:field xpath="@autorId"/>
    </xsd:keyref>
    
    <xsd:key name="claveIDUsuario">
      <xsd:selector xpath="usuarios/usuario"/>
      <xsd:field xpath="@id"/>
    </xsd:key>
  </xsd:element>
  
  <xsd:complexType name="autoresType">
    <xsd:sequence>
      <xsd:element name="autor" type="autorType" maxOccurs="unbounded"/>
    </xsd:sequence>
  </xsd:complexType>
  
  <xsd:complexType name="autorType">
    <xsd:sequence>
      <xsd:element name="nombre" type="xsd:string"/>
      <xsd:element name="nacionalidad" type="xsd:string"/>
      <xsd:element name="fechaNacimiento" type="xsd:date"/>
    </xsd:sequence>
    <xsd:attribute name="id" type="idAutorType" use="required"/>
  </xsd:complexType>
  
  <xsd:simpleType name="idAutorType">
    <xsd:restriction base="xsd:string">
      <xsd:pattern value="A[0-9]"/>
    </xsd:restriction>
  </xsd:simpleType>
  
  <xsd:complexType name="librosType">
    <xsd:sequence>
      <xsd:element name="libro" type="libroType" maxOccurs="unbounded"/>
    </xsd:sequence>
  </xsd:complexType>
  
  <xsd:complexType name="libroType">
    <xsd:sequence>
      <xsd:element name="titulo" type="xsd:string"/>
      <xsd:element name="genero" type="xsd:string"/>
      <xsd:element name="anioPublicacion" type="anioPublicacionType"/>
      <xsd:element name="disponibilidad" type="disponibilidadType"/>
    </xsd:sequence>
    <xsd:attribute name="isbn" type="isbnType" use="required"/>
    <xsd:attribute name="autorId" type="idAutorType" use="required"/>
  </xsd:complexType>
  
  <xsd:simpleType name="anioPublicacionType">
    <xsd:restriction base="xsd:integer">
      <xsd:minInclusive value="1800"/>
      <xsd:maxInclusive value="2500"/>
    </xsd:restriction>
  </xsd:simpleType>
  
  <xsd:simpleType name="isbnType">
    <xsd:restriction base="xsd:string">
      <xsd:pattern value="[0-9]{3}-[0-9]{1}-[0-9]{2,4}-[0-9]{4,6}-[0-9]{1}"/>
    </xsd:restriction>
  </xsd:simpleType>
  
  <xsd:complexType name="disponibilidadType">
    <xsd:sequence>
      <xsd:element name="usuario" type="xsd:string"/>
    </xsd:sequence>
    <xsd:attribute name="estado" type="estadoType" use="required"/>
  </xsd:complexType>
  
  <xsd:simpleType name="estadoType">
    <xsd:restriction base="xsd:string">
      <xsd:enumeration value="Disponible"/>
      <xsd:enumeration value="Prestado"/>
      <xsd:enumeration value="Reservado"/>
    </xsd:restriction>
  </xsd:simpleType>
  
  <xsd:complexType name="usuariosType">
    <xsd:sequence>
      <xsd:element name="usuario" type="usuarioType" minOccurs="0" maxOccurs="unbounded"/>
    </xsd:sequence>
  </xsd:complexType>
  
  <xsd:complexType name="usuarioType">
    <xsd:sequence>
      <xsd:element name="nombre" type="xsd:string"/>
      <xsd:element name="email" type="emailType"/>
      <xsd:element name="librosPrestados" type="xsd:string"/>
    </xsd:sequence>
    <xsd:attribute name="id" type="idUsuarioType" use="required"/>
  </xsd:complexType>
  
  <xsd:simpleType name="emailType">
    <xsd:restriction base="xsd:string">
      <xsd:pattern value="[a-zA-Z0-9._+-]+@[a-zA-Z0-9._+-]+\.[a-z]{2,10}"/>
    </xsd:restriction>
  </xsd:simpleType>
  
  <xsd:simpleType name="idUsuarioType">
    <xsd:restriction base="xsd:string">
      <xsd:pattern value="U[0-9]"/>
    </xsd:restriction>
  </xsd:simpleType>
  
</xsd:schema>
```