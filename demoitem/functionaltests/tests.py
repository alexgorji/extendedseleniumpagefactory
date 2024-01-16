from django.urls import reverse
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from seleniumpagefactory.Pagefactory import ElementNotFoundException

from .base import FunctionalTest
from .src.pages import DemoCreatePage, DemoListPage, DemoLoadElementPage, DemoDetailPage


class TesDemoItems(FunctionalTest):
    def test_demo_items(self):
        demo_create_page = DemoCreatePage(self.driver)
        demo_list_page = DemoListPage(self.driver)
        demoe_detail_page = DemoDetailPage(self.driver)
        "Tester goes to demo item list page and wants to add a new item. He finds a link on this page for adding items."
        self.driver.get(f"{self.live_server_url}{reverse('demo_items')}")
        demo_list_page.assert_page()
        demo_list_page.add_item_link.click()
        demo_create_page.assert_page()
        "She adds as name but cancel the process."
        demo_create_page.name.set_text('Testing')
        demo_create_page.cancel.click()
        demo_list_page.assert_page()
        "She goes back to the create item page and ..."
        demo_list_page.add_item_link.click()
        "... adds another name and clicks the save and new button."
        demo_create_page.name.set_text('Testing a')
        demo_create_page.save_and_new.click()
        "She adds as another name and clicks the save button."
        self.driver.get(f"{self.live_server_url}{reverse('demo_create_item')}")
        demo_create_page.name.set_text('Testing b')
        demo_create_page.save.click()
        "She scrolls down and finds at the bottom of the page a button to save and delete. What does it do? She trys " \
        "it out."
        demo_create_page.save_and_delete.click()
        "She tests if both nav links work."
        demo_create_page.demo_items_links.click()
        demo_list_page.assert_page()
        demo_list_page.demo_projects_links.click()
        "She sees a link to the demo item and clicks it"
        demo_list_page.demo_item_link.click()
        "She gets to the demo page"
        demoe_detail_page.assert_page(title_extension=': Item')
