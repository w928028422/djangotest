from django.shortcuts import render
from django.shortcuts import render_to_response
# Create your views here.
from django.http import HttpResponse
from django.core.paginator import Paginator,PageNotAnInteger
from order.models import *

def index(request):
    pagenum = request.GET.get('pid')
    products = Product.objects.all()
    p = Paginator(products,5)
    try:
        page = p.page(pagenum)
    except PageNotAnInteger:
        page = p.page(1)

    return render(request,'index.html',{'user':request.user, 'p':p, 'page':page})

def query(request):
    pagenum = request.GET.get('pid')
    products = []
    try:
        products = Product.objects.filter(name__contains=request.POST['productname'])
    except:
        products = Product.objects.all()
    p = Paginator(products, 5)
    try:
        page = p.page(pagenum)
    except PageNotAnInteger:
        page = p.page(1)

    return render(request,'index.html', {'user': request.user, 'p': p, 'page': page})

def order(request):
    print(request.user)
    try:
        produce = Product.objects.get(id=request.GET.get('pid'))
        user = UserProfile.objects.get(username=request.user)
        orderobj = Order.objects.create(product=produce,user=user)
    except:
        orderobj = None

    return render(request,'order.html',{'order':orderobj})