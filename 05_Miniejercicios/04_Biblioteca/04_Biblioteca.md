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
