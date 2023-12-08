from django.shortcuts import render,redirect,reverse
from django.http import StreamingHttpResponse
from .models import *
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from .forms import *
import datetime as dt

#Display all the available articles
def articles(request):
    if request.user.is_authenticated:
        pagination = Paginator(Article.objects.all(),4)
        page_no = request.GET.get("page")
        return render(request, "articles.html", context={"articles":pagination.get_page(page_no)})
    else:
        request.session["status"] = 3
        return redirect("login")

#Search funtionality for title,tags,author
def search(request):
    if request.user.is_authenticated:
        query = request.POST.get('search')
        if query:
            title = Article.objects.filter(title__icontains = query)
            tags = Article.objects.filter(tags__icontains = query)
            author = Article.objects.filter(author__icontains = query)
            data = title.union(tags).union(author)
        else:
            # This is there is case of pagination query is passed as parameter
            query = request.GET.get("q")
            title = Article.objects.filter(title__icontains = query)
            tags = Article.objects.filter(tags__icontains = query)
            author = Article.objects.filter(author__icontains = query)
            data = title.union(tags).union(author)
        
        pagination = Paginator(data,4)
        page_no = request.GET.get("page")
        data = pagination.get_page(page_no)
        difference = 4-len(data) # This is to decide whether to display paginations buttons and to create spaces
        try:
            data = pagination.page(page_no)
        except PageNotAnInteger:
            data = pagination.page(1)
        except EmptyPage:
            data = pagination.page(pagination.num_pages)
        return render(request, "articles.html", context={"articles":data,"difference":difference,"range":range(difference),"query":query})


    else:
        request.session["status"] = 3
        return redirect("login")

#Creating a Article
def Write(request):
    if request.user.is_authenticated:
        article = Article_Form(request.POST, request.FILES,None)
        if request.method == "POST":
            article.is_valid()
            article = article.cleaned_data
            title,content,file,tags = article['title'],article['content'],article['file'],article['tags']
            new_entry = Article.objects.create(title=title,content=content,tags=tags,files=file,author=str(request.user),date=dt.datetime.today())
            new_entry.save()
            article = Article_Form()
            return render(request,'write.html',{'form':article,'status':1})
        
        return render(request,'write.html',{'form':article})
    else:
        request.session["status"] = 3
        return redirect("login")

#Displaying user specific articles
def MyArticles(request):
    if request.user.is_authenticated:
        status = int(request.GET.get("status")) if request.GET.get("status") else 0
        pagination = Paginator(Article.objects.filter(author=str(request.user)),4)
        page_no = request.GET.get("page")
        return render(request, "author_articles.html", context={"articles":pagination.get_page(page_no),'status':status})
    else:
        request.session["status"] = 3
        return redirect("login")

#Deleting a article   
def delete(request,id:int):
    if request.user.is_authenticated:
        obj = Article.objects.filter(id = id)
        obj.delete()
        return redirect(reverse("MyArticles")+"?status=1")
    else:
        request.session["status"] = 3
        return redirect("login")

#Updating a article   
def save_changes(request,id:int):
    if request.user.is_authenticated:
        obj = Article.objects.filter(id = id)
        values = request.GET.get('q').split('-/%')[:-1]
        obj.update(
            title = values[0],
            content = values[1],
            tags = values[2][6:],
            date = dt.datetime.today(),

        )
        return redirect(reverse("MyArticles")+"?status=2")
    else:
        request.session["status"] = 3
        return redirect("login")

#Streaming response to download attachments    
def get_attachment(request,id:int):
    if request.user.is_authenticated:
        article = Article.objects.filter(id=id)[0]
        file_path = article.files.path

        def file_iterator(file_path, chunk_size=8192):
            with open(file_path, 'rb') as file:
                while True:
                    data = file.read(chunk_size)
                    if not data:
                        break
                    yield data

        response = StreamingHttpResponse(file_iterator(file_path))
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = f'attachment; filename="{article.files.name[21:]}"'
        return response
    else:
        request.session["status"] = 3
        return redirect("login")
    