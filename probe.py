import json
import os

from vars import *
from seleniumdriver import ChromeDriver


def main():
    """ Инициализация и авторизация """
    driver_path = os.path.join('webdrivers', 'chromedriver.exe')
    url = 'http://85.93.148.190:8090/'
    if not os.path.exists('data'):
        os.mkdir('data')
    path = os.path.abspath('data')
    print(path)
    driver = ChromeDriver(driver_path=driver_path, url=url, download_path=path)
    driver.authorisation(LOGIN, PASSWORD, url)



    """ В цикле по всем spaces """

    counter = 3
    list_dict = []
    new_dict = driver.parse_space(dict['spaces'][counter], counter=counter+1)
#
    #for item in dict['spaces']:
    #    counter += 1
    #    if counter > 6:
    #        break
    #   #href = item['link'][1]['href']
    #   #print(href)
#
    #    new_dict = driver.parse_space(item, counter)
    #    list_dict.append(new_dict)
    #new_dict = driver.parse_space(dict['spaces'][5], counter)
    #print(list_dict)
    #with open('data.json', 'w', encoding='utf-8') as file:
    #    json.dump(list_dict, file, indent=4, ensure_ascii=False)

    driver.driver.get('http://yandex.ru')
if __name__ == "__main__":
    main()