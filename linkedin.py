from selenium.webdriver.common.keys import Keys


def login(driver):
    username = 'clash320fclans@gmail.com'
    password = 'mrjackal_lantern'

    username_ele = driver.find_element_by_id('session_key')
    username_ele.send_keys(username)

    password_ele = driver.find_element_by_id('session_password')
    password_ele.send_keys(password)

    log_in = driver.find_element_by_class_name('sign-in-form__submit-button')
    log_in.click()


def search_for_contacts(driver, contact):
    driver.implicitly_wait(20)
    search = driver.find_element_by_xpath('/html/body/div[6]/header/div/div/div/div[1]/div[2]/input')

    search.click()
    search.send_keys(contact)

    driver.find_element_by_xpath("/html/body/div[6]/header/div/div/div/div[1]/div[2]/input").send_keys(Keys.RETURN)


def connect(driver):
    driver.implicitly_wait(20)

    button1 = driver.find_element_by_xpath(
        '/html/body/div[6]/div[3]/div/div[1]/div/div[1]/main/div/div/div[1]/ul/li[1]/div/div/div[3]/button')

    # button2 = driver.find_element_by_xpath('/html/body/div[6]/div[3]/div/div[1]/div/div[1]/main/div/div/div[2]/ul/li[1]/div/div/div[3]/button')

    button1.click()
    # button2.click()

    # pag.click(875, 420)


def add_note(driver):
    addnote = driver.find_element_by_xpath('/html/body/div[3]/div/div/div[3]/button[1]')

    addnote.click()

    note = driver.find_element_by_xpath('/html/body/div[3]/div/div/div[2]/div/textarea')
    note.send_keys('Hello')

    # From the Research Exploration Workshop on IoT and Privacy, would love to connect!


def send_connection(driver):
    driver.implicitly_wait(20)

    send = driver.find_element_by_xpath('/html/body/div[3]/div/div/div[3]/button[2]/span')
    send.click()


def connect_on_linkedin(driver, people):
    for name in people:

        search_for_contacts(driver, name)
        connect(driver)
        add_note(driver)
        send_connection(driver)

