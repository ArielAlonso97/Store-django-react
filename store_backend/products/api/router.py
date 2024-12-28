from rest_framework.routers import SimpleRouter
from .viewSet import ProductViewSet

router = SimpleRouter()
router.register('products',ProductViewSet)
urlpatterns = router.urls