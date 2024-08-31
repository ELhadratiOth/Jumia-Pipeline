from sqlalchemy import create_engine, Column, Float, Text, Integer
from sqlalchemy.orm import sessionmaker , declarative_base
import pandas as pd
from configparser import ConfigParser

config = ConfigParser()
config.read('config.ini')
searched_product = config['SEARCH_TARGET']['serched_product']

df = pd.read_csv(f"{searched_product}.csv")

URL_DATABASE = f"postgresql+psycopg2://{config['POSTGRESQL_CONFIG']['username']}:{config['POSTGRESQL_CONFIG']['password']}@localhost:5432/{config['POSTGRESQL_CONFIG']['database_name']}"
engine = create_engine(URL_DATABASE)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class Products(Base):
    __tablename__ = config['POSTGRESQL_CONFIG']['tablename']
    id = Column(Integer, primary_key=True, index=True)
    product_name = Column(Text)
    product_price = Column(Float)
    product_link = Column(Text)
    
    
try :
          Base.metadata.create_all(bind=engine)
          df.to_sql(config['POSTGRESQL_CONFIG']['tablename'], engine, if_exists='append', index=False)
          print("All records have been successfully loaded")
except Exception as e :
          print(f"An error occurred : {str(e)}")
finally :
          session = SessionLocal()
          session.close()
