# MANUAL XSD
## 1. Definición de un elemento
- name: Nombre del elemento
- type: Tipo del elemento
- maxOccurs: Número máximo de veces que puede aparecer un elemento [0-unbounded]
- minOccurs: Número mínimo de veces que puede aparecer un elemento
Por defecto maxOccurs y minOccurs, aparece una sola vez.

``` xml
<!-- XSD -->
<?xml version="1.0" encoding="UTF-8"?>
<xsd:schema xmlns:xsd="http://www.w3.org/2001/XMLSchema">
   <!-- Definición del elemento "peliculas" que puede contener múltiples elementos "pelicula" -->

   <xsd:element name="peliculas">
        <xsd:complexType>
            <xsd:sequence>
                <xsd:element name="pelicula" type="xsd:string" maxOccurs="unbounded"/> <!-- numero ilimitado -->
            </xsd:sequence>
        </xsd:complexType>
    </xsd:element>

</xsd:schema>

<!-- XML -->
<peliculas>
    <pelicula>Matrix</pelicula>
    <pelicula>Inception</pelicula>
    <pelicula>Interstellar</pelicula>
</peliculas>
```

## 2. Tipos de elementos
- Elemento simple: no permite elementos hijos ni atributos
- Elemento compuesto: permite elementos hijos y atributos, y a su vez puede tener elementos simples
    - Contenido simple: elemento con texto, y puede tener atributos. No elementos hijos
    ```xml
    <xsd:complexType name="Producto">
        <xsd:simpleContent>
            <xsd:extension base="xsd:string">
                <xsd:attribute name="id" type="xsd:int"/>
            </xsd:extension>
        </xsd:smpleContent>
    </xsd:complexType>

    <!-- XML -->
    <Producto id="123">Laptop</Producto>
    ```
      
    - Contenido compuesto: un elemento permite hijos y atributos
    ```xml 
    <?xml version="1.0" encoding="UTF-8"?>
    <xsd:schema xmlns:xsd="http://www.w3.org/2001/XMLSchema">

        <xsd:element name="personas">
            <xsd:complexType>
            <xsd:sequence>
                <xsd:element name="persona" type="personaType" maxOccurs="unbounded"/>
            </xsd:sequence>
            </xsd:complexType>
        </xsd:element>
        
        <xsd:complexType name="personaBase">  <!-- Define persona sólo con nombre y edad-->
            <xsd:sequence>
            <xsd:element name="nombre" type="xsd:string"/>
            <xsd:element name="edad" type="xsd:integer"/>
            </xsd:sequence>
        </xsd:complexType>
        
        <xsd:complexType name="personaType">  <!-- Hereda nombre y edad de personaBase -->
            <xsd:complexContent>      
                <xsd:extension base="personaBase">    <!-- Dentro de extension se añaden nuevos elementos -->
                    <xsd:sequence>
                        <xsd:element name="telefono" type="xsd:integer" maxOccurs="3"/> <!-- Añade nuevo elemento: telefono -->
                    </xsd:sequence>
                    <xsd:attribute name="id" type="xsd:integer" use="required"/>  <!-- Añade nuevo atributo: id -->
                </xsd:extension>
            </xsd:complexContent>
        </xsd:complexType>
        
    </xsd:schema>

    <!-- XML -->
    <personas>
        <persona id="1">
            <nombre>Juan</nombre>
            <edad>30</edad>
            <telefono>658497854</telefono>
            <telefono>629356148</telefono>
        </persona>
        <persona id="2">
            <nombre>Ana</nombre>
            <edad>25</edad>
            <telefono>785412369</telefono>
        </persona>
    </personas>
    ```

### 2.1. Tipos Simples
Contienen un solo valor sin subelementos. Se definene con `<xsd:element>` junto con el atributo type.

``` xml
<xsd:element name="texto" type="xsd:string"/>
```
Existen varios tipos de datos predefinidos en XSD que se pueden utilizar para definir elementos simples mediante el atributo *type*, como:
- **xsd:string**: Cadena de texto.
- **xsd:integer**:	Número entero.
- **xsd:positiveInteger**:	Número entero positivo.
- **xsd:negativeInteger**:	Número entero negativo.
- **xsd:boolean**:	Valor booleano (true o false).
- **xsd:date**:	Fecha en formato YYYY-MM-DD.
- **xsd:time**:	Hora en formato HH:MM:SS.
- **xsd:decimal**:	Nnúmero decimal.
- **xsd:float**:	Números de punto flotante de 32 bits de precisión simple.
- **xsd:double**:	Números de punto flotante de 64 bits de doble precisión.

