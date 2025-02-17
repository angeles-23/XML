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

---

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
- **xsd:all**: Permite que aparezca todos los elementos pero solo 1 vez, da igual el orden.

1. **`<xsd:sequence>`**: Ejemplo, se define un tipo complejo llamado «Persona» que contiene dos elementos hijos: «Nombre» y «Apellido». Ambos elementos tienen un tipo de dato simple «xsd:string».

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

2. **`<xsd:choice>`**: Ejemplo, se define un tipo complejo «Animal» que permite que aparezcan todos los elementos hijos en cualquier orden. También es posible que solo uno de los elementos hijos («perro», «gato» o «Bird») esté presente en un momento dado, para ello hay que modificar choice.

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

3. **`<xsd:attribute>`**: Ejemplo 1, se agrega el atributo «edad» al tipo complejo «persona» con un tipo de dato «xsd:string».
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

4. **`<xsd:all>`**: Ejemplo, define un tipo complejo «direccion» que necesita todos los elementos hijos («calle», «ciudad» y «pais») estén presentes en cualquier orden.

```xml
    <xsd:schema xmlns:xsd="http://www.w3.org/2001/XMLSchema">

    <xsd:element name="direccion" type="direccionType"/>

    <xsd:complexType name="direccionType">
        <xs:all>
            <xsd:element name="calle" type="xsd:string"/>
            <xsd:element name="ciudad" type="xsd:string"/>
            <xsd:element name="pais" type="xsd:string"/>
        </xsd:all>
    </xsd:complexType>

    </xsd:schema>

    <!-- XML -->
    <direccion>
        <pais>España</pais>
        <ciudad>Zaragoza</ciudad>
        <calle>Calle Aventura 12</calle>
    </direccion>
```

---

## 3. Restricciones de elementos
### 3.1. Tipos de datos
- **Enteros**
  - **`<xsd:byte>`**: Con signo de 8 bits.
  - **`<xsd:short>`**: Con signo de 16 bits.
  - **`<xsd:int>`**: Con signo de 32 bits.
  - **`<xsd:long>`**: Con signo de 64 bits.
  - **`<xsd:integer>`**: Sin límite de tamaño.
  - **`<xsd:unsignedByte>`**: Sin signo de 8 bits.
  - **`<xsd:unsignedShort>`**: Sin signo de 16 bits.
  - **`<xsd:unsignedInt>`**: Sin signo de 32 bits.
  - **`<xsd:unsignedLong>`**: Sin signo de 64 bits.
  
- **Números Reales**
    - **`<xsd:decimal>`**: De precisión arbitraria.
    - **`<xsd:float>`**: De precisión simple (32 bits). 
    - **`<xsd:double>`**: De precisión doble (64 bits). 
- **Texto**
    - **`<xsd:string>`**: Cadena de caracteres que respetan los espacios en blanco.
    - **`<xsd:normalizedString>`**: Cadena de caracteres donde los espacios en blanco consecutivos se reemplazan por un solo espacio.
- **Fechas y tiempos**
    - **`<xsd:date>`**: Formato fecha `AAAA-MM-DD`.
    - **`<xsd:time>`**: Formato hora `HH:MM:SS.C`
    - **`<xsd:dateTime>`**: Formato combinado `AAAA-MM-DDTHH:MM:SS.C`
- **Otros Tipos**
    - **`<xsd:duration>`**: Períodos de tiempo como `P1Y4M21DT8H` (1 año, 4 meses, 21 días, 8 horas).
    - **`<xsd:boolean>`**: `true` o `false`.
    - **`<xsd:anyURI>`**: Direcciones URI.
    - **`<xsd:anyType>`**: Tipo genérico similar a la clase `Object` en Java


### 3.2. Derivaciones de Tipos Simples *`<xsd:simpleType>`*
Utilizando el elemento `<xsd:simpleType>` con el atributo name para establecer un nombre, se puede agregar restricciones adicionales al valor del elemento, como rangos numéricos, patrones de caracteres, valores permitidos, entre otros.

Dentro del elemento `<xsd:simpleType>`, se pueden establecer restricciones utilizando otros elementos como los siguientes:

- **`<xsd:restriction>`**: Para poner rangos, patrones, enumerar posibles valores etc.
- **`<xsd:list>`**: Para definir un tipo de lista.
- **`<xsd:union>`**: Para unir varios tipos definidos anteriormente en uno.


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


