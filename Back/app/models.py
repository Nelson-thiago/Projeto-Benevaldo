from sqlalchemy import Column, Integer, Boolean, Text, Date, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
class IdentificacaoProblemas(Base):
    __tablename__ = "identificacao_problemas"
    id_problema = Column(Integer, primary_key=True, index=True)
    id_requisicao = Column(Integer) # Não precisa da FK aqui, só o campo
    titulo = Column(String(255))
    descricao = Column(Text)
    tipo_manutencao = Column(String(50))
    prioridade = Column(String(20))
    data_identificacao = Column(Date)
    identificado_por = Column(String(100))
    status = Column(String(1))
    versao_afetada = Column(String(20))

class Analise(Base):
    __tablename__ = "analise"

    id_analise = Column(Integer, primary_key=True, index=True)
    id_problema = Column(Integer, ForeignKey("identificacao_problemas.id_problema")) 
    viabilidade = Column(Boolean)
    alternativas = Column(Text)
    impacto = Column(Text)
    escopo = Column(Text)
    data_analise = Column(Date)
    status = Column(String(1))
    analista_responsavel = Column(String(100))