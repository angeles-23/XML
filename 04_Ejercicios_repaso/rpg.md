
# 📌 **Ejercicio: Sistema de Gestión de un Videojuego de Rol (RPG)**

## 🎯 **Objetivo**
Crear un **XML** que modele un videojuego de rol (RPG), incluyendo información sobre **personajes, misiones, objetos, enemigos y localizaciones**. También se debe desarrollar su correspondiente **DTD** y **XSD** para validar la estructura y definir restricciones.

---

## 📖 **Especificaciones del XML**

El documento XML debe tener un elemento raíz `<rpg>`, que contiene las siguientes secciones:

### **1️⃣ Videojuego**
- `<videojuego>` almacena la información general del RPG:
  - `<titulo>`: Nombre del videojuego.
  - `<desarrollador>`: Nombre de la empresa que lo creó.
  - `<plataformas>`: Plataformas en las que está disponible (PC, PlayStation, Xbox, etc.).
  - `<año_lanzamiento>`: Año en formato `AAAA`.
  - `<version>`: Versión del juego en formato `X.Y`.

### **2️⃣ Personajes**
- `<personajes>` almacena una lista de `<personaje>`, cada uno con:
  - **Atributos**:
    - `id`: Identificador único del personaje.
  - **Elementos**:
    - `<nombre>`, `<raza>`, `<clase>` (Guerrero, Mago, Pícaro, etc.).
    - `<nivel>` (número entero entre 1 y 100).
    - `<stats>` con `<fuerza>`, `<agilidad>`, `<inteligencia>`, `<vida>`.
    - `<inventario>` con `<objeto>` que el personaje posee.

### **3️⃣ Misiones**
- `<misiones>` contiene múltiples `<mision>`, cada una con:
  - **Atributos**:
    - `id`: Identificador único de la misión.
  - **Elementos**:
    - `<titulo>`, `<descripcion>`, `<dificultad>` (Fácil, Media, Difícil).
    - `<recompensa>` con `<oro>` y `<experiencia>`.

### **4️⃣ Objetos**
- `<objetos>` almacena `<objeto>` con:
  - **Atributos**:
    - `id`: Identificador único del objeto.
  - **Elementos**:
    - `<nombre>`, `<tipo>` (arma, armadura, consumible).
    - `<valor>` (precio en monedas del juego).
    - `<efecto>` (modificación de atributos que otorga).

### **5️⃣ Enemigos**
- `<enemigos>` almacena `<enemigo>` con:
  - **Atributos**:
    - `id`: Identificador único del enemigo.
  - **Elementos**:
    - `<nombre>`, `<nivel>`, `<vida>`, `<daño>`.
    - `<tipo>` (bestia, humanoide, demonio, etc.).
    - `<loot>` con `<objeto>` que puede soltar al ser derrotado.

### **6️⃣ Localizaciones**
- `<mapa>` contiene `<localizacion>` con:
  - **Atributos**:
    - `id`: Identificador único de la localización.
  - **Elementos**:
    - `<nombre>`, `<bioma>` (bosque, desierto, cueva, ciudad).
    - `<enemigos_presentes>` con `<enemigo>` que habita en la zona.

---

## 📜 **Instrucciones**
1. **Crea el archivo XML** con al menos:
   - 1 videojuego registrado.
   - 3 personajes con diferentes clases y niveles.
   - 3 misiones con diferentes dificultades.
   - 5 objetos de distintos tipos.
   - 3 enemigos con diferentes niveles y loot.
   - 3 localizaciones con enemigos asignados.
   
2. **Define el DTD** para validar la estructura del XML:
   - Debe incluir la relación entre `<personaje>`, `<mision>`, `<enemigo>` y `<objeto>`.
   - `<inventario>`, `<loot>` y `<enemigos_presentes>` deben contener referencias válidas.

