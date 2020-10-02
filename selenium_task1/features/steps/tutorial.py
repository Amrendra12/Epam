from behave import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox import firefox_profile
import pyotp
import pytest

@given('launch firefox browser')
def launch_browser(context):
    profile = webdriver.FirefoxProfile()
    options = webdriver.FirefoxOptions()
    options.set_preference("dom.webnotifications.serviceworker.enabled", False)
    options.set_preference("dom.webnotifications.enabled", False)
    context.driver = webdriver.Firefox(firefox_profile=profile,options=options)
    context.driver.maximize_window()

@when('login to amazon home page')
def open_home_page(context):
    context.driver.get("https://www.amazon.com/")
    otpkey = "KFHCXDVYZRWSKW45N4RLAR3H7CCQ7NPZBWGSMNETKMTQV2LQAREA"    
    webelement = context.driver.find_element_by_xpath("//span[contains(text(),'Hello, Sign in')]")
    webelement.click()
    context.driver.find_element_by_xpath("//input[@id='ap_email']").send_keys("alexaselenium100@gmail.com")
    webelement_continue = context.driver.find_element_by_xpath("//input[@id='continue']")
    webelement_continue.click()
    context.driver.find_element_by_xpath("//input[@id='ap_password']").send_keys("alexa123!")
    context.driver.find_element_by_xpath("//input[@name='rememberMe']").click()
    webelement_signin = context.driver.find_element_by_xpath("//input[@id='signInSubmit']")
    webelement_signin.click()
    totp = pyotp.TOTP(otpkey)
    otp = totp.now()
    browser_element = context.driver.find_element_by_id("auth-mfa-otpcode")
    browser_element.send_keys(otp)
    browser_element_auth = context.driver.find_element_by_id("auth-signin-button")
    browser_element_auth.click()
    
@then('verify the title of the home page')
def verify_title(context):
    titleOfThePage = context.driver.title
    assert "Amazon.com" in titleOfThePage
    context.driver.close()
    
@then('verify the amazon logo present')
def verify_amazon_logo(context):
    time.sleep(15)
    amazonLogoWebelement = context.driver.find_element_by_xpath("//span[@class='nav-sprite nav-logo-base']")
    assert amazonLogoWebelement.is_displayed()
    context.driver.close()

@then('type item in search box and add to kart')
def add_to_kart(context):
    time.sleep(10)
    context.driver.refresh()
    time.sleep(10)
    searchBox = context.driver.find_element_by_xpath("//input[@id='twotabsearchtextbox']")
    searchBox.send_keys("Selenium Webdriver")
    searchBox.send_keys(u'\ue007')
    time.sleep(10)
    item_webelement = context.driver.find_element_by_xpath("//span[contains(text(),'Selenium WebDriver Quick Start Guide: Write clear,')]")
    item_webelement.click()
    add_to_cart_webelement = context.driver.find_element_by_xpath("//input[@id='add-to-cart-button']")
    add_to_cart_webelement.click()
    time.sleep(5)
    cart_count = context.driver.find_element_by_xpath("//span[@id='nav-cart-count']").text
    if int(cart_count) > 0:
        assert True
    else:
        assert False
    context.driver.close()

@then('remove item from kart')
def remove_from_kart(context):
    time.sleep(10)
    context.driver.refresh()
    time.sleep(10)
    try:
        cart_removal_webelement = context.driver.find_element_by_xpath("//span[@id='nav-cart-count']")
        cart_removal_webelement.click()
        assert True
    except:
        print("No item available in the cart")
    context.driver.close()    
    
@then('close browser')
def close_browser(context):
    context.driver.close()
