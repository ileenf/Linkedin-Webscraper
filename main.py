import participants
import speakers_gradstudents
from selenium import webdriver
from linkedin import login, connect_on_linkedin

# https://www.linkedin.com/pulse/how-easy-scraping-data-from-linkedin-profiles-david-craven/
# get data (school, major?) from linked page and see if college is correct for top 3 profiles

def main():
    linkedin_url = "http://linkedin.com/"
    speakers_url = 'https://sites.uci.edu/explorecsrworkshop/2021-academic-and-industry-speakers/'
    grad_students_url = 'https://sites.uci.edu/explorecsrworkshop/graduate-and-alumni-panelist/'

    students_dict = participants.get_participants_dict()
    speakers_list = speakers_gradstudents.get_speakers_list(speakers_url)
    grad_students_list = speakers_gradstudents.get_speakers_list(grad_students_url)

    driver = webdriver.Chrome('/Users/ileenf/Downloads/chromedriver')
    driver.get(linkedin_url)

    login(driver)

    connect_on_linkedin(driver, students_dict)
    connect_on_linkedin(driver, speakers_list)
    connect_on_linkedin(driver, grad_students_list)


    print('Finished!')


if __name__ == '__main__':
    main()







