from django.db import models
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin



class UserManager(BaseUserManager):
    
    def create_user(self, email, nickname, password=None):
        if not email:
            raise ValueError('must have user email')
        
        user = self.model(
            email=self.normalize_email(email),
            nickname = nickname,
        )
        user.set_password(password) 
        user.save(using=self._db)
        return user

    def create_superuser(self, email = None, nickname=None, password=None):
        superuser = self.create_user(
            email=email,
            password=password,
            nickname=nickname
        )

        superuser.is_admin = True
        superuser.is_staff = True
        superuser.is_superuser = True
        superuser.is_active = True
        superuser.save(using=self._db)

        return superuser


class User(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True)  # pk

    email = models.EmailField(default='', max_length=100, null=False, unique=True)
    nickname = models.CharField(max_length=10, null=False, unique=True)

    cover_image_url=models.CharField(max_length=500, null= False)
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    updated_at = models.DateTimeField(auto_now=True, null=False)
    is_deleted = models.BooleanField(default=False, null=False)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    #이메일로 로그인
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    
    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin

    def __str__(self):
        return self.id

class Diary(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    title = models.CharField(max_length=50, null=False)
    weather = models.IntegerField
    drawing_url = models.CharField(max_length=500, null=False)
    contents = models.CharField(max_length=50, null=False)
    diary_date = models.DateField(null=False)
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    updated_at = models.DateTimeField(auto_now=True, null=False)
    is_deleted = models.BooleanField(null=False)

    def __str__(self):
        return self.id

class Keyword(models.Model):
    id = models.AutoField(primary_key=True)
    keyword = models.CharField(max_length=10, null=False)
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    updated_at = models.DateTimeField(auto_now=True, null=False)
    is_deleted = models.BooleanField(null=False)

    def __str__(self):
        return self.keyword

class Drawing(models.Model):
    id = models.AutoField(primary_key=True)
    Keyword = models.ForeignKey(Keyword, on_delete=models.CASCADE, null=False)
    image_url = models.CharField(max_length=500, null=False)
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    updated_at = models.DateTimeField(auto_now=True, null=False)
    is_deleted = models.BooleanField(null=False)

    def __str__(self):
        return self.id