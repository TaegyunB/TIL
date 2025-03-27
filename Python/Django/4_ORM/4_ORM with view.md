## 전체 게시글 조회
### 2가지 Read(조회)
1. 전체 게시글 조회
2. 단일 게시글 조회

#### 1. 전체 게시글 조회
~~~python
# crud/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', include('articles.urls')),
]
~~~

~~~python
# articles/urls.py

from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
]
~~~

~~~python
# articles/views.py

from django.shortcuts import render
from .models import Article

# Create your views here.
# 전체 게시글 조회 후 응답하는 함수
def index(request):
    # 1. DB에 전체 게시글 요청
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }

    return render(request, 'articles/index.html', context)
~~~

~~~html
<!-- articles/templates/articles.index.html -->
<body>
    <h1>Articles</h1>
    <hr>
    {% for article in articles %}
        <p>글 번호: {{ article.pk }}</p>
        <p>글 제목: {{ article.title }}</p>
        <p>글 내용: {{ article.content }}</p>
    <hr>
    {% endfor %}
</body>
~~~