#### 3.2.4. Element *`<xsd:union>`*
- Combina varios tipos en uno solo, aceptando cualquier valor permitido por los tipos incluidos.
- Útiles cuando se necesitan valores flexibles que puedan pertenecer a siferentes categorías.
    ``` xml
    <xsd:schema xmlns:xsd="http://www.w3.org/2001/XMLSchema">
        <!-- Elemento que utiliza la unión de tipos simples -->
        <xsd:element name="contacto" type="codigoPostalONumeroType"/>

        <!-- Unión de tipos simples: código postal o número de teléfono -->
        <xsd:simpleType name="codigoPostalONumeroType">
            <xsd:union memberTypes="codigoPostalType telefonoType"/>
        </xsd:simpleType>

        <!-- Definición de tipo simple para el código postal -->
        <xsd:simpleType name="codigoPostalType">
            <xsd:restriction base="xsd:string">
                <xsd:pattern value="[0-9]{5}"/>
            </xsd:restriction>
        </xsd:simpleType>

        <!-- Definición de tipo simple para el número de teléfono -->
        <xsd:simpleType name="telefonoType">
            <xsd:restriction base="xsd:string">
                <xsd:pattern value="[0-9]{3}-[0-9]{3}-[0-9]{4}"/>
            </xsd:restriction>
        </xsd:simpleType>

    </xsd:schema>

    <!-- XML -->
    <contacto>12345</contacto>  <!-- Ambos son correctos, pero solo existe 1 elemento raíz: contacto --> 
    <contacto>123-456-7890</contacto>
    ```


### 3.3. Tipos de Restricciones en XSD
Se utilizan para definir reglas sobre los **datos que hay dentro de los elementos y atributos**

#### 3.3.1. Restricciones Numéricas
Nnúmeros enteros o decimales:
- **`<xsd:minInclusive>`**: Valor mínimo (incluido)
- **`<xsd:maxInclusive>`**: Valor máximo (incluido)
- **`<xsd:minExclusive>`**: Valor mínimo (excluido)
- **`<xsd:maxExclusive>`**: Valor máximo (excluido)

Ejemplo: Tipo para edades entre 16 y 65 años.
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
<edad>20</edad>
``` 


#### 3.3.2. Restricciones Longitud de Cadenas
Cadenas o listas:
- **`<xsd:length>`**: Longitud exacta.
- **`<xsd:minLength>`**: Longitud mínima.
- **`<xsd:maxLength>`**: Longitud máxima.

Ejemplo: Nombre de longitud entre 3 y 15 caracteres.
``` xml
<xsd:schema xmlns:xsd="http://www.w3.org/2001/XMLSchema">
    <xsd:element name="nombre" type="nombreType"/>
    
    <xsd:simpleType name="nombreType">
        <xsd:restriction base="xsd:string">
            <xsd:minLength value="3"/>
            <xsd:maxLength value="15"/>
        </xsd:restriction>
    </xsd:simpleType>
  
</xsd:schema>

<!-- XML -->
<nombre>José Enrique</nombre>
``` 


#### 3.3.3. Restricciones de Valores Específicos
Valores predefinidos:
- **`<xsd:enumeration>`**: Valores específicos permitidos.
Ejemplo: Género con valores "Hombre" o "Mujer".
``` xml
<xsd:schema xmlns:xsd="http://www.w3.org/2001/XMLSchema">
    <xsd:element name="genero" type="generoType"/>
  
    <xsd:simpleType name="generoType">
        <xsd:restriction base="xsd:string">
            <xsd:enumeration value="Hombre"/>
            <xsd:enumeration value="Mujer"/>
        </xsd:restriction>
  </xsd:simpleType>
  
</xsd:schema>

<!-- XML -->
<genero>Hombre</genero>
``` 


#### 3.3.4. Restricciones de Patrones
Cadenas con un patrón definido con expresiones regulares:
- **`<xsd:pattern>`**: patrón a seguir.

Ejemplo: Un patrón para el email.
``` xml
<xsd:schema xmlns:xsd="http://www.w3.org/2001/XMLSchema">
    <xsd:element name="email" type="emailType"/>
  
    <xsd:simpleType name="emailType">
        <xsd:restriction base="xsd:string">
            <xsd:pattern value="[a-zA-Z0-9_.+-]+@[a-zA-Z0-9_.+-]+\.[a-zA-Z]{2,10}"/>
        </xsd:restriction>
  </xsd:simpleType>
  
</xsd:schema>

