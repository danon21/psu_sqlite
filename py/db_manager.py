from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from py.src.models import Client, Personnel, Order 

class DatabaseManager:
    def __init__(self, db_file):
        self.engine = create_engine(f'sqlite:///{db_file}')
        self.Session = sessionmaker(bind=self.engine)

    def get_orders_by_date_range(self, start_date, end_date):
        session = self.Session()
        try:
            orders = session.query(Order).filter(Order.o_date.between(start_date, end_date)).all()
            return orders
        finally:
            session.close()

    def get_orders_by_personnel(self, p_code):
        session = self.Session()
        try:
            orders = session.query(Order).filter_by(o_p_code=p_code).all()
            return orders
        finally:
            session.close()

    def get_all_personnel(self):
        session = self.Session()
        try:
            personnel = session.query(Personnel).all()
            return personnel
        finally:
            session.close()

    def get_personnel_by_code(self, p_code):
        session = self.Session()
        try:
            personnel = session.query(Personnel).filter_by(p_code=p_code).first()
            return personnel
        finally:
            session.close()

    def get_client_by_code(self, c_code):
        session = self.Session()
        try:
            client = session.query(Client).filter_by(p_code=c_code).first()
            return client
        finally:
            session.close()

    def get_personnel_dict(self):
        session = self.Session()
        try:
            personnel_records = session.query(Personnel).all()
            personnel_dict = {record.p_code: record.p_full_name for record in personnel_records}
            return personnel_dict
        finally:
            session.close()

    def get_client_dict(self):
        session = self.Session()
        try:
            client_records = session.query(Client).all()
            client_dict = {record.c_code: record.c_full_name for record in client_records}
            return client_dict
        finally:
            session.close()