
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
   - `<año_lanzamiento>` debe tener 4 dígitos.
   - `<dificultad>` de las misiones solo puede ser "Fácil", "Media" o "Difícil".
   - `<bioma>` solo puede ser "Bosque", "Desierto", "Cueva", "Ciudad", "Montaña", "Nieve".

---

¡Buena suerte! 🚀🎮

#### SOLUCIÓN XML
``` xml
<?xml version="1.0" encoding="UTF-8"?>
<rpg>
    <videojuego> <!-- al menos 1: + -->
        <titulo>Mundo de magia</titulo>
        <desarrollador>MagiaSoft</desarrollador>
        <plataformas>
            <plataforma>PC</plataforma> <!-- + -->
            <plataforma>Xbox</plataforma>
        </plataformas>
        <anio_lanzamiento>2024</anio_lanzamiento> <!-- formato AAAA -->
        <version>1.8</version> <!-- formato X.Y-->
    </videojuego>
    
    <personajes>
        <personaje id="P_001"> <!-- id único -->
            <nombre>Garnalf</nombre>
            <raza>Humano</raza>
            <clase>Mago</clase>
            <nivel>85</nivel> <!-- 1 - 100-->
            <stats>
                <fuerza>50</fuerza>
                <agilidad>60</agilidad>
                <inteligencia>90</inteligencia>
                <vida>200</vida> <!-- numero positivo -->
            </stats> 
            <inventario>
                <objeto id="O_001"></objeto> <!-- ref id objeto -->
            </inventario>
        </personaje>
        <personaje id="P_002"> 
            <nombre>Kilwer</nombre>
            <raza>Elfo</raza>
            <clase>Arquero</clase>
            <nivel>50</nivel> 
            <stats>
                <fuerza>40</fuerza>
                <agilidad>80</agilidad>
                <inteligencia>40</inteligencia>
                <vida>400</vida>
            </stats> 
            <inventario>
                <objeto id="O_002"></objeto>
            </inventario>
        </personaje>
        <personaje id="P_003"> 
            <nombre>Legolas</nombre>
            <raza>Esqueleto</raza>
            <clase>Guerrero</clase>
            <nivel>70</nivel> 
            <stats>
                <fuerza>50</fuerza>
                <agilidad>70</agilidad>
                <inteligencia>60</inteligencia>
                <vida>300</vida>
            </stats> 
            <inventario>
                <objeto>O_002</objeto> 
            </inventario>
        </personaje>
        
    </personajes>
    
    <misiones>
        <mision id="M_001"> <!-- id único -->
            <titulo>Salvar al Reino</titulo>
            <descripcion>Derrotar al dragón y salvar al reino de la oscuridad</descripcion>
            <dificultad>Difícil</dificultad> <!-- Fácil, Media, Difícil -->
            <recompensa>
                <oro>500</oro>
                <experiencia>1000</experiencia>
            </recompensa>
        </mision>
        <mision id="M_002">
            <titulo>Recuperar la Espada</titulo>
            <descripcion>Encuentra y recupera la espada mágica perdida</descripcion>
            <dificultad>Media</dificultad>
            <recompensa>
                <oro>300</oro>
                <experiencia>800</experiencia>
            </recompensa>
        </mision>
        <mision id="M_003">
            <titulo>Pergamino en camino</titulo>
            <descripcion>LLevar el pergamino al rey</descripcion>
            <dificultad>Fácil</dificultad>
            <recompensa>
                <oro>50</oro>
                <experiencia>10</experiencia>
            </recompensa>
        </mision>
    </misiones>
    
    <objetos>
        <objeto id="O_001"> <!-- id único -->
            <nombre>Espada de la Vida</nombre>
            <tipo>Arma</tipo> <!-- arma, armadura, consumible -->
            <valor>1200</valor> <!-- precio en monedas del juego-->
            <efecto>Aumenta la vida en 100 puntos</efecto> <!-- modificación de atributos que otorga: PCDATA -->
        </objeto>
        <objeto id="O_002">
            <nombre>Varita de la Libertad</nombre>
            <tipo>Arma</tipo>
            <valor>1100</valor>
            <efecto>Aumenta la agilidad en 50 puntos</efecto>
        </objeto>
        <objeto id="O_003">
            <nombre>Casco del Dragón</nombre>
            <tipo>Armadura</tipo> <!-- arma, armadura, consumible -->
            <valor>1300</valor> <!-- precio en monedas del juego-->
            <efecto>Aumenta el vida en un 15%</efecto> <!-- modificación de atributos que otorga: PCDATA -->
        </objeto>
        <objeto id="O_004">
            <nombre>Setas del mago</nombre>
            <tipo>Consumible</tipo> 
            <valor>150</valor>
            <efecto>Reducen el daño del enemigo en 10 puntos</efecto>
        </objeto>
        <objeto id="O_005"> 
            <nombre>Manzana envenenada</nombre>
            <tipo>Consumible</tipo>
            <valor>200</valor>
            <efecto>Reduce la vida de los enemigos en 30 puntos</efecto>
        </objeto>
    </objetos>
    
    <enemigos>
        <enemigo id="E_001"> <!-- id único -->
            <nombre>Demonio de Fuego</nombre>
            <nivel>100</nivel>
            <vida>1000</vida>
            <daño>500</daño>
            <tipo>Demonio</tipo>
            <loot>
                <objeto idref="O_001"></objeto> <!-- texto: referencia a objeto -->
            </loot>
        </enemigo>
        <enemigo id="E_002">
            <nombre>Troll de las Cavernas</nombre>
            <nivel>400</nivel>
            <vida>900</vida>
            <daño>30</daño>
            <tipo>Elfo</tipo>
            <loot>
                <objeto>O_005</objeto>
            </loot>
        </enemigo>
        <enemigo id="E_003">
            <nombre>Mago del fuego</nombre>
            <nivel>500</nivel>
            <vida>1300</vida>
            <daño>60</daño>
            <tipo>Hechicero</tipo>
            <loot>
                <objeto>O_004</objeto>
            </loot>
        </enemigo>
    </enemigos>
    
    <localizaciones>
        <mapa>
            <localizacion id="L_001"> <!-- id único -->
                <nombre>Bosque Encantado</nombre>
                <bioma>Bosque</bioma> <!-- bosque, desierto, cueva, ciudad -->
                <enemigos_presentes>
                    <enemigo>E_003</enemigo> <!-- ref enemigo -->
                </enemigos_presentes>
            </localizacion>
            <localizacion id="L_002">
                <nombre>Río del Destino</nombre>
                <bioma>Bosque</bioma>
                <enemigos_presentes>
                    <enemigo>E_001</enemigo>
                </enemigos_presentes>
            </localizacion> 
            <localizacion id="L_003">
                <nombre>Montaña Fantasma</nombre>
                <bioma>Desierto</bioma>
                <enemigos_presentes>
                    <enemigo>E_002</enemigo>
                </enemigos_presentes>
            </localizacion> 
        </mapa>
    </localizaciones>
    
</rpg>
```


