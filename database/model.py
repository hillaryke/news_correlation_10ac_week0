from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class NewsData(Base):
    __tablename__ = 'news_data'

    source_id = Column(String, primary_key=True)
    title = Column(String)
    published_at = Column(DateTime)
    content = Column(String)
    category = Column(String)
    source_name = Column(String)
    topic = Column(Integer)
    tags = Column(String)
    cluster = Column(Integer)
    event = Column(String)