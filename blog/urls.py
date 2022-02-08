from django.urls import path
from django.views.generic import UpdateView

from . import views
from blog.views import WatchDetail, WatchList, create_watch, ConditionView, LikeView, watchSearch, UpdateWatch, \
    MaisonListView, MaisonDetailView

app_name = 'blog'

urlpatterns = [
    path('<int:pk>/detail/', WatchDetail.as_view(), name="blogPostDetail"),
    path('list/', WatchList.as_view(), name="blogPostList"),
    path('insert/', views.create_watch, name="blogPostCreate"),
    path('update/<int:pk>/', UpdateWatch.as_view(), name="blogPostUpdate"),
    path('insert/', views.create_watch, name="blogPostCreate"),
    path('insert/', views.create_watch, name="blogPostCreate"),
    path('like/<int:pk>', LikeView, name="like_post"),
    path('search/', views.watchSearch, name="watchSearch"),
    path('condizione/<str:condition>', ConditionView, name="conditionWatch"),
    path('categoria_watch/', views.conditionListView, name='conditionWatchList'),
    path('maison_list/', MaisonListView.as_view(), name='MaisonList'),
    path('maison_detail/<int:pk>/', MaisonDetailView.as_view(), name='MaisonDetail'),
    path('favorite/', views.favorite_watch_view, name='favoriteWatch'),
    path('suggestion/', views.watch_suggestion, name='suggestionWatch'),
]
