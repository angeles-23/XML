# Ejercicios de repaso en clase

---

## 📌 **Ejercicio 1: Gestión de Pedidos en una Tienda Online**
Crea los siguientes archivos:
- Un **XML** que almacene información sobre pedidos, clientes y productos.
- Un **DTD** que valide la estructura básica del XML.
- Un **XSD** que agregue restricciones avanzadas.

### 🎯 **Requisitos**
- `<pedidos>` es el elemento raíz.
- `<pedido>` representa un pedido y contiene:
  - `id` (atributo único).
  - `fecha` (elemento con formato AAAA-MM-DD).
  - `<cliente>` con:
    - `id` (atributo único).
    - `<nombre>`, `<email>` y `<telefono>`.
  - `<productos>` que contiene una lista de `<producto>`, cada uno con:
    - `id` (atributo único).
    - `<nombre>`, `<precio>` (decimal positivo) y `<cantidad>` (entero positivo).
- Restricciones:
  - El `email` del cliente debe seguir un patrón válido.
  - La `cantidad` de cada producto debe ser al menos 1.
  - `fecha` debe seguir el formato `AAAA-MM-DD`.
  - Los `id` de `<cliente>` y `<producto>` deben ser únicos en el XML.

**XML + DTD:**
```xml
<pedidos>

    <pedido idPedido="Pe001"> <!-- id único -->

        <fecha>2025-02-26</fecha> <!-- AAAA-MM-DD -->
        <cliente idCliente="C001"> <!-- id único -->
            <nombre>Rodrigo Torres Sánchez</nombre>
            <email>pedrotorres@gmail.com</email> <!-- patron válido -->
            <telefono>666666666</telefono>
        </cliente>
        <productos>
            <producto idProducto="Pr001"> <!-- id único -->
                <nombre>Ordenador</nombre>
                <precio>599.99</precio> <!-- decimal positivo -->
                <cantidad>6</cantidad> <!-- entero positivo, al menos uno -->
            </producto>
        </productos>

    </pedido>

</pedidos>

<!DOCTYPE pedidos [
    <!ELEMENT pedidos (pedido+)>
    <!ATTLIST pedido 
        idPedido ID #REQUIRED
    >
    <!ELEMENT pedido (fecha, cliente, productos)>
    <!ATTLIST cliente 
        idCliente ID #REQUIRED
    >
    <!ELEMENT cliente (nombre, email, telefono)>
    <!ELEMENT productos (producto+)>
    <!ATTLIST producto 
        idProducto ID #REQUIRED
    >
    <!ELEMENT producto (nombre, precio, cantidad+)>

    <!ELEMENT fecha (#PCDATA)>
    <!ELEMENT nombre (#PCDATA)>
    <!ELEMENT email (#PCDATA)>
    <!ELEMENT telefono (#PCDATA)>
    <!ELEMENT precio (#PCDATA)>
    <!ELEMENT cantidad (#PCDATA)>
]>

```

