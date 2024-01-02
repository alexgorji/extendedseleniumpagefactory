from django.urls import reverse

from extendedseleniumpagefactory.demoitem.functionaltests.base import FunctionalTest
from extendedseleniumpagefactory.demoitem.functionaltests.src.pages import DemoCreatePage, DemoListPage


class TesDemoItems(FunctionalTest):
    def test_demo_items(self):
        demo_create_page = DemoCreatePage(self.driver)
        demo_list_page = DemoListPage(self.driver)
        "Tester goes to demo item list page and wants to add a new item. He finds a link on this page for adding items."
        self.driver.get(f"{self.live_server_url}{reverse('demo_items')}")
        demo_list_page.assert_page()
        demo_list_page.add_item_link.click()
        demo_create_page.assert_page()
        "She adds as name but cancel the process."
        demo_create_page.name.set_text('Testing')
        demo_create_page.click_cancel()
        demo_list_page.assert_page()
        "She goes back to the create item page and ..."
        demo_list_page.add_item_link.click()
        "... adds another name and clicks the save and new button."
        demo_create_page.name.set_text('Testing a')
        demo_create_page.click_save_and_new()
        "She adds as another name and clicks the save button."
        demo_create_page.name.set_text('Testing b')
        demo_create_page.click_save()
        "She tests if both nav links work."
        demo_create_page.demo_items_links.click()
        demo_list_page.assert_page()
        demo_list_page.demo_projects_links.click()
