# FranceProyect
IA Player movement in a Maze

A tener en cuenta:
    1) Los llamados a metodos de una clase deben hacerse con nombre() por mas que no se les pase ningun parametro. De otra manera
    python no entiende que queremos referenciar un metodo y lo saltea en vez de ejecutarlo

    2) Al maze se accede con coordnadas [y][x]

ERROR actual:
Cuando el camino se bloquea funciona bien la vuelta hasta encontrar otro camino posible pero por alguna razon estamos perdiendo la celda anterior. La linea 247 me genera desconfianza, pero si la saco entramos en un loop infinito entre dos posiciones.
