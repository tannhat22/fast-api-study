from sqlalchemy.orm import Session

from hashing import Hash
import schemas
import models

# BLOGS:
def create_blog(db: Session, blog: schemas.Blog):
    newBlog = models.Blog(title=blog.title, body=blog.body, user_id=1)
    db.add(newBlog)
    db.commit()
    db.refresh(newBlog)
    return newBlog

def get_blog(db: Session, id: int):
    return db.query(models.Blog).filter(models.Blog.id == id).first()

def get_blogs(db: Session):
    return db.query(models.Blog).all()

def update_blog(db: Session, id: int, blogUpdate: schemas.Blog):
    blog = db.query(models.Blog).filter(models.Blog.id == id) 
    if not blog.first():
        return False
    blog.update(blogUpdate.model_dump(), synchronize_session=False)
    db.commit()
    return "Updated success"


def delete_blog(db: Session, id: int):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        return False
    blog.delete(synchronize_session=False)
    db.commit()
    return {'done'}

# USERS:
def create_user(db: Session, user: schemas.User):
    newUser = models.User(name=user.name, email=user.email, password=Hash.bcrypt(user.password))
    db.add(newUser)
    db.commit()
    db.refresh(newUser)
    return newUser

def get_user(db: Session, id: int):
    return db.query(models.User).filter(models.User.id == id).first()