**XSD:**
```xml
<xsd:schema xmlns:xsd="http://www.w3.org/2001/XMLSchema">

    <xsd:element name="pedidos">
        <xsd:complexType>
            <xsd:sequence>
                <xsd:element name="pedido" type="pedidoType" maxOccurs="unbounded"/>
            </xsd:sequence>
        </xsd:complexType>

        <xsd:key name="claveIDPedido">
            <xsd:selector xpath="pedido"/>
            <xsd:field xpath="@idPedido"/>
        </xsd:key>

        <xsd:key name="claveIDCliente">
            <xsd:selector xpath="pedido/cliente"/>
            <xsd:field xpath="@idCliente"/>
        </xsd:key>

        <xsd:key name="claveIDProducto">
            <xsd:selector xpath="pedido/productos/producto"/>
            <xsd:field xpath="@idProducto"/>
        </xsd:key>

    </xsd:element>

    <xsd:complexType name="pedidoType">
        <xsd:sequence>
            <xsd:element name="fecha" type="fechaType"/>
            <xsd:element name="cliente" type="clienteType"/>
            <xsd:element name="productos" type="productosType"/>
        </xsd:sequence>
        <xsd:attribute name="idPedido" type="idPedidoType" use="required"/>
    </xsd:complexType>

    <xsd:simpleType name="idPedidoType">
        <xsd:restriction base="xsd:string">
            <xsd:pattern value="Pe[0-9]{3}"/>
        </xsd:restriction>
    </xsd:simpleType>

    <xsd:simpleType name="fechaType">
        <xsd:restriction base="xsd:string">
            <xsd:pattern value="[0-9]{4}-[0-9]{2}-[0-9]{2}"/>        
        </xsd:restriction>
    </xsd:simpleType>

    <xsd:complexType name="clienteType">
        <xsd:sequence>
            <xsd:element name="nombre" type="xsd:string"/>
            <xsd:element name="email" type="emailType"/>
            <xsd:element name="telefono" type="xsd:integer"/>
        </xsd:sequence>
        <xsd:attribute name="idCliente" type="idClienteType" use="required"/>
    </xsd:complexType>

    <xsd:simpleType name="idClienteType">
        <xsd:restriction base="xsd:string">
            <xsd:pattern value="C[0-9]{3}"/>
        </xsd:restriction>
    </xsd:simpleType>

    <xsd:simpleType name="emailType">
        <xsd:restriction base="xsd:string">
            <xsd:pattern value="[a-zA-Z0-9_+-]+@[a-zA-Z0-9_+-]+\.[a-zA-Z0-9]{2,10}"/>
        </xsd:restriction>
    </xsd:simpleType>

    <xsd:complexType name="productosType">
        <xsd:sequence>
            <xsd:element name="producto" type="productoType"/>
        </xsd:sequence>
    </xsd:complexType>

    <xsd:complexType name="productoType">
        <xsd:sequence>
            <xsd:element name="nombre" type="xsd:string"/>
            <xsd:element name="precio" type="precioType"/>
            <xsd:element name="cantidad" type="cantidadType" maxOccurs="unbounded"/>
        </xsd:sequence>
        <xsd:attribute name="idProducto" type="idProductoType" use="required"/>
    </xsd:complexType>

    <xsd:simpleType name="idProductoType">
        <xsd:restriction base="xsd:string">
            <xsd:pattern value="Pr[0-9]{3}"/>
        </xsd:restriction>
    </xsd:simpleType>

    <xsd:simpleType name="precioType">
        <xsd:restriction base="xsd:decimal">
            <xsd:totalDigits value="8"/>
            <xsd:fractionDigits value="2"/>
            <xsd:minInclusive value="0.01"/>
        </xsd:restriction>
    </xsd:simpleType>

    <xsd:simpleType name="cantidadType">
        <xsd:restriction base="xsd:integer">
            <xsd:minInclusive value="0"/>
        </xsd:restriction>
    </xsd:simpleType>

</xsd:schema>
```

---

## 📌 **Ejercicio 2: Plataforma de Apuestas Deportivas**  
Crea:  
- **XML** con información de usuarios, eventos deportivos y apuestas.  
- **DTD** para validar la estructura básica.  
- **XSD** con validaciones avanzadas.  

### 🎯 **Estructura del XML**  
- `<casaApuestas>` es el elemento raíz.  
- `<usuarios>` contiene múltiples `<usuario>` con:  
  - `id` (atributo único).  
  - `<nombre>`, `<edad>` (mínimo 18 años), `<email>` y `<saldo>`.  
- `<eventos>` contiene múltiples `<evento>` con:  
  - `id` (atributo único).  
  - `<deporte>`, `<equipo1>`, `<equipo2>`, `<fecha>` (formato AAAA-MM-DD).  
- `<apuestas>` almacena las apuestas realizadas con:  
  - `<apuesta>` que tiene:  
    - `id` (atributo único).  
    - `usuarioId` (referencia a un `<usuario>`).  
    - `eventoId` (referencia a un `<evento>`).  
    - `<monto>` (cantidad apostada).  
    - `<tipo>` (ganador, marcador exacto, etc.).  
#### ✏️ **Ejemplos de `<tipo>` de Apuestas**  

1. **Ganador del partido** → Se apuesta por el equipo que ganará el evento: `<tipo>ganador</tipo>`
2. **Marcador exacto** → Se apuesta por el resultado exacto del partido: `<tipo>marcador_exacto</tipo>`  
3. **Número total de goles/puntos** → Se apuesta si la suma de puntos o goles será mayor o menor a un valor determinado: `<tipo>over_under</tipo>`
4. **Primer goleador/anotador** → Se apuesta sobre qué jugador marcará primero: `<tipo>primer_goleador</tipo>`  
5. **Apuesta combinada** → Varias apuestas en una sola (por ejemplo, ganador + número de goles): `<tipo>combinada</tipo>`  

