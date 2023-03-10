from django.db import models
from django.contrib.auth import models as auth_models

class UserManager(auth_models.BaseUserManager):
    
    def create_user(self, profile_name: str, email: str, cpf: str, cellphone_number: str, password :str = None, is_staff=False, 
                    is_superuser=False,  ) -> "User":
        
        if not cpf:
            raise ValueError("CPF é um campo obrigatório")
        if not profile_name:
            raise ValueError("Nome do usuário é um campo obrigatório")
        if not email:
            raise ValueError("E-mail é um campo obrigatório")
        if not cellphone_number:
            raise ValueError("Número de celular é um campo obrigatório")
        
        user = self.model(email=self.normalize_email(email))
        user.profile_name = profile_name
        user.set_password(password)
        user.cpf = cpf,
        user.cellphone_number = cellphone_number,
        user.is_active = True
        user.is_staff = is_staff
        user.is_superuser = is_superuser
        user.save()
        
        return user
    
    def create_superuser(self, profile_name: str, cpf: str, email: str, cellphone_number: str, password :str = None, is_staff=False, 
                    is_superuser=False ) -> "User":
        
        user = self.create_user(
            profile_name = profile_name,
            email= email,
            cpf = cpf,
            password= password,
            cellphone_number= cellphone_number,
            is_staff= True,
            is_superuser= True,
        )
        
        return user
        
        

class User(auth_models.AbstractUser):
    profile_name = models.CharField(max_length=255, null=True, blank=False)
    cpf = models.CharField(max_length=11, null=True, blank=False, unique=True)
    email = models.EmailField(max_length=50, blank=False, null=True, unique=True)
    password = models.CharField(max_length=255, blank=False, null=True)
    username = None
    
    cellphone_number = models.CharField(max_length=14, blank=False, null=True)
    insta_profile = models.CharField(max_length=50, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    
    objects = UserManager()
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["profile_name", "cpf", "password", "cellphone_number"]
    
    def __str__(self):
        return self.email
    