from django.shortcuts import render, get_object_or_404
from . models import Article, Category
from django.core.mail import send_mail
import plotly.express as px
import plotly.io as pio
import pandas as pd
from plotly.offline import plot
from plotly.graph_objs import Scatter


# Create your views here.
def home(request):
    news = Article.objects.order_by("-created_date")[:3]
    context = {
        "news":news,
        
    }
    return render(request,"index.html",context)

def guide(request):
    article = Article.objects.all()
    context = {
        "article":article
    }
    return render(request,"guides.html",context)

def about(request):
    return render(request,"about.html")

def contact(request):
    if request.method == "POST":
        txtName = request.POST['txtName']
        txtEmail = request.POST['txtEmail']
        txtMsg = request.POST['txtMsg']
        send_mail(
            txtName,
            txtMsg,
            txtEmail,
            ['teamback2future@gmail.com'],
        )
        context = {
            'txtName':txtName
        }
        return render(request,"contact.html",context)
    else:
        return render(request,"contact.html",{})

def CategoryView(request, cats):
    category_articles = Article.objects.filter(category=cats)
    return render(request,"categories.html",{'cats':cats, 'category_articles':category_articles})

def detail(request,id):
    #article = Article.objects.filter(id=id).first()
    article = get_object_or_404(Article,id = id)
    city = Category.objects.all()

    context = {
        "article":article,
        "city":city

    }
    
    return render(request,"guide_detail.html",context)



def plotx(request):
    df = pd.DataFrame()
    df['Cities'] = ['Istanbul', "Tokyo", "Londra", "Amsterdam", "Paris", " Viyana"]
    df['Corona Risk'] = [60, 40, 35, 50, 45, 30]
    fig = px.bar(df, x="Cities", y="Corona Risk", title='Corona risks in touristic cities')
    div = pio.to_html(fig, include_plotlyjs=False, full_html=False)
    
    return render(request, "plot.html", context={'plot_div': div})

