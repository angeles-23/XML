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
