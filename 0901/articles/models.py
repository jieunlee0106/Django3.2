from django.db import models

# Create your models here.
class Article(models.Model): # 테이블 이름은 appname_classname
    # 필드정의 ==> 이름 = 필드타입
    # primary-key ==> id라는 필드가 자동으로 생성(따로 설정하지 않으면)/unique 한 값
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


def __str__(self):
    return f'{self.title}-{self.content}'