from rest_framework.routers import SimpleRouter
from .viewSet import CartViewSet

router = SimpleRouter()

router.register("cart",CartViewSet)

urlpatterns = router.urls