from django.test import TestCase
from restaurant.models import Menu

class MenuModelTest(TestCase):
  def test_get_item(self):
    item = Menu.objects.create(title='Guacamole', price=7.99, inventory=80)
    self.assertEqual(str(item), 'Guacamole: 7.99')