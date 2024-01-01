from extendedseleniumpagefactory.demoitem.functionaltests.base import FunctionalTest
from extendedseleniumpagefactory.demoitem.functionaltests.src.pages import DemoCreatePage, DemoListPage


class TesDemotItems(FunctionalTest):
    def test_demo_items(self):
        demo_create_page = DemoCreatePage()
        demo_list_page = DemoListPage()

