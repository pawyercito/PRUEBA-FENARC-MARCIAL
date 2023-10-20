from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
class ElementsToProcess(Base):
    __tablename__ = 'ElementsToProcess'

    id = Column(Integer, primary_key=True)
    idBulk = Column(Integer, nullable=False)
    retries = Column(Integer, default=0)
    status = Column(Integer, nullable=False)
    name = Column(String(100), nullable=False)

    def __init__(self, idBulk, status, name):
        self.idBulk = idBulk
        self.status = status
        self.name = name

        
