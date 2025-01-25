from sqlmodel import SQLModel, create_engine, Session
from app.env import SETTINGS

engine = create_engine(SETTINGS.sqlmodel_url, echo=True)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session
