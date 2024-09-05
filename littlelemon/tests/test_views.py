from django.test import TestCase
from restaurant.models import Menu

class MenuViewTest(TestCase):
  @classmethod
  def setUpTestData(cls):
    Menu.objects.create(title='Guacamole', price=7.99, inventory=80)
    Menu.objects.create(title='Nachos', price=10.49, inventory=45)

  def test_getall(self):
    response = self.client.get('http://127.0.0.1:8000/restaurant/menu/')
    response.render
    self.assertEqual(response.content, b'[{"id":2,"title":"Guacamole","price":"7.99","inventory":80},{"id":3,"title":"Nachos","price":"10.49","inventory":45}]')