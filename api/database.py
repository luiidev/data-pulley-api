from sqlalchemy import create_engine, URL
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from os import environ

connection_url = URL.create(
    drivername=environ.get("DB_CONNECTION"),
    username=environ.get("DB_USERNAME"),
    password=environ.get("DB_PASSWORD"),
    host=environ.get("DB_HOST"),
    port=environ.get("DB_PORT"),
    database=environ.get("DB_DATABASE"),
)

engine = create_engine(connection_url, echo=True)
db_session = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=engine)
)
Base = declarative_base()
Base.query = db_session.query_property()

metadata = Base.metadata


def init_db():
    from api.models import user_model
    from api.models import analyst_model
    from api.models import customer_model
    from api.models import project_model
    from api.models import project_proposal_model
    from api.models import project_log_model
    from api.models import payment_method_model
    from api.models import payment_state_model

    Base.metadata.create_all(bind=engine)
