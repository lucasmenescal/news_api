from django.shortcuts import render
import requests
# Create your views here.


def get(request):
    # Endereço da News API
    url = ('https://newsapi.org/v2/everything?q=Apple&sortBy=popularity&apiKey=c9bf327003514a86b7bc71586573ecf6')
    response = requests.get(url)
    news = response.json()
    articles = news['articles']
    descricao = []
    titulo = []
    imagem = []

    for i in range(len(articles)):
        article = articles[i]
        titulo.append(article['title'])
        descricao.append(article['description'])
        imagem.append(article['urlToImage'])
    
    myList = zip(titulo, descricao, imagem)
    context = {'myList':myList}

    return render(request, 'index.html', context)