Ejemplo: Esquema para validar la edad de un trabajador, es un valor entero entre 16 y 65
``` xml
<xsd:schema xmlns:xsd="http://www.w3.org/2001/XMLSchema">

    <xsd:element name="edad" type="edadType"/>

    <xsd:simpleType name="edadType">
        <xsd:restriction base="xsd:integer">
            <xsd:minInclusive value="16"/>
            <xsd:maxInclusive value="65"/>
        </xsd:restriction>
    </xsd:simpleType>

</xsd:schema>

<!-- XML -->
<edad>30</edad>
```

### 2.2. Tipos Complejos
El elemento `<xsd:complexType>` se utiliza para definir tipos de datos complejos que tienen sub-elementos y/o atributos. Los tipos de datos complejos permiten especificar la estructura interna, es decir, sus atributos y elementos hijos.

``` xml
<xsd:schema xmlns:xsd="http://www.w3.org/2001/XMLSchema">

    <!-- Elemento raíz -->
    <xsd:element name="clase">
        <xsd:complexType>
            <xsd:sequence>
                <xsd:element name="alumno" type="alumnoType" minOccurs="0" maxOccurs="unbounded"/>
            </xsd:sequence>    
        </xsd:complexType>
    </xsd:element>

    <!-- Elemento alumno -->
    <xsd:complexType name="alumnoType">
        <xsd:sequence>
            <!-- Subelementos de alumno -->
            <xsd:element name="nombre" type="xsd:string"/>
            <xsd:element name="apellido" type="xsd:string"/>
            <xsd:element name="anio" type="xsd:int"/>
        </xsd:sequence>
    </xsd:complexType>

</xsd:schema>

<!-- XML -->
<clase>
    <alumno>
        <nombre>Juan</nombre>
        <apellido>Pérez</apellido>
        <anio>2023</anio>
    </alumno>
</clase>
```

Dentro del elemento `<xsd:complexType>`, se pueden agregar elementos como los siguientes:

- **xsd:sequence**:	Especifica una secuencia ordenada de elementos hijos. Los elementos deben aparecer en el orden indicado.
- **xsd:choice**:	Se utiliza cuando el orden o la combinación de elementos hijos no está restringida, es decir, no impone un orden fijo entre los elementos hijos.
- **xsd:attribute**: Agrega atributos a un tipo complejo. Se puede especificar el nombre (name) y el tipo de atributo (type).


1. `<xsd:sequence>`: Ejemplo, se define un tipo complejo llamado «Persona» que contiene dos elementos hijos: «Nombre» y «Apellido». Ambos elementos tienen un tipo de dato simple «xsd:string».

    ``` xml
    <xsd:complexType name="persona">
        <xsd:sequence>
            <xsd:element name="nombre" type="xsd:string" minOccurs="0" maxOccurs="unbounded"/>
            <xsd:element name="apellido" type="xsd:string" minOccurs="0" maxOccurs="unbounded"/>
        </xsd:sequence>
    </xsd:complexType>
    
    <!-- XML -->
    <persona>
        <nombre>Silvester</nombre>
        <apellido>Stalone</apellido>
    </persona>
    ```

2. `<xsd:choice>`: Ejemplo, se define un tipo complejo «Animal» que permite que aparezcan todos los elementos hijos en cualquier orden. También es posible que solo uno de los elementos hijos («perro», «gato» o «Bird») esté presente en un momento dado, para ello hay que modificar choice.

    ``` xml
    <xsd:complexType name="animal">
        <xsd:choice maxOccurs="unbounded"><!-- deordenado e ilímitado -->   <!-- <xsd:choice> una vez-->
            <xsd:element name="perro" type="xsd:string"/>
            <xsd:element name="gato" type="xsd:string"/>
            <xsd:element name="pajaro" type="xsd:string"/>
        </xsd:choice>
    </xsd:complexType>

    <!-- XML -->
    <!--  <xsd:choice maxOccurs="unbounded">  -->
    <animal>
        <gato>Miau</gato>
        <perro>Auuuu</perro>
        <perro>Guau</perro>
        <gato>Ronron</gato>
        <pajaro>Pio</pajaro>
    </animal>

    <!--  <xsd:choice">  -->
    <animal>
      <gato>Miau</gato>
    </animal>
    ```

