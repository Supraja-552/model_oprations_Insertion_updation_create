from django.shortcuts import render
from django.db.models import Q

# Create your views here.
from app.models import *
from django.http import HttpResponse
from django.db.models.functions import Length
def display_topic(request):
    QLTO=Topic.objects.all()
    QLTO=Topic.objects.order_by('topic_name')
    QLTO=Topic.objects.all().order_by('topic_name')
    QLTO=Topic.objects.all().order_by('-topic_name')
    QLTO=Topic.objects.order_by('-topic_name')
    QLTO=Topic.objects.filter(topic_name='cricket')
    QLTO=Topic.objects.order_by(Length('topic_name').desc())
    QLTO=Topic.objects.filter(topic_name='cricket')
    QLTO=Topic.objects.filter(topic_name='cricket')
    d={'QLTO':QLTO}
    return render(request,'display_topic.html',d)
def webpage(request):
    QLWO=Webpage.objects.all()
   
    QLWO=Webpage.objects.filter(id__lt='4')
    QLWO=Webpage.objects.filter(name__startswith='d')
    QLWO=Webpage.objects.all()
    QLWO=Webpage.objects.filter(pk__lt='4')
    QLWO=Webpage.objects.filter(name__startswith='r')
    QLWO=Webpage.objects.filter(name__startswith='D')
    QLWO=Webpage.objects.filter(Q(name__startswith='r')|Q(url__endswith='in'))
    QLWO=Webpage.objects.filter(Q(name__startswith='D')&Q(url__endswith='in'))
    QLWO=Webpage.objects.filter(topic_name='cricket',name__endswith='t')
    QLWO=Webpage.objects.filter(Q(email__contains='h')| Q(id__lt='3'))
    QLWO=Webpage.objects.filter(Q(email__contains='h')& Q(id__lt='3'))
    QLWO=Webpage.objects.filter(Q(email__contains='in')| Q(topic_name='Basket Ball'))

    
    d={'QLWO':QLWO}

    return render(request,'webpages.html',d)
def insert_access(request):
    QLAO=AccessRecord.objects.all()
    QLAO=AccessRecord.objects.filter(id__gte=3)
    QLAO=AccessRecord.objects.filter(id__gt=3)
    QLAO=AccessRecord.objects.filter(id__lt=3)
    QLAO=AccessRecord.objects.filter(id__lte=3)
    QLAO=AccessRecord.objects.filter(date__month='2')
    QLAO=AccessRecord.objects.all()
    QLAO=AccessRecord.objects.filter(date__year='2023')
    QLAO=AccessRecord.objects.filter(date__month='12')
    QLAO=AccessRecord.objects.filter(date__day='7')
    QLAO=AccessRecord.objects.filter(author__startswith='s')
    QLAO=AccessRecord.objects.filter(author__contains='s')
    QLAO=AccessRecord.objects.filter(author__endswith='t')
    QLAO=AccessRecord.objects.filter(id__in=[1,3])
    #QLAO=AccessRecord.objects.filter(name__startswith='d')
    QLAO=AccessRecord.objects.all()
    #QLAO=AccessRecord.objects.filter(name__startswith='D')
    QLAO=AccessRecord.objects.filter(Q(date__lt='2023-11-14')|Q(author__contains='s'))
    QLAO=AccessRecord.objects.filter(Q(date__day='12')|Q(date__month='1'))
    d={'QLAO':QLAO}
    
    return render(request,'access_record.html',d)
def insert_topic(request):
    topic_name=input('enter topic name')
   
    TO=Topic.objects.get_or_create(topic_name=topic_name)
    NTO=Topic.objects.all()
    d={'QLTO':NTO}
    return render(request,'display_topic.html',d)
def insert_webpage(request):
    tn=input('enter topic name')
    n=input()
    u=input()
    e=input()
    To=Topic.objects.get(topic_name=tn)
    QLWO=Webpage.objects.get_or_create(topic_name=To,name=n,url=u,email=e)[0]
    QLWO=Webpage.objects.all()
    
    
    d={'QLWO':QLWO}
    return render(request,'webpages.html',d)
def access_record(request):
    p=int(input('enter primary key'))
    d=input('enter date')
    a=input('enter author')
    PWO=Webpage.objects.get(pk=p)
    QLAO=AccessRecord.objects.get_or_create(name=PWO,date=d,author=a)[0]
    QLAO=AccessRecord.objects.all()
    d={'QLAO':QLAO}
    return render(request,'access_record.html',d)
def update_webpage(request):
    #Webpage.objects.filter(topic_name='cricket').update(name='msd')
    #Webpage.objects.filter(topic_name='Vali Ball').update(name='Rohit')
    #CTO=Topic.objects.get_or_create(topic_name='Boxing')
    #Webpage.objects.update_or_create(name='Rohit',defaults={'topic_name':CTO})
    #Webpage.objects.update_or_create(topic_name='cricket',defaults={'name':'Rohit Sharma'})
    #Webpage.objects.filter(name='Rohit').update(url='https://rohit.in')
    #Webpage.objects.filter(topic_name='Cricket').update(email='india@gmail.com')
    Webpage.objects.filter()
    QLWO=Webpage.objects.all()
    d={'QLWO':QLWO}
    return render(request,'webpages.html',d)
def delete_webpage(request):
    
