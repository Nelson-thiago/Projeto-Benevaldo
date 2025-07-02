from pydantic import BaseModel
from datetime import date

class AnaliseBase(BaseModel):
    id_problema: int
    viabilidade: bool
    alternativas: str
    impacto: str
    escopo: str
    data_analise: date
    status: str
    analista_responsavel: str

class AnaliseCreate(AnaliseBase):
    pass

class AnaliseUpdate(AnaliseBase):
    pass

class AnaliseOut(AnaliseBase):
    id_analise: int

    class Config:
        orm_mode = True