3. `<xsd:attribute>`: Ejemplo 1, se agrega el atributo «edad» al tipo complejo «persona» con un tipo de dato «xsd:string».
    ``` xml
    <xsd:complexType name="persona">
        <xsd:sequence>
            <xsd:element name="nombre" type="xsd:string"/>
            <xsd:element name="apellido" type="xsd:string"/>
        </xsd:sequence>
        <xsd:attribute name="edad" type="xsd:integer"/>
    </xsd:complexType>
    
    <!-- XML --> 
    <persona edad="30">
        <nombre>Pedro</nombre>
        <apellido>González</apellido>
    </persona>
    ```

    Ejemplo 2, definimos «libro» con dos elementos hijos («titulo» y «autor») y dos atributos («id» y «fechaPublicacion»).
    ``` xml
    <xsd:schema xmlns:xsd="http://www.w3.org/2001/XMLSchema">
        
        <xsd:element name="libro">   <!-- Definición elemento "libro" con atributos -->
            <xsd:complexType>
                <xsd:sequence>
                    <xsd:element name="titulo" type="xsd:string"/>
                    <xsd:element name="autor" type="xsd:string"/>
                </xsd:sequence>
                <xsd:attribute name="id" type="xsd:positiveInteger"/>   <!-- atributos de "libro" -->
                <xsd:attribute name="fechaPublicacion" type="xsd:date"/>
            </xsd:complexType>
      </xsd:element>

    </xsd:schema>
    
    <!-- XML -->
    <libro id="123" fechaPublicacion="2019-05-16">
        <titulo>A través de mi ventana</titulo>
        <autor>Ariana Godoy</autor>
    </libro>
      ```

## 3. Restricciones de elementos
### 3.1. Tipos de datos
- **Enteros**
  - `<xsd:byte>`: Con signo de 8 bits.
  - `<xsd:short>`: Con signo de 16 bits.
  - `<xsd:int>`: Con signo de 32 bits.
  - `<xsd:long>`: Con signo de 64 bits.
  - `<xsd:integer>`: Sin límite de tamaño.
  - `<xsd:unsignedByte>`: Sin signo de 8 bits.
  - `<xsd:unsignedShort>`: Sin signo de 16 bits.
  - `<xsd:unsignedInt>`: Sin signo de 32 bits.
  - `<xsd:unsignedLong>`: Sin signo de 64 bits.
  
- **Números Reales**
    - `<xsd:decimal>`: De precisión arbitraria.
    - `<xsd:float>`: De precisión simple (32 bits). 
    - `<xsd:double>`: De precisión doble (64 bits). 
- **Texto**
    - `<xsd:string>`: Cadena de caracteres que respetan los espacios en blanco.
    - `<xsd:normalizedString>`: Cadena de caracteres donde los espacios en blanco consecutivos se reemplazan por un solo espacio.
- **Fechas y tiempos**
    - `<xsd:date>`: Formato fecha `AAAA-MM-DD`.
    - `<xsd:time>`: Formato hora `HH:MM:SS.C`
    - `<xsd:dateTime>`: Formato combinado `AAAA-MM-DDTHH:MM:SS.C`
- **Otros Tipos**
    - `<xsd:duration>`: Períodos de tiempo como `P1Y4M21DT8H` (1 año, 4 meses, 21 días, 8 horas).
    - `<xsd:boolean>`: `true` o `false`.
    - `<xsd:anyURI>`: Direcciones URI.
    - `<xsd:anyType>`: Tipo genérico similar a la clase `Object` en Java


### 3.2. Derivaciones de Tipos Simples *`<xsd:simpleType>`*
Utilizando el elemento `<xsd:simpleType>` con el atributo name para establecer un nombre, se puede agregar restricciones adicionales al valor del elemento, como rangos numéricos, patrones de caracteres, valores permitidos, entre otros.

Dentro del elemento `<xsd:simpleType>`, se pueden establecer restricciones utilizando otros elementos como los siguientes:

`<xsd:restriction>`: Para poner rangos, patrones, enumerar posibles valores etc.
`<xsd:list>`: Para definir un tipo de lista.
`<xsd:union>`: Para unir varios tipos definidos anteriormente en uno.

