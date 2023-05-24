from django.shortcuts import render, redirect
from posts.models import Post, Comment
from django.views import generic
from django.urls import reverse_lazy
from posts.forms import CommentForm, CreateForm
from django.contrib.auth.models import User

class IndexView(generic.ListView):
    queryset = Post.objects.filter(status = True)
    template_name = "posts/index.html"
    context_object_name = "posts"

class PostDetailView(generic.DetailView):
    model = Post
    template_name = "posts/post_detail.html"
    context_object_name = "post"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentForm()
        return context

    def post(self, request, pk):
        post = Post.objects.get(pk=pk)
        form = CommentForm(request.POST)
        if form.is_valid():
            pre_saved_comment = form.save(commit=False)
            pre_saved_comment.post = post
            pre_saved_comment.save()
        return redirect("post-detail", pk)
    
class PostCreateView(generic.CreateView):
    model = Post
    template_name = "posts/post_create.html"
    form_class = CreateForm
    success_url = reverse_lazy("index-page")

def create_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        user = User.objects.create_user(username=username, password=password, email=email)
        return redirect('index-page')
    return render(request, 'create_user.html')

class PostDeleteView(generic.DeleteView):
    model = Post
    success_url = reverse_lazy("index-page")
 
class PostUpdateView(generic.UpdateView):
    model = Post
    template_name = "posts/post_update.html"
    fields = ["title", "content"]
    success_url = reverse_lazy("index-page")

class PostDeleteConfirmView(generic.DeleteView):
    model = Post
    template_name = "posts/post_confirm_delete.html"
    success_url = reverse_lazy("index-page")
    fields = ["title", "content"]



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
    
