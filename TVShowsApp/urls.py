from django.urls import path
from . import views

urlpatterns = [
    # ******* intial render paths *********
    path('', views.index),
    path('allShows', views.allShows),
    path('editShow/<int:show_id>', views.editShow),
    path('showInfo/<int:show_id>', views.showInfo),

    # ***** redirecting paths to initial renders *****

    path('create_new_show', views.create_new_show),
    path('delete_show/<int:show_id>', views.delete_show),
    path('update_show/<int:show_id>', views.update_show)
]
