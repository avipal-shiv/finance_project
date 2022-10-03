from django.shortcuts import render, HttpResponse

from bs4 import BeautifulSoup
import requests
from scrapes_data_app.models import * 
from scrapes_data_app.models import * 
from urllib.parse import urlencode
from django.http import JsonResponse


# Create your views here.
from .serializers import WebscrapSerializer 
from rest_framework.response import Response
from rest_framework import viewsets,status



class WebscrapViewSet(viewsets.ViewSet):
    def post(self, request): 
        #Webscrap.objects.all().delete()
        num=1
        name =[]
        price =[]
        market=[]
        h_one_twenty_h_seven_day = []
        twenty_h =[]
        sday=[]
        circulating=[]        
        volume=[]
        page=5
        while num<page:
            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}

            url = "https://coinmarketcap.com?page="+str(num)
               
            
            response = requests.get(url,headers=headers)
            html_doc=response.content
            #print(html_doc)
            soup = BeautifulSoup(html_doc, 'html.parser')     
        
                    
            table=soup.find('table',  attrs={'class': 'h7vnx2-2 juYUEZ cmc-table'}).find('tbody').find_all('tr')    

            g=0
            for row in table: 

                td=row.find_all('td') 
                      
                
                for i in range(2,len(td)):         

                    h_one_twenty_h_seven_days=td[i].find('span')
                    if h_one_twenty_h_seven_days is not None:
                        h_one_twenty_h_seven_day.append(h_one_twenty_h_seven_days.get_text())
                
                    title=td[i].find('p',class_='sc-14rfo7b-0 lhJnKD')
                    if title is not None:
                        name.append(title.get_text())
                    

                    prices=td[i].find('div',class_='sc-131di3y-0 cLgOOr') 
                    if prices is not None:
                        price.append(prices.get_text())    
                    
                    markets=td[i].find('span',class_='sc-1ow4cwt-1 ieFnWP')     
                    if markets is not None:
                        market.append(markets.get_text())

                    circulatings=td[i].find('div',class_='sc-1prm8qw-0 sc-1gslw1d-1 gPKWfm')     
                    if circulatings is not None:
                        circulating.append(circulatings.get_text())

                    volumes=td[i].find('p',class_='sc-14rfo7b-0 fVSMmK font_weight_500')     
                    if volumes is not None:
                        volume.append(volumes.get_text())    
           
           
                
            #-----------------------insert in to table-----------#
            n=5
            new_list=[]
            for s in h_one_twenty_h_seven_day:
                if s!='':
                    new_list.append(s)

            chunk_list_1h_tewnty_h_seven_days =[new_list[i:i+n] for i in range(0,len(new_list),n)] 
            
            new_list_second =[]
            for p in range(len(name)):
                new_list_second.append(chunk_list_1h_tewnty_h_seven_days[p])
            
            
            num +=1

        
        for k in range(len(name)):
            
            try:
                n = name[k]
                p = price[k]
                m = market[k]
                v = volume[k]
                c= circulating[k]
            except IndexError:
                pass
            for w in range(len(new_list_second[k])):
                try:
                    hour=new_list_second[k][1]
                    twenty_hours=new_list_second[k][2]
                    seven_days=new_list_second[k][3]            
                except IndexError:
                    pass

            Webscrap.objects.create(
                name = n,
                price = p,
                hour =  hour,
                twenty_hours= twenty_hours,
                seven_days=  seven_days,  
                market_cap = m,
                volume = v,
                circulating_supply= c

            )
        web = Webscrap.objects.all()
        serialize = WebscrapSerializer(web, many=True)
        #response={'data': serialize.data,"message" :"Product list"}
        
        #return Response('hi')
        
        return JsonResponse({'foo':'bar'})

    
    def list(self,request): 
        Webscrap.objects.all().delete()           
        web = Webscrap.objects.all()
        serialize = WebscrapSerializer(web, many=True)
        response={'data': serialize.data,"message" :"Product list"}
        
        return Response(serialize.data)

def remove(duplicate):
    final_list = []
    found = set([])
    for num in duplicate:
        lst = []
        for element in num:
            if element not in found:
                found.add(element)
                lst.append(element)
        final_list.append(lst)
    return final_list



