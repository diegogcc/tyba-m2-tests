import time 

from base_page import BasePage
from locators import CalculatorLocators

class Calculator(BasePage):
    """
        Calculator forms
    """
    def _assert_credit_form_visibility(self):
        self.assert_element_visible(CalculatorLocators.MONTHLY_INCOME_INPUT)
        assert not self.read_element_value(CalculatorLocators.MONTHLY_INCOME_INPUT)
        self.assert_element_visible(CalculatorLocators.CREDIT_DURATION_DROPDOWN)
        self.assert_element_not_visible(CalculatorLocators.MONTHLY_INCOME_WARNING)
        self.assert_element_not_enabled(CalculatorLocators.CALCULATE_CREDIT_BUTTON)
        self.assert_element_visible(CalculatorLocators.CREDIT_IMAGE)

    def _assert_fee_form_visibility(self):
        self.assert_element_visible(CalculatorLocators.LOAN_AMOUNT_INPUT)
        assert not self.read_element_value(CalculatorLocators.LOAN_AMOUNT_INPUT)
        self.assert_element_visible(CalculatorLocators.LOAN_DURATION_DROPDOWN)
        self.assert_element_not_visible(CalculatorLocators.LOAN_AMOUNT_WARNING)
        self.assert_element_not_enabled(CalculatorLocators.CALCULATE_FEE_BUTTON)
        self.assert_element_visible(CalculatorLocators.FEE_IMAGE)

    def assert_section_initial_state(self):
        self.assert_element_text_contains(CalculatorLocators.CALCULATOR_TITLE, "calculadora")
        # assert self.get_element_attribute(CalculatorLocators.CREDIT_TAB, "aria-expanded")
        # assert not self.get_element_attribute(CalculatorLocators.FEE_TAB, "aria-expanded")
        self._assert_credit_form_visibility()
        # self.assert_element_value_contains(CalculatorLocators.CREDIT_DURATION_DROPDOWN, "15")

    def write_to_input_and_return_value(self, form, text):
        if "credit" in form:
            input_element = CalculatorLocators.MONTHLY_INCOME_INPUT
            self.click(CalculatorLocators.CREDIT_TAB)
        elif "fee" in form:
            input_element = CalculatorLocators.LOAN_AMOUNT_INPUT
            self.click(CalculatorLocators.FEE_TAB)
        else:
            raise ValueError("Invalid value for input form. Must be 'credit' or 'fee'")
        self.enter_keys(input_element, text)
        # click away
        self.click(CalculatorLocators.CALCULATOR_TITLE)
        return self.read_element_value(input_element)
        
    def verify_form_warning_visibility(self, form):
        if "credit" in form:
            warn_element = CalculatorLocators.MONTHLY_INCOME_WARNING
            self.click(CalculatorLocators.CREDIT_TAB)
        elif "fee" in form:
            warn_element = CalculatorLocators.LOAN_AMOUNT_WARNING
            self.click(CalculatorLocators.FEE_TAB)
        else:
            raise ValueError("Invalid value for warning form. Must be 'credit' or 'fee'")
        self.assert_element_visible(warn_element)

    def assert_tooltip(self):
        self.hover_to(CalculatorLocators.CREDIT_HELP_ICON)
        assert self.read_element_text(CalculatorLocators.CREDIT_TOOLTIP)
        self.assert_element_visible(CalculatorLocators.CREDIT_TOOLTIP)

    def assert_credit_dropdown_options_by_index(self, form, index, expected_value):
        if "credit" in form:
            dropdown = CalculatorLocators.CREDIT_DURATION_DROPDOWN
            self.click(CalculatorLocators.CREDIT_TAB)
        elif "fee" in form:
            dropdown = CalculatorLocators.LOAN_DURATION_DROPDOWN
            self.click(CalculatorLocators.FEE_TAB)
        else:
            raise ValueError("Invalid value for dropdown form. Must be 'credit' or 'fee'")
        self.select_dropdown_by_index(dropdown, index)
        self.assert_element_value_contains(dropdown, expected_value)

    def assert_calculator_results(self, form):
        if "credit" in form:
            results = CalculatorLocators.CREDIT_RESULTS_TEXTS
            self.click(CalculatorLocators.CREDIT_TAB)
        elif "fee" in form:
            results = CalculatorLocators.FEE_RESULTS_TEXTS
            self.click(CalculatorLocators.FEE_TAB)
        else:
            raise ValueError("Invalid value for dropdown form. Must be 'credit' or 'fee'")
        assert self.count_elements(results) == 4

    def fill_form(self, form, input_value, dropdown_index):
        if "credit" in form:
            self.click(CalculatorLocators.CREDIT_TAB)
            self._assert_credit_form_visibility()
            input_element = CalculatorLocators.MONTHLY_INCOME_INPUT
            dropdown = CalculatorLocators.CREDIT_DURATION_DROPDOWN
            button = CalculatorLocators.CALCULATE_CREDIT_BUTTON
        elif "fee" in form:
            self.click(CalculatorLocators.FEE_TAB)
            self._assert_fee_form_visibility()
            input_element = CalculatorLocators.LOAN_AMOUNT_INPUT
            dropdown = CalculatorLocators.LOAN_DURATION_DROPDOWN
            button = CalculatorLocators.CALCULATE_FEE_BUTTON
        else:
            raise ValueError("Invalid value for form. Must be 'credit' or 'fee'")
        self.enter_keys(input_element, input_value)
        self.select_dropdown_by_index(dropdown, dropdown_index)
        self.click(button)

    def verify_calc_button_enabled(self, form):
        if "credit" in form:
            button = CalculatorLocators.CALCULATE_CREDIT_BUTTON
            self.click(CalculatorLocators.CREDIT_TAB)
        elif "fee" in form:
            button = CalculatorLocators.CALCULATE_FEE_BUTTON
            self.click(CalculatorLocators.FEE_TAB)
        else:
            raise ValueError("Invalid value for form. Must be 'credit' or 'fee'")
        self.assert_element_enabled(button)