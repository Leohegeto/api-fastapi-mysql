from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

DATABASE_URL = "mysql+mysqlconnector://usuario:senha@localhost/nome_do_banco"

# Criar conexão com o banco
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Criar a aplicação FastAPI
app = FastAPI()

# Definir o modelo da tabela users
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)

# Criar as tabelas no banco de dados
Base.metadata.create_all(bind=engine)

# Dependência para obter a sessão do banco
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Rota inicial
@app.get("/")
def read_root():
    return {"message": "API de Gestão de Usuários funcionando!"}

# Rota para adicionar um usuário
@app.post("/users/")
def create_user(username: str, email: str, password_hash: str, db: Session = Depends(get_db)):
    user = User(username=username, email=email, password_hash=password_hash)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

# Rota para listar todos os usuários
@app.get("/users/")
def list_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return users