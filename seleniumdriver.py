import codecs
import glob
import json
import os
import time
import urllib.request

from util import relocator, unzip
from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class ChromeDriver:

    """ Инициализация бота, создание драйвера
    driver_path : Полный путь до драйвера
    url : адрес тестируемого веб приложения
    """
    def __init__(self, driver_path, url, download_path, headless=False):
        self.driver_path = Service(driver_path)
        self.options = webdriver.ChromeOptions()
        self.headless = headless
        self.url = url
        self.download_path = download_path


        self._options()

        """ desired_capabilities позволяет получать логи браузера"""
    def _options(self):
        #self.options.add_argument(
        #    "browser.helperApps.neverAsk.saveToDisk", "application/md")
        #self.options.add_argument("browser.download.folderList", 2)
        #self.options.add_argument("browser.download.dir", os.getcwd())
        #self.options.add_argument("pdfjs.disabled", True)

        #prefs = {'download.default_directory': self.download_path}
        #self.options.add_experimental_option('prefs', prefs)

        #self.options.add_argument(f"download.default_directory={self.download_path}")
        #self.options.headless = self.headless

        preferences = {
            "profile.default_content_settings.popups": 0,
            "download.default_directory": self.download_path,
            "directory_upgrade": True
        }

        self.options.add_experimental_option('prefs', preferences)

        #self.d = DesiredCapabilities.CHROME
        #self.d['goog:loggingPrefs'] = {'browser': 'ALL'}
        self.driver = webdriver.Chrome(service=self.driver_path, options=self.options)


    """ Обязательно после использования драйвера его нужно закрыть """
    def final(self):
        self.driver.close()
        self.driver.quit()

    def authorisation(self, login, pswd, login_url):
        self.driver.get(login_url)

        time.sleep(3)
        login_wind = self.driver.find_element(By.NAME, 'os_username')
        pswd_wind = self.driver.find_element(By.NAME, 'os_password')

        login_wind.send_keys(login)
        pswd_wind.send_keys(pswd)
        button = self.driver.find_element(By.NAME, 'login').click()
        time.sleep(2)

    def parse_space(self, item, counter):
        try:


            url = item['link'][1]['href']
            if not os.path.exists(f'data/{item["name"]}'):
                os.mkdir(f'data/{item["name"]}')
            if not os.path.exists(f'data/{item["name"]}/assets/'):
                os.mkdir(f'data/{item["name"]}/assets/')
            if not os.path.exists(f'data/{item["name"]}/assets/imgs'):
                os.mkdir(f'data/{item["name"]}/assets/imgs')

                """ Заполнение словаря """
            #dict_for_json[f'{item["name"]}'] =

            self.driver.get(url)

            self.driver.find_element(By.ID, 'action-menu-link').click()
            self.driver.implicitly_wait(1)
            exp = self.driver.find_element(By.ID, 'export-to-markdown').click()
            time.sleep(3)


            """ Задаю родительсий словарь """
            new_name = f"{str(counter).zfill(2)}.md"
            for file in glob.glob('data/*.md'):
                print(file)

                os.rename(file, f"data/{item['name']}/{new_name}")




            dictionary = {}
            dictionary['name'] = item['name']
            description = item['description']
            description = description.encode('utf-8')
            print(description)
            dictionary['description'] = item['description']
            dictionary['id'] = counter
            dictionary['path'] = f'data/{item["name"]}/{new_name}'
            dictionary['pages'] = []
            time.sleep(2)



            self.parse_attachments()
            """ Перемещение и раззиповка файлов """
            path_to_relocate = os.path.join('data', f'{item["name"]}')

            relocator(os.path.abspath('data'), os.path.abspath('data' + '/' + f'{item["name"]}'))
            time.sleep(3)
            unzip(os.path.abspath('data' + '/' + f'{item["name"]}'+'/assets'), os.path.abspath('data' + '/' + f'{item["name"]}'))
            time.sleep(3)
            relocator(os.path.abspath('data'), os.path.abspath('data' + '/' + f'{item["name"]}'))

            """ Переход на вкладку 'страницы' """
            a = self.driver.find_element(By.XPATH, '//*[@id="breadcrumbs"]/li[1]/span/a')
            print(a.text)
            a.click()
            time.sleep(1)

            list_tree = self.driver.find_element(By.CLASS_NAME, 'plugin_pagetree_children_list').find_elements(By.CLASS_NAME, 'plugin_pagetree_children_span')
            print(list_tree)
            counter_elem = 0
            counter_id = 0
            for item_space in range(len(list_tree)):
                self.driver.find_elements(By.CLASS_NAME, 'plugin_pagetree_children_span')[item_space].click()
                self.driver.implicitly_wait(2)
                self.driver.find_element(By.ID, 'action-menu-link').click()
                self.driver.implicitly_wait(2)
                exp = self.driver.find_element(By.ID, 'export-to-markdown').click()
                self.driver.implicitly_wait(2)
                self.parse_attachments()

                """ Создание словаря элемента """


                for file in glob.glob('data/*.md'):
                    counter_elem += 1
                    counter_id += 1
                    new_name = f"{dictionary['path'].split('/')[-1].split('.')[0]}_{str(counter_elem).zfill(2)}.md"
                    os.rename(file, f"data/{item['name']}/{new_name}")

                    elem_dict = {}
                    elem_dict['name'] = str(file).split('.')[0].split('\\')[1]
                    elem_dict['id'] = counter_id
                    elem_dict['path'] = f'data/{item["name"]}/{new_name}'


                    relocator(os.path.abspath('data'), os.path.abspath('data' + '/' + f'{item["name"]}'))
                    time.sleep(2)
                    unzip(os.path.abspath('data' + '/' + f'{item["name"]}' + '/assets'),
                          os.path.abspath('data' + '/' + f'{item["name"]}'))
                    time.sleep(2)


                    """ Поиск вложенностей внутри вложенностей """
                    try:
                        self.driver.find_element(By.CLASS_NAME, 'ia-splitter').find_element(By.CLASS_NAME, 'ia-fixed-sidebar').find_element(By.CLASS_NAME, 'ia-secondary-header-title').find_element(By.CLASS_NAME, 'icon').click()
                        childs = self.driver.find_element(By.CLASS_NAME, 'contextual-nav-child-pages').find_elements(By.CLASS_NAME, 'child-item')
                        print(f'..........{childs}...........')
                        time.sleep(1)


                        if childs:
                            elem_dict['pages'] = []
                            elem_in_elem_dict = self.parse_child(elem_dict, childs, item)
                            """Тройная вложенность"""
                                #try:
                            #    self.driver.find_element(By.CLASS_NAME, 'ia-splitter').find_element(By.CLASS_NAME,
                            #                                                                        'ia-fixed-sidebar').find_element(
                            #        By.CLASS_NAME, 'ia-secondary-header-title').find_element(By.CLASS_NAME,
                            #                                                                 'icon').click()
                            #    child_child = self.driver.find_element(By.CLASS_NAME, 'contextual-nav-child-pages').find_elements(By.CLASS_NAME, 'child-item')
                            #    print(f'..........{child_child}...........')
                            #    if child_child:
                            #        elem_in_elem_dict['pages'] = []
                            #        child_child_dict = self.parse_child(elem_in_elem_dict, child_child, item)
