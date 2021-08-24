from django.urls import path
from .views import Index,addWork,UpdateWork,DeleteWork

app_name = "SurfaceApp"

urlpatterns = [
	path('',Index,name="index"),
	path('add-work-details/',addWork,name="AddWork"),
	path('update-work-details/<str:slug>/',UpdateWork,name="UpdateWork"),
	path('delete-work/<str:slug>/',DeleteWork,name="DeleteWork"),
]