from django.urls import path, include
from . import views
from rest_framework import routers

# router = routers.DefaultRouter()
# router.register(r"brands", views.BrandViewSet)
# router.register(r'madels', views.MadelViewSet)


urlpatterns = [
    # path('', include(router.urls))

    path('brands/', views.BrandView.as_view(), name='brand-list'),
    path('brands/<int:pk>/detail/', views.BrandView.as_view(), name='brand-detail'),

    path('madels/', views.MadelView.as_view(), name='madel-list'),
    path('madels/<int:pk>/detail/', views.MadelView.as_view(), name='madel-detail'),
]