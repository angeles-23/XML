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