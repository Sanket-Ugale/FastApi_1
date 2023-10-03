from fastapi import APIRouter, status, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm
from .. import schemas, database, models, token
from sqlalchemy.orm import Session
from passlib.context import CryptContext 

router=APIRouter(
    tags=['Authentication']
)

pwd_cxt= CryptContext( schemes=["bcrypt"],deprecated="auto")
@router.post('/login')
def login(request:OAuth2PasswordRequestForm=Depends(), db:Session=Depends(database.get_db)):
    user=db.query(models.User).filter(models.User.email==request.username).first()
    if not user:
         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='Invalid Credentials')
    if not pwd_cxt.verify(request.password,user.password):
         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='Invalid Username or Password.')
    access_token=token.create_access_token(data={"sub":user.email})
    return {"access_token":access_token, "token_type":"bearer"}