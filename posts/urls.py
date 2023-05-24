from django.urls import path
from posts import views

urlpatterns = [
    # path("", views.get_index, name='view-get_index'),
    path("", views.IndexView.as_view(), name='index-page'),
    path("contacts/", views.get_contacts, name='contacts-page'),
    path("about/", views.get_about, name='about-page'),
    path("posts/<int:pk>/", views.PostDetailView.as_view(), name='post-detail'),
    path("create_post/", views.PostCreateView.as_view(), name="post-create"),
    path("delete_post/<int:pk>/", views.PostDeleteView.as_view(), name="post-delete"),
    path("update_post/<int:pk>/", views.PostUpdateView.as_view(), name="post-update"),
    path('post/delete/<int:pk>', views.PostDeleteConfirmView.as_view(), name='post-confirm-delete'),
    # path("update_post/<int:pk>", views.update_post, name="post-update"),
    path('post/delete/<int:pk>', views.PostDeleteConfirmView.as_view(), name='post-confirm-delete'),
]