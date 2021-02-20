from Browser import *
from Browser.utils.data_types import *
from concurrent.futures import Future
from robot.api import logger
from datetime import timedelta
from typing import Any, List, Dict

_local_browser = Browser(enable_playwright_debug = True)

class SeleniumToBrowser:

    def __init__(self, enable_conversion_deprecation_message: bool = False):
        self.show_deprecation_message = enable_conversion_deprecation_message
        self.browser = _local_browser
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
            "chrome": SupportedBrowsers.chromium,
            "edge": SupportedBrowsers.chromium,
            "firefox": SupportedBrowsers.firefox,
            "safari": SupportedBrowsers.webkit,
            "ie": SupportedBrowsers.chromium
        }
        self.browser.new_browser (browser_translation[browser], headless=False, timeout = '30s')
        self.browser.new_page (url)

    def handle_alert(self, action: str = 'accept'):
        self.show_deprecation("Please consider using 'Handle Future Dialogs' keyword from Browser library.")
        if action.lower() == 'accept':
            return self.browser.handle_future_dialogs(action=DialogAction.accept)
        else:
            return self.browser.handle_future_dialogs(action=DialogAction.dismiss)

    def wait_until_page_contains_element(self, locator: str, timeout: str = None, error: str = None, limit: int = None):
        self.show_deprecation("Waits keywords are no longer needed in Browser library.")
        return self.browser.wait_for_elements_state(selector=self.pre_locator + locator, state=ElementState.attached)

    def wait_until_page_does_not_contain_element(self, locator: str, timeout: str = None, error: str = None, limit: int = None):
        self.show_deprecation("Waits keywords are no longer needed in Browser library.")
        return self.browser.wait_for_elements_state(selector=self.pre_locator + locator, state=ElementState.detached)

    def wait_until_element_is_enabled(self, locator: str, timeout: str = None, error: str = None, limit: int = None):
        self.show_deprecation("Waits keywords are no longer needed in Browser library.")
        return self.browser.wait_for_elements_state(selector=self.pre_locator + locator, state=ElementState.enabled)

    def wait_until_element_is_visible(self, locator: str, timeout: str = None, error: str = None):
        self.show_deprecation("Waits keywords are no longer needed in Browser library.")
        return self.browser.wait_for_elements_state(selector=self.pre_locator + locator, state=ElementState.visible)

    def wait_until_element_is_not_visible(self, locator: str, timeout: str = None, error: str = None):
        self.show_deprecation("Waits keywords are no longer needed in Browser library.")
        return self.browser.wait_for_elements_state(selector=self.pre_locator + locator, state=ElementState.hidden)

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
        return self.browser.close_browser('ALL')

    ########################################################################################## Browser Built-in Keywords ####################################################################################################

    def add_cookie(self, name: str, value: str, url: str = None, domain: str = None, path: str = None, expires: str = None, httpOnly: bool = None, secure: bool = None, sameSite: CookieSameSite = None):
        return self.browser.add_cookie(name=name, value=value, url=url, domain=domain, path=path, expires=expires, httpOnly=httpOnly, secure=secure, sameSite=sameSite)

    def add_style_tag(self, content: str):
        return self.browser.add_style_tag(content=content)

    def check_checkbox(self, selector: str):
        return self.browser.check_checkbox(selector=self.pre_locator + selector)

    def clear_text(self, selector: str):
        return self.browser.clear_text(selector=self.pre_locator + selector)

    def click(self, selector: str, button: MouseButton = MouseButton.left, clickCount: int = 1, delay: timedelta = None, position_x: float = None, position_y: float = None, force: bool = False, noWaitAfter: bool = False, *modifiers: KeyboardModifier):
        return self.browser.click(selector=self.pre_locator + selector, button=button, clickCount=clickCount, delay=delay, position_x=position_x, position_y=position_y, force=force, noWaitAfter=noWaitAfter, modifiers=modifiers)

    def close_browser(self, browser: str = 'CURRENT'):
        return self.browser.close_browser(browser=browser)

    def close_context(self, context: str = 'CURRENT', browser: str = 'CURRENT'):
        return self.browser.close_context(context=context, browser=browser)

    def close_page(self, page: str = 'CURRENT', context: str = 'CURRENT', browser: str = 'CURRENT'):
        return self.browser.close_page(page=page, context=context, browser=browser)

    def connect_to_browser(self, wsEndpoint: str, browser: SupportedBrowsers = SupportedBrowsers.chromium):
        return self.browser.connect_to_browser(wsEndpoint=wsEndpoint, browser=browser)

    def delete_all_cookies(self):
        return self.browser.delete_all_cookies()

    def deselect_options(self, selector: str):
        return self.browser.deselect_options(selector=self.pre_locator + selector)

    def download(self, url: str):
        return self.browser.download(url=url)

    def drag_and_drop(self, selector_from: str, selector_to: str, steps: int = 1):
        return self.browser.drag_and_drop(selector_from=selector_from, selector_to=selector_to, steps=steps)

    def drag_and_drop_by_coordinates(self, from_x: float, from_y: float, to_x: float, to_y: float, steps: int = 1):
        return self.browser.drag_and_drop_by_coordinates(from_x=from_x, from_y=from_y, to_x=to_x, to_y=to_y)

    def eat_all_cookies(self):
        return self.browser.eat_all_cookies()

    def execute_javascript(self, function: str, selector: str = ''):
        return self.browser.execute_javascript(function=function, selector=self.pre_locator + selector)

    def fill_secret(self, selector: str, secret: str):
        return self.browser.fill_secret(selector=self.pre_locator + selector, secret=secret)

    def fill_text(self, selector: str, text: str):
        return self.browser.fill_text(selector=self.pre_locator + selector, text=text)

    def focus(self, selector: str):
        return self.browser.focus(selector=self.pre_locator + selector)

    def get_attribute(self, selector: str, attribute: str, assertion_operator: AssertionOperator = None, assertion_expected: Any = None, message: str = None):
        return self.browser.get_attribute(selector=self.pre_locator + selector, attribute=attribute, assertion_operator=assertion_operator, assertion_expected=assertion_expected, message=message)

    def get_attribute_names(self, selector: str, assertion_operator: AssertionOperator = None, *assertion_expected, message: str = None):
        return self.browser.get_attribute_names(selector=self.pre_locator + selector, assertion_operator=assertion_operator, assertion_expected=assertion_expected, message=message)

    def get_boundingbox(self, selector: str, key: BoundingBoxFields = BoundingBoxFields.ALL, assertion_operator: AssertionOperator = None, assertion_expected: Any = None, message: str = None):
        return self.browser.get_boundingbox(selector=self.pre_locator + selector, key=key, assertion_operator=assertion_operator, assertion_expected=assertion_expected, message=message)

    def get_browser_catalog(self, assertion_operator: AssertionOperator = None, assertion_expected: Any = None, message: str = None):
        return self.browser.get_browser_catalog(assertion_operator=assertion_operator, assertion_expected=assertion_expected, message=message)

    def get_browser_ids(self, browser: SelectionType = SelectionType.ALL):
        return self.browser.get_browser_ids(browser=browser)

    def get_checkbox_state(self, selector: str, assertion_operator: AssertionOperator = None, expected_state: str = 'Unchecked', message: str = None):
        return self.browser.get_checkbox_state(selector=self.pre_locator + selector, assertion_operator=assertion_operator, expected_state=expected_state, message=message)

    def get_classes(self, selector: str, assertion_operator: AssertionOperator = None, *assertion_expected, message: str = None):
        return self.browser.get_classes(selector=self.pre_locator + selector, assertion_operator=assertion_operator, assertion_expected=assertion_expected, message=message)

    def get_client_size(self, selector: str = None, key: SizeFields = SizeFields.ALL, assertion_operator: AssertionOperator = None, assertion_expected: Any = None, message: str = None):
        return self.browser.get_client_size(selector=self.pre_locator + selector, key=key, assertion_operator=assertion_operator, assertion_expected=assertion_expected, message=message)

    def get_context_ids(self, context: SelectionType = SelectionType.ALL, browser: SelectionType = SelectionType.ALL):
        return self.browser.get_context_ids(context=context, browser=browser)

    def get_cookie(self, cookie: str, return_type: CookieType = CookieType.dictionary):
        return self.browser.get_cookie(cookie=cookie, return_type=return_type)

    def get_cookies(self, return_type: CookieType = CookieType.dictionary):
        return self.browser.get_cookies(return_type=return_type)

    def get_device(self, name: str):
        return self.browser.get_device(name=name)

    def get_devices(self):
        return self.browser.get_devices()

    def get_element(self, selector: str):
        return self.browser.get_element(selector=self.pre_locator + selector)

    def get_element_count(self, selector: str, assertion_operator: AssertionOperator = None, expected_value: int = 0, message: str = None):
        return self.browser.get_element_count(selector=self.pre_locator + selector, assertion_operator=assertion_operator, expected_value=expected_value, message=message)

    def get_element_state(self, selector: str, state: ElementStateKey = ElementStateKey.visible, assertion_operator: AssertionOperator = None, assertion_expected: bool = True, message: str = None):
        return self.browser.get_element_state(selector=self.pre_locator + selector, state=state, assertion_operator=assertion_operator, assertion_expected=assertion_expected, message=message)

    def get_elements(self, selector: str):
        return self.browser.get_elements(selector=self.pre_locator + selector)

    def get_page_ids(self, page: SelectionType = SelectionType.ALL, context: SelectionType = SelectionType.ALL, browser: SelectionType = SelectionType.ALL):
        return self.browser.get_page_ids(page=page, context=context, browser=browser)

    def get_page_source(self, assertion_operator: AssertionOperator = None, assertion_expected: Any = None, message: str = None):
        return self.browser.get_page_source(assertion_operator=assertion_operator, assertion_expected=assertion_expected, message=message)

    def get_property(self, selector: str, property: str, assertion_operator: AssertionOperator = None, assertion_expected: Any = None, message: str = None):
        return self.browser.get_property(selector=self.pre_locator + selector, property=property, assertion_operator=assertion_operator, assertion_expected=assertion_expected, message=message)

    def get_scroll_position(self, selector: str = None, key: AreaFields = AreaFields.ALL, assertion_operator: AssertionOperator = None, assertion_expected: Any = None, message: str = None):
        return self.browser.get_scroll_position(selector=self.pre_locator + selector, key=key, assertion_operator=assertion_operator, assertion_expected=assertion_expected, message=message)

    def get_scroll_size(self, selector: str = None, key: SizeFields = SizeFields.ALL, assertion_operator: AssertionOperator = None, assertion_expected: Any = None, message: str = None):
        return self.browser.get_scroll_size(selector=self.pre_locator + selector, key=key, assertion_operator=assertion_operator, assertion_expected=assertion_expected, message=message)

    def get_select_options(self, selector: str, assertion_operator: AssertionOperator = None, assertion_expected: Any = None, message: str = None):
        return self.browser.get_select_options(selector=self.pre_locator + selector, assertion_operator=assertion_operator, assertion_expected=assertion_expected, message=message)

    def get_selected_options(self, selector: str, option_attribute: SelectAttribute = SelectAttribute.label, assertion_operator: AssertionOperator = None, *assertion_expected):
        return self.browser.get_selected_options(selector=self.pre_locator + selector, option_attribute=option_attribute, assertion_operator=assertion_operator, assertion_expected=assertion_expected)

    def get_style(self, selector: str, key: str = 'ALL', assertion_operator: AssertionOperator = None, assertion_expected: Any = None, message: str = None):
        return self.browser.get_style(selector=self.pre_locator + selector, key=key, assertion_operator=assertion_operator, assertion_expected=assertion_expected, message=message)

    def get_text(self, selector: str, assertion_operator: AssertionOperator = None, assertion_expected: Any = None):
        return self.browser.get_text(selector=self.pre_locator + selector, assertion_operator=assertion_operator, assertion_expected=assertion_expected)

    def get_textfield_value(self, selector: str, assertion_operator: AssertionOperator = None, assertion_expected: Any = None, message: str = None):
        return self.browser.get_textfield_value(selector=self.pre_locator + selector, assertion_operator=assertion_operator, assertion_expected=assertion_expected, message=message)

    def get_title(self, assertion_operator: AssertionOperator = None, assertion_expected: Any = None, message: str = None):
        return self.browser.get_title(assertion_operator=assertion_operator, assertion_expected=assertion_expected, message=message)

    def get_url(self, assertion_operator: AssertionOperator = None, assertion_expected: Any = None, message: str = None):
        return self.browser.get_url(assertion_operator=assertion_operator, assertion_expected=assertion_expected, message=message)

    def get_viewport_size(self, key: SizeFields = SizeFields.ALL, assertion_operator: AssertionOperator = None, assertion_expected: Any = None, message: str = None):
        return self.browser.get_viewport_size(key=key, assertion_operator=assertion_operator, assertion_expected=assertion_expected, message=message)

    def go_back(self):
        return self.browser.go_back()

    def go_forward(self):
        return self.browser.go_forward()

    def go_to(self, url: str, timeout: timedelta = None):
        return self.browser.go_to(url=url, timeout=timeout)

    def handle_future_dialogs(self, action: DialogAction, prompt_input: str = ''):
        return self.browser.handle_future_dialogs(action=action, prompt_input=prompt_input)

    def highlight_elements(self, selector: str, duration: timedelta = timedelta(seconds=5), width: str = '2px', style: str = 'dotted', color: str = 'blue'):
        return self.browser.highlight_elements(selector=self.pre_locator + selector, duration=duration, width=width, style=style, color=color)

    def hover(self, selector: str, position_x: float = None, position_y: float = None, force: bool = False, *modifiers: KeyboardModifier):
        return self.browser.hover(selector=self.pre_locator + selector, position_x=position_x, position_y=position_y, force=force, modifiers=modifiers)

    def http(self, url: str, method: RequestMethod = RequestMethod.GET, body: str = None, headers: dict = None):
        return self.browser.http(url=url, method=method, body=body, headers=headers)

    def keyboard_input(self, action: KeyboardInputAction, input: str, delay: int = 0):
        return self.browser.keyboard_input(action=action, input=input, delay=delay)

    def keyboard_key(self, action: KeyAction, key: str):
        return self.browser.keyboard_key(action=action, key=key)

    def localstorage_clear(self):
        return self.browser.localstorage_clear()

    def localstorage_get_item(self, key: str, assertion_operator: AssertionOperator = None, assertion_expected: Any = None, message: str = None):
        return self.browser.localstorage_get_item(key=key, assertion_operator=assertion_operator, assertion_expected=assertion_expected, message=message)

    def localstorage_remove_item(self, key: str):
        return self.browser.localstorage_remove_item(key=key)

    def localstorage_set_item(self, key: str, value: str):
        return self.browser.localstorage_set_item(key=key, value=value)

    def mouse_button(self, action: MouseButtonAction, x: float = None, y: float = None, button: MouseButton = MouseButton.left, clickCount: int = 1, delay: int = 0):
        return self.browser.mouse_button(action=action, x=x, y=y, button=button, clickCount=clickCount, delay=delay)

    def mouse_move(self, x: float, y: float, steps: int = 1):
        return self.browser.mouse_move(x=x, y=y, steps=steps)

    def mouse_move_relative_to(self, selector: str, x: float = 0.0, y: float = 0.0, steps: int = 1):
        return self.browser.mouse_move_relative_to(selector=self.pre_locator + selector, x=x, y=y, steps=steps)

    def new_browser(self, browser: SupportedBrowsers = SupportedBrowsers.chromium, headless: bool = True, executablePath: str = None, args: List[str] = None, ignoreDefaultArgs: List[str] = None,
                        proxy: Proxy = None, downloadsPath: str = None, handleSIGINT: bool = True, handleSIGTERM: bool = True, handleSIGHUP: bool = True, timeout: timedelta = timedelta(seconds=30),
                        env: dict = None, devtools: bool = False, slowMo: timedelta = timedelta(seconds=0)):
        return self.browser.new_browser(browser=browser, headless=headless, executablePath=executablePath, args=args, ignoreDefaultArgs=ignoreDefaultArgs, proxy=proxy, downloadsPath=downloadsPath, handleSIGINT=handleSIGINT,
                                handleSIGTERM=handleSIGTERM, handleSIGHUP=handleSIGHUP, timeout=timeout, env=env, devtools=devtools, slowMo=slowMo)

    def new_context(self, acceptDownloads: bool = False, ignoreHTTPSErrors: bool = False, bypassCSP: bool = False, viewport: ViewportDimensions = None, userAgent: str = None, deviceScaleFactor: float = 1.0,
                        isMobile: bool = False, hasTouch: bool = False, javaScriptEnabled: bool = True, timezoneId: str = None, geolocation: GeoLocation = None, locale: str = None, permissions: List[str] = None,
                        extraHTTPHeaders: Dict[str, str] = None, offline: bool = False, httpCredentials: HttpCredentials = None, colorScheme: ColorScheme = None, proxy: Proxy = None, videosPath: str = None,
                        videoSize: ViewportDimensions = None, defaultBrowserType: SupportedBrowsers = None, hideRfBrowser: bool = False, recordVideo: RecordVideo = None):
        return self.browser.new_context(acceptDownloads=acceptDownloads, ignoreHTTPSErrors=ignoreHTTPSErrors, bypassCSP=bypassCSP, viewport=viewport, userAgent=userAgent, deviceScaleFactor=deviceScaleFactor,
                                isMobile=isMobile, hasTouch=hasTouch, javaScriptEnabled=javaScriptEnabled, timezoneId=timezoneId, geolocation=geolocation, locale=locale, permissions=permissions,
                                extraHTTPHeaders=extraHTTPHeaders, offline=offline, httpCredentials=httpCredentials, colorScheme=colorScheme, proxy=proxy, videosPath=videosPath,
                                videoSize=videoSize, defaultBrowserType=defaultBrowserType, hideRfBrowser=hideRfBrowser, recordVideo=recordVideo)

    def new_page(self, url: str = None):
        return self.browser.new_page(url=url)

    def promise_to(self, kw: str, *args):
        return self.browser.promise_to(kw=kw, args=args)

    def promise_to_wait_for_download(saveAs: str = ''):
        return self.browser.promise_to_wait_for_download(saveAs=saveAs)

    def register_keyword_to_run_on_failure(self, keyword: str):
        return self.browser.register_keyword_to_run_on_failure(keyword=keyword)

    def reload(self):
        return self.browser.reload()

    def scroll_by(self, selector: str = None, vertical: str = 'height', horizontal: str = '0', behavior: ScrollBehavior = ScrollBehavior.auto):
        return self.browser.scroll_by(selector=self.pre_locator + selector, vertical=vertical, horizontal=horizontal, behavior=behavior)

    def scroll_to(self, selector: str = None, vertical: str = 'top', horizontal: str = 'left', behavior: ScrollBehavior = ScrollBehavior.auto):
        return self.browser.scroll_to(selector=self.pre_locator + selector, vertical=vertical, horizontal=horizontal, behavior=behavior)

    def select_options_by(self, selector: str, attribute: SelectAttribute, *values):
        return self.browser.select_options_by(selector=self.pre_locator + selector, attribute=attribute, values=values)

    def sessionstorage_clear(self):
        return self.browser.sessionstorage_clear()

    def sessionstorage_get_item(self, key: str, assertion_operator: AssertionOperator = None, assertion_expected: Any = None):
        return self.browser.sessionstorage_get_item(key=key, assertion_operator=assertion_operator, assertion_expected=assertion_expected)

    def sessionstorage_remove_item(self, key: str):
        return self.browser.sessionstorage_remove_item(key=key)

    def sessionstorage_set_item(self, key: str, value: str):
        return self.browser.sessionstorage_set_item(key=key, value=value)

    def set_browser_timeout(self, timeout: timedelta):
        return self.browser.set_browser_timeout(timeout=timeout)

    def set_geolocation(self, latitude: float, longitude: float, accuracy: float = None):
        return self.browser.set_geolocation(latitude=latitude, longitude=longitude, accuracy=accuracy)

    def set_offline(self, offline: bool = True):
        return self.browser.set_offline(offline=offline)

    def set_retry_assertions_for(self, timeout: timedelta):
        return self.browser.set_retry_assertions_for(timeout=timeout)

    def set_viewport_size(self, width: int, height: int):
        return self.browser.set_viewport_size(width=width, height=height)

    def switch_browser(self, id: str):
        return self.browser.switch_browser(id=id)

    def switch_context(self, id: str, browser: str = 'CURRENT'):
        return self.browser.switch_context(id=id, browser=browser)

    def switch_page(self, id: str, context: str = 'CURRENT', browser: str = 'CURRENT'):
        return self.browser.switch_page(id=id, context=context, browser=browser)

    def take_screenshot(self, filename: str = 'robotframework-browser-screenshot-{index}', selector: str = '', fullPage: bool = False):
        return self.browser.take_screenshot(filename=filename, selector=self.pre_locator + selector, fullPage=fullPage)

    def type_secret(self, selector: str, secret: str, delay: timedelta = timedelta(seconds=0), clear: bool = True):
        return self.browser.type_secret(selector=self.pre_locator + selector, secret=secret, delay=delay, clear=clear)

    def type_text(self, selector: str, text: str, delay: timedelta = timedelta(seconds=0), clear: bool = True):
        return self.browser.type_text(selector=self.pre_locator + selector, text=text, delay=delay, clear=clear)

    def uncheck_checkbox(self, selector: str):
        return self.browser.uncheck_checkbox(selector=self.pre_locator + selector)

    def upload_file(self, path: str):
        return self.browser.upload_file(path=path)

    def wait_for(self, *promises: Future):
        return self.browser.wait_for(promises=promises)

    def wait_for_all_promises(self):
        return self.browser.wait_for_all_promises()

    def wait_for_download(self, saveAs: str = ''):
        return self.browser.wait_for_download(saveAs=saveAs)

    def wait_for_elements_state(self, selector: str, state: ElementState = ElementState.visible, timeout: timedelta = None, message: str = None):
        return self.browser.wait_for_elements_state(selector=self.pre_locator + selector, state=state, timeout=timeout, message=message)

    def wait_for_function(self, function: str, selector: str = '', polling: str = 'raf', timeout: timedelta = None, message: str = None):
        return self.browser.wait_for_function(function=function, selector=self.pre_locator + selector, polling=polling, timeout=timeout, message=message)

    def wait_for_request(self, matcher: str = '', timeout: timedelta = None):
        return self.browser.wait_for_request(matcher=matcher, timeout=timeout)

    def wait_for_response(self, matcher: str = '', timeout: timedelta = None):
        return self.browser.wait_for_response(matcher=matcher, timeout=timeout)

    def wait_until_network_is_idle(self, timeout: timedelta = None):
        return self.browser.wait_until_network_is_idle(timeout=timeout)
