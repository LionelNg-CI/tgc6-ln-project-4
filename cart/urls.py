from django.urls import path
import cart.views

urlpatterns = [
  path('add/<product_id>', cart.views.add_to_cart, name='add_to_cart'),
  path('view', cart.views.view_cart, name='view_cart'),
  path('remove/<product_id>', cart.views.remove_from_cart, name='remove_from_cart'),
  path('add_number/<product_id>', cart.views.add_number, name='add_number'),
  path('minus_number/<product_id>', cart.views.minus_number, name='minus_number'),
]