3. **Crea el XSD** con restricciones avanzadas:
   - `<nivel>` de personajes y enemigos entre 1 y 100.
   - `<vida>` debe ser un número positivo.
   - `<email>` de los jugadores debe seguir el formato correcto.
   - `<año_lanzamiento>` debe tener 4 dígitos.
   - `<dificultad>` de las misiones solo puede ser "Fácil", "Media" o "Difícil".
   - `<bioma>` solo puede ser "Bosque", "Desierto", "Cueva", "Ciudad", "Montaña", "Nieve".

---
¡Buena suerte! 🚀🎮


#### SOLUCIÓN XML
``` xml
<rpg>

    <!-- VIDEOJUEGO -->
    <videojuego>
        <titulo>Mundo de magia</titulo>
        <desarrollador>MagiaGama</desarrollador>
        <plataformas>
            <plataforma>PC</plataforma> <!-- PC, PlayStation, Xbox , etc-->
            <plataforma>PlayStation</plataforma> <!-- PC, PlayStation, Xbox, etc -->
        </plataformas>
        <año_lanzamiento>2024</año_lanzamiento>  <!-- 4 digitos: AAAA -->
        <version>1.3</version> <!--X.Y -->
    </videojuego>
  
  
  <!-- PERSONAJES -->
    <personajes>
        <personaje idPersonaje="P001"> <!-- id unico-->
            <nombre>Oswell</nombre>
            <raza>Humano</raza>
            <clase>Guerrero</clase> <!-- Guerrero, Mago, Pícaro, etc -->
            <nivel>20</nivel> <!-- 1-100 -->
            <stats>
                <fuerza>60</fuerza>
                <agilidad>40</agilidad>
                <inteligencia>50</inteligencia>
                <vida>500</vida>  <!-- + -->
            </stats>
            <inventario>
                <objeto_personaje id_objeto_personaje="O001"></objeto_personaje>
            </inventario>
        </personaje>
    
        <personaje idPersonaje="P002"> <!-- id unico-->
            <nombre>Olin</nombre>
            <raza>Mascota</raza>
            <clase>Mago</clase> <!-- Guerrero, Mago, Pícaro -->
            <nivel>35</nivel> <!-- 1-100 -->
            <stats>
                <fuerza>60</fuerza>
                <agilidad>50</agilidad>
                <inteligencia>40</inteligencia>
                <vida>200</vida>  <!-- + -->
            </stats>
            <inventario>
                <objeto_personaje id_objeto_personaje="O002"></objeto_personaje>
            </inventario>
        </personaje>
        
        <personaje idPersonaje="P003"> <!-- id unico-->
            <nombre>Titan</nombre>
            <raza>Humano</raza>
            <clase>Pícaro</clase> <!-- Guerrero, Mago, Pícaro -->
            <nivel>60</nivel> <!-- 1-100 -->
            <stats>
                <fuerza>40</fuerza>
                <agilidad>20</agilidad>
                <inteligencia>70</inteligencia>
                <vida>200</vida>  <!-- + -->
            </stats>
            <inventario>
                <objeto_personaje id_objeto_personaje="O003"></objeto_personaje>
            </inventario>
        </personaje>
    
  </personajes>
  
  
  <!-- MISIONES -->
  <misiones>
        <mision idMision="M001"> <!-- id unico-->
            <titulo>Salvar al castillo</titulo>
            <descripcion>Proteger el castillo de los trolls</descripcion>
            <dificultad>Media</dificultad>  <!-- Fácil, Media o Difícil -->
            <recompensa>
                <oro>150</oro>
                <experiencia>30</experiencia>
            </recompensa>
        </mision>
        
        <mision idMision="M002"> <!-- id unico-->
            <titulo>Rescatar al rey</titulo>
            <descripcion>Derrotar al dragón para rescatar al rey</descripcion>
            <dificultad>Difícil</dificultad>  <!-- Fácil, Media o Difícil -->
            <recompensa>
                <oro>300</oro>
                <experiencia>80</experiencia>
            </recompensa>
        </mision>
    
        <mision idMision="M003"> <!-- id unico-->
            <titulo>LLevar información</titulo>
            <descripcion>Transmitir la información de un personaje a otro</descripcion>
            <dificultad>Fácil</dificultad>  <!-- Fácil, Media o Difícil -->
            <recompensa>
                <oro>10</oro>
                <experiencia>5</experiencia>
            </recompensa>
        </mision>
  </misiones>
  
  
  <!-- OBJETOS -->
    <objetos>
        <objeto idObjeto="O001"> <!-- id unico -->
            <nombre>Escudo</nombre>
            <tipo>Armadura</tipo> <!-- arma, armadura, consumible -->
            <valor>80</valor>  <!-- precio en monedas de juego -->
            <efecto>Reduce el golpe del enemigo en 10 puntos</efecto>
        </objeto>
    
        <objeto idObjeto="O002"> <!-- id unico -->
            <nombre>Barita mágica</nombre>
            <tipo>Arma</tipo> <!-- arma, armadura, consumible -->
            <valor>90</valor>  <!-- precio en monedas de juego -->
            <efecto>Congela al enemigo durante 10 segundos</efecto>
        </objeto>
        
        <objeto idObjeto="O003"> <!-- id unico -->
            <nombre>Hongos</nombre>
            <tipo>Consumible</tipo> <!-- arma, armadura, consumible -->
            <valor>40</valor>  <!-- precio en monedas de juego -->
            <efecto>Aumenta la fuerza 30 puntos de fuerza</efecto>
        </objeto>
        
        <objeto idObjeto="O004"> <!-- id unico -->
            <nombre>Espada</nombre>
            <tipo>Arma</tipo> <!-- arma, armadura, consumible -->
            <valor>100</valor>  <!-- precio en monedas de juego -->
            <efecto>Mejora la agilidad en 40 puntos</efecto>
        </objeto>
        
        <objeto idObjeto="O005"> <!-- id unico -->
            <nombre>Casco</nombre>
            <tipo>Armadura</tipo> <!-- arma, armadura, consumible -->
            <valor>120</valor>  <!-- precio en monedas de juego -->
            <efecto>Reduce la fuerza del enemigo</efecto>
        </objeto>
    </objetos>
  
  
  <!-- ENEMIGOS -->
    <enemigos>
        <enemigo idEnemigo="E001"> <!-- id unico -->
            <nombre>Trolls</nombre>
            <nivel>60</nivel> <!-- 1-100 -->
            <vida>40</vida>  <!-- + -->
            <daño>30</daño>
            <tipo>Elfo</tipo> <!-- (bestia, humanoide, demonio, etc.) -->
            <loot>
                <objeto_enemigo id_objeto_enemigo="O005"></objeto_enemigo>
            </loot>
        </enemigo>
    
        <enemigo idEnemigo="E002"> <!-- id unico -->
            <nombre>Dragón</nombre>
            <nivel>100</nivel> <!-- 1-100 -->
            <vida>1500</vida>  <!-- + -->
            <daño>900</daño>
            <tipo>Demonio</tipo> <!-- (bestia, humanoide, demonio, etc.) -->
                <loot>
                    <objeto_enemigo id_objeto_enemigo="O003"></objeto_enemigo>
                </loot>
        </enemigo>
    
        <enemigo idEnemigo="E003"> <!-- id unico -->
            <nombre>Arqueros</nombre>
            <nivel>40</nivel> <!-- 1-100 -->
            <vida>50</vida>  <!-- + -->
            <daño>40</daño>
            <tipo>Humanoide</tipo> <!-- (bestia, humanoide, demonio, etc.) -->
            <loot>
                <objeto_enemigo id_objeto_enemigo="O001"></objeto_enemigo>
            </loot>
        </enemigo>

    </enemigos>
  
  
    <!-- LOCALIZACIONES -->
    <localizaciones>
        <localizacion idLocalizacion="L001"> <!-- id unico-->
            <nombre>Bosque encantado</nombre>
            <bioma>Bosque</bioma>   <!-- Bosque, Desierto, Cueva, Ciudad, Montaña, Nieve -->
            <enemigos_presentes>
                <enemigo_localizacion id_enemigo_localizacion="E002"></enemigo_localizacion>
            </enemigos_presentes>
        </localizacion>

        <localizacion idLocalizacion="L002"> <!-- id unico-->
            <nombre>Cueva de la muerte</nombre>
            <bioma>Cueva</bioma>   <!-- Bosque, Desierto, Cueva, Ciudad, Montaña, Nieve -->
            <enemigos_presentes>
                <enemigo_localizacion id_enemigo_localizacion="E001"></enemigo_localizacion>
            </enemigos_presentes>
        </localizacion>

        <localizacion idLocalizacion="L003"> <!-- id unico-->
            <nombre>Pico de los misterios </nombre>
            <bioma>Montaña</bioma>   <!-- Bosque, Desierto, Cueva, Ciudad, Montaña, Nieve -->
            <enemigos_presentes>
                <enemigo_localizacion id_enemigo_localizacion="E003"></enemigo_localizacion>
            </enemigos_presentes>
        </localizacion>

    </localizaciones>

</rpg>
```



