# Ejercicio: repeticiones de opciones
Se necesita un formato de archivo para intercambiar productos entre almacenes de productos de librería y se desea una DTD que incluya estas restricciones:

- Debe haber un elemento raíz pedido que puede constar de libros, cuadernos y/o lápices. Los tres elementos pueden aparecer repetidos y en cualquier orden. Tambien pueden aparecer por ejemplo 4 libros, 2 lapices y luego 4 lapices de nuevo.

- Todo libro tiene un atributo obligatorio titulo.

- Los elementos cuaderno tiene un atributo optativo num_hojas.

- Todo elemento lápiz debe tener dentro un elemento obligatorio número.