<!-- XML -->
<email>an-Ge.le+s@g_ma+il.com</email>
``` 


#### 3.3.5. Restricciones para Listas
Listas de valores restringidos:
- **`<xsd:restriction>`**: con patrones específicos.

Ejemplo: Lista de colores separados por espacios
``` xml
<xsd:schema xmlns:xsd="http://www.w3.org/2001/XMLSchema">
    <xsd:element name="colores" type="coloresType"/>
  
    <xsd:simpleType name="coloresType">
        <xsd:restriction base="xsd:string">
            <xsd:pattern value="(rojo|verde|azul)( (rojo|verde|azul))*"/>
        </xsd:restriction>
  </xsd:simpleType>
  
</xsd:schema>

<!-- XML -->
<colores>rojo verde rojo rojo verde azul</colores>
``` 


#### 3.3.6. Restricciones de Espacios en Blanco
Controla cómo se manejan los espacios en blanco:
- **`<xsd:whiteSpace>`**:
  - `preserve`: Mantiene los espacios tal como están.
  - `replace`: Sustituye secuencias de espacios por un solo espacio.
  - `collapse`: Elimina espacios al inicio y al final, y reduce múltiples espacios intermedios a uno.

Ejemplos:  
``` xml
<xsd:schema xmlns:xsd="http://www.w3.org/2001/XMLSchema">

    <xsd:element name="texto" type="textoType"/>

    <xsd:simpleType name="textoType">
        <xsd:restriction base="xsd:string">
            <xsd:whiteSpace value="preserve"/>
        </xsd:restriction>
    </xsd:simpleType>

</xsd:schema>

<!-- XML -->
<!-- preserve --> <texto>  Este   es un   ejemplo    de texto  preserve  </texto>
<!-- replace --> <texto> Este es un ejemplo de texto replace </texto>
<!-- collapse --> <texto>Este es un ejemplo de texto collapse</texto>
``` 


#### 3.3.7. Restricciones para decimales
Representa números decimales con restricciones específicas:
- **`<xsd:totalDigits>`**: Número total de dígitos permitidos (enteros y decimales).
- **`<xsd:fractionDigits>`**: Número máximo de dígitos permitidos después del punto decimal.
- **`<xsd:minInclusive>`**: Valor mínimo (incluido).
- **`<xsd:maxInclusive>`**: Valor máximo (incluido).
- **`<xsd:minExclusive>`**: Valor mínimo (excluido).
- **`<xsd:maxExclusive>`**: Valor máximo (excluido).

Ejemplo 1: Precio con un máximo de 6 dígitos en total, 2 decimales, y un rango entre 0.01 y 9999.99.
``` xml
<xsd:schema xmlns:xsd="http://www.w3.org/2001/XMLSchema">

    <xsd:element name="precios" type="preciosType"/> 

    <xsd:complexType name="preciosType">
        <xsd:sequence>
            <xsd:element name="precio" type="precioType" maxOccurs="unbounded"/>
        </xsd:sequence>
    </xsd:complexType>

    <xsd:simpleType name="precioType">
        <xsd:restriction base="xsd:decimal">
            <xsd:totalDigits value="6"/>
            <xsd:fractionDigits value="2"/>
            <xsd:minInclusive value="0.01"/>
            <xsd:maxInclusive value="9999.99"/>
        </xsd:restriction>
    </xsd:simpleType>

</xsd:schema>

<!-- XML -->
<precios>
    <precio>0.1</precio>
    <precio>9999.99</precio>
</precios>
``` 

Ejemplo 2: Temperatura con 1 decimal permitida entre -50.0 y 50.0.
``` xml
<xsd:schema xmlns:xsd="http://www.w3.org/2001/XMLSchema">
  
    <xsd:element name="temperatura" type="temperaturaType"/>
    
    <xsd:simpleType name="temperaturaType">
        <xsd:restriction base="xsd:decimal">
            <xsd:totalDigits value="4"/>
            <xsd:fractionDigits value="1"/>
            <xsd:minInclusive value="-50.0"/>
            <xsd:maxInclusive value="50.0"/>
        </xsd:restriction>
    </xsd:simpleType>
  
</xsd:schema>

