from sqlalchemy import Column, Integer, String, Date, ForeignKey, Float, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class Blog(Base):
	__tablename__ = 'blog'
	blog_id = Column(Integer, primary_key = True)
	title = Column(String)
	image = Column(String)
	details = Column(String)