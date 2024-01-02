An extension for PageFactory class (selenium-page-factory)


Main class: 

**ExtendedPageFactory(AssertPageMixin, NavLocatorsMixin, FormButtonsMixin, PageFactory)**


Mixins:

**AssertPageMixin** (title) -> Checks if the current page has the same title as given.

**NavLocatorsMixin** (nav_locators) -> Provides a class attribute to be added to PageFactory attribute locators. This is
a convenient way to add common navbar locators to several Page classes.

**FormButtonsMixin** (form_buttons) -> Provides a list of form inputs such as save (value='Save'), save_and_new (
value='Save & New'), delete (value='Delete') etc. as a class attribute (form_buttons=[save, save_and_new, delete]). If
a tuple is given the second value indicates the locator. For example if the cancel button is in reality a
link: `<a href="">Cancel</a>`, add (cancel, "LINK_TEXT") to form_buttons.
This class provides click methods for each input or link according to form_buttons list: click_save(),
click_save_and_new(), click_delete() and click_cancel() would be the click methods in our example case.
Other methods with scrolling and delaying options before clicking a button (scroll_down_and_click_...) are planed as
future features of this Mixin.

