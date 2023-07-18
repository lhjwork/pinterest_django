from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Profile(models.Model):
    #연결 된 user 객체가 없어질때 정책행동을 담당함 -> CASCADE 함
    # related_name 은 request.user.profile 형식으로 가져 올 수 있게 한다?
    # 더 나아가서 nickname 변수 생성시 request.user.profile.nickname으로 가져올 수 있다.
    user = models.OneToOneField(User,on_delete=models.CASCADE, related_name='profile')

    #이전에 settings.py에서 STATIC_ROOT ->  /meida/profile형식으로 업로드 될 것임
    #null = True 프로필 사진 꼭 없어도 됨
    image = models.ImageField(upload_to='profile/', null=True)
    nickname = models.CharField(max_length=20, unique=True, null=True)
    message = models.CharField(max_length=100, null=True)
    