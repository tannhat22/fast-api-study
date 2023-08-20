from typing import List
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from .. import schemas, database, oauth2
from ..repository import blog
# import oauth2

router = APIRouter(
    prefix="/blog",
    tags=['Blogs']
)

get_db = database.get_db

# Tạo 1 blog mới
@router.post('', status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.create_blog(db, request)

# Lấy toàn bộ dữ liệu blog
@router.get('', response_model=List[schemas.ShowBlog])
def read(db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.get_blogs(db)

# Lấy dữ liệu 1 blog
@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowBlog)
def read(id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.get_blog(db, id)

# Chỉnh sửa blog
@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id: int, request: schemas.Blog, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.update_blog(db,id,request)

# Xóa blog
@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.delete_blog(db, id)