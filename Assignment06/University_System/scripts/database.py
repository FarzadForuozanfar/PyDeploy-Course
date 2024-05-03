from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLALCHEMY_DATABASE_URL = "postgresql://root:DB1234@localhost:5432/database_university" 
# SQLALCHEMY_DATABASE_URL = "postgresql://root:veO80ulzrg30IWsMarRxnPVX@farzad-py-deployment-db:5432/postgres" 
SQLALCHEMY_DATABASE_URL = "postgres://root:atuOw9iNHdEy5BcbBWZ74RmZLPfbW2fM@dpg-coqh9kdjm4es73an38kg-a/unidb_ymes" 


engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()