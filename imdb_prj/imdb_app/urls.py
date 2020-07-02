from django.urls import path,include
from imdb_app import views
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('movieviewset',views.ImdbMovieViewSet)


urlpatterns = [

    path('',include(router.urls)),
    path('movielistgenerics/',views.ImdbMovieListAPIView.as_view(),name='movie_list'),

    path('movielist/', views.MovieList.as_view()),
    path('moviecreate/', views.MovieCreate.as_view()),
    path('movie/<int:pk>', views.MovieDetail.as_view()),
]









