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