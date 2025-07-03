from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app import models, schemas
from app.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependência do banco
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# CRUD
@app.post("/analise", response_model=schemas.AnaliseOut)
def criar_analise(analise: schemas.AnaliseCreate, db: Session = Depends(get_db)):
    db_analise = models.Analise(**analise.dict())
    db.add(db_analise)
    db.commit()
    db.refresh(db_analise)
    return db_analise

@app.get("/analise", response_model=List[schemas.AnaliseOut])
def listar_analises(db: Session = Depends(get_db)):
    return db.query(models.Analise).all()

@app.get("/analise/{id_analise}", response_model=schemas.AnaliseOut)
def obter_analise(id_analise: int, db: Session = Depends(get_db)):
    analise = db.query(models.Analise).filter(models.Analise.id_analise == id_analise).first()
    if not analise:
        raise HTTPException(status_code=404, detail="Análise não encontrada")
    return analise

@app.put("/analise/{id_analise}", response_model=schemas.AnaliseOut)
def atualizar_analise(id_analise: int, dados: schemas.AnaliseUpdate, db: Session = Depends(get_db)):
    analise = db.query(models.Analise).filter(models.Analise.id_analise == id_analise).first()
    if not analise:
        raise HTTPException(status_code=404, detail="Análise não encontrada")
    for key, value in dados.dict().items():
        setattr(analise, key, value)
    db.commit()
    db.refresh(analise)
    return analise

@app.delete("/analise/{id_analise}")
def deletar_analise(id_analise: int, db: Session = Depends(get_db)):
    analise = db.query(models.Analise).filter(models.Analise.id_analise == id_analise).first()
    if not analise:
        raise HTTPException(status_code=404, detail="Análise não encontrada")
    db.delete(analise)
    db.commit()
    return {"message": "Análise deletada com sucesso"}
