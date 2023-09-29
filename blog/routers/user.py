from fastapi import APIRouter, HTTPException, status, Depends, Response
from typing import List
from .. import database, schemas, models
from sqlalchemy.orm import Session
from passlib.context import CryptContext 
router=APIRouter(
    prefix="/user",
    tags=['Users']
)
get_db=database.get_db
pwd_cxt= CryptContext( schemes=["bcrypt"],deprecated="auto")

@router.post('/',status_code=status.HTTP_201_CREATED)
def create_user(request:schemas.User,db:Session=Depends(get_db)):
    hashedPassword=pwd_cxt.hash(request.password)
    new_user=models.User(name=request.name, email=request.email, password=hashedPassword)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.get('/',response_model=List[schemas.ShowUser])
def all(db:Session=Depends(get_db)):
    return db.query(models.User).all()


@router.get('/', response_model=List[schemas.ShowUser])
def all(db:Session=Depends(get_db)):
    users=db.query(models.User).all()
    return users


@router.get('/{id}', status_code=200, response_model=schemas.ShowUser)
def show(id, response:Response, db:Session=Depends(get_db)):
    user=db.query(models.User).filter(models.User.id==id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'User with the id {id} is not available.')
    return user

@router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT)
def destroy(id,db:Session=Depends(get_db)):
    user=db.query(models.User).filter(models.User.id == id)
    if not user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'User with the id {id} is not found.')
    user.delete(synchronize_session=False)
    db.commit()
    return 'Deleted Successfully.'