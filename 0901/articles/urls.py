
from django.urls import path
from . import views

#name은 herf 할 때 url 로 하려고

app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
    # 게시글 생성 양식/ srticles/new 
    path('new/', views.new, name='new'),
    # 게시글 db에 반영
    path('create/', views.create, name='create'),

    # 게시글 상세 조회 /articles/글번호(pk)/, /articles/2/
    # path converter <변환 할 데이터 타입:이름>
    path('<int:pk>/', views.detail, name='detail'),

    # 게시글 삭제 /article/글번호(pk)/delete
    path('<int:pk>/delete/', views.delete, name='delete'),

    # 게시글 수정 / articles/글번호(pk)/edit
    path('<int:pk>/edit/', views.edit, name='edit'),

    # 게시글 수정 업데이트 / articles/글번호/update
    path('<int:pk>/update/', views.update, name='update'),
]

