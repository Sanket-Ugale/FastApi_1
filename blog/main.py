from typing import List
from fastapi import Depends, FastAPI, status, Response, HTTPException
from blog.database import SessionLocal, engine
from blog import models
from . import schemas
from sqlalchemy.orm import Session
from passlib.context import CryptContext 
app=FastAPI()

models.Base.metadata.create_all(engine)
def get_db():
    db=SessionLocal()
    try:
        yield db
    finally: 
        db.close()

@app.put('/blog/{id}',status_code=status.HTTP_202_ACCEPTED, tags=['Blogs'])
def update(id, request:schemas.Blog,db:Session=Depends(get_db)):
    blog=db.query(models.Blog).filter(models.Blog.id==id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Blog with the id {id} is not found.')
    blog.update({'title':request.title,'body':request.body})
    db.commit()
    return 'updated successfully.'

@app.post('/blog',status_code=status.HTTP_201_CREATED, tags=['Blogs'])
def create(request:schemas.Blog,db:Session=Depends(get_db)):
    new_blog=models.Blog(title=request.title, body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

@app.get('/blog', response_model=List[schemas.ShowBlog], tags=['Blogs'])
def all(db:Session=Depends(get_db)):
    blogs=db.query(models.Blog).all()
    return blogs


@app.get('/blog/{id}', status_code=200, response_model=schemas.ShowBlog, tags=['Blogs'])
def show(id, response:Response, db:Session=Depends(get_db)):
    blog=db.query(models.Blog).filter(models.Blog.id==id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog with the id {id} is not available.')
        # response.status_code=status.HTTP_404_NOT_FOUND
        # return{'detail':f'Blog with the id {id} is not available.'}
    return blog

@app.delete('/blog/{id}',status_code=status.HTTP_204_NO_CONTENT, tags=['Blogs'])
def destroy(id,db:Session=Depends(get_db)):
    blog=db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Blog with the id {id} is not found.')
    blog.delete(synchronize_session=False)
    db.commit()
    return 'Deleted Successfully.'
# {'response':'Blog deleted Successfully.'}


pwd_cxt= CryptContext( schemes=["bcrypt"],deprecated="auto")

@app.post('/user',status_code=status.HTTP_201_CREATED, tags=['Users'])
def create_user(request:schemas.User,db:Session=Depends(get_db)):
    hashedPassword=pwd_cxt.hash(request.password)
    new_user=models.User(name=request.name, email=request.email, password=hashedPassword)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@app.get('/user',response_model=List[schemas.ShowUser], tags=['Users'])
def all(db:Session=Depends(get_db)):
    return db.query(models.User).all()


@app.get('/user', response_model=List[schemas.ShowUser], tags=['Users'])
def all(db:Session=Depends(get_db)):
    users=db.query(models.User).all()
    return users


@app.get('/user/{id}', status_code=200, response_model=schemas.ShowUser, tags=['Users'])
def show(id, response:Response, db:Session=Depends(get_db)):
    user=db.query(models.User).filter(models.User.id==id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'User with the id {id} is not available.')
    return user

@app.delete('/user/{id}',status_code=status.HTTP_204_NO_CONTENT, tags=['Users'])
def destroy(id,db:Session=Depends(get_db)):
    user=db.query(models.User).filter(models.User.id == id)
    if not user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'User with the id {id} is not found.')
    user.delete(synchronize_session=False)
    db.commit()
    return 'Deleted Successfully.'