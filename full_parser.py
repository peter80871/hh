from selenium.webdriver import Chrome

driver = Chrome()


file = open('vacancies.txt', 'r').read().split(';')

for f in file:
    driver.get(f)
    print(f[-8:])

    page = driver.find_element_by_tag_name('html').get_attribute("innerHTML")

    open(f'{f[-8:]}.html', 'w').write(str(page))
