from django.urls import path
from . views import home, add, details, delete, update, comment
from . import views


urlpatterns = [
	# path('', views.home, name = 'home'),
	path('', home.as_view(), name = 'home'),
	path('add/', add.as_view(), name = 'add'),
	path('details/<int:pk>', details.as_view(), name = 'details'),
	path('details/delete/<int:pk>', delete.as_view(), name = 'delete'),
	path('details/update/<int:pk>', update.as_view(), name = 'update'),
	path('details/comment/<int:pk>', comment.as_view(), name = 'comment'),
]