from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

class User(Base):
    """
    ユーザモデル
    """

    __tablename__ = 'pbl_users'

    id = Column('id', Integer, primary_key=True)
    name = Column('name', String(10))
    role = Column('role', String(10))
    color = Column('color', String(10))

    def __init__(self,id,name,role,color):#コンストラクタを明示的に
        self.id = id
        self.name = name
        self.role = role
        self.color = color

    
