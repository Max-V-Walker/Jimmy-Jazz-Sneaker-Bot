from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

option = webdriver.ChromeOptions()
option.add_experimental_option("excludeSwitches", ["enable-automation"])
option.add_experimental_option('useAutomationExtension', False)
option.add_argument('--disable-blink-features=AutomationControlled')
bot = webdriver.Chrome(service=Service('/Users/maxwalker/Downloads/chromedriver'), options=option)
option.add_argument("window-size=1280,800")
option.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36")


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# ProductSelect within page source to find release sizes..
variables = {
    'brand': 'nike',
    'sneaker_full_name': 'lebron-20',
    'product_id': 'dj5423-500',
    'product_select': '7115858313423',
    'wanted_size_index': 5, #sz10
    'email': 'ENTERYOUREMAIL',
    'first_name': 'FIRSTNAME',
    'last_name': 'LASTNAME',
    'address1': 'STREET ADDRESS',
    'address2': 'APT #',
    'city': 'CITY',
    'zipcode': 'ZIPCODE',
    'phone': 'PHONE #',
    'card_number1': '0000',
    'card_number2': '0000',
    'card_number3': '0000',
    'card_number4': '0000',
    'card_expiration_month': '00',
    'card_expiration_year': '00',
    'card_cvv': '000'
}

url = "https://www.jimmyjazz.com/products/{}-{}-{}".format(variables['brand'], variables['sneaker_full_name'], variables['product_id'])

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Functionallity
def add_to_cart():
    size_btn = WebDriverWait(bot, 1000).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="ProductSelect-{}-option-0"]/div[{}]/label'.format(variables['product_select'], variables['wanted_size_index'])))
    )
    size_btn.click()
    sleep(.5)
    add_to_cart_btn = bot.find_element(By.ID, 'AddToCart-{}'.format(variables['product_select']))
    add_to_cart_btn.click()


def proceed_to_checkout():
    add_to_cart()

    checkout_btn = WebDriverWait(bot, 15).until(
        EC.visibility_of_element_located((By.CLASS_NAME, 'cart__checkout'))
    )
    checkout_btn.click()

    # Captcha appears now to resolve.. Giving 30 secs to get through.
    email_input = WebDriverWait(bot, 30).until(
        EC.presence_of_element_located((By.NAME, 'checkout[email]'))
    )
    
    first_name_input = bot.find_element(By.ID, 'checkout_shipping_address_first_name')
    last_name_input = bot.find_element(By.ID, 'checkout_shipping_address_last_name')
    address1_input = bot.find_element(By.ID, 'checkout_shipping_address_address1')
    address2_input = bot.find_element(By.ID, 'checkout_shipping_address_address2')
    city_input = bot.find_element(By.ID, 'checkout_shipping_address_city')
    zipcode_input = bot.find_element(By.ID, 'checkout_shipping_address_zip')
    phone_input = bot.find_element(By.ID, 'checkout_shipping_address_phone')
    continue_to_shipping_btn = bot.find_element(By.ID, 'continue_button')

    email_input.send_keys(variables['email'])
    sleep(.05)
    first_name_input.send_keys(variables['first_name'])
    sleep(.05)
    last_name_input.send_keys(variables['last_name'])
    sleep(.05)
    address1_input.send_keys(variables['address1'])
    sleep(.05)
    address2_input.send_keys(variables['address2'])
    sleep(.05)
    city_input.send_keys(variables['city'])
    sleep(.05)
    zipcode_input.send_keys(variables['zipcode'])
    sleep(.05)
    phone_input.send_keys(variables['phone'])
    sleep(.05)
    continue_to_shipping_btn.click()


def proceed_to_payment():
    proceed_to_checkout()
    # On shipping method page.
    bot.refresh()

    continue_to_payment_btn = WebDriverWait(bot, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'step__footer__continue-btn'))
    )
    continue_to_payment_btn.click()

    # On payment page
    bot.refresh()

    payment_iframes = WebDriverWait(bot, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, 'card-fields-iframe'))
    )

    bot.switch_to.frame(payment_iframes[0])
    card_number_input = bot.find_element(By.ID, 'number')
    card_number_input.send_keys(variables['card_number1'])
    card_number_input.send_keys(variables['card_number2'])
    card_number_input.send_keys(variables['card_number3'])
    card_number_input.send_keys(variables['card_number4'])

    bot.switch_to.default_content()

    bot.switch_to.frame(payment_iframes[1])
    name_on_card_input = WebDriverWait(bot, 10).until(
        EC.presence_of_element_located((By.ID, 'name'))
    )
    name_on_card_input.send_keys(variables['first_name'] + ' MIDDLE NAME IF NEEDED' + variables['last_name'])

    bot.switch_to.default_content()

    bot.switch_to.frame(payment_iframes[2])
    card_expiration_input = WebDriverWait(bot, 10).until(
        EC.presence_of_element_located((By.ID, 'expiry'))
    )
    card_expiration_input.send_keys(variables['card_expiration_month'])
    card_expiration_input.send_keys(variables['card_expiration_year'])

    bot.switch_to.default_content()

    bot.switch_to.frame(payment_iframes[3])
    cvv_input = WebDriverWait(bot, 10).until(
        EC.presence_of_element_located((By.ID, 'verification_value'))
    )
    cvv_input.send_keys(variables['card_cvv'])

    bot.switch_to.default_content()

    pay_now_btn = WebDriverWait(bot, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="continue_button"]'))
    )
    print('pay_now btn found and available!')
    # pay_now_btn.click()

    # print('Order placed!')


bot.get(url)
proceed_to_payment()
