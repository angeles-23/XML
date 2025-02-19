### Tarea: Crear un XML, DTD y XSD para la Gestión de Eventos

### Instrucciones Generales:
Deberás crear tres documentos:
1. **XML**: Contendrá información sobre una agenda de eventos.
2. **DTD**: Definirá las reglas básicas para validar la estructura del XML.
3. **XSD**: Especificará las reglas avanzadas de validación, incluyendo restricciones para atributos y elementos.

### Especificaciones del XML:

#### **Estructura General del XML:**
- El documento XML tiene un elemento raíz llamado `<agenda>`.
- Dentro de `<agenda>` hay dos secciones principales:
  - `<eventos>`: Lista de eventos.
  - `<relaciones>`: Conexiones entre eventos.

#### **Detalles de cada sección:**

##### **1. Lista de eventos:**
- Cada evento será un elemento `<evento>` dentro de `<eventos>`.
- Atributos y elementos requeridos:
  - **`id` (atributo)**: Identificador único del evento.
  - **`tipo` (atributo)**: Tipo del evento ("Conferencia", "Taller", "Reunión", "Mesa Redonda").
  - `<fecha>`: Fecha del evento en formato `AAAA-MM-DD`.
  - `<hora>`: Hora del evento en formato `HH:MM`.
  - `<lugar>`: Información del lugar, con los siguientes sub-elementos:
    - `<calle>`: Dirección específica.
    - `<ciudad>`: Ciudad.
    - `<pais>`: País.
  - `<participantes>`: Contiene una lista de participantes, donde cada uno es un elemento `<participante>` con:
    - `<nombre>`: Nombre completo del participante.
    - `<email>`: Correo electrónico del participante.
    - `<rol>`: Rol del participante en el evento ("Ponente", "Moderador", "Asistente", etc.).

##### **2. Relaciones entre eventos:**
- Cada relación será un elemento `<relacion>` dentro de `<relaciones>`.
- Atributos requeridos:
  - **`origen` (atributo)**: Referencia al `id` del evento de origen.
  - **`destino` (atributo)**: Referencia al `id` del evento relacionado.

#### **Contenido Requerido:**
- **4 eventos** con información completa (tipo, fecha, hora, lugar, participantes).
- **3 relaciones** que conecten eventos mediante sus IDs.

``` xml
<?xml version="1.0" encoding="UTF-8"?>

<agenda>
  <eventos>
    <evento id="e_001" tipo="Conferencia">
      <fecha>2024-02-05</fecha> <!-- AAAA-MM-DD -->
      <hora>11:45</hora>   <!-- HH:MM -->
      <lugar>
        <calle>Juan Carlos I</calle>
        <ciudad>Lorca</ciudad>
        <pais>España</pais>
      </lugar>
      <participantes>
        <participante>
          <nombre>Miguel Fernández Cuadrado</nombre>
          <email>miguel@gmail.com</email>
          <rol>Asistente</rol>
        </participante>
      </participantes>
    </evento>
    
    <evento id="e_002" tipo="Taller">
      <fecha>2024-06-08</fecha> <!-- AAAA-MM-DD -->
      <hora>10:45</hora>   <!-- HH:MM -->
      <lugar>
        <calle>Avenida Libertad</calle>
        <ciudad>Madrid</ciudad>
        <pais>España</pais>
      </lugar>
      <participantes>
        <participante>
          <nombre>Ana López Pérez</nombre>
          <email>ana@gmail.com</email>
          <rol>Ponente</rol>
        </participante>
      </participantes>
    </evento>
    
    <evento id="e_003" tipo="Reunión">
      <fecha>2024-09-07</fecha> <!-- AAAA-MM-DD -->
      <hora>16:00</hora>   <!-- HH:MM -->
      <lugar>
        <calle>Calle Mayor</calle>
        <ciudad>Murcia</ciudad>
        <pais>España</pais>
      </lugar>
      <participantes>
        <participante>
          <nombre>Juan Martínez García</nombre>
          <email>juan@gmail.com</email>
          <rol>Moderador</rol>
        </participante>
      </participantes>
    </evento>
    
    <evento id="e_004" tipo="MesaRedonda">
      <fecha>2024-11-19</fecha> <!-- AAAA-MM-DD -->
      <hora>18:00</hora>   <!-- HH:MM -->
      <lugar>
        <calle>Gran Vía</calle>
        <ciudad>Valencia</ciudad>
        <pais>España</pais>
      </lugar>
      <participantes>
        <participante>
          <nombre>Pedro Álvarez Jiménez</nombre>
          <email>pedro@gmail.com</email>
          <rol>Asistente</rol>
        </participante>
      </participantes>
    </evento>
  </eventos>
  
  <relaciones>
    <relacion origen="e_001" destino="e_002"></relacion>
    <relacion origen="e_002" destino="e_003"></relacion>
    <relacion origen="e_003" destino="e_004"></relacion>
  </relaciones>
</agenda>
```





