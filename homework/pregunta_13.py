"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""
from homework.utils import get_dataframe, get_column_values_by_group

def pregunta_13():
    """
    Si la columna `c0` es la clave en los archivos `tbl0.tsv` y `tbl2.tsv`,
    compute la suma de `tbl2.c5b` por cada valor en `tbl0.c1`.

    Rta/
    c1
    A    146
    B    134
    C     81
    D    112
    E    275
    Name: c5b, dtype: int64
    """
    # Load the series
    # get the series with the column c1 as index and the list of ints that refers to values of c0 gruped by c1
    grouped1 = get_column_values_by_group("files/input/tbl0.tsv", "c1", "c0").apply(lambda x: [int(i) for i in x])
    grouped2 = get_column_values_by_group("files/input/tbl2.tsv", "c0", "c5b").sum()

    # Mix two series
    result = grouped1.apply(lambda x: grouped2[x].sum())
    result.index.name = "c1"
    return result


if __name__ == "__main__":
    print(pregunta_13())
