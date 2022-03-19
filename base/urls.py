from django.urls import path
from .views import ContactsList,contactDetail,NewContact,updateContact,deleteContact

urlpatterns = [
    path("",ContactsList.as_view(),name="home"),
    path("detail/<str:pk>/",contactDetail,name="detail"),
    path("new/",NewContact.as_view(),name="add"),
    path("update/<str:pk>/",updateContact,name="update"),
    path("delete/<str:pk>/",deleteContact,name="delete-contact"),
]
