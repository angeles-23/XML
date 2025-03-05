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