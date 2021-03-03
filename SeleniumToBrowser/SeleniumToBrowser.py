from Browser import *
from Browser.utils.data_types import *
from concurrent.futures import Future
from robot.libraries.BuiltIn import BuiltIn
from robot.api import logger
from datetime import timedelta
from typing import Any, List, Dict


class SeleniumToBrowser:

    def __init__(self, enable_conversion_deprecation_message: bool = False):
        self.show_deprecation_message = enable_conversion_deprecation_message
        self.browser = BuiltIn().get_library_instance('Browser')
        self.pre_locator = ''
        pass

    def show_deprecation (self, msg: str):
        if self.show_deprecation_message:
            logger.warn(msg)

    def select_frame(self, locator: str):
        if self.pre_locator == '':
            self.pre_locator = locator + ' >>> '
        else:
            self.pre_locator = self.pre_locator + locator + ' >>> '
        pass

    def exit_frame(self):
        self.pre_locator = ''
        pass

    def unselect_frame(self):
        return self.exit_frame()

    def assign_id_to_element(self, locator: str, id: str):
        pass

    def capture_page_screenshot(self, filename: str = 'robotframework-browser-screenshot-{index}'):
        self.show_deprecation("Please consider using 'Take Screenshot' keyword from Browser library.")
        return self.browser.take_screenshot()

    def input_text(self, locator: str, text: str, clear: bool = True):
        self.show_deprecation("Please consider using 'Fill Text' keyword from Browser library.")
        return self.browser.fill_text(selector=self.pre_locator + locator, text=text)

    def press_keys(self, locator: str = None, *keys: str):

        translator = {
            'ADD' : 'Add',
            'ALT' : 'Alt',
            'ARROW_DOWN' : 'ArrowDown',
            'ARROW_LEFT' : 'ArrowLeft',
            'ARROW_RIGHT'	: 'ArrowRight',
            'ARROW_UP' : 'ArrowUp',
            'BACK_SPACE' : 'Backspace',
            'CANCEL' : 'Cancel',
            'CLEAR' : 'Clear',
            'COMMAND' : 'Meta',
            'CONTROL' : 'Control',
            'DELETE' : 'Delete',
            'DIVIDE' : 'Divide',
            'END' : 'End',
            'ENTER' : 'Enter',
            'ESCAPE' : 'Escape',
            'F1' : 'F1',
            'F2' : 'F2',
            'F3' : 'F3',
            'F4' : 'F4',
            'F5' : 'F5',
            'F6' : 'F6',
            'F7' : 'F7',
            'F8' : 'F8',
            'F9' : 'F9',
            'F10' : 'F10',
            'F11' : 'F11',
            'F12' : 'F12',
            'HELP' : 'Help',
            'HOME' : 'GoHome',
            'INSERT' : 'Insert',
            'META' : 'Meta',
            'MULTIPLY' : 'Multiply',
            'PAGE_DOWN' : 'PageDown',
            'PAGE_UP' : 'PageUp',
            'PAUSE' : 'Pause',
            'RETURN' : 'Enter',
            'SEPARATOR' : 'Separator',
            'SHIFT' : 'Shift',
            'SPACE' : ' ',
            'SUBTRACT' : 'Subtract',
            'TAB' : 'Tab'
        }

        translated_keys = ''
        new_keys = []

        for k in keys:
            new_keys.append(k.split('+'))

        for keys in new_keys:
            for k in keys:
                if translated_keys == '':
                    if k.upper() in translator:
                        translated_keys = translated_keys + translator[k.upper()]
                    else:
                        translated_keys = translated_keys + k
                else:
                    if k.upper() in translator:
                        translated_keys = translated_keys + '+' + translator[k.upper()]
                    else:
                        translated_keys = translated_keys + '+' + k

        return self.browser.press_keys(self.pre_locator + locator, translated_keys)

    def open_browser(self, url: str = None, browser: str = 'chrome', alias: str = None, options: Any = None):
        browser_translation = {
            "googlechrome": SupportedBrowsers.chromium,
            "chrome": SupportedBrowsers.chromium,
            "edge": SupportedBrowsers.chromium,
            "firefox": SupportedBrowsers.firefox,
            "safari": SupportedBrowsers.webkit,
            "ie": SupportedBrowsers.chromium
        }
        self.browser.new_browser(browser=browser_translation[browser], headless=False, timeout=timedelta(seconds=30))
        self.browser.new_page(url)

    def handle_alert(self, action: str = 'accept'):
        self.show_deprecation("Please consider using 'Handle Future Dialogs' keyword from Browser library.")
        if action.lower() == 'accept':
            return self.browser.handle_future_dialogs(action=DialogAction.accept)
        else:
            return self.browser.handle_future_dialogs(action=DialogAction.dismiss)

    def wait_until_page_contains_element(self, locator: str, timeout: int = 10, error: str = None, limit: int = None):
        self.show_deprecation("Waits keywords are no longer needed in Browser library.")
        return self.browser.wait_for_elements_state(selector=self.pre_locator + locator, state=ElementState.attached, timeout=timedelta(seconds=timeout))

    def wait_until_page_does_not_contain_element(self, locator: str, timeout: int = 10, error: str = None, limit: int = None):
        self.show_deprecation("Waits keywords are no longer needed in Browser library.")
        return self.browser.wait_for_elements_state(selector=self.pre_locator + locator, state=ElementState.detached, timeout=timedelta(seconds=timeout))

    def wait_until_element_is_enabled(self, locator: str, timeout: int = 10, error: str = None, limit: int = None):
        self.show_deprecation("Waits keywords are no longer needed in Browser library.")
        return self.browser.wait_for_elements_state(selector=self.pre_locator + locator, state=ElementState.enabled, timeout=timedelta(seconds=timeout))

    def wait_until_element_is_visible(self, locator: str, timeout: int = 10, error: str = None):
        self.show_deprecation("Waits keywords are no longer needed in Browser library.")
        return self.browser.wait_for_elements_state(selector=self.pre_locator + locator, state=ElementState.visible, timeout=timedelta(seconds=timeout))

    def wait_until_element_is_not_visible(self, locator: str, timeout: int = 10, error: str = None):
        self.show_deprecation("Waits keywords are no longer needed in Browser library.")
        return self.browser.wait_for_elements_state(selector=self.pre_locator + locator, state=ElementState.hidden, timeout=timedelta(seconds=timeout))

    def page_should_contain(self, text: str, loglevel: str = 'TRACE'):
        self.show_deprecation("Please consider using 'Get Text' keyword from Browser library.")
        return self.browser.get_text(selector='css:html', assertion_operator=AssertionOperator['*='], assertion_expected=text)

    def page_should_not_contain(self, text: str, loglevel: str = 'TRACE'):
        self.show_deprecation("Please consider using 'Get Text' keyword from Browser library.")
        return self.browser.get_text(selector='css:html', assertion_operator=AssertionOperator['!='], assertion_expected=text)

    def page_should_contain_element(self, locator: str, message: str = None, loglevel: str = 'TRACE', limit: str = None):
        self.show_deprecation("Please consider using 'Wait For Elements State' keyword from Browser library.")
        return self.browser.wait_for_elements_state(selector=self.pre_locator + locator, state=ElementState.attached)

    def page_should_not_contain_element(self, locator: str, message: str = None, loglevel: str = 'TRACE', limit: str = None):
        self.show_deprecation("Please consider using 'Wait For Elements State' keyword from Browser library.")
        return self.browser.wait_for_elements_state(selector=self.pre_locator + locator, state=ElementState.detached)

    def page_should_contain_button(self, locator: str, message: str = None, loglevel: str = 'TRACE'):
        self.show_deprecation("Please consider using 'Wait For Elements State' keyword from Browser library.")
        return self.browser.wait_for_elements_state(selector=self.pre_locator + locator, state=ElementState.attached)

    def element_should_be_visible(self, locator: str, message: str = None):
        self.show_deprecation("Please consider using 'Wait For Elements State' keyword from Browser library.")
        return self.browser.wait_for_elements_state(selector=self.pre_locator + locator, state=ElementState.visible)

    def element_should_not_be_visible(self, locator: str, message: str = None):
        self.show_deprecation("Please consider using 'Wait For Elements State' keyword from Browser library.")
        return self.browser.wait_for_elements_state(selector=self.pre_locator + locator, state=ElementState.hidden)

    def element_should_be_disabled(self, locator: str):
        self.show_deprecation("Please consider using 'Wait For Elements State' keyword from Browser library.")
        return self.browser.wait_for_elements_state(selector=self.pre_locator + locator, state=ElementState.disabled)

    def element_should_contain(self, locator: str, expected: str, message: str = None, ignore_case: bool = False):
        self.show_deprecation("Please consider using 'Get Text' keyword from Browser library.")
        return self.browser.get_text(selector=self.pre_locator + locator, assertion_operator=AssertionOperator["*="], assertion_expected=expected)

    def element_text_should_be(self, locator: str, expected: str, message: str = None, ignore_case: bool = False):
        self.show_deprecation("Please consider using 'Get Text' keyword from Browser library.")
        return self.browser.get_text(selector=self.pre_locator + locator, assertion_operator=AssertionOperator["=="], assertion_expected=expected)

    def location_should_be(self, url: str, message: str = None):
        self.show_deprecation("Please consider using 'Get Url' keyword from Browser library.")
        return self.browser.get_url(assertion_operator=AssertionOperator["=="], assertion_expected=url)

    def get_element_attribute(self, locator: str, attribute: str):
        self.show_deprecation("Please consider using 'Get Attribute' keyword from Browser library.")
        return self.browser.get_attribute(selector=self.pre_locator + locator, attribute=attribute)

    def get_webelement(self, locator: str):
        self.show_deprecation("Please consider using 'Get Element' keyword from Browser library.")
        return self.browser.get_element(selector=self.pre_locator + locator)

    def get_value(self, locator: str):
        self.show_deprecation("This keyword doesn't do anything, please use another one to accomplish your goal.")
        pass

    def radio_button_should_be_set_to(self, group_name: str, value: str):
        self.show_deprecation("This keyword doesn't do anything, please use another one to accomplish your goal.")
        pass

    def click_element(self, selector: str, modifier: str = False, action_chain: bool = False ):
        self.show_deprecation("Please consider using 'Click' keyword from Browser library.")
        if selector.startswith('class='):
            return self.browser.click('xpath=//*[@class="{}"]'.format(selector[6:]))
        else:
            return self.browser.click(selector=self.pre_locator + selector)

    def click_link(self, link: str = '', id: str = '', xpath: str = '', modifier: str = False):
        self.show_deprecation("Please consider using 'Click' keyword from Browser library.")
        if link != '':
            return self.browser.click('xpath=//a[contains(text(),"{}")]'.format(link))
        elif id != '':
            return self.browser.click('xpath=//a[@id="{}"]'.format(id))
        elif xpath != '':
            return self.browser.click(xpath)

    def click_button(self, locator: str, modifier: str = False):
        self.show_deprecation("Please consider using 'Click' keyword from Browser library.")
        return self.browser.click(locator)

    def drag_and_drop_by_offset(self, locator: str, xoffset: float, yoffset: float):
        self.show_deprecation("Please consider using 'Drag And Drop By Coordinates' keyword from Browser library.")
        locator_coordinates = self.browser.get_boundingbox(selector=self.pre_locator + locator)
        xstart = locator_coordinates['x']
        ystart = locator_coordinates['y']
        return self.browser.drag_and_drop_by_coordinates(from_x=xstart, from_y=ystart, to_x=xstart + xoffset, to_y= ystart + yoffset)

    def select_from_list_by_value(self, locator: str, values: str):
        self.show_deprecation("Please consider using 'Select Options By' keyword from Browser library.")
        return self.browser.select_options_by(locator, SelectAttribute.value, values)

    def select_from_list_by_label(self, locator: str, values: str):
        self.show_deprecation("Please consider using 'Select Options By' keyword from Browser library.")
        return self.browser.select_options_by(locator, SelectAttribute.label, values)

    def scroll_element_into_view(self, locator: str):
        self.show_deprecation("Please consider using 'Scroll To' keyword from Browser library.")
        return self.browser.scroll_to(selector=self.pre_locator + locator)

    def set_focus_to_element(self, locator: str):
        self.show_deprecation("Please consider using 'Focus' keyword from Browser library.")
        return self.browser.focus(selector=self.pre_locator + locator)

    def set_selenium_speed(self, value: str):
        return None

    def set_selenium_timeout(self, value: str):
        self.show_deprecation("Please consider using 'Set Browser Timeout' keyword from Browser library.")
        return self.browser.set_browser_timeout(value)

    def set_window_size(self, width: int, height: int, inner: bool = False):
        self.show_deprecation("Please consider using 'Set Viewport Size' keyword from Browser library.")
        return self.browser.set_viewport_size(width=width, height=height)

    def input_password(self, locator: str, password: str, clear: bool = True):
        self.show_deprecation("Please consider using 'Fill Secret' keyword from Browser library.")
        return self.browser.fill_secret(locator, password)

    def mouse_over(self, locator: str):
        self.show_deprecation("Please consider using 'Hover' keyword from Browser library.")
        return self.browser.hover(selector=self.pre_locator + locator)

    def reload_page(self):
        self.show_deprecation("Please consider using 'Reload' keyword from Browser library.")
        return self.browser.reload()

    def close_all_browsers(self):
        self.show_deprecation("Please consider using 'Close Browser' keyword from Browser library.")
        self.browser.close_browser('ALL')
    