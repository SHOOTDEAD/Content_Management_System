from django.urls import path
from .views import *

urlpatterns = [
    path("articles",articles,name='articles'),
    path("search",search,name='search'),
    path("write",Write,name="Write"),
    path("myarticles",MyArticles,name="MyArticles"),
    path("delete/<int:id>",delete,name="delete"),
    path("save_changes/<int:id>",save_changes,name='save_changes'),
    path("get_attachment/<int:id>",get_attachment,name='get_attachment')
]