<!-- XML -->
<temperatura>15.3</temperatura>
``` 

---

## 4. Atributos Schema
Los atributos especifican:
    - Nombre del atributo
    - Tipo de daro que debe contener
    - Requisitos (required, optional o default="valor_por_defecto")

Se declaran dentro de un `xsd:complexType` usando `xsd:attribute`. Sintaxis:  
``` xml
<xsd:attribute name="nombre_atributo" type="tipo_dato" use="opcionalidad"/>
```


### 4.1. Tipos de atributos
#### 4.1.1. Atributos obligatorios
Debe aparecer en el elemento.
Ejemplo: un elemento producto con un atributo codigo obligatorio de tipo cadena
``` xml
<xsd:schema xmlns:xsd="http://www.w3.org/2001/XMLSchema">
  
    <xsd:element name="producto" type="productoType"/>
    
    <xsd:complexType name="productoType">
        <xsd:simpleContent>
            <xsd:extension base="xsd:string">
                <xsd:attribute name="codigo" type="xsd:string" use="required"/>
            </xsd:extension>
        </xsd:simpleContent>
    </xsd:complexType>

</xsd:schema>

<!-- XML -->
<producto codigo="A123">Teclado</producto>
```


#### 4.1.2. Atributos opcionales
Puede aparecer o no.
Ejemplo: un elemento producto con un atributo codigo obligatorio de tipo cadena
``` xml
<xsd:schema xmlns:xsd="http://www.w3.org/2001/XMLSchema">
  
    <xsd:element name="producto" type="productoType"/>
    
    <xsd:complexType name="productoType">
        <xsd:simpleContent>
            <xsd:extension base="xsd:string">
                <xsd:attribute name="codigo" type="xsd:string" use="optional"/>
            </xsd:extension>
        </xsd:simpleContent>
    </xsd:complexType>
</xsd:schema>

<!-- XML -->
<producto>Monitor LG</producto>
```


#### 4.1.3. Atributos con valor predeterminado
El valor predeterminado se usará si no está en el XML.
Ejemplo: 
``` xml
<xsd:schema xmlns:xsd="http://www.w3.org/2001/XMLSchema">
  
    <xsd:element name="producto" type="productoType"/>
    
    <xsd:complexType name="productoType">
        <xsd:simpleContent>
            <xsd:extension base="xsd:string">
                <xsd:attribute name="codigo" type="xsd:string" default="Desconocido"/>
            </xsd:extension>
        </xsd:simpleContent>
    </xsd:complexType>

</xsd:schema>

<!-- XML -->
<producto codigo=''>Móvil</producto> <!--   ->   <producto codigo="Desconocido">Móvil</producto>
-->
```


### 4.2. Como se forman los atributos en el XSD
#### 4.2.1. Elemento SIN elementos hijos
1. Elemento **EMPTY**
   ``` xml
    <xsd:schema xmlns:xsd="http://www.w3.org/2001/XMLSchema">
  
        <xsd:element name="producto" type="productoType"/>
        <!-- Al no tener elementos hijos no hace falta poner sequence -->
        <xsd:complexType name="productoType">
            <xsd:attribute name="codigo" type="xsd:string" use="required"/>
            <xsd:attribute name="descripcion" type="xsd:string" use="optional"/>
        </xsd:complexType>
    
    </xsd:schema>

    <!-- XML -->
   <proucto codigo="A123" descripcion="Teclado ergonómico"/>
   ```


2. Elemento **NO EMPTY**
   Sin restricciones
   ```xml
    <xsd:schema xmlns:xsd="http://www.w3.org/2001/XMLSchema">
  
        <xsd:element name="producto" type="productoType"/>
        
        <xsd:complexType name="productoType">
            
            <xsd:simpleContent>     <!-- Contiene información(texto) -->
                <xsd:extension base="xsd:string">    <!-- La información es una cadena -->
                
                    <!-- Posibles restricciones del elemento
                    <xsd:restriction base=xsd:string>
                    ...
                    </xsd:restriction> -->
                    
                    <!-- extension > ( restriction | attribute ) -->
                    <xsd:attribute name="codigo" type="xsd:string" use="required"/>
                    <xsd:attribute name="descripcion" type="xsd:string" use="optional"/>

                </xsd:extension> 
            </xsd:simpleContent>
            
        </xsd:complexType>
    
    </xsd:schema>

   <!-- XML -->
    <producto codigo="Z954" descripcion="Teclado gamer">Corsair K55</producto>
   ```
   
    Con restricciones en el elemento y en el atributo.
    Ejemplo: El elemento tipo moneda no puede ser menor de 0, el atributo moneda es una lista, puede ser € o $.       
    ```xml
    <xsd:schema xmlns:xsd="http://www.w3.org/2001/XMLSchema">
  
        <xsd:element name="precio">
            <xsd:complexType>
                <xsd:simpleContent>
                    <xsd:extension base="precioType">
                        <xsd:attribute name="moneda" type="monedaType" use="required"/>
                    </xsd:extension>
                </xsd:simpleContent>
            </xsd:complexType>
        </xsd:element>
        
        <xsd:simpleType name="monedaType">
            <xsd:restriction base="xsd:string">
                <xsd:enumeration value="€"/>
                <xsd:enumeration value="$"/>
            </xsd:restriction>
        </xsd:simpleType>
        
        <xsd:simpleType name="precioType">
            <xsd:restriction base="xsd:decimal">
                <xsd:totalDigits value="6"/>
                <xsd:fractionDigits value="2"/>
                <xsd:minInclusive value="0"/>
                <xsd:maxInclusive value = "100000"/>
            </xsd:restriction>
        </xsd:simpleType>
    
    </xsd:schema>

    <!-- XML -->
    <precioType moneda="$">150.50</precioType>
   ``` 


#### 4.2.1. Elemento CON elementos hijos
``` xml
<xsd:schema xmlns:xsd="http://www.w3.org/2001/XMLSchema">

