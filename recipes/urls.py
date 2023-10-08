from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from core.views import index
from core.views import detail
from core.views import addRecipe
from core.views import login_user
from core.views import logout_user
from core.views import my_recipes
from core.views import register_user
from django.urls import path
from django.conf import settings

urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    path('<int:pk>/', detail, name="detail"),
    path('addRecipe/', addRecipe, name="addRecipe"),
    path('login/', login_user, name="login"),
    path('logout/', logout_user, name="logout"),
    path('my_recipes/<author_id>/', my_recipes, name="my_recipes"),
    path('register_user/', register_user, name="register_user"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