### 🎯 **Restricciones**  
- `edad` debe ser 18 o más.  
- `email` debe cumplir un formato válido.  
- `usuarioId` y `eventoId` deben referenciar IDs existentes.  
- `monto` debe ser un número positivo.  

**XML + DTD:**  
```xml

```  

**XSD:**  
```xml

```

---

## 📌 **Ejercicio 3: Plataforma de Streaming**  
Desarrolla:  
- **XML** con información de películas, series, directores y usuarios.  
- **DTD** con la estructura base.  
- **XSD** con restricciones avanzadas.  

### 🎯 **Estructura del XML**  
- `<streaming>` es el elemento raíz.  
- `<contenido>` contiene múltiples `<titulo>` con:  
  - `id` (atributo único).  
  - `<nombre>`, `<tipo>` (película o serie), `<genero>`, `<anioEstreno>`.  
  - `<directorId>` (referencia a `<director>`).  
  - `<calificacion>` (edad recomendada).  
- `<directores>` contiene `<director>` con:  
  - `id` (atributo único).  
  - `<nombre>`, `<pais>`.  
- `<usuarios>` contiene `<usuario>` con:  
  - `id` (atributo único).  
  - `<nombre>`, `<email>`, `<suscripcion>` que puede ser: `básica`, `estándar` o `premium.
  - Además `<suscripcion>` cuenta con dos atributos `dia-renovación` (tiene que ser un número entero positivo y como valor máximo que pueda tomar 31) y `fin-contrato` (opcional, dia del mes en el que se finaliza el contrato, numero entero, que toma como valor máximo 31).  
  - `<historial>` con múltiples `<visualizacion>`:  
    - `contenidoId` (referencia a `<titulo>`).  
    - `<fecha>`, `<progreso>` (% visto).  

### 🎯 **Restricciones**  
- `email` debe cumplir con un formato válido.  
- `anioEstreno` debe ser un número de 4 dígitos.  
- `contenidoId` debe referenciar un `<titulo>` existente.  
- `progreso` debe estar entre 0 y 100.  
- `suscripcion` solo puede ser "básica", "estándar" o "premium".  

**XML + DTD:**  
```xml

```  

**XSD:**  
```xml

```

---

## 📌 **Ejercicio 4: Biblioteca de Juegos en Steam**  
Desarrolla:  
- **XML** con información de juegos, desarrolladores y usuarios.  
- **DTD** para la estructura base.  
- **XSD** con validaciones avanzadas.  

### 🎯 **Estructura del XML**  
- `<biblioteca>` es el elemento raíz.  
- `<juego>` representa un videojuego y tiene:  
  - `id` (atributo único).  
  - `<nombre>`, `<genero>`, `<fecha_lanzamiento>`.  
  - `<desarrollador>` con `<nombre_estudio>`, `<pais>`.  
  - `<usuarios>` con múltiples `<usuario>`:  
    - `id` (atributo único).  
    - `<nombre>`, `<email>`, `<horas_jugadas>`.  

### 🎯 **Restricciones**  
- `email` debe cumplir con el formato correcto.  
- `fecha_lanzamiento` debe seguir el formato `AAAA-MM-DD`.  
- `horas_jugadas` debe ser un número positivo.  
- `id` de `<juego>` y `<usuario>` deben ser únicos.  

**XML + DTD:**  
```xml

```  

**XSD:**  
```xml

```
---

## 📌 **Ejercicio 5: Reserva de Pingüinos**  
Desarrolla:  
- **XML** con información de especies, hábitats y cuidadores.  
- **DTD** con la estructura base.  
- **XSD** con restricciones avanzadas.  

### 🎯 **Estructura del XML**  
- `<reserva>` es el elemento raíz.  
- `<especies>` contiene `<especie>` con:  
  - `id` (atributo único).  
  - `<nombre>`, `<tamaño>` (en cm), `<peso>` (en kg).  
- `<habitats>` contiene `<habitat>` con:  
  - `id` (atributo único).  
  - `<nombre>`, `<temperatura>`, `<superficie>` (en m²).  
- `<cuidadores>` contiene `<cuidador>` con:  
  - `id` (atributo único).  
  - `habitatId` (referencia a `<habitat>`).  
  - `<nombre>`, `<experiencia>` (años).  

### 🎯 **Restricciones**  
- `tamaño` debe estar entre 30 y 130 cm.  
- `peso` debe estar entre 1 y 40 kg.  
- `habitatId` debe referenciar un `<habitat>` existente.  

**XML + DTD:**  
```xml

```  

**XSD:**  
```xml

```