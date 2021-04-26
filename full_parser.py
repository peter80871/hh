from selenium.webdriver import Chrome

driver = Chrome()

file = open('finish.txt', 'r').readlines()


file = list(set(file))

def parse(f):
    driver.get(f)
    print('new parsed')

    page = driver.find_element_by_tag_name('html').get_attribute("innerHTML")

    open(f'web/{f[-8:]}.html', 'w').write(str(page))
    print('writed')


for f in file:
    print(f.split('\n')[0])
    parse(f.split('\n')[0])

