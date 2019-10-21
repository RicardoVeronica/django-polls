from . import views
from django.urls import path

app_name = 'polls'
urlpatterns = [
    path('', views.index, name="index_url"),
    path('<int:question_id>/', views.detail, name="detail_url"),
    path('<int:question_id>/results/', views.results, name="results_url"),
    path('<int:question_id>/vote/', views.vote, name="vote_url"),
]
