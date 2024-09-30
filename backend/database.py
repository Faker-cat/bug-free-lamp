from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy import asc
import models

# 接続先DBの設定
DATABASE = 'postgresql+psycopg://user:postgres@db:5432/postgres'

# Engine の作成
Engine = create_engine(
  DATABASE,
  echo=True
)

# Sessionの作成
session = Session(
  autoflush = True,
  bind = Engine
)

def read_users():
    return session.query(models.User).order_by(asc(models.User.id)).all() #SELECT*FROM USERS と意味は同じ。id順に表示

def create_user(id,name,role,color):
    db_user = models.User(id,name,role,color) #コンストラクタを呼び出す
    session.add(db_user) #追加
    session.commit()
