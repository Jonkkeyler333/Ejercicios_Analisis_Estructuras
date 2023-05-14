from empty import Empty
from pilas import Pila

def test_Pila():
    # Crear una pila vacía
    p = Pila()

    # Verificar que la pila está vacía
    assert p.is_Empty() == True
    assert len(p) == 0

    # Agregar algunos elementos a la pila
    p.push('a')
    p.push('b')
    p.push('c')

    # Verificar que la pila no está vacía
    assert p.is_Empty() == False
    assert len(p) == 3

    # Verificar que el último elemento agregado está en la cima de la pila
    assert p.top() == 'c'

    # Remover el último elemento agregado
    assert p.pop() == 'c'

    # Verificar que el último elemento agregado que queda está en la cima de la pila
    assert p.top() == 'b'

    # Remover todos los elementos de la pila
    p.clear()

    # Verificar que la pila está vacía de nuevo
    assert p.is_Empty() == True
    assert len(p) == 0

    # Intentar remover un elemento de la pila vacía y verificar que se levanta la excepción Empty
    try:
        p.pop()
    except Empty:
        pass
    else:
        assert False, "Se esperaba una excepción Empty pero no se levantó ninguna excepción"

    # Intentar obtener el elemento en la cima de la pila vacía y verificar que se levanta la excepción Empty
    try:
        p.top()
    except Empty:
        pass
    else:
        assert False, "Se esperaba una excepción Empty pero no se levantó ninguna excepción"

if __name__ == '__main__':
    test_Pila()