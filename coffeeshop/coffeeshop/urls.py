from django.contrib import admin
from django.conf.urls import url,include
from rest_framework import routers
from api import views
from django.conf.urls.static import static
from django.conf import settings
import debug_toolbar
####################################################

router = routers.DefaultRouter()
router.register(r'Users', views.UserViewSet)
router.register(r'Products', views.ProductViewSet,'products')
router.register(r'Images', views.ImageViewSet,'Images')
router.register(r'Categories', views.CategoryViewSet)
router.register(r'Updete', views.IsUpdateViewSet)
router.register(r'Contact', views.ContactUsViewSet)
router.register(r'Productcomments', views.ProductCommentViewSet)
router.register(r'Comment2Us', views.Comment2UsViewSet)
router.register(r'Reportedcomments', views.ReportedCommentViewSet)
router.register(r'ChefSuggest', views.ChefSuggestViewSet)
router.register(r'UserProfile', views.UserProfileViewSet)
router.register(r'MainItem', views.MainItemViewSet,'MainItemList')

#router.register(r'QualityApi', views.QMViewSet)
#router.register(r'QQApi', views.QQViewSet,'QQApi')
######################################################
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls)),
    url(r'^__debug__/', include(debug_toolbar.urls)),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)