### Especificaciones del DTD:

1. **Define los elementos:**
   - `<agenda>` es el elemento raíz.
   - `<eventos>` y `<relaciones>` son hijos directos de `<agenda>`.
   - `<evento>` es hijo de `<eventos>`.
   - `<relacion>` es hijo de `<relaciones>`.
   - `<participante>` es hijo de `<participantes>`.

2. **Define los atributos:**
   - Los eventos tienen atributos `id` y `tipo`.
   - Las relaciones tienen atributos `origen` y `destino`.

3. **Estructura del DTD:**
   - Define reglas básicas para los elementos y atributos.

``` xml
<?xml version="1.0" encoding="UTF-8"?>

<!DOCTYPE agenda [
  <!ELEMENT agenda (eventos, relaciones)>
  <!ELEMENT eventos (evento+)>
  <!ELEMENT evento (fecha, hora, lugar, participantes)>
  <!ELEMENT lugar (calle, ciudad, pais)>
  <!ELEMENT participantes (participante+)>
  <!ELEMENT participante (nombre, email, rol)>
  <!ELEMENT relaciones (relacion+)>
  <!ATTLIST evento
    id ID #REQUIRED
    tipo (Conferencia|Taller|Reunión|MesaRedonda) #REQUIRED
  >
  <!ATTLIST relacion
    origen IDREF #REQUIRED
    destino IDREF #REQUIRED
  >
  <!ELEMENT fecha (#PCDATA)>
  <!ELEMENT hora (#PCDATA)>
  <!ELEMENT calle (#PCDATA)>
  <!ELEMENT ciudad (#PCDATA)>
  <!ELEMENT pais (#PCDATA)>
  <!ELEMENT nombre (#PCDATA)>
  <!ELEMENT email (#PCDATA)>
  <!ELEMENT rol (#PCDATA)>
  <!ELEMENT relacion (#PCDATA)>
]>
```





### Especificaciones del XSD:

1. **Define las claves (`ID` y `IDREF`):**
   - El atributo `id` de `<evento>` debe ser único.
   - Los atributos `origen` y `destino` de `<relacion>` deben referenciar un `id` existente en la lista de eventos.

2. **Define restricciones avanzadas:**
   - Los elementos `<fecha>` y `<hora>` deben seguir formatos específicos (`AAAA-MM-DD` y `HH:MM`).
   - Los correos electrónicos deben validarse con un patrón que incluya `@` y un dominio.
   - **Restricción adicional:** El elemento `<rol>` debe aceptar únicamente valores predefinidos:
     - "Ponente", "Moderador", "Asistente", "Instructor".
   - **Restricción adicional:** El atributo `tipo` de `<evento>` debe ser uno de los siguientes:
     - "Conferencia", "Taller", "Reunión", "MesaRedonda".
   - **Restricción adicional:** El elemento `<ciudad>` debe tener una longitud mínima de 3 caracteres y máxima de 50 caracteres.

3. **Estructura del XSD:**
   - Define todos los elementos, atributos y sus tipos de datos.
   - Incluye validación de patrones y restricciones de claves.

### Entregables:

1. **XML**: Archivo que contiene información sobre la agenda de eventos.
2. **DTD**: Archivo que define las reglas básicas de validación.
3. **XSD**: Archivo que incluye reglas avanzadas de validación.

