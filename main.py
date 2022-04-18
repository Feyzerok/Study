import os
import time
from util import relocator
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
    #for item in dict['spaces']:
    #    href = item['link'][1]['href']
    #    print(href)
    """ Создаю директорию под пространство """
    if not os.path.exists(f'data/{dict["spaces"][0]["name"]}'):
        os.mkdir(f'data/{dict["spaces"][0]["name"]}')
    if not os.path.exists(f'data/{dict["spaces"][0]["name"]}/assets'):
        os.mkdir(f'data/{dict["spaces"][0]["name"]}/assets')

    """ Парсинг файлов """
    href = dict['spaces'][0]['link'][1]['href']
    driver.parse_space(href)
    time.sleep(4)

    path_to_relocate = os.path.join('data', f'{dict["spaces"][0]["name"]}')
    print(path_to_relocate)
    relocator(os.path.abspath('data'), os.path.abspath('data'+'/'+ f'{dict["spaces"][0]["name"]}'))

    driver.final()
if __name__ == "__main__":
    main()