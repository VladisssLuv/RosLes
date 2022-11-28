"""testDjangosite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from djangoForest.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('djangoForest.urls')),
    path('api/v1/gettable', TestAPIView.as_view()),
    path('allforest', AllForestlyViewSet.as_view({'get': 'list'})),
    path('subjectRF', SubjectRFview.as_view()),
    path('subjectRF/<int:pk>', SubjectRFview.as_view()),
    path('profile', ProfileView.as_view()),
    path('profile/<int:pk>', ProfileView.as_view()),
    path('list', ListView.as_view()),
    path('list/<int:pk>', ListView.as_view()),
    path('gps', GpsView.as_view()),
    path('gps/<int:pk>', GpsView.as_view()),
    # path('region', RegionView.as_view()),
    # path('region/<int:pk>', RegionView.as_view()),
    path('listregion', ListRegionView.as_view()),
    path('listregion/<int:pk>', ListRegionView.as_view()),
    path('sample', SampleView.as_view()),
    path('sample/<int:pk>', SampleView.as_view()),
    path('post', PostView.as_view()),
    path('post/<int:pk>', PostView.as_view()),
    path('workingbreed', WorkingBreedView.as_view()),
    path('workingbreed/<int:pk>', WorkingBreedView.as_view()),
    path('role', RoleView.as_view()),
    path('role/<int:pk>', RoleView.as_view()),
    path('reproduction', ReproductionView.as_view()),
    path('reproduction/<int:pk>', ReproductionView.as_view()),
    path('forestly', ForestlyView.as_view()),
    path('forestly/<int:pk>', ForestlyView.as_view()),
    path('districtforestly', DistrictForestlyView.as_view()),
    path('districtforestly/<int:pk>', ReproductionView.as_view()),
    path('breed', BreedView.as_view()),
    path('breed/<int:pk>', BreedView.as_view()),
    path('branches', BranchesView.as_view()),
    path('branches/<int:pk>', BranchesView.as_view()),
    path('erp/', include('erp.urls'))
]
