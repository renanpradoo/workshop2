import pandera as pa
from pandera.typing import Series

class MyDataFrameSchema(pa.SchemaModel):
    id_produto: Series[int]
    nome: Series[str]
    quantidade: Series[int]
    preco: Series[float]
    categoria: Series[str]

    class Config:
        coerce = True
        strict = True
