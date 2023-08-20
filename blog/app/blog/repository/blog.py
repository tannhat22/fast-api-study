from sqlalchemy.orm import Session
from fastapi import Depends, status, HTTPException

from .. import schemas, models


# BLOGS:
def create_blog(db: Session, blog: schemas.Blog):
    newBlog = models.Blog(title=blog.title, body=blog.body, user_id=1)
    db.add(newBlog)
    db.commit()
    db.refresh(newBlog)
    return newBlog

def get_blog(db: Session, id: int):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with the id {id} not found")
    return blog

def get_blogs(db: Session):
    return db.query(models.Blog).all()

def update_blog(db: Session, id: int, blogUpdate: schemas.Blog):
    blog = db.query(models.Blog).filter(models.Blog.id == id) 
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with the id {id} not found")
    blog.update(blogUpdate.model_dump(), synchronize_session=False)
    db.commit()
    return "Updated success"

def delete_blog(db: Session, id: int):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with the id {id} not found")
    blog.delete(synchronize_session=False)
    db.commit()
    return {'done'}