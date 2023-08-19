from sqlalchemy.orm import Session
import schemas
import models

def create_blog(db: Session, blog: schemas.Blog):
    newBlog = models.Blog(title=blog.title, body=blog.body)
    db.add(newBlog)
    db.commit()
    db.refresh(newBlog)
    return newBlog

def get_blog(db: Session, id: int):
    return db.query(models.Blog).filter(models.Blog.id == id).first()

def get_blogs(db: Session):
    return db.query(models.Blog).all()

def update_blog(db: Session, id: int, blogUpdate: schemas.Blog):
    db.query(models.Blog).filter(models.Blog.id == id).update({'title': blogUpdate.title, 'body': blogUpdate.body}, synchronize_session=False)
    db.commit()
    return "Updated success"


def delete_blog(db: Session, id: int):
    db.query(models.Blog).filter(models.Blog.id == id).delete(synchronize_session=False)
    db.commit()
    return {'done'}
