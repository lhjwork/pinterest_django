from django.contrib.auth.models import User
from django.db import models

from projectapp.models import Project


# Create your models here.
class Article(models.Model):
    # set_null article이 회원 탈퇴했을떄 article이 사라지지 않고 알수 없는 게시글로 남도록하기 위해서
    # related_name='article' -> user 객체에서 article에 접근할떄 쓰는 네임이어서 더 직관적이므로
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='article', null=True)
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, related_name='article', null=True)

    title = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='article/', null=False)
    content = models.TextField(null=True)

    create_at = models.DateField(auto_created=True, null=True)
