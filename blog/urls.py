from django.urls import path
from . import views
urlpatterns = [
    path('',views.BlogListView.as_view(), name='blog_list'),
    path('<int:pk>/',views.BlogDetailView.as_view(), name='blog_detail'),
    path('edit/ <int:pk>',views.BlogEditView.as_view(), name='blog_edit'),
    path('delete/ <int:pk>',views.BlogDeleteView.as_view(), name='blog_delete'),
    path('new/',views.BlogCreatView.as_view(), name='blog_new'),
]
