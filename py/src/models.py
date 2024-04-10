from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Client(Base):
    __tablename__ = 'clients'
    c_code = Column(Integer, primary_key=True)
    c_full_name = Column(String)
    c_telephone = Column(String)
    c_address = Column(String)
    orders = relationship("Order", back_populates="client")

class Personnel(Base):
    __tablename__ = 'personnels'
    p_code = Column(Integer, primary_key=True)
    p_full_name = Column(String)
    p_address = Column(String)
    p_telephone = Column(String)
    p_job_title = Column(String)
    orders = relationship("Order", back_populates="personnel")

class Order(Base):
    __tablename__ = 'orders'
    o_code = Column(Integer, primary_key=True)
    o_p_code = Column(Integer, ForeignKey('personnels.p_code'))
    o_date = Column(Integer)
    o_car_brand = Column(String)
    o_detail = Column(String)
    o_type_work = Column(String)
    o_color = Column(String)
    o_price = Column(Integer)
    o_c_code = Column(Integer, ForeignKey('clients.c_code'))
    o_state = Column(Integer)
    client = relationship("Client", back_populates="orders")
    personnel = relationship("Personnel", back_populates="orders")