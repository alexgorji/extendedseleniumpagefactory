from time import sleep
import re

from seleniumpagefactory import PageFactory


class AssertPageError(Exception):
    pass


class AssertPageMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    title = None

    def assert_page(self):
        if not self.title:
            raise AttributeError(f'class attribute: title is not set!')
        if self.driver.title != self.title:
            raise AssertPageError(f'title of driver: {self.driver.title} != title of page: {self.title}')
        assert self.driver.title == self.title


class NavLocatorsMixin:
    nav_locators = {}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.locators.update(self.nav_locators)


class FormButtonsMixin:
    form_buttons = []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        form_buttons = self._create_locators(self.form_buttons)
        self.locators.update(form_buttons)

    def _create_locators(self, form_buttons):
        output = {}
        for key in form_buttons:
            if isinstance(key, tuple):
                loc = key[1]
                output[key[0]] = (
                    loc,
                    ' '.join([x.capitalize() for x in key[0].replace('and', '&').split('_')])
                )
            else:
                output[key] = (
                    "CSS",
                    f"input[value='{' '.join([x.capitalize() for x in key.replace('and', '&').split('_')])}']")
        return output

    def _max_window_and_scroll_down(self, time):
        self.driver.maximize_window()
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        sleep(time)

    def _click(self, loc):
        return self.__getattr__(loc).click

    def _scroll_down_and_click(self, time, loc):
        self._max_window_and_scroll_down(time)
        self._click(loc)

    def __getattr__(self, item):
        try:
            locator = re.search(r'^scrolldown_and_click_(.*)', item).group(1)
            return self._scroll_down_and_click(time=0.5, loc=locator)
        except AttributeError:
            try:
                locator = re.search(r'^click_(.*)', item).group(1)
                return self._click(loc=locator)
            except AttributeError:
                return super().__getattr__(item)


class ExtendedPageFactory(AssertPageMixin, NavLocatorsMixin, FormButtonsMixin, PageFactory):
    locators = {}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not self.locators:
            print('No locators set!')
