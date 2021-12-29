from model import Base, Blog
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///blog.db?check_same_thread=False')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_blog(title, image, details):
	blog_object = Blog(
	title = title,
	image = image,
	details = details)
	session.add(blog_object)
	session.commit()

def return_all_blogs():
	blogs = session.query(Blog).all()
	return blogs

def return_blog(id):
	blog = session.query(Blog).filter_by(blog_id = id).first()
	return blog

def edit_blog(id, title, image,details):
	blog_object = session.query(Blog).filter_by(blog_id = id).first()
	blog_object.title = title
	blog_object.image = image
	blog_object.details = details
	session.commit()
	return

def delete_blog1(blog_id):
	session.query(Blog).filter_by(blog_id=blog_id).delete()
	session.commit()