#### SOLUCIÓN DTD
``` xml
<!DOCTYPE rpg [
    <!ELEMENT rpg (videojuego, personajes, misiones, objetos, enemigos, localizaciones)>

    <!-- VIDEOJUEGO -->
    <!ELEMENT videojuego (titulo, desarrollador, plataformas, año_lanzamiento, version)>
    <!ELEMENT plataformas (plataforma+)>


    <!-- PERSONAJES -->
    <!ELEMENT personajes (personaje+)>
    <!ATTLIST personaje 
        idPersonaje ID #REQUIRED
    >
    <!ELEMENT personaje (nombre, raza, clase, nivel, stats, inventario)>
    <!ELEMENT stats (fuerza, agilidad, inteligencia, vida)>
    <!ELEMENT inventario (objeto_personaje+)>
    <!ELEMENT objeto_personaje EMPTY>
    <!ATTLIST objeto_personaje 
        id_objeto_personaje IDREF #REQUIRED
    >


    <!-- MISIONES -->
    <!ELEMENT misiones (mision+)>
    <!ATTLIST mision 
        idMision ID #REQUIRED
    >
    <!ELEMENT mision (titulo, descripcion, dificultad, recompensa)>
    <!ELEMENT recompensa (oro, experiencia)>

    <!-- OBJETOS -->
    <!ELEMENT objetos (objeto+)>
    <!ATTLIST objeto
        idObjeto ID #REQUIRED
    >
    <!ELEMENT objeto (nombre, tipo, valor, efecto)>

    <!-- ENEMIGOS -->
    <!ELEMENT enemigos (enemigo+)>
    <!ATTLIST enemigo
        idEnemigo ID #REQUIRED
    >
    <!ELEMENT enemigo (nombre, nivel, vida, daño, tipo, loot)>
    <!ELEMENT loot (objeto_enemigo+)>
    <!ELEMENT objeto_enemigo EMPTY>
    <!ATTLIST objeto_enemigo
        id_objeto_enemigo IDREF #REQUIRED
    >

    <!-- LOCALIZACIONES -->
    <!ELEMENT localizaciones (localizacion+)>
    <!ATTLIST localizacion
        idLocalizacion ID #REQUIRED
    >
    <!ELEMENT localizacion (nombre, bioma, enemigos_presentes)>
    <!ELEMENT enemigos_presentes (enemigo_localizacion)>
    <!ELEMENT enemigo_localizacion EMPTY>
    <!ATTLIST enemigo_localizacion
        id_enemigo_localizacion IDREF #REQUIRED
    >

    <!ELEMENT titulo (#PCDATA)>
    <!ELEMENT desarrollador (#PCDATA)>
    <!ELEMENT plataforma (#PCDATA)>
    <!ELEMENT año_lanzamiento (#PCDATA)>
    <!ELEMENT version (#PCDATA)>
    <!ELEMENT nombre (#PCDATA)>
    <!ELEMENT raza (#PCDATA)>
    <!ELEMENT clase (#PCDATA)>
    <!ELEMENT nivel (#PCDATA)>
    <!ELEMENT fuerza (#PCDATA)>
    <!ELEMENT agilidad (#PCDATA)>
    <!ELEMENT inteligencia (#PCDATA)>
    <!ELEMENT vida (#PCDATA)>
    <!ELEMENT descripcion (#PCDATA)>
    <!ELEMENT dificultad (#PCDATA)>
    <!ELEMENT oro (#PCDATA)>
    <!ELEMENT experiencia (#PCDATA)>
    <!ELEMENT tipo (#PCDATA)>
    <!ELEMENT valor (#PCDATA)>
    <!ELEMENT efecto (#PCDATA)>
    <!ELEMENT daño (#PCDATA)>
    <!ELEMENT bioma (#PCDATA)>
]>
```



