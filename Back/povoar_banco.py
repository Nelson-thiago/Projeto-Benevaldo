import datetime
from sqlalchemy import create_engine, Column, Integer, String, Date, Text, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker

# --- 1. CONFIGURAÇÃO DO BANCO DE DADOS ---
# ATENÇÃO: Substitua 'USUARIO', 'SENHA' e 'NOME_DO_BANCO' pelos dados do seu XAMPP/MySQL.
DATABASE_URL = "mysql+mysqlclient://root:@localhost/projeto_ieee"

engine = create_engine(DATABASE_URL, echo=True)
Base = declarative_base()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# --- 2. DEFINIÇÃO DOS MODELOS DAS TABELAS ANTERIORES ---

# [cite_start]Modelo para a Tabela: requisicao_alteracao (Módulo 01) [cite: 34]
class RequisicaoAlteracao(Base):
    __tablename__ = 'requisicao_alteracao'

    [cite_start]id_requisicao = Column(Integer, primary_key=True, autoincrement=True) # [cite: 35]
    [cite_start]titulo = Column(String(255)) # [cite: 35]
    [cite_start]descricao = Column(Text) # [cite: 35]
    [cite_start]solicitante = Column(String(100)) # [cite: 35]
    [cite_start]data_solicitacao = Column(Date) # [cite: 35]
    [cite_start]analista_responsavel = Column(String(100)) # [cite: 35]
    [cite_start]status = Column(String(1)) # [cite: 35]

# [cite_start]Modelo para a Tabela: identificacao_problemas (Módulo 02) [cite: 36]
class IdentificacaoProblemas(Base):
    __tablename__ = 'identificacao_problemas'

    [cite_start]id_problema = Column(Integer, primary_key=True, autoincrement=True) # [cite: 37]
    [cite_start]id_requisicao = Column(Integer, ForeignKey('requisicao_alteracao.id_requisicao')) # [cite: 37]
    [cite_start]titulo = Column(String(255)) # [cite: 37]
    [cite_start]descricao = Column(Text) # [cite: 37]
    [cite_start]tipo_manutencao = Column(String(50)) # [cite: 37]
    [cite_start]prioridade = Column(String(20)) # [cite: 37]
    [cite_start]data_identificacao = Column(Date) # [cite: 37]
    [cite_start]identificado_por = Column(String(100)) # [cite: 37]
    [cite_start]status = Column(String(1)) # [cite: 37]
    [cite_start]versao_afetada = Column(String(20)) # [cite: 37]

# --- 3. FUNÇÃO PRINCIPAL PARA POVOAR O BANCO ---

def popular_dados():
    # Cria as tabelas no banco de dados, se não existirem
    Base.metadata.create_all(bind=engine)
    print("Modelos de tabela verificados/criados.")

    session = SessionLocal()

    try:
        # --- Dados para Tabela 'requisicao_alteracao' ---
        print("Inserindo dados na tabela 'requisicao_alteracao'...")
        req1 = RequisicaoAlteracao(
            [cite_start]titulo="Corrigir bug de login em navegadores mobile", # [cite: 35]
            [cite_start]descricao="Usuários não conseguem fazer login usando Chrome em dispositivos Android.", # [cite: 35]
            [cite_start]solicitante="Equipe de Suporte", # [cite: 35]
            [cite_start]data_solicitacao=datetime.date(2025, 6, 20), # [cite: 35]
            [cite_start]analista_responsavel="Warlison Samuel", # [cite: 35]
            [cite_start]status="2" # [cite: 35]
        )
        req2 = RequisicaoAlteracao(
            [cite_start]titulo="Adicionar novo relatório de vendas anuais", # [cite: 35]
            [cite_start]descricao="O setor de vendas precisa de um relatório consolidado anual com gráficos.", # [cite: 35]
            [cite_start]solicitante="Diretoria de Vendas", # [cite: 35]
            [cite_start]data_solicitacao=datetime.date(2025, 6, 25), # [cite: 35]
            [cite_start]analista_responsavel="Lívia Silva", # [cite: 35]
            [cite_start]status="2" # [cite: 35]
        )
        req3 = RequisicaoAlteracao(
            [cite_start]titulo="Atualizar sistema para nova regulamentação fiscal", # [cite: 35]
            [cite_start]descricao="O sistema precisa ser adaptado para a nova Lei Fiscal XYZ, que entra em vigor em agosto.", # [cite: 35]
            [cite_start]solicitante="Setor Contábil", # [cite: 35]
            [cite_start]data_solicitacao=datetime.date(2025, 7, 1), # [cite: 35]
            [cite_start]analista_responsavel="Warlison Samuel", # [cite: 35]
            [cite_start]status="1" # [cite: 35]
        )
        session.add_all([req1, req2, req3])
        session.commit() # Commit para que os IDs sejam gerados e possam ser usados abaixo
        print("Dados de requisição inseridos.")

        # --- Dados para Tabela 'identificacao_problemas' ---
        # Usamos os objetos de requisição acima para manter a relação de FK
        print("Inserindo dados na tabela 'identificacao_problemas'...")
        prob1 = IdentificacaoProblemas(
            [cite_start]id_requisicao=req1.id_requisicao, # [cite: 37]
            [cite_start]titulo="Investigar falha no componente de autenticação mobile", # [cite: 37]
            [cite_start]descricao="A falha parece ocorrer durante a validação do token JWT em telas de baixa resolução.", # [cite: 37]
            [cite_start]tipo_manutencao="Corretiva", # [cite: 37]
            [cite_start]prioridade="Alta", # [cite: 37]
            [cite_start]data_identificacao=datetime.date(2025, 6, 21), # [cite: 37]
            [cite_start]identificado_por="Diego da Silva Raposo", # [cite: 37]
            [cite_start]status="2", # Status 'Aceito' e pronto para análise [cite: 37]
            [cite_start]versao_afetada="v2.3.1" # [cite: 37]
        )
        prob2 = IdentificacaoProblemas(
            [cite_start]id_requisicao=req2.id_requisicao, # [cite: 37]
            [cite_start]titulo="Definir escopo do novo relatório de vendas", # [cite: 37]
            [cite_start]descricao="Necessário detalhar as fontes de dados, os cálculos e o layout do relatório.", # [cite: 37]
            [cite_start]tipo_manutencao="Evolutiva", # [cite: 37]
            [cite_start]prioridade="Média", # [cite: 37]
            [cite_start]data_identificacao=datetime.date(2025, 6, 26), # [cite: 37]
            [cite_start]identificado_por="Douglas da Costa Cruz", # [cite: 37]
            [cite_start]status="2", # Status 'Aceito' e pronto para análise [cite: 37]
            [cite_start]versao_afetada="v2.3.1" # [cite: 37]
        )
        session.add_all([prob1, prob2])
        session.commit()
        print("Dados de problemas inseridos.")

        print("\n✅ Povoamento do banco de dados concluído com sucesso!")
        print(f"Problema ID {prob1.id_problema} e {prob2.id_problema} estão prontos para serem analisados pela sua API.")

    except Exception as e:
        print(f"❌ Ocorreu um erro: {e}")
        session.rollback()
    finally:
        session.close()

if __name__ == "__main__":
    popular_dados()