#
#
                            #        try:
                            #            self.driver.find_element(By.CLASS_NAME,
                            #                                     'ia-splitter').find_element(
                            #                By.CLASS_NAME,
                            #                'ia-fixed-sidebar').find_element(
                            #                By.CLASS_NAME, 'ia-secondary-header-title').find_element(
                            #                By.CLASS_NAME,
                            #                'icon').click()
                            #            child_child_child = self.driver.find_element(By.CLASS_NAME,
                            #                                                   'contextual-nav-child-pages').find_elements(
                            #                By.CLASS_NAME, 'child-item')
                            #            print(f'..........{child_child}...........')
                            #            if child_child_child:
                            #                child_child_dict['pages'] = []
                            #                child_child_child_dict = self.parse_child(child_child_dict, child_child_child, item)
#
                            #                child_child_dict['pages'].append(child_child_child_dict)
                            #                #self.driver.back()
                            #                self.driver.find_element(By.CLASS_NAME, 'ia-splitter').find_element(
                            #                    By.CLASS_NAME,
                            #                    'ia-fixed-sidebar').find_element(
                            #                    By.CLASS_NAME, 'ia-secondary-header-title').find_element(By.CLASS_NAME,
                            #                                                                             'icon').click()
                            #        except Exception as exc:
                            #            print(f'Ошибка 4 ого вложения {exc}')
                            #        elem_in_elem_dict['pages'].append(child_child_dict)
                            #        #self.driver.back()
                            #        self.driver.find_element(By.CLASS_NAME, 'ia-splitter').find_element(
                            #            By.CLASS_NAME,
                            #            'ia-fixed-sidebar').find_element(
                            #            By.CLASS_NAME, 'ia-secondary-header-title').find_element(By.CLASS_NAME,
                            #                                                                     'icon').click()
                            #except Exception as exc:
                            #    print(f'Ошибка 3 ого вложения {exc}')
                            #elem_dict['pages'].append(elem_in_elem_dict)
                            ##self.driver.back()
                            #self.driver.find_element(By.CLASS_NAME, 'ia-splitter').find_element(
                            #    By.CLASS_NAME,
                            #    'ia-fixed-sidebar').find_element(
                            #    By.CLASS_NAME, 'ia-secondary-header-title').find_element(By.CLASS_NAME,
                            #                                                             'icon').click()
                            elem_dict['pages'].append(elem_in_elem_dict)
                    except Exception as exc:
                        print(f'Ошибка 2 ого вложения {exc}')
                        self.driver.back()
                        self.driver.find_element(By.CLASS_NAME, 'ia-splitter').find_element(By.CLASS_NAME,
                                                                                            'ia-fixed-sidebar').find_element(
                            By.CLASS_NAME, 'ia-secondary-header-title').find_element(By.CLASS_NAME, 'icon').click()



                relocator(os.path.abspath('data'), os.path.abspath('data' + '/' + f'{item["name"]}'))
                time.sleep(3)
                unzip(os.path.abspath('data' + '/' + f'{item["name"]}' + '/assets'), os.path.abspath('data' + '/' + f'{item["name"]}'))
                time.sleep(3)

                self.driver.back()
                self.driver.implicitly_wait(5)


            with open(f'data/{item["name"]}/{item["name"]}.json', 'w', encoding='utf-8') as f:
                json.dump(dictionary, f, indent=4, ensure_ascii=False)

            return dictionary
        except Exception as exc:
            print(f'Что-то не так {exc}')


    def parse_attachments(self):
        try:
            self.driver.find_element(By.ID, 'content-metadata-attachments').click()
            self.driver.implicitly_wait(2)
            try:
                a = self.driver.find_element(By.ID, 'download-all-link')
                b = self.driver.find_element(By.CLASS_NAME, 'filename')
                print(b)
                if a:
                    print(a)
                    a.click()
                elif b:
                    link = b.get_attribute('href')
                    print(link)
                    urllib.request.urlretrieve(link)
            except Exception as exc:
                print(f'Нет ссылки скачать все {exc}')





            #os.path.abspath('data')


            self.driver.implicitly_wait(2)
            self.driver.back()
        except Exception as exc:
            print(f'Нет вложений {exc}')
            return

    def parse_child(self, elem_dict, childs, item):
        counter_elem_in_elem = 0
        counter_id_in_elem = 0
        for i in range(len(childs)):
            self.driver.find_element(By.CLASS_NAME, 'contextual-nav-child-pages').find_elements(By.CLASS_NAME, 'child-item')[i].find_element(By.TAG_NAME, 'a').click()
            time.sleep(2)

            self.driver.find_element(By.ID, 'action-menu-link').click()
            self.driver.implicitly_wait(2)
            exp = self.driver.find_element(By.ID, 'export-to-markdown').click()
            self.driver.implicitly_wait(2)
            self.parse_attachments()
            time.sleep(2)

            for files in glob.glob('data/*.md'):
                counter_elem_in_elem += 1
                counter_id_in_elem += 1
                new_name = f"{elem_dict['path'].split('/')[-1].split('.')[0]}_{str(counter_elem_in_elem).zfill(2)}.md"
                os.rename(files, f"data/{item['name']}/{new_name}")


                elem_in_elem_dict = {}
                elem_in_elem_dict['name'] = str(files).split('.')[0].split('\\')[1]
                elem_in_elem_dict['id'] = counter_id_in_elem
                elem_in_elem_dict['path'] = f'data/{item["name"]}/{new_name}'
                 ##################################


                relocator(os.path.abspath('data'),
                          os.path.abspath('data' + '/' + f'{item["name"]}'))
                time.sleep(4)
                unzip(os.path.abspath('data' + '/' + f'{item["name"]}' + '/assets'),
                      os.path.abspath('data' + '/' + f'{item["name"]}'))
                time.sleep(3)
                try:
                    self.driver.find_element(By.CLASS_NAME,
                                             'ia-splitter').find_element(
                        By.CLASS_NAME,
                        'ia-fixed-sidebar').find_element(
                        By.CLASS_NAME, 'ia-secondary-header-title').find_element(
                        By.CLASS_NAME,
                        'icon').click()
                    child_child_child = self.driver.find_element(By.CLASS_NAME,
                                                                 'contextual-nav-child-pages').find_elements(
                        By.CLASS_NAME, 'child-item')
                    print(child_child_child)
                    if child_child_child:
                        elem_in_elem_dict['pages'] = []
                        child_child_dict = self.parse_child(elem_in_elem_dict, child_child_child, item)
                        elem_in_elem_dict['pages'].append(child_child_dict)
                except Exception as exc:
                    self.driver.back()
                    self.driver.find_element(By.CLASS_NAME, 'ia-splitter').find_element(By.CLASS_NAME,
                                                                                        'ia-fixed-sidebar').find_element(
                        By.CLASS_NAME, 'ia-secondary-header-title').find_element(By.CLASS_NAME, 'icon').click()

                elem_dict['page'].append(elem_in_elem_dict)


            self.driver.back()
            time.sleep(2)
            self.driver.find_element(By.CLASS_NAME, 'ia-splitter').find_element(By.CLASS_NAME, 'ia-fixed-sidebar').find_element(By.CLASS_NAME, 'ia-secondary-header-title').find_element(By.CLASS_NAME, 'icon').click()
            time.sleep(2)
        return elem_dict

