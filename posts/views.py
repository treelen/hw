from django.shortcuts import render
# from django.http import HttpResponse
from posts.models import Post
from django.views import generic
from django.urls import reverse_lazy

class IndexView(generic.ListView):
    # model = Post
    queryset = Post.objects.filter(status = True)
    template_name = "posts/index.html"
    context_object_name = "posts"

class PostDetailView(generic.DetailView):
    model = Post
    template_name = "posts/post_detail.html"
    context_object_name = "post"
    
class PostCreateView(generic.CreateView):
    model = Post
    template_name = "posts/post_create.html"
    fields = ["title", "content", "category"]
    success_url = reverse_lazy("index-page")

class PostDeleteView(generic.DeleteView):
    model = Post
    success_url = reverse_lazy("index-page")
 
class PostUpdateView(generic.UpdateView):
    model = Post
    template_name = "posts/post_update.html"
    fields = ["title", "content"]
    success_url = reverse_lazy("index-page")

class PostDeleteConfirimView(generic.DeleteView):
    model = Post
    template_name = "posts/post_confirm_delete.html"
    success_url = reverse_lazy("index-page")
    fields = ["title", "content"]


# def get_index(request):
#     posts = Post.objects.all()
#     context = {
#         "title": "Главная страница Жаныша",
#         "posts": posts    
#     }
#     return render(request, "posts/index.html", context = context)

# def get_post(request, pk):
#     post = Post.objects.get(pk=pk)
#     return render(request, "posts/post_detail.html", {"post": post})

def get_contacts(request):
    context = {
        "title": "Страница Контактов",
    }
    return render(request, "posts/contacts.html", context = context)

def get_about(request):
    context = {
        "title": "Страница О Нас",
    }
    return render(request, "posts/about.html", context = context) 
    
# def update_post(request):
#     context = {
#         "h1": "Да работает"
#     }
#     return render(request, "posts/post_update.html", context = context)

# def delete_post(request):
#     context = {
#         "h1": "Запись работает?"
#     }
#     return render(request, "posts/post_delete.html", context = context)