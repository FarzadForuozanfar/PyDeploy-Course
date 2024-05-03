from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLALCHEMY_DATABASE_URL = "postgresql://root:DB1234@localhost:5432/database_university" 
# SQLALCHEMY_DATABASE_URL = "postgresql://root:muiBJrnwBJW36ZHPA8Gdi8bK@farzad-py-deployment-db:5432/postgres" 
SQLALCHEMY_DATABASE_URL = "postgres://root:sywdtZIlCI3Q8QswjrZHCtjL0vz57jse@dpg-coqhmmtjm4es73anb4pg-a.oregon-postgres.render.com/unidb_s5zr" 


engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()