#### SOLUCIÓN DTD
``` xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE rpg [
    <!ELEMENT rpg (videojuego+, personajes, misiones, objetos, enemigos, localizaciones)>
    <!ELEMENT videojuego (titulo, desarrollador, plataformas, anio_lanzamiento, version)>
    <!ELEMENT plataformas (plataforma+)>
    <!ELEMENT personajes (personaje+)>
    <!ELEMENT personaje (nombre, raza, clase, nivel, stats, inventario)>
    <!ELEMENT stats (fuerza, agilidad, inteligencia, vida)>
    <!ELEMENT inventario (objeto+)>
    <!ELEMENT objeto EMPTY>
    <!ATTLIST personaje
      id IDREF #REQUIRED
    >
    <!ELEMENT misiones (mision+)>
    <!ATTLIST mision
      id ID #REQUIRED
    >
    <!ELEMENT mision (titulo, descripcion, dificultad, recompensa)>
    <!ELEMENT recompensa (oro, experiencia)>
    <!ELEMENT objetos (objeto+)>
    <!ATTLIST objeto
      id ID #REQUIRED
    >
    <!ELEMENT objeto (nombre, tipo, valor, efecto)>
    <!ELEMENT enemigos (enemigo+)>
    <!ATTLIST enemigo
      id ID #REQUIRED
    >
    <!ELEMENT enemigo (nombre, nivel, vida, daño, tipo, loot)>
    <!ELEMENT loot (objeto+)>
    <!ATTLIST objeto
      id IDREF #REQUIRED
    >
    <!ELEMENT localizaciones (mapa)>
    <!ELEMENT mapa (localicacion)>
    <!ELEMENT  ()>
    <!ELEMENT  ()>
    <!ELEMENT  ()>
    <!ELEMENT  ()>
    <!ELEMENT  ()>
    <!ELEMENT  ()>
    <!ELEMENT  ()>
    <!ELEMENT  ()>
    <!ELEMENT  ()>
    <!ELEMENT  ()>
    <!ELEMENT  ()>
    <!ATTLIST 
      
    >
    <!ATTLIST 
      
    >
    <!ATTLIST 
      
    >
    <!ATTLIST 
      
    >
    <!ATTLIST 
      
    >
    <!ATTLIST 
      
    >
    <!ATTLIST 
      
    >
    <!ELEMENT  ()>
    <!ELEMENT  ()>
    <!ELEMENT  ()>
    <!ELEMENT  ()>
    <!ELEMENT  ()>
    <!ELEMENT  ()>
    <!ELEMENT  ()>
    <!ELEMENT  ()>
    <!ELEMENT  ()>
    <!ELEMENT  ()>
    <!ELEMENT  ()>
    <!ELEMENT  ()>
    <!ELEMENT  ()>
    <!ELEMENT  ()>
    <!ELEMENT  ()>
    <!ELEMENT  ()>
    <!ELEMENT  ()>
    <!ELEMENT  ()>
    <!ELEMENT  ()>
    <!ELEMENT  ()>
    <!ELEMENT  ()>
    <!ELEMENT  ()>
    <!ELEMENT  ()>
    <!ELEMENT  ()>
    

]>
```

#### SOLUCIÓN XSD
``` xml

```