---

``` xml
<agenda>
  <eventos>
    <evento id="e_001" tipo="Conferencia">
      <fecha>2024-02-05</fecha> <!-- AAAA-MM-DD -->
      <hora>11:45</hora>   <!-- HH:MM -->
      <lugar>
        <calle>Juan Carlos I</calle>
        <ciudad>Lorca</ciudad>
        <pais>España</pais>
      </lugar>
      <participantes>
        <participante>
          <nombre>Miguel Fernández Cuadrado</nombre>
          <email>miguel@gmail.com</email>
          <rol>Asistente</rol>
        </participante>
      </participantes>
    </evento>
    
    <evento id="e_002" tipo="Taller">
      <fecha>2024-06-08</fecha> <!-- AAAA-MM-DD -->
      <hora>10:45</hora>   <!-- HH:MM -->
      <lugar>
        <calle>Avenida Libertad</calle>
        <ciudad>Madrid</ciudad>
        <pais>España</pais>
      </lugar>
      <participantes>
        <participante>
          <nombre>Ana López Pérez</nombre>
          <email>ana@gmail.com</email>
          <rol>Ponente</rol>
        </participante>
      </participantes>
    </evento>
    
    <evento id="e_003" tipo="Reunión">
      <fecha>2024-09-07</fecha> <!-- AAAA-MM-DD -->
      <hora>16:00</hora>   <!-- HH:MM -->
      <lugar>
        <calle>Calle Mayor</calle>
        <ciudad>Murcia</ciudad>
        <pais>España</pais>
      </lugar>
      <participantes>
        <participante>
          <nombre>Juan Martínez García</nombre>
          <email>juan@gmail.com</email>
          <rol>Moderador</rol>
        </participante>
      </participantes>
    </evento>
    
    <evento id="e_004" tipo="MesaRedonda">
      <fecha>2024-11-19</fecha> <!-- AAAA-MM-DD -->
      <hora>18:00</hora>   <!-- HH:MM -->
      <lugar>
        <calle>Gran Vía</calle>
        <ciudad>Valencia</ciudad>
        <pais>España</pais>
      </lugar>
      <participantes>
        <participante>
          <nombre>Pedro Álvarez Jiménez</nombre>
          <email>pedro@gmail.com</email>
          <rol>Asistente</rol>
        </participante>
      </participantes>
    </evento>
  </eventos>

  <relaciones>
    <relacion origen="e_001" destino="e_002"/>
    <relacion origen="e_002" destino="e_003"/>
    <relacion origen="e_003" destino="e_004"/>
  </relaciones>
</agenda>
```



### 1. SOLICIÓN XML
```xml
<?xml version="1.0" encoding="UTF-8"?>
<agenda>

  <eventos>
    <evento id="e_001" tipo="Conferencia">
      <fecha>2025-02-12</fecha>
      <hora>08:30</hora>
      <lugar>
        <calle>Juan Carlos I</calle>
        <ciudad>Lorca</ciudad>
        <pais>España</pais>
      </lugar>
      <participantes>
        <participante>
          <nombre>Alicia Sierra López</nombre>
          <email>alicia@gmail.com</email>
          <rol>Ponente</rol>
        </participante>
      </participantes>
    </evento>
    
    <evento id="e_002" tipo="Taller">
      <fecha>2025-02-06</fecha>
      <hora>17:00</hora>
      <lugar>
        <calle>Avenida Central 123</calle>
        <ciudad>Ciudad de México</ciudad>
        <pais>México</pais>
      </lugar>
      <participantes>
        <participante>
          <nombre>Antonio Ramirez Sánchez</nombre>
          <email>antonio@gmail.com</email>
          <rol>Moderador</rol>
        </participante>
      </participantes>
    </evento>
    
    <evento id="e_003" tipo="Reunión">
      <fecha>2025-01-25</fecha>
      <hora>19:15</hora>
      <lugar>
        <calle>Calle Principal 456</calle>
        <ciudad>Barcelona</ciudad>
        <pais>España</pais>
      </lugar>
      <participantes>
        <participante>
          <nombre>Lucas Rueda Ibañez</nombre>
          <email>lucas@gmail.com</email>
          <rol>Asistente</rol>
        </participante>
      </participantes>
    </evento>
    
    <evento id="e_004" tipo="MesaRedonda">
      <fecha>2025-01-21</fecha>
      <hora>10:30</hora>
      <lugar>
        <calle>Calle Molinos</calle>
        <ciudad>Madrid</ciudad>
        <pais>España</pais>
      </lugar>
      <participantes>
        <participante>
          <nombre>Ricardo Jérez Pérez</nombre>
          <email>ricardo.j@gmail.com</email>
          <rol>Ponente</rol>
        </participante>
      </participantes>
    </evento>
  </eventos>
  
  <relaciones>
    <relacion origen="e_001" destino="e_002"></relacion>
    <relacion origen="e_002" destino="e_003"></relacion>
    <relacion origen="e_003" destino="e_004"></relacion>
  </relaciones>
  
</agenda>
```


