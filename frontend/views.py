
#for import page number
from django.core.paginator import Paginator
from django.shortcuts import render,redirect
from django.contrib import messages
#get the data form the data base
from .models import *
#get the date and time
import datetime

from django.db.models import Q

# Create your views here.


def home(request):
    #braking news
    first_news = News.objects.first()
    #next four braking news
    second_news = News.objects.all().order_by('-id')[1:5]
    # display the category
    sp_news = category.objects.all()
    #Display the news by the category
    cat_news = category.objects.all()
    #display the all news in home page
    all_news = News.objects.all()
    #recent news for bellow the tags 
    recnt_news = News.objects.all().order_by('-id')[:6]

    # to limit the news and use the page number
    page_num = Paginator(all_news, 5)
    page = request.GET.get('page')
    pg_num= page_num.get_page(page) #data
    
    # to display the time
    c_dt = datetime.datetime.now()
    
    return render(request, 'index.html', 
    {'first_news':first_news,
     'second_news' : second_news,
      'cat_news' : cat_news,
      'sp_news':sp_news,
      'c_dt':c_dt,
      'all_news':all_news,
      'pg_num':pg_num,
      'recnt_news':recnt_news })




# all_news
def all_news(request):
    # display the category on the header
    sp_news = category.objects.all()
    # to display the time
    c_dt = datetime.datetime.now()
    # to display the all news
    all_news = News.objects.all()
    #recent news for bellow the tags 
    recnt_news = News.objects.all().order_by('-id')[:6]

    # to limit the news and use the page number
    page_num = Paginator(all_news, 7)
    page = request.GET.get('page')
    pg_num= page_num.get_page(page) #data
    

    return render(request, 'blog.html',
     {'all_news': all_news,
     'sp_news':sp_news,
      'c_dt':c_dt,
      'pg_num':pg_num,
      'recnt_news':recnt_news})


# reed one single Full news
def detail(request,id,title=None):
    # display the category on the header
    sp_news = category.objects.all()
    # to display the time
    c_dt = datetime.datetime.now()
    #recent news for bellow the tags 
    recnt_news = News.objects.all().order_by('-id')[:6]

    # to read the full news
    news = News.objects.get(pk=id)
    Category = category.objects.get(id=news.category.id)
    rel_news=News.objects.filter(category=Category).exclude(id=id).order_by('-id')

   
    return render(request, 'detail.html',
     {'news': news,
     'rel_news' : rel_news,
     'sp_news':sp_news,
      'c_dt':c_dt,
      'recnt_news':recnt_news
     })


# display the category
def all_category(request):
    # display the category on the header
    sp_news = category.objects.all()
    # to display the time
    c_dt = datetime.datetime.now()
    # to display the category
    cats=category.objects.all()
    return render(request,'category.html',{
        'cats':cats,
        'sp_news':sp_news,
        'c_dt':c_dt
    })

# contect_us
def contect_us(request):
    # to display the time
    c_dt = datetime.datetime.now()
    # display the category on the header
    sp_news = category.objects.all()
    #recent news for bellow the tags 
    recnt_news = News.objects.all().order_by('-id')[:6]

    return render(request,'Contact_us.html', {
        'recnt_news':recnt_news,
        'sp_news':sp_news,
        'c_dt':c_dt
        
        })


# to display the news by the categry news

def category_news(request,id,title=None):
    # display the category on the header
    sp_news = category.objects.all()
    # to display the time
    c_dt = datetime.datetime.now()
    # to display the news by the category
    Category=category.objects.get(id=id)
    news=News.objects.filter(category=Category).order_by('-id')
    #recent news for bellow the tags 
    recnt_news = News.objects.all().order_by('-id')[:6]

    # to limit the news and use the page number
    
    page_num = Paginator(news, 5)
    page = request.GET.get('page')
    pg_num= page_num.get_page(page) #data
    
    return render(request,'category_news.html',{
        'news':news,
        'category':Category,
        'sp_news':sp_news,
        'c_dt':c_dt,
        'pg_num':pg_num,
        'recnt_news':recnt_news
    })



#for search

def search(request):
    # display the category on the header
    sp_news = category.objects.all()
    # to display the time
    c_dt = datetime.datetime.now()
    # to display the all news
    all_news = News.objects.all()
    #recent news for bellow the tags 
    recnt_news = News.objects.all().order_by('-id')[:6]

    # to limit the news and use the page number
    page_num = Paginator(all_news, 7)
    page = request.GET.get('page')
    pg_num= page_num.get_page(page) #data

    # search fields
    q = request.GET['q']

    data = News.objects.filter(keyword__icontains=q).order_by('-id')
   


    return render(request, 'search.html', {
        'data':data,
        'pg_num':pg_num,
        'sp_news':sp_news,
        'c_dt':c_dt,
        'recnt_news':recnt_news

        
        })    


# list the product's

def ecom_product(request):
    return render(request, 'ecom_product.html')
