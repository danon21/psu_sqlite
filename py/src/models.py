from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Brand(Base):
    __tablename__ = 'brand'
    m_code = Column(Integer, primary_key=True)
    m_name = Column(String)

class Color(Base):
    __tablename__ = 'color'
    c_code = Column(Integer, primary_key=True)
    c_name = Column(String)

class Detail(Base):
    __tablename__ = 'detail'
    d_code = Column(Integer, primary_key=True)
    d_name = Column(String)

class WorkType(Base):
    __tablename__ = 'work_type'
    w_code = Column(Integer, primary_key=True)
    w_name = Column(String)

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
    o_car_brand = Column(Integer, ForeignKey('brand.m_code'))
    o_detail = Column(Integer, ForeignKey('detail.d_code'))
    o_type_work = Column(Integer, ForeignKey('work_type.w_code'))
    o_color = Column(Integer, ForeignKey('color.c_code'))
    o_price = Column(Integer)
    o_c_code = Column(Integer, ForeignKey('clients.c_code'))
    o_state = Column(Integer)
    client = relationship("Client", back_populates="orders")
    personnel = relationship("Personnel", back_populates="orders")
    brand = relationship("Brand")
    detail = relationship("Detail")
    work_type = relationship("WorkType")
    color = relationship("Color")