#### 3.2.1. Element *`<xsd:restriction>`*
Estructura básica: 
``` xml
<xsd:restriction base="tipoDeDatoBase">
    <!-- Restricciones y atributos adicionales aquí -->
</xsd:restriction>
```

Restricciones más comunes:
- **`<xsd:length>`**: Longitud exacta del valor permitido.
- **`<xsd:minLength>`**: Longitud mínima.
- **`<xsd:maxLength>`**: Longitud máxima.
- **`<xsd:minInclusive>`**: Valor mínimo incluido.
- **`<xsd:maxInclusive>`**: Valor máximo incluido.
- **`<xsd:minExclusive>`**: Valor mínimo excluido.
- **`<xsd:maxExclusive>`**: Valor máximo excluido.
- **`<xsd:enumeration>`**: Conjunto de valores permitidos para seleccionar.
- **`<xsd:pattern>`**: Patrón utilizando expresiones regulares.

Ejemplo: Crear un tipo que permita valores decimales con hasta 2 cifras decimales.
``` xml
<xsd:simpleType name="tipoPrecio">
    <xsd:restriction base="xsd:decimal">
            <xsd:totalDigits value="5"/>
            <xsd:fractionDigits value="2"/>
    </xsd:restriction>
</xsd:simpleType>

<!-- XML -->
<precio>123.45</precio>
```

#### 3.2.2. Element *`<xsd:extension>`*
- Amplia un tipo que ya existe agregando atributos o elementos adicionales
- Son útiles para definir tipos más complejos a partir de otros más simples
  
Ejemplo: Crear un tipo extendido para representar una dirección con campos adicionales.
``` xml
<xsd:schema xmlns:xsd="http://www.w3.org/2001/XMLSchema">
  
    <xsd:element name="direccion" type="direccionType"/>

    <xsd:complexType name="direccionBase">
        <xsd:sequence>
            <xsd:element name="calle" type="xsd:string"/>
            <xsd:element name="ciudad" type="xsd:string"/>
        </xsd:sequence>
    </xsd:complexType>

  <!-- Tipo extendido 'direccionCompleta' que añade un nuevo elemento 'codigoPostal' -->
  <xsd:complexType name="direccionType">
        <xsd:complexContent>
            <xsd:extension base="direccionBase">
                <xsd:sequence>
                    <xsd:element name="codigoPostal" type="xsd:string"/>
                </xsd:sequence>
            </xsd:extension>
        </xsd:complexContent>
  </xsd:complexType>

</xsd:schema>

<!-- XML-->
<direccion>
    <calle>Av. Santa Fe</calle>
    <ciudad>Buenos Aires</ciudad>
    <codigoPostal>C1425BCV</codigoPostal>
</direccion>
```
Explicación:
- Elemento raíz `<xsd:direccion>` de tipo `<direccionType>`
- Tipo complejo `<direccionBase>`
- Dentro, `<xsd:sequence>` para indicar el orden
- Elementos hijos: `calle` y `ciudad`, ambos `<xsd:string>`
- Tipo complejo `<direccionType>`
- Dentro, `<xsd:complexContent>` indica que el contenido complejo se basa en otro tipo complejo
- Dentro de `<xsd:complexContent>`, se usa `<xsd:extension base="direccionBase">` para extender direccionBase, es decir, que `<direccionType>` hereda los elementos calle y ciudad de direccionBase.



#### 3.2.3. Element *`<xsd:list>`*
- Son listas de valores del mismo tipo.
- Representan conjuntos de datos separados por espacios.
  ```xml
  <xsd:schema xmlns:xsd="http://www.w3.org/2001/XMLSchema">

    <xsd:element name="colores" type="listaColores">

    <xsd:simpleType name="listaColores">
        <xsd:list itemType="xsd:string"/>   <!-- itemType: valor de la lista-->
    </xsd:simpleType>

  </xsd:schema>
  
  <!-- XML -->
  <colores>rojo azul verde amarillo</colores>
    ```

#### 3.2.4. Element *`<xsd:restriction>`*


#### 3.2.5. Element *`<xsd:restriction>`*


#### 3.2.6. Element *`<xsd:restriction>`*






``` xml

```



``` xml

```



``` xml

```