<xsd:element name="producto">
    <xsd:complexType>
    
    <xsd:sequence>
        <xsd:element name="nombre" type="xsd:string"/>
        <xsd:element name="precio" type="xsd:decimal"/>
    </xsd:sequence>
    
    <xsd:attribute name="codigo" type="xsd:string" use="required"/>
    <xsd:attribute name="descripcion" type="xsd:string" use="optional"/>
    
    </xsd:complexType>
</xsd:element>

</xsd:schema>

<!-- XML -->
<producto codigo="A123" descripcion="Teclado ergonómico">
    <nombre>Corsair K55</nombre>
    <precio>19.99</precio>
</producto>
```

---

## 5. Restricciones en atributos de elementos XSD
Pasamos de esto: `<xsd:attribute name="nombre_atributo" type="xsd:tipo_atributo" use="required"/>`
A esto (quitando type y use): `<xsd:attribute name="nombre_atributo"></xsd:attribute>`
Sintaxis:
```xml
<xsd:attribute name="nombre_atributo">
    <xsd:simpleType>
        <xsd:restriction base="tipo">
            <!-- Restricción -->
        </xsd:restriction>
    </xsd:simpleType>
</xsd:attribute>
```

Ejemplo: Elemento producto EMPTY con 3 atributos (codigo, precio y descripcion)
- codigo: cadena de texto con formato LNNN (letra y numero)
- precio: máximo 2 decimales y no puede ser negativo
- descripcion: cadena de texto con 3 caracteres como mínimo y 50 como máximo
``` xml
<?xml version="1.0" encoding="UTF-8"?>
<xsd:schema xmlns:xsd="http://www.w3.org/2001/XMLSchema">
  
    <xsd:element name="producto">
        <xsd:complexType>
        
        <xsd:attribute name="codigo">
            <xsd:simpleType>
                <xsd:restriction base="xsd:string">
                    <xsd:pattern value="[A-Z][0-9]{3}"/>
                </xsd:restriction>
            </xsd:simpleType>
        </xsd:attribute>
        
        <xsd:attribute name="precio">
            <xsd:simpleType>
                <xsd:restriction base="xsd:decimal">
                    <xsd:totalDigits value="10"/>
                    <xsd:fractionDigits value="2"/>
                    <xsd:minInclusive value="0.01"/>
                </xsd:restriction>
            </xsd:simpleType>
        </xsd:attribute>
        
        <xsd:attribute name="descripcion">
            <xsd:simpleType>
                <xsd:restriction base="xsd:string">
                    <xsd:minLength value="3"/>
                    <xsd:maxLength value="50"/>
                </xsd:restriction>
            </xsd:simpleType>
        </xsd:attribute>
        
        </xsd:complexType>
    </xsd:element>
  
</xsd:schema>

