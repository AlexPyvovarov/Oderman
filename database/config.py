from sqlmodel import create_engine, SQLModel, Session

engine = create_engine("sqlite:///database.sql")
session = Session(bind=engine)

def restart_db():
    SQLModel.metadata.drop_all(bind=engine)
    SQLModel.metadata.create_all(bind=engine)