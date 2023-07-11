from django.shortcuts import render
import time
import requests
from bs4 import BeautifulSoup
from news.models import New

# Create your views here.

from rest_framework.views import APIView, Response, Request, status
from .models import New
from django.forms.models import model_to_dict
from news.apps import AppConfig
from rest_framework.pagination import PageNumberPagination
from django.shortcuts import get_object_or_404


# Create your views here.
    

class NewView(APIView, PageNumberPagination):

    def get(self, request: Request) -> Request:
        news_list = []
        news = New.objects.all()
        titulo = request.GET.get('title')

        if titulo:
            news= news.filter(title__icontains=titulo)
        for new in news:
            news_list.append(model_to_dict(new))

        reverse = list(reversed(news_list))
        result_page = self.paginate_queryset(reverse, request)
        

        return self.get_paginated_response(result_page)
        


    def post(self, request: Request) -> Request:
        ...

        # return Response(team_dict, status.HTTP_201_CREATED)


class NewDetailView(APIView):
    def get(self, request: Request, news_id: int) -> Response:
        new = get_object_or_404(New, id = news_id)
        new_response = model_to_dict(new)
        
        return Response(new_response, status.HTTP_200_OK)


    def delete(self, request: Request, news_id: int) -> Response:
       ...

        # return Response(status=status.HTTP_204_NO_CONTENT)

    def patch(self, request: Request, news_id: int) -> Response:
       ...


        # return Response(team_dict, status.HTTP_200_OK)

class NewStartScrappyView(APIView):
    def get(self, request: Request) -> Request:
            print('Execultando get')
            
            news_list = []
       
            url = 'https://www.bing.com/news/search?q=Carbon+Credits&qpvt=carbon+credits+news&FORM=EWRE'
            response = requests.get(url)

            soup = BeautifulSoup(response.content, 'html.parser')
            articles = soup.find_all(class_='news-card')
            

               
            
            for article in articles:
                new_content = {}

                src_value = ""
                img = article.find(class_= "right")
                if img is not None:
                    imgLink = img.find("a")
                    if imgLink is not None:
                        imgA = imgLink.find("img")
                        if imgA and 'data-src-hq' in imgA.attrs:
                            src_value = imgA['data-src-hq']
                            print(src_value)
                        else:
                            print("A tag da imagem não possui o atributo 'src'.")
                
              

                title = article.find(class_="title")
                link = title['href']
                titleText = title.text
                if New.objects.filter(title = titleText).exists():
                    continue
                source = article.find(class_="source") 
                text = article.find(class_="snippet").text


             

                if source is not None:
                    company = source.find('a')
                    if company is not None:
                        companyName = company.get_text()
         
                
   
                # pretty_text = text.prettify().strip().replace("\n", "").replace("\t", "")
                
                new_content['title'] = titleText
                new_content['thumb'] = "https://th.bing.com" + src_value
                new_content['link'] = link
                new_content['company'] = companyName
                new_content['text'] = text

                new_addict = New.objects.create(**new_content)
                news_list.append(new_content)

            
            return Response(news_list, status.HTTP_200_OK)

    def post(self, request: Request) -> Request:
        print('Service running')
        url = 'http://127.0.0.1:8000/api/news/startscrappy/'
        while True:
            response = requests.get(url)
            print(response.text)
            time.sleep(1800)
        



        