<!-- XML -->
<producto codigo="B456" precio="199.99" descripcion="Teclado mecánico retroiluminado"/>
```

### 5.1. Restricción con patrón (validación de formato)
Ejemplo: El atributo *codigo* debe seguir el formato de 3L seguidads de 3N
``` xml
<xsd:schema xmlns:xsd="http://www.w3.org/2001/XMLSchema">

    <xsd:element name="producto" type="productoType"/>
    
    <xsd:complexType name="productoType">
        <xsd:simpleContent>
            <xsd:extension base="xsd:string">
                <xsd:attribute name="codigo" type="codigoType" use="required"/>
            </xsd:extension>
        </xsd:simpleContent>
    </xsd:complexType>
    
    <xsd:simpleType name="codigoType">
        <xsd:restriction base="xsd:string">
            <xsd:pattern value="[A-Z]{3}[0-9]{3}"/>
        </xsd:restriction>
    </xsd:simpleType>

</xsd:schema>

<!-- XML -->
<producto codigo="ABC123">Tablet Samung A8</producto>
```


### 5.2. Restricción con valores enumerados
Ejemplo: El atributo *color* solo puede ser rojo, azul o verde.
``` xml
<xsd:schema xmlns:xsd="http://www.w3.org/2001/XMLSchema">
  
    <xsd:element name="producto" type="productoType"/>
    
    <xsd:complexType name="productoType">
        <xsd:simpleContent>
            <xsd:extension base="xsd:string">
                <xsd:attribute name="codigo" type="xsd:string" use="required"/>
                <xsd:attribute name="color" type="colorType" use="required"/>
            </xsd:extension>
        </xsd:simpleContent>
    </xsd:complexType>

    <xsd:simpleType name="colorType">
        <xsd:restriction base="xsd:string">
            <xsd:enumeration value="rojo"/>
            <xsd:enumeration value="azul"/>
            <xsd:enumeration value="verde"/>
        </xsd:restriction>
    </xsd:simpleType>
  
</xsd:schema>

<!-- XML -->
<producto codigo="A123" color="rojo">Teclado</producto>
```



### 5.3. Restricción de longitud en atributos
Ejemplo: El atributo *codigo* tienen una longitud de 5 caracteres  
``` xml
<xsd:schema xmlns:xsd="http://www.w3.org/2001/XMLSchema">
  
    <xsd:element name="producto" type="productoType"/>
    
    <xsd:complexType name="productoType">
        <xsd:sequence>
            <xsd:element name="nombre" type="xsd:string"/>
            <xsd:element name="descripcion" type="xsd:string"/>
        </xsd:sequence>
        <xsd:attribute name="codigo" type="codigoType" use="optional"/>
    </xsd:complexType>
    
    <xsd:simpleType name="codigoType">
        <xsd:restriction base="xsd:string">
            <xsd:length value="5"/>
        </xsd:restriction>
    </xsd:simpleType>
  
</xsd:schema>

<!-- XML -->
<producto codigo="ABC12">
    <nombre>Corsair K55</nombre>
    <descripcion>Teclado de membrana compatible con software iCUE®️</descripcion>
</producto>
```


### 5.4. Restriccción de valores numéricos en atributos
Ejemplo: El atributo *precio* puede ser hasta 5 digitos, 2 decimales y va desde 0.01 - 9999.99
``` xml
<xsd:schema xmlns:xsd="http://www.w3.org/2001/XMLSchema">
  
    <xsd:element name="producto" type="productoType"/>
    
    <xsd:complexType name="productoType">
        <xsd:simpleContent>
            <xsd:extension base="xsd:string">
                <xsd:attribute name="precio" type="precioType" use="required"/>
            </xsd:extension>
        </xsd:simpleContent>
    </xsd:complexType>

    <xsd:simpleType name="precioType">
        <xsd:restriction base="xsd:decimal">
            <xsd:totalDigits value="5"/>
            <xsd:fractionDigits value="2"/>
            <xsd:minInclusive value="0.01"/>
            <xsd:maxInclusive value="999.99"/>
        </xsd:restriction>
    </xsd:simpleType>
  
</xsd:schema>

<!-- XML -->
<producto precio="19.99">Teclado</producto>
```

---

## 6 Claves y Claves Foráneas
Las claves **`xsd:key`** y **`xsd:keyref`** en XSD sirven para garantizar unicidad e integridad referencial en documentos XML, similar a claves primarias y foráneas en bases de datos.

### 6.1. Claves(`key`)
**`xsd:key`** (Clave primaria): Define un valor único dentro de un conjunto de elementos.

Sintaxis: 
``` xml
<xsd:key name="nombreClave">
    <xsd:selector xpath="rutaElementos"/>
    <xsd:field xpath="rutaCampo"/>
