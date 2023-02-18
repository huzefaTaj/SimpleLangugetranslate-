from django.shortcuts import render
from .models import Article

# Create your views here.
def index(request):

    if request.method=='POST':
        En=request.POST.get('en','')
        Fr=request.POST.get('fr','')
        content=request.POST.get('content','')
        title={'en':En,
               'fr':Fr}
        article=Article(title=title,content=content)
        article.save()
        return render(request,'index.html')
    obj=Article.objects.all()
    article={'obj':obj}
    return render(request,'index.html',article)

def fr(request):
    if request.method=='POST':
        En=request.POST.get('en','')
        Fr=request.POST.get('fr','')
        content=request.POST.get('content','')
        title={'en':En,
               'fr':Fr}
        article=Article(title=title,content=content)
        article.save()
        return render(request,'fr.html')
    obj=Article.objects.all()
    article={'obj':obj}

    return render(request,'fr.html',article)
