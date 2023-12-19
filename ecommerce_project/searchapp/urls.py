from django.urls import path

from searchapp import views

app_name = 'searchapp'

urlpatterns = [
    path('',views.Searchresult,name='Searchresult')

]