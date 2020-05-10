import pytest 
import sys      # add /pages to the sys.path

sys.path.insert(1, "../pages/")

from calculator import Calculator

def test_calculator_elements_on_load(driver):
    """Load the page and verify that the correct elements are displayed
    on the Calculator section """
    calculator = Calculator(driver)
    calculator.assert_section_initial_state()

def test_enter_text_into_monthly_income_input(driver):
    """Load the page and verify the functionlity of the monthly income input.
    It should only accept numeric values"""
    form = "credit"
    calculator = Calculator(driver)
    input_value = calculator.write_to_input_and_return_value(form=form, text="metrocuadrado")
    assert not input_value

def test_enter_low_quantity_monthly_income_input(driver):
    """Load the page and verify the functionality of the monthly income input.
    The entered quantity should be greater than 737717 """
    form = "credit"
    income = "1234"
    calculator = Calculator(driver)
    input_value = calculator.write_to_input_and_return_value(form=form, text=income)
    calculator.verify_form_warning_visibility(form=form)

def test_enter_high_quantity_monthly_income_input(driver):
    """Load the page and verify the functionality of the monthly income input.
    The entered quantity should have maximum 9 digits"""
    form = "credit"
    income = "1020304050"
    calculator = Calculator(driver)
    input_value = calculator.write_to_input_and_return_value(form=form, text=income)
    assert len(input_value) == 12

def test_tooltip_visibility(driver):
    """Load the page and verify the functionality of the help icon,
    a tooltip should be displayed when hovered"""
    calculator = Calculator(driver)
    calculator.assert_tooltip()

def test_credit_duration_dropdown_select_last_option(driver):
    """Load the page and verify the funcionality of the duration dropdown
    on the credit form. Last option should be 20 years"""
    form = "credit"
    index = 3
    expected = "20"
    calculator = Calculator(driver)
    calculator.assert_credit_dropdown_options_by_index(form=form, index=index, expected_value=expected)

def test_fill_credit_form_valid_data_button_enabled(driver):
    """Load the page and see the functionality of the credit form.
    The button should now be enabled"""
    form = "credit"
    income = "20000000"
    index = 3
    calculator = Calculator(driver)
    calculator.fill_form(form=form, input_value=income, dropdown_index=index)
    calculator.verify_calc_button_enabled(form=form)

def test_credit_button_generates_report(driver):
    """Load the page, fill the credit form and check that the results are generated"""
    form = "credit"
    income = "20000000"
    index = 3
    calculator = Calculator(driver)
    calculator.fill_form(form=form, input_value=income, dropdown_index=index)
    calculator.verify_calc_button_enabled(form=form)
    calculator.assert_calculator_results(form=form)

def test_enter_text_into_loan_input(driver):
    """Load the page and verify the functionlity of the fee calculator input.
    It should only accept numeric values"""
    form = "fee"
    calculator = Calculator(driver)
    input_value = calculator.write_to_input_and_return_value(form=form, text="metrocuadrado")
    assert not input_value

def test_enter_low_quantity_loan_input(driver):
    """Load the page and verify the functionality of the fee calculator input.
    The entered quantity should be greater than 15000000 """
    form = "fee"
    loan = "1234"
    calculator = Calculator(driver)
    input_value = calculator.write_to_input_and_return_value(form=form, text=loan)
    calculator.verify_form_warning_visibility(form=form)

def test_enter_high_quantity_loan_input(driver):
    """Load the page and verify the functionality of the fee calculator input.
    The entered quantity should have maximum 10 digits"""
    form = "fee"
    loan = "10203040506"
    calculator = Calculator(driver)
    input_value = calculator.write_to_input_and_return_value(form=form, text=loan)
    assert len(input_value) == 14

def test_fee_duration_dropdown_select_last_option(driver):
    """Load the page and verify the funcionality of the duration dropdown
    on the fee form. Last option should be 20 years"""
    form = "fee"
    index = 3
    expected = "20"
    calculator = Calculator(driver)
    calculator.assert_credit_dropdown_options_by_index(form=form, index=index, expected_value=expected)

def test_fill_fee_form_valid_data_button_enabled(driver):
    """Load the page and see the functionality of the fee form.
    The button should now be enabled"""
    form = "fee"
    loan = "200000000"
    index = 3
    calculator = Calculator(driver)
    calculator.fill_form(form=form, input_value=loan, dropdown_index=index)
    calculator.verify_calc_button_enabled(form=form)

def test_fee_button_generates_report(driver):
    """Load the page, fill the fee form and check that the results are generated"""
    form = "fee"
    loan = "200000000"
    index = 3
    calculator = Calculator(driver)
    calculator.fill_form(form=form, input_value=loan, dropdown_index=index)
    calculator.verify_calc_button_enabled(form=form)
    calculator.assert_calculator_results(form=form)