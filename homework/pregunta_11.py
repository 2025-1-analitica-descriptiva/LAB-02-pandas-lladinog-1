"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""
from homework.utils import new_dataframe, get_column_values_by_group, get_unique_column_values

def pregunta_11():
    """
    Construya una tabla que contenga `c0` y una lista separada por ',' de
    los valores de la columna `c4` del archivo `tbl1.tsv`.

    Rta/
         c0       c4
    0     0    b,f,g
    1     1    a,c,f
    2     2  a,c,e,f
    3     3      a,b
    ...
    37   37  a,c,e,f
    38   38      d,e
    39   39    a,d,f
    """
    column0= get_unique_column_values("files/input/tbl1.tsv", "c0")
    grouped = get_column_values_by_group("files/input/tbl1.tsv", "c0", "c4")
    result = new_dataframe(["c0","c4"], [column0,grouped.apply(lambda x: ','.join(sorted(set(x))))])

    return result
