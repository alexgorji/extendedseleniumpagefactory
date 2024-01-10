from extendedseleniumpagefactory import ExtendedPageFactory

NAV_LOCATORS = {
    'demo_items_links': ('LINK_TEXT', 'Demo Items'),
    'demo_projects_links': ('LINK_TEXT', 'Demo Projects'),
}


class DemoCreatePage(ExtendedPageFactory):
    def __init__(self, driver, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.driver = driver

    locators = {
        'name': ("ID", 'id_name')
    }

    nav_locators = NAV_LOCATORS

    title = 'Create Demo Item'

    form_buttons = ['save', 'save_and_new', ('cancel', 'LINK_TEXT'), 'save_and_delete']


class DemoListPage(ExtendedPageFactory):
    def __init__(self, driver, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.driver = driver

    locators = {
        'add_item_link': ('LINK_TEXT', 'Add Item')
    }

    nav_locators = NAV_LOCATORS

    title = 'Demo Items'


class DemoLoadElementPage(ExtendedPageFactory):
    def __init__(self, driver, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.driver = driver

    form_buttons = ['save']