### 2. SOLUCIÓN DTD
```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE agenda [
  <!ELEMENT agenda (eventos, relaciones)>
  <!ELEMENT eventos (evento+)>
  <!ELEMENT relaciones (relacion+)>
  <!ATTLIST evento
    id ID #REQUIRED
    tipo (Conferencia|Taller|Reunión|MesaRedonda) #REQUIRED
  >
  <!ELEMENT evento (fecha, hora, lugar, participantes)>
  <!ELEMENT lugar (calle, ciudad, pais)>
  <!ELEMENT participantes (participante+)>
  <!ELEMENT participante (nombre, email, rol)>
  <!ELEMENT relaciones (relacion+)>
  <!ATTLIST relacion
    origen IDREF #REQUIRED
    destino IDREF #REQUIRED
  >
  <!ELEMENT relacion EMPTY>
  <!ELEMENT fecha (#PCDATA)>
  <!ELEMENT hora (#PCDATA)>
  <!ELEMENT calle (#PCDATA)>
  <!ELEMENT ciudad (#PCDATA)>
  <!ELEMENT pais (#PCDATA)>
  <!ELEMENT nombre (#PCDATA)>
  <!ELEMENT email (#PCDATA)>
  <!ELEMENT rol (#PCDATA)>
]>

```

### 3. SOLUCIÓN XSD
```xml
<?xml version="1.0" encoding="UTF-8"?>
<xsd:schema xmlns:xsd="http://www.w3.org/2001/XMLSchema">

  <xsd:element name="agenda">
    <xsd:complexType>
      <xsd:sequence>
        <xsd:element name="eventos" type="eventosType"/>
        <xsd:element name="relaciones" type="relacionesType"/>
      </xsd:sequence>
    </xsd:complexType>
  </xsd:element>
  
  <xsd:complexType name="eventosType">
    <xsd:sequence>
      <xsd:element name="evento" type="eventoType" maxOccurs="unbounded"/>
    </xsd:sequence>
  </xsd:complexType>
  
  <xsd:complexType name="eventoType">
    <xsd:sequence>
      <xsd:element name="fecha" type="fechaType"/> <!--xsd:string: para que no de error -->
      <xsd:element name="hora" type="horaType"/>  <!--xsd:string: para que no de error -->
      <xsd:element name="lugar" type="lugarType"/>
      <xsd:element name="participantes" type="participantesType"/>
    </xsd:sequence>
    <xsd:attribute name="id" type="idEventosType" use="required"/>
    <xsd:attribute name="tipo" type="tipoEventosType" use="required"/>
  </xsd:complexType>
  
  <xsd:simpleType name="idEventosType">
    <xsd:restriction base="xsd:string">
      <xsd:pattern value="[e]_[0-9]{3}"/>
    </xsd:restriction>
  </xsd:simpleType>
  
  <xsd:simpleType name="tipoEventosType">
    <xsd:restriction base="xsd:string">
      <xsd:enumeration value="Conferencia"/>
      <xsd:enumeration value="Taller"/>
      <xsd:enumeration value="Reunión"/>
      <xsd:enumeration value="MesaRueda"/>
    </xsd:restriction>
  </xsd:simpleType>
  
</xsd:schema>

```