</xsd:key>
```

Explicacion:
- `name="nombreClave"`: nombre de la clave e identificador único. Nombre más común: atributoID.
- `selector: xpath`: indica la ruta de elementos afectados. Empezando desde la raíz y al acabar se le añade un `/`.
- `field: xpath`: señala el valor que no debe repetirse. Al incio va un @ y le sigue el nombre del atributo.
Todo esto va dentro del elemento de la raíz.

Ejemplo: 
``` xml
<xsd:schema xmlns:xsd="http://www.w3.org/2001/XMLSchema">

    <xsd:element name="datos">
        <xsd:complexType>
            <xsd:sequence>
                <xsd:element name="productos" type="productosType"/>
            </xsd:sequence>
        </xsd:complexType>
        
        <!-- Claves -->
        <xsd:key name="codigoID">
            <xsd:selector xpath="productos/producto"/>
            <xsd:field xpath="@codigo"/>
        </xsd:key>
        
    </xsd:element>
    
    <xsd:complexType name="productosType">
        <xsd:sequence>
            <xsd:element name="producto" type="productoType" maxOccurs="unbounded"/>
        </xsd:sequence>
    </xsd:complexType>

    <xsd:complexType name="productoType">
        <xsd:simpleContent>
            <xsd:extension base="xsd:string">
                <xsd:attribute name="codigo" type="codigoType" use="required"/>
            </xsd:extension>
        </xsd:simpleContent>
    </xsd:complexType>

    <xsd:simpleType name="codigoType">
        <xsd:restriction base="xsd:string">
            <xsd:pattern value="P[0-9]{3}"/>
        </xsd:restriction>
    </xsd:simpleType>

</xsd:schema>

<!-- XML -->
<datos>
    <productos>
        <producto codigo="P001">Teclado</producto>
        <producto codigo="P002">Ratón</producto>
        <producto codigo="P003">Monitor</producto>
    </productos>
</datos>
```


### 6.1. Claves Foráneas(`keyref`)
**`xsd:keyref`** (Clave foránea): Hace referencia a una clave definida con `xsd:key`, asegurando que un valor existe antes de ser referenciado.

Sintaxis:
``` xml
<xsd:keyref name="nombreClaveForanea" refer="nombreClave">
    <xsd:selector xpath="rutaElementos"/>
    <xsd:field xpath="rutaCampo"/>
</xsd:keyref>
```

Explicacion:
- `name="nombreClaveForanea"`: nombre de la clave foránea e identificador único. Nombre más común: atributoIDRefer.
- `refer="nombreClave"`: hace referencia a un `xsd:key` previamente definido. El nombreClave es el nombe de una key.
- `selector: xpath`: indica la ruta de elementos afectados. Empezando desde la raíz y al acabar se le añade un solo **\\**.
- `field: xpath`: señala el valor que no debe repetirse. Al incio va un **@** y le sigue el nombre del atributo **key** al que hace referencia.
Todo esto va dentro del elemento de la raíz.

Ejemplo: 
``` xml
<xsd:schema xmlns:xsd="http://www.w3.org/2001/XMLSchema">

    <xsd:element name="datos">
        <xsd:complexType>
            <xsd:sequence>
                <xsd:element name="productos" type="productosType"/>
                <xsd:element name="pedidos" type="pedidosType"/>
            </xsd:sequence>
        </xsd:complexType>
        
        <!-- Claves -->
        <xsd:key name="codigoID">
            <xsd:selector xpath="productos/producto"/>
            <xsd:field xpath="@codigo"/>
        </xsd:key>
        
        <xsd:keyref name="codigoProductoIDRef" refer="codigoID">
            <xsd:selector xpath="pedidos/pedido"/>
            <xsd:field xpath="@codigoProducto"/>
        </xsd:keyref>
        
    </xsd:element>
    
    <xsd:complexType name="productosType">
        <xsd:sequence>
            <xsd:element name="producto" type="productoType" maxOccurs="unbounded"/>
        </xsd:sequence>
    </xsd:complexType>

    <xsd:complexType name="productoType">
        <xsd:simpleContent>
            <xsd:extension base="xsd:string">
                <xsd:attribute name="codigo" type="codigoType" use="required"/>
            </xsd:extension>
        </xsd:simpleContent>
    </xsd:complexType>

    <xsd:simpleType name="codigoType">
        <xsd:restriction base="xsd:string">
            <xsd:pattern value="P[0-9]{3}"/>
        </xsd:restriction>
    </xsd:simpleType>
    
    <xsd:complexType name="pedidosType">
        <xsd:sequence>
            <xsd:element name="pedido" type="pedidoType" maxOccurs="unbounded"/>
        </xsd:sequence>
    </xsd:complexType>

    <xsd:complexType name="pedidoType">
        <xsd:simpleContent>
            <xsd:extension base="xsd:string">
                <xsd:attribute name="codigoProducto" type="codigoProductoType" use="required"/>
            </xsd:extension>
        </xsd:simpleContent>
    </xsd:complexType>

    <xsd:simpleType name="codigoProductoType">
        <xsd:restriction base="xsd:string">
            <xsd:pattern value="P[0-9]{3}"/>
        </xsd:restriction>
    </xsd:simpleType>

