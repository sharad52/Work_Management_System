from django.urls import path
from .views import Index,addWork,UpdateWork,DeleteWork

app_name = "SurfaceApp"

urlpatterns = [
	path('',Index,name="index"),
	path('add-work-details/',addWork,name="AddWork"),
	path('update-work-details/<int:pk>/',UpdateWork,name="UpdateWork"),
	path('delete-work/<int:pk>/',DeleteWork,name="DeleteWork"),
]