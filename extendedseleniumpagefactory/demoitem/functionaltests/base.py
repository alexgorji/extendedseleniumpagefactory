from datetime import datetime
from pathlib import Path

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

SCREEN_DUMP_LOCATION = Path(__file__).parent / 'screendumps'


class FunctionalTest(StaticLiveServerTestCase):
    def setUp(self) -> None:
        chrome_options = Options()
        # chrome_options.add_argument("--headless=new")
        self.driver = webdriver.Chrome(options=chrome_options)
        super().setUp()

    def tearDown(self) -> None:
        if self._test_has_failed():
            if not Path.exists(SCREEN_DUMP_LOCATION):
                SCREEN_DUMP_LOCATION.mkdir()
            for ix, handle in enumerate(self.driver.window_handles):
                self._windowid = ix
                self.driver.switch_to.window(handle)
                self.take_screenshot()
                self.dump_html()
        self.driver.quit()
        super().tearDown()

    def _test_has_failed(self):
        return any(error for (methode, error) in self._outcome.result.errors)

    def take_screenshot(self):
        filename = self._get_filename() + '.png'
        print('screenshotting to', filename)
        self.driver.get_screenshot_as_file(filename)

    def dump_html(self):
        filename = self._get_filename() + '.html'
        print('dumping page HTML to', filename)
        with open(filename, 'w') as f:
            f.write(self.driver.page_source)

    def _get_filename(self):
        timestamp = datetime.now().isoformat().replace(':', '.')[:19]
        return f'{SCREEN_DUMP_LOCATION}/{self.__class__.__name__}.{self._testMethodName}-window{self._windowid}-{timestamp}'
