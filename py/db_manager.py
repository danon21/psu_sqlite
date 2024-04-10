from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from py.src.models import Client, Personnel, Order, Brand, Color, Detail, WorkType

class DatabaseManager:
    def __init__(self, db_file=None):
        if db_file:
            self.db_file = db_file
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
            row = session.query(Client).filter_by(c_code=c_code).first()
            return row
        finally:
            session.close()
    
    def get_order_by_code(self, o_code):
        session = self.Session()
        try:
            row = session.query(Order).filter_by(o_code=o_code).first()
            return row
        finally:
            session.close()
    
    def get_brand_by_code(self, b_code):
        session = self.Session()
        try:
            brand = session.query(Brand).filter_by(b_code=b_code).first()
            return brand
        finally:
            session.close()
    
    def get_color_by_code(self, c_code):
        session = self.Session()
        try:
            row = session.query(Color).filter_by(c_code=c_code).first()
            return row
        finally:
            session.close()
    
    def get_detail_by_code(self, d_code):
        session = self.Session()
        try:
            row = session.query(Detail).filter_by(d_code=d_code).first()
            return row
        finally:
            session.close()
    
    def get_work_type_by_code(self, w_code):
        session = self.Session()
        try:
            row = session.query(WorkType).filter_by(w_code=w_code).first()
            return row
        finally:
            session.close()
    

    def get_client_dict(self):
        session = self.Session()
        try:
            clients = session.query(Client).all()
            client_dict = {client.c_code: client.c_full_name for client in clients}
            return client_dict
        finally:
            session.close()
    
    def get_personnals_dict(self):
        session = self.Session()
        try:
            personnels = session.query(Personnel).all()
            personnel_dict = {personnel.p_code: personnel.p_full_name for personnel in personnels}
            return personnel_dict
        finally:
            session.close()
    
    def get_order_dict(self):
        session = self.Session()
        try:
            orders = session.query(Order).all()
            order_dict = {order.o_code: str(order.o_code) for order in orders}
            return order_dict
        finally:
            session.close()
    
    def get_brand_dict(self):
        session = self.Session()
        try:
            brands = session.query(Brand).all()
            brand_dict = {brand.m_code: brand.m_name for brand in brands}
            return brand_dict
        finally:
            session.close()
    
    def get_color_dict(self):
        session = self.Session()
        try:
            colors = session.query(Color).all()
            color_dict = {color.c_code: color.c_name for color in colors}
            return color_dict
        finally:
            session.close()
    
    def get_detail_dict(self):
        session = self.Session()
        try:
            details = session.query(Detail).all()
            detail_dict = {detail.d_code: detail.d_name for detail in details}
            return detail_dict
        finally:
            session.close()
    
    def get_work_type_dict(self):
        session = self.Session()
        try:
            work_types = session.query(WorkType).all()
            work_type_dict = {work_type.w_code: work_type.w_name for work_type in work_types}
            return work_type_dict
        finally:
            session.close()
    

    def delete_by_model(self, model):
        session = self.Session()
        try:
            if model:
                session.delete(model)
                session.commit()
                res = True
        except Exception:
            res = False
        finally:
            session.close()
            return res
    
    def create_by_model(self, model):
        session = self.Session()
        try:
            if model:
                session.add(model)
                session.commit()
                res = True
        except Exception:
            res = False
        finally:
            session.close()
            return res

    def save_changes(self):
        session = self.Session()
        try:
            session.commit()
            res = True
        except Exception:
            res = False
        finally:
            session.close()
            return res

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