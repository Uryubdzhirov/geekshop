from django.urls import path

import mainapp.views as mainapphhhhggdt

app_name = "mainapp"

urlpatterns = [
    path("", mainapp.products, name="index"),
    path("category/<int:pk>/", mainapp.products, name="category"),
]
