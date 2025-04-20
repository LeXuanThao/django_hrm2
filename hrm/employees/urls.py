from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from .views import LoginApiView

urlpatterns = [
    # path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('login/', LoginApiView.as_view(), name='login'),
]
# API urls
# from django.urls import include
# from django.urls import path
# from rest_framework.routers import DefaultRouter
# from .views import EmployeeViewSet, DepartmentViewSet, PositionViewSet, OrganizationViewSet
# from organizations.views import OrganizationViewSet

# router = DefaultRouter()
# router.register(r'employees', EmployeeViewSet)
# router.register(r'departments', DepartmentViewSet)
# router.register(r'positions', PositionViewSet)
# router.register(r'organizations', OrganizationViewSet)
# urlpatterns += [
#     path('api/', include(router.urls)),
# ]