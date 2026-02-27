from django.urls import path
from .views import FeatureImageUploadView, ExtraImagesUploadView

urlpatterns = [
    path('events/<int:event_id>/feature-image/', FeatureImageUploadView.as_view(), name='event-feature-image'),
    path('events/<int:event_id>/extra-images/', ExtraImagesUploadView.as_view(), name='event-extra-images'),

]
