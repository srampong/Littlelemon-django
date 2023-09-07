from django.test import TestCase
from restaurant.models import Menu

class MenuItemTest(TestCase):
   def setUp(self):
        Menu.objects.create(Title="IceCream", Price=80, Inventory=100)
        Menu.objects.create(Title="Yoghurt", Price=40, Inventory=40)
        Menu.objects.create(Title="Fanmilk", Price=20, Inventory=200)

   def test_getall(self):
        menuitems = Menu.objects.all()
        self.assertEqual(str(menuitems),str(Menu.objects.all()))
        
