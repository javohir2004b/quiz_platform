# from rest_framework.documentation import include_docs_urls
#
# from django.contrib import admin
# from django.urls import path,include
# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('questions/', include('questions.urls')),
#     path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
#     path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
#     path('docs/', include_docs_urls(title='Quiz API Docs')),
#
# ]


from django.contrib import admin
from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('questions/', include('questions.urls')),  # ✅ shu chiziq kerak
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('docs/', include_docs_urls(title='Quiz API Docs')),
]
