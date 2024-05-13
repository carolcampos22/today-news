from django.shortcuts import render
from base.forms import RegisterNews
from base.models import Register
import requests
from django.shortcuts import get_object_or_404

# Create your views here.
def home(request):
    return render(request, 'home.html')

def get_news_from_api():
    url = 'http://localhost:8000/api/news'
    
    try:
        response = requests.get(url)
        response.raise_for_status() 
        
        data = response.json()
        return data
    except requests.RequestException as e:
        print(f'Erro ao conectar à API: {e}')
        return None

def register(request):
    sucesso = False
    form = RegisterNews(request.POST or None)
    if form.is_valid():
        sucesso = True
        form.save()
    contexto = {
        'form': form,
        'sucesso': sucesso
    }
    return render(request, 'register.html', contexto)

def technology_news(request):
    news = get_news_from_api()
    return render(request, 'technology_news.html', {'news': news})
    
def education_news(request):
    news = get_news_from_api()
    return render(request, 'education_news.html', {'news': news})

def science_news(request):
    news = get_news_from_api()
    return render(request, 'science_news.html', {'news': news})

def movies_and_series_news(request):
    news = get_news_from_api()
    return render(request, 'movies_and_series_news.html', {'news': news})

def health_news(request):
    news = get_news_from_api()
    return render(request, 'health_news.html', {'news': news})

def entertainment_news(request):
    news = get_news_from_api()
    return render(request, 'entertainment_news.html', {'news': news})


def news_detail(request, news_id):
    news = get_object_or_404(Register, id=news_id)
    return render(request, 'news_detail.html', {'news': news})