</xsd:schema>


<!-- XML -->
<datos>
    <productos>
        <producto codigo="P001">Teclado</producto>
        <producto codigo="P002">Ratón</producto>
        <producto codigo="P003">Monitor</producto>
    </productos>

    <pedidos>
        <pedido codigoProducto="P001"/>
        <pedido codigoProducto="P002"/>
        <!-- <pedido codigoProducto="P004"/>    Error: No existe este código  -->
    </pedidos>
</datos>
```


--- 


# MANUAL DTD

## 1. DECLARACIÓN
``` xml
<!DOCTYPE raiz [
<!ELEMENT raiz (elemento1, elemento2)>
<!ELEMENT elemento1 (subelemento+)>
<!ELEMENT elemento2 EMPTY>
<!ATTLIST nombre_elemento
    atributo1 ID #REQUIRED
    atributo2 CDATA #IMLIED
>
]>
```
## 2. Tipos de elementos
### 2.1. Secuenciales
Conienen elementos hijos.
```xml
<!ELEMENT elemento (subelemento1, subelemento2, subelemento3)>
<!ELEMENT receta (titulo, ingredientes, pasos)>
```

### 2.2. Enumeración o alternativos
Conienen **sólo uno** de los elementos hijos.
```xml
<!ELEMENT elemento (subelemento1 | subelemento2 | subelemento3)>
<!ELEMENT producto (telefono | tablet | ordenador)>
```

### 2.3. Elemento Vacío
Son elementos que no tiene contenido interno. Se usa 'EMPTY'.
```xml
<!ELEMENT elemento EMPTY>
<!ELEMENT plato EMPTY>
```

### 2.4. Elemento que contiene Datos
Son elementos que contienen cualquier texto sin formato.
```xml
<!ELEMENT elemento (#PCDATA)>
<!ELEMENT titulo (#PCDATA)>
```
### 2.5. Elementos con factor de repetición
Son elementos que contienen cualquier texto sin formato.
- Opcional (**?**): Aparece 0 o 1 vez
- Obligatorio (**+**): Aparece 1 o más veces.
- Cero o muchas veces (***\****): Aparece 0 o muchas veces. Es opcional y puede repetirse
- Obligatorio ( ): Aparece solo 1 vez


## 3. Tipos de Atributos
```xml
<!ATTLIST elemento                       <!-- <!A producto           por defecto será ⬇️    -->                         
    atributo tipo valorPredeterminado  <!-- categoria (electronicos|ropa|libros) 'electronicos'> -->
>
```
- **atributo**: nombre_atributo
- **tipo**: CDATA, enumeración o ID/IDREF
    - **CDATA**: texto
    - **enumeracion**: se colocan las enumeraciones entre '()' separados por '|'
    - **ID**: identificador único, debe empezar con una letra
    - **IDREF**: identificador que hace referencia a un ID existente
- **valorPredeterminado**: #REQUIRED, #IMPLIED, #FIXED
    - **REQUIRED**: obligatorio
    - **IMPLIED**: opcional
    - **FIXED**: valor fijo declarado en el DTD
Valor por defecto del atributo: es opcional en caso de no poner nada

Ejemplo:
```xml
<!ELEMENT libro (titulo?, isbn, año, (nombre|apellido)+ )> <!-- una u otra se puede repetir más de una vez y da iugal el orden-->
<!ELEMENT titulo (#PCDATA)>
<!ELEMENT isbn (#PCDATA)>
<!ELEMENT año (#PCDATA)>

<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE libro SYSTEM "libro.dtd">
<libro>
    <isbn>154984P</isbn>
    <año>2025</año>
    <apellido>Pérez Durán</apellido>
    <nombre>Ana María</nombre>
</libro>
```