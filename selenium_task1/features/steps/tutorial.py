from behave import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox import firefox_profile
import pyotp

@given('launch firefox browser')
def launchBrowser(context):
    profile = webdriver.FirefoxProfile()
    options = webdriver.FirefoxOptions()
    options.set_preference("dom.webnotifications.serviceworker.enabled", False)
    options.set_preference("dom.webnotifications.enabled", False)
    context.driver = webdriver.Firefox(firefox_profile=profile,options=options)
    context.driver.maximize_window()

@when('open amazon home page')
def openHomePage(context):
    context.driver.get("https://www.amazon.com/")
    otpkey = "KFHCXDVYZRWSKW45N4RLAR3H7CCQ7NPZBWGSMNETKMTQV2LQAREA"    
    webelement = context.driver.find_element_by_xpath("//span[contains(text(),'Hello, Sign in')]")
    webelement.click()
    context.driver.find_element_by_xpath("//input[@id='ap_email']").send_keys("alexaselenium100@gmail.com")
    webelement1 = context.driver.find_element_by_xpath("//input[@id='continue']")
    webelement1.click()
    context.driver.find_element_by_xpath("//input[@id='ap_password']").send_keys("alexa123!")
    context.driver.find_element_by_xpath("//input[@name='rememberMe']").click()
    webelement2 = context.driver.find_element_by_xpath("//input[@id='signInSubmit']")
    webelement2.click()
    totp = pyotp.TOTP(otpkey)
    otp = totp.now()
    browser_element = context.driver.find_element_by_id("auth-mfa-otpcode")
    browser_element.send_keys(otp)
    browser_element1 = context.driver.find_element_by_id("auth-signin-button")
    browser_element1.click()
    
@then('verify the title of the home page')
def verifyTitle(context):
    titleOfThePage = context.driver.title
    assert "Amazon.com" in titleOfThePage

@then('verify the amazon logo present')
def verifyAmazonLogo(context):
    amazonLogoWebelement = context.driver.find_element_by_xpath("//span[@class='nav-sprite nav-logo-base']")
    assert amazonLogoWebelement.is_displayed()
    
@then('close browser')
def closeBrowser(context):
    context.driver.close()
    