"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""
from homework.utils import new_dataframe, get_column_values_by_group, get_unique_column_values

def pregunta_12():
    """
    Construya una tabla que contenga `c0` y una lista separada por ','
    de los valores de la columna `c5a`  y `c5b` (unidos por ':') de la
    tabla `tbl2.tsv`.

    Rta/
         c0                                   c5
    0     0        bbb:0,ddd:9,ggg:8,hhh:2,jjj:3
    1     1              aaa:3,ccc:2,ddd:0,hhh:9
    2     2              ccc:6,ddd:2,ggg:5,jjj:1
    ...
    37   37                    eee:0,fff:2,hhh:6
    38   38                    eee:0,fff:9,iii:2
    39   39                    ggg:3,hhh:8,jjj:5
    """
    column0 = get_unique_column_values("files/input/tbl2.tsv", "c0")
    grouped = get_column_values_by_group("files/input/tbl2.tsv", "c0", ["c5a", "c5b"])

    # Combine c5a and c5b into a single string with 'c5a:c5b' format sorted alphabetically
    combined = grouped.apply(lambda x: ','.join(sorted(f"{a}:{b}" for a, b in zip(x['c5a'], x['c5b']))))

    result = new_dataframe(["c0", "c5"], [column0, combined])

    return result

