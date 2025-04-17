from sqlalchemy import Boolean, Column, Integer, String, Date

from db import Model


class Customer(Model):
    __tablename__ = 'customer'

    customer_id = Column(Integer, primary_key=True)
    first_name = Column(String)
    create_date = Column(Date)
    activebool = Column(Boolean)
