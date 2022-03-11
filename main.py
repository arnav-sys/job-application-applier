from selenium import webdriver
from selenium.webdriver.common.keys import Keys

email = "YOUR_EMAIL"
password = "YOUR_PASSWORD"

chrome_driver_path = "/Users/Surface/Development/chromedriver"
driver = webdriver.Chrome(executable_path = chrome_driver_path)

driver.get("https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0")

sign_button = driver.find_element_by_css_selector(".nav__cta-container .nav__button-secondary")
sign_button.click()

email_button = driver.find_element_by_css_selector("#username")
email_button.send_keys(email)

password_button = driver.find_element_by_css_selector("#password")
password_button.send_keys(password)

click_btn = driver.find_element_by_xpath('//*[@id="organic-div"]/form/div[3]/button')
click_btn.click()

all_listings = driver.find_element_by_css_selector(".job-card-container--clickable")

for listing in all_listings:
    listing.click()

    try:
        apply_button = driver.find_element_by_css_selector(".job-s-apply button")
        apply_button.click()

        phone = driver.find_element_by_class_name("fb-single-line-text__input")
        if phone.text == "":
            phone.send_keys("3241234")

        submit_button = driver.find_element_by_css_selector("footer button")

        if submit_button.get_attribute("data-control-name") == "continue_unify":
            close_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
            close_button.click()
            discard_button = driver.find_elements_by_class_name("artdeco-modal__confirm-dailog-btn")[1]
            discard_button.click()
            continue
        else:
            submit_button.click()

        close_button = driver.find_elements_by_class_name("artdeco-modal__dismiss")
        close_button.click()

    except:
        print("No application button, skipped.")

driver.quit()