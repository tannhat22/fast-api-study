from fastapi import FastAPI, Depends, status, HTTPException
from sqlalchemy.orm import Session
from schemas import Blog
import CRUD
import models
from database import engine, SessionLocal


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post('/blog', status_code=status.HTTP_201_CREATED)
def create(request: Blog, db: Session = Depends(get_db)):
    return CRUD.create_blog(db, request)

@app.get('/blog')
def all(db: Session = Depends(get_db)):
    return CRUD.get_blogs(db)

@app.get('/blog/{id}', status_code=status.HTTP_200_OK)
def all(id: int, db: Session = Depends(get_db)):
    blog = CRUD.get_blog(db, id)
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with the id {id} is not found")
    return blog

@app.put('/blog/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id: int, request: Blog, db: Session = Depends(get_db)):
    print(type(request))
    return CRUD.update_blog(db,id,request)

@app.delete('/blog/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id: int, db: Session = Depends(get_db)):
    return CRUD.delete_blog(db, id)