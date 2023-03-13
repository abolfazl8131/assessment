from django.db import transaction 
from .models import BaseUser, Profile


def create_profile(*, user:BaseUser, bio:str | None) -> Profile:
    return Profile.objects.create(user=user, bio=bio)

def create_user(*, email:str, password:str , ID , first_name , last_name) -> BaseUser:
    return BaseUser.objects.create_user(email=email,
        password=password , 
        ID=ID , 
        first_name=first_name , 
        last_name=last_name)

def create_superuser(* ,email:str, password:str , first_name , last_name,  ID ) -> BaseUser:
        return BaseUser.objects.create_superuser(email=email,
            password=password , 
            ID=ID , 
            first_name=first_name , 
            last_name=last_name)

def update_profile(*, user:BaseUser, bio:str | None) -> Profile :
    Profile.objects.filter(user=user).update(bio=bio)
    return Profile.objects.get(user=user)

def update_user(*, email:str,  ID , first_name , last_name) -> BaseUser:
        BaseUser.objects.filter(ID=ID).update(email = email , 
            first_name=first_name , 
            last_name=last_name)
        
        return BaseUser.objects.get(ID=ID)
            
        
@transaction.atomic
def register(*, bio:str|None, ID:int , first_name:str,last_name:str,email:str, password:str) -> BaseUser:

    user = create_user(email=email, 
        password=password,
        first_name=first_name , 
        last_name = last_name,
        ID = ID
        )
    create_profile(user=user, bio=bio)

    return user

@transaction.atomic
def register_superuser(*,  email:str,ID:int , first_name:str,last_name:str, password:str,bio:str|None) -> BaseUser:

    user = create_superuser(email=email, 
        password=password,
        first_name=first_name , 
        last_name = last_name,
        ID = ID
        )
    create_profile(user=user, bio=bio)

    return user

@transaction.atomic
def update(* , bio:str|None, ID:int , first_name:str,last_name:str,email:str) -> BaseUser:
    user = update_user(
        email = email,
        ID = ID,
        first_name=first_name,
        last_name=last_name
    )
    update_profile(user=user , bio=bio)
    return user