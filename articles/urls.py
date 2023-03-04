from django.urls import path
from .views import article_list_view
from .views import article_list_view,article_detail_view,article_update_view,article_delete_view,article_create_view

# from .views import ArticleListView, ArticleUpdateView,ArticleDetailView,ArticleDeleteView,ArticleCreateView

#
# urlpatterns = [
#     path('', ArticleListView.as_view(), name='article_list'),
#     path('update/<int:pk>/', ArticleUpdateView.as_view(), name='article_update'),
#     path('<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
#     path('delete/<int:pk>/', ArticleDeleteView.as_view(), name='article_delete'),
#     path('create/', ArticleCreateView.as_view(), name='article_create'),
# ]


urlpatterns = [
    path('', article_list_view, name='article_list'),
    path('<int:pk>/', article_detail_view, name='article_detail'),
    path('update/<int:pk>/', article_update_view, name='article_update'),

    path('delete/<int:pk>/', article_delete_view, name='article_delete'),
    path('create/', article_create_view, name='article_create'),
]
