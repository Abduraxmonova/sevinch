from django.urls import path
from .views import index, single, category, contact

urlpatterns = [
    path('',index,name='i'),
    path('s/<int:id>',single, name='s'),
    path('cat', category, name='cat'),
    path('con',contact,name='con')
]
