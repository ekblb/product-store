from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

from configuration import DB_CONNECTION

Model = declarative_base(name='Model')

engine = create_engine(
    DB_CONNECTION
)

Session = sessionmaker(engine, autoflush=False, expire_on_commit=False)

session = Session()
