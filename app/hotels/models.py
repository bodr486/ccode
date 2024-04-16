from core.database import Base
from sqlalchemy import JSON,Integer,String,Column


class Hotels(Base):
    __tablename__= "hotels"

    id = Column(Integer, primary_key= True)
    location = Column(String, nullable= False)
    name = Column(String, nullable= False)
    image_id = Column(Integer)