#### SOLUCIÓN XSD
``` xml
<xsd:schema xmlns:xsd="http://www.w3.org/2001/XMLSchema">

    <xsd:element name="rpg">
        <xsd:complexType>
            <xsd:sequence>
                <xsd:element name="videojuego" type="videojuegoType"/>
                <xsd:element name="personajes" type="personajesType"/>
                <xsd:element name="misiones" type="misionesType"/>
                <xsd:element name="objetos" type="objetosType"/>
                <xsd:element name="enemigos" type="enemigosType"/>
                <xsd:element name="localizaciones" type="localizacionesType"/>
            </xsd:sequence>
        </xsd:complexType>

        <xsd:key name="claveIDPersonaje">
            <xsd:selector xpath="rpg/personajes/personaje"/>
            <xsd:field xpath="@idPersonaje"/>
        </xsd:key>

        <xsd:key name="claveIDMision">
            <xsd:selector xpath="rpg/misiones/mision"/>
            <xsd:field xpath="@idMision"/>
        </xsd:key>

        <xsd:key name="claveIDObjeto">
            <xsd:selector xpath="rpg/objetos/objeto"/>
            <xsd:field xpath="@idObjeto"/>
        </xsd:key>

        <xsd:key name="claveIDEnemigo">
            <xsd:selector xpath="rpg/enemigos/enemigo"/>
            <xsd:field xpath="@idEnemigo"/>
        </xsd:key>

        <xsd:key name="claveIDLocalizacion">
            <xsd:selector xpath="rpg/localizaciones/localizacion"/>
            <xsd:field xpath="@idLocalizacion"/>
        </xsd:key>

        <xsd:keyref name="claveRefObjetoPersonaje" refer="claveIDObjeto">
            <xsd:selector xpath="rpg/personajes/personaje/inventario/objeto_personaje"/>
            <xsd:field xpath="@id_objeto_personaje"/>
        </xsd:keyref>

        <xsd:keyref name="claveRefObjetoEnemigo" refer="claveIDObjeto">
            <xsd:selector xpath="rpg/enemigos/enemigo/loot/objeto_enemigo"/>
            <xsd:field xpath="@id_objeto_enemigo"/>
        </xsd:keyref>

        <xsd:keyref name="claveRefEnemigoLocalizacion" refer="claveIDEnemigo">
            <xsd:selector xpath="rpg/localizaciones/localizacion/enemigos_presentes/enemigo_localizacion"/>
            <xsd:field xpath="@id_enemigo_localizacion"/>
        </xsd:keyref>

    </xsd:element>

    <!-- VIDEOJUEGO -->
    <xsd:complexType name="videojuegoType">
        <xsd:sequence>
            <xsd:element name="titulo" type="xsd:string"/>
            <xsd:element name="desarrollador" type="xsd:string"/>
            <xsd:element name="plataformas" type="plataformasType"/>
            <xsd:element name="año_lanzamiento" type="año_lanzamientoType"/>
            <xsd:element name="version" type="versionType"/>
        </xsd:sequence>
    </xsd:complexType>

    <xsd:complexType name="plataformasType">
        <xsd:sequence>
            <xsd:element name="plataforma" type="xsd:string" maxOccurs="unbounded"/>
        </xsd:sequence>
    </xsd:complexType>

    <xsd:simpleType name="año_lanzamientoType">
        <xsd:restriction base="xsd:integer">
            <xsd:totalDigits value="4"/>
        </xsd:restriction>
    </xsd:simpleType>

    <xsd:simpleType name="versionType">
        <xsd:restriction base="xsd:decimal">
            <xsd:totalDigits value="2"/>
            <xsd:fractionDigits value="1"/>
        </xsd:restriction>
    </xsd:simpleType>

    <!-- PERSONAJES -->
    <xsd:complexType name="personajesType">
        <xsd:sequence>
            <xsd:element name="personaje" type="personajeType" maxOccurs="unbounded"/>
        </xsd:sequence>
    </xsd:complexType>

    <xsd:complexType name="personajeType">
        <xsd:sequence>
            <xsd:element name="nombre" type="xsd:string"/>
            <xsd:element name="raza" type="xsd:string"/>
            <xsd:element name="clase" type="xsd:string"/>
            <xsd:element name="nivel" type="nivelType"/>
            <xsd:element name="stats" type="statsType"/>
            <xsd:element name="inventario" type="inventarioType"/>
        </xsd:sequence>
        <xsd:attribute name="idPersonaje" type="xsd:string" use="required"/>
    </xsd:complexType>

    <xsd:simpleType name="nivelType">
        <xsd:restriction base="xsd:integer">
            <xsd:minInclusive value="1"/>
            <xsd:maxInclusive value="100"/>
        </xsd:restriction>
    </xsd:simpleType>

    <xsd:complexType name="statsType">
        <xsd:sequence>
            <xsd:element name="fuerza" type="xsd:integer"/>
            <xsd:element name="agilidad" type="xsd:integer"/>
            <xsd:element name="inteligencia" type="xsd:integer"/>
            <xsd:element name="vida" type="vidaType"/>
        </xsd:sequence>
    </xsd:complexType>

    <xsd:simpleType name="vidaType">
        <xsd:restriction base="xsd:integer">
            <xsd:minInclusive value="1"/>
        </xsd:restriction>
    </xsd:simpleType>

    <xsd:complexType name="inventarioType">
        <xsd:sequence>
            <xsd:element name="objeto_personaje" type="objeto_personajeType"/>
        </xsd:sequence>
    </xsd:complexType>

    <xsd:complexType name="objeto_personajeType">
        <xsd:attribute name="id_objeto_personaje" type="idObjetoType" use="required"/>
    </xsd:complexType>

    <!-- MISIONES -->
    <xsd:complexType name="misionesType">
        <xsd:sequence>
            <xsd:element name="mision" type="misionType" maxOccurs="unbounded"/>
        </xsd:sequence>
    </xsd:complexType>

    <xsd:complexType name="misionType">
        <xsd:sequence>
            <xsd:element name="titulo" type="xsd:string"/>
            <xsd:element name="descripcion" type="xsd:string"/>
            <xsd:element name="dificultad" type="dificultadType"/>
            <xsd:element name="recompensa" type="recompensaType"/>
        </xsd:sequence>
        <xsd:attribute name="idMision" type="xsd:string" use="required"/>
    </xsd:complexType>

    <xsd:simpleType name="dificultadType">
        <xsd:restriction base="xsd:string">
            <xsd:enumeration value="Media"/>
            <xsd:enumeration value="Fácil"/>
            <xsd:enumeration value="Difícil"/>
        </xsd:restriction>
    </xsd:simpleType>
    
    <xsd:complexType name="recompensaType">
        <xsd:sequence>
            <xsd:element name="oro" type="xsd:integer"/>
            <xsd:element name="experiencia" type="xsd:integer"/>
        </xsd:sequence>
    </xsd:complexType>

    <!-- OBJETOS -->
    <xsd:complexType name="objetosType">
        <xsd:sequence>
            <xsd:element name="objeto" type="objetoType" maxOccurs="unbounded" />
        </xsd:sequence>
    </xsd:complexType>

    <xsd:complexType name="objetoType">
        <xsd:sequence>
            <xsd:element name="nombre" type="xsd:string"/>
            <xsd:element name="tipo" type="tipoType"/>
            <xsd:element name="valor" type="precioType"/>
            <xsd:element name="efecto" type="xsd:string"/>
        </xsd:sequence>
        <xsd:attribute name="idObjeto" type="idObjetoType" use="required"/>
    </xsd:complexType>

    <xsd:simpleType name="tipoType">
        <xsd:restriction base="xsd:string">
            <xsd:enumeration value="Armadura"/>
            <xsd:enumeration value="Arma"/>
            <xsd:enumeration value="Consumible"/>
        </xsd:restriction>
    </xsd:simpleType>

    <xsd:simpleType name="precioType">
        <xsd:restriction base="xsd:integer">
            <xsd:minInclusive value="0"/>
        </xsd:restriction>
    </xsd:simpleType>

    <xsd:simpleType name="idObjetoType">
        <xsd:restriction base="xsd:string">
            <xsd:pattern value="O[0-9]{3}"/>
        </xsd:restriction>
    </xsd:simpleType>

    <!-- ENEMIGOS -->
    <xsd:complexType name="enemigosType">
        <xsd:sequence>
            <xsd:element name="enemigo" type="enemigoType" maxOccurs="unbounded"/>
        </xsd:sequence>
    </xsd:complexType>

    <xsd:complexType name="enemigoType">
        <xsd:sequence>
            <xsd:element name="nombre" type="xsd:string"/>
            <xsd:element name="nivel" type="nivelType"/>
            <xsd:element name="vida" type="vidaType"/>
            <xsd:element name="daño" type="xsd:integer"/>
            <xsd:element name="tipo" type="xsd:string"/>
            <xsd:element name="loot" type="lootType"/>
        </xsd:sequence>
        <xsd:attribute name="idEnemigo" type="idEnemigoType" use="required"/>
    </xsd:complexType>

    <xsd:complexType name="lootType">
        <xsd:sequence>
            <xsd:element name="objeto_enemigo" type="objeto_enemigoType"/>
        </xsd:sequence>
    </xsd:complexType>

    <xsd:complexType name="objeto_enemigoType">
        <xsd:attribute name="id_objeto_enemigo" type="idObjetoType" use="required"/>
    </xsd:complexType>

    <xsd:simpleType name="idEnemigoType">
        <xsd:restriction base="xsd:string">
            <xsd:pattern value="E[0-9]{3}"/>
        </xsd:restriction>
    </xsd:simpleType>

    <!-- LOCALIZACIONES -->
    <xsd:complexType name="localizacionesType">
        <xsd:sequence>
            <xsd:element name="localizacion" type="localizacionType" maxOccurs="unbounded"/>
        </xsd:sequence>
    </xsd:complexType>

    <xsd:complexType name="localizacionType">
        <xsd:sequence>
            <xsd:element name="nombre" type="xsd:string"/>
            <xsd:element name="bioma" type="biomaType"/>
            <xsd:element name="enemigos_presentes" type="enemigos_presentesType"/>
        </xsd:sequence>
        <xsd:attribute name="idLocalizacion" type="idLocalizacionType" use="required"/>
    </xsd:complexType>

    <xsd:complexType name="enemigos_presentesType">
        <xsd:sequence>
            <xsd:element name="enemigo_localizacion" type="enemigo_localizacionType"/>
        </xsd:sequence>
    </xsd:complexType>

    <xsd:complexType name="enemigo_localizacionType">
        <xsd:attribute name="id_enemigo_localizacion" type="idEnemigoType" />
    </xsd:complexType>

    <xsd:simpleType name="biomaType">
        <xsd:restriction base="xsd:string">
            <xsd:enumeration value="Bosque"/>
            <xsd:enumeration value="Desierto"/>
            <xsd:enumeration value="Cueva"/>
            <xsd:enumeration value="Ciudad"/>
            <xsd:enumeration value="Montaña"/>
            <xsd:enumeration value="Nieve"/>
        </xsd:restriction>
    </xsd:simpleType>

    <xsd:simpleType name="idLocalizacionType">
        <xsd:restriction base="xsd:string">
            <xsd:pattern value="L[0-9]{3}"/>
        </xsd:restriction>
    </xsd:simpleType>

</xsd:schema>
```