from rest_framework.routers import DefaultRouter
from .views import CategoryView, CarView



router = DefaultRouter()

router.register('categories', CategoryView, basename='categories')
router.register('car', CarView, basename='car')

urlpatterns = router.urls