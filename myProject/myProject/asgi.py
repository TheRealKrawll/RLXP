import os

from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
import rlxp.routing #not sure about this one

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myProject.settings')

application = ProtocolTypeRouter({
  'http': get_asgi_application(),
  'websocket': AuthMiddlewareStack(
    URLRouter(
      rlxp.routing.websocket_urlpatterns
    )
  )
})


