from sqlalchemy import Column, Integer, Boolean, Text, Date, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Analise(Base):
    __tablename__ = "analise"

    id_analise = Column(Integer, primary_key=True, index=True)
    id_problema = Column(Integer, ForeignKey("identificacao_problemas.id_problema"))
    viabilidade = Column(Boolean)
    alternativas = Column(Text)
    impacto = Column(Text)
    escopo = Column(Text)
    data_analise = Column(Date)
    status = Column(String(1))  # [1] - Em andamento, [2] - Em projeto
    analista_responsavel = Column(String(100))
