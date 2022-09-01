from django.shortcuts import render, redirect
from . models import Article

# Create your views here.
def index(request):
    articles = Article.objects.order_by('-pk') # - 는 내림차순 정렬
    
    context = {
        'articles':articles,
    }
    ret = render(request, 'articles/index.html', context)
    return ret

def new(request):
    return render(request, 'articles/new.html')

def create(request):
    print(request.POST)
    title = request.POST.get('title')
    content = request.POST.get('content')
    # make instance 
    article = Article(title=title, content=content)
    #db 반영
    article.save()

    #print(title, content)
    #print(type(title), type(content)) # 정수로 받아도 문자열이다. 문자열을 입력받는 양식이니까
    
    # return render(request, 'articles/create.html')
    # return render(request, 'articles/index.html') 

    # url을 creare 가 아닌 index로
    # redirect에서는 url 을 써줌 
    #return redirect('articles:index') # or '/articles/'

    # 글 작성하면 상세 페이지로 가기
    return redirect('articles:detail', article.pk) # or '/articles/'

# /articles/<int:pk>/
def detail(request, pk ):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)

def delete(request, pk):
    if request.method == 'POST':
        article = Article.objects.get(pk=pk)
        article.delete()

    return redirect('articles:index')

def edit(request, pk ):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/edit.html', context)


def update(request, pk):
    article = Article.objects.get(pk=pk)
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    article.save()
    return redirect('articles:detail', article.pk) # or '/articles/'
