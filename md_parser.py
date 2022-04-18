import glob

from vars import dict
import re
import os

def replace_from_imgs(item):

    list = os.listdir(f'data/{item["name"]}')
    #print(list)
    for file_md in glob.glob(f'data/{item["name"]}/*.md'):
        print(file_md)
        if os.path.isfile(file_md):
            #print(file_md)

            with open(f'{file_md}', 'r', encoding='utf-8') as md_file:
                textFromMd = md_file.read()
                s = re.findall(r"\!\[\]\(.+?\)", textFromMd)
                #print(s)
                for i in s:
                    for file in os.listdir(f'data/{item["name"]}/assets/imgs'):
                        #print(file)
                        if file in i:
                            if file != '':
                                path = f'assets/imgs/{file}'
                                print(path)
                                textFromMd = textFromMd.replace(i, f"![]({path})")
                    #if i in textFromMd:
                    #    textFromMd = textFromMd.replace(i, f"")

            with open(f'{file_md}', 'w', encoding='utf-8') as f:
                f.write(textFromMd)


def replace_from_imgs2(item):

    list = os.listdir(f'data/{item["name"]}')
    #print(list)
    for file_md in glob.glob(f'data/{item["name"]}/*.md'):
        print(file_md)
        if os.path.isfile(file_md):
            #print(file_md)

            with open(f'{file_md}', 'r', encoding='utf-8') as md_file:
                textFromMd = md_file.read()
                s = re.findall(r"\[\!\[\]\(.+?\)]\(.+?\)", textFromMd)
                #print(s)
                for i in s:
                    for file in os.listdir(f'data/{item["name"]}/assets/imgs'):
                        #print(file)
                        if file in i:
                            path = f'assets/imgs/{file}'
                            print(path)
                            textFromMd = textFromMd.replace(i, f"![]({path})")
                    #if i in textFromMd:
                    #    textFromMd = textFromMd.replace(i, f"")

            with open(f'{file_md}', 'w', encoding='utf-8') as f:
                f.write(textFromMd)

def replace_from_assets(item):

     list = os.listdir(f'data/{item["name"]}')
     #print(list)
     for file_md in glob.glob(f'data/{item["name"]}/*.md'):
         print(file_md)
         if os.path.isfile(file_md):
             #print(file_md)

             with open(f'{file_md}', 'r', encoding='utf-8') as md_file:
                 textFromMd = md_file.read()
                 s = re.findall(r"\[.+?]\(.+?\)", textFromMd)
                 #print(s)
                 for i in s:
                     list_dir = os.listdir(f'data/{item["name"]}/assets')
                     list_dir.remove('imgs')
                     for file in list_dir:
                         if os.path.isdir(file):
                            print(file)
                         else:
                            if file in i:
                                path = f'assets/{file}'
                                print(path)
                                textFromMd = textFromMd.replace(i, f"![]({path})")


             with open(f'{file_md}', 'w', encoding='utf-8') as f:
                 f.write(textFromMd)

def remove_others(item):
    list = os.listdir(f'data/{item["name"]}')
    print(list)
    for file_md in glob.glob(f'data/{item["name"]}/*.md'):
        print(file_md)
        if os.path.isfile(file_md):
            print(file_md)
            with open(f'{file_md}', 'r', encoding='utf-8') as md_file:
                textFromMd = md_file.read()
                s = re.findall(r"\!\[\]\(.plugins.+?\)", textFromMd)
                print(s)
                for i in s:
                    textFromMd = textFromMd.replace(i, "")

            with open(f'{file_md}', 'w', encoding='utf-8') as f:
                f.write(textFromMd)

def remove_others2(item):
    list = os.listdir(f'data/{item["name"]}')
    print(list)
    for file_md in glob.glob(f'data/{item["name"]}/*.md'):
        print(file_md)
        if os.path.isfile(file_md):
            print(file_md)
            with open(f'{file_md}', 'r', encoding='utf-8') as md_file:
                textFromMd = md_file.read()
                s = re.findall(r"\[.+?]\(http:\/\/85.93.+?\)", textFromMd)
                print(s)
                for i in s:
                    textFromMd = textFromMd.replace(i, "")

            with open(f'{file_md}', 'w', encoding='utf-8') as f:
                f.write(textFromMd)

def remove_others3(item):
    list = os.listdir(f'data/{item["name"]}')
    print(list)
    for file_md in glob.glob(f'data/{item["name"]}/*.md'):
        print(file_md)
        if os.path.isfile(file_md):
            print(file_md)
            with open(f'{file_md}', 'r', encoding='utf-8') as md_file:
                textFromMd = md_file.read()
                s = re.findall(r"\[.+?]\(\/pages.+?\)", textFromMd)
                print(s)
                for i in s:
                    textFromMd = textFromMd.replace(i, "")

            with open(f'{file_md}', 'w', encoding='utf-8') as f:
                f.write(textFromMd)

def remove_others4(item):
    list = os.listdir(f'data/{item["name"]}')
    print(list)
    for file_md in glob.glob(f'data/{item["name"]}/*.md'):
        print(file_md)
        if os.path.isfile(file_md):
            print(file_md)
            with open(f'{file_md}', 'r', encoding='utf-8') as md_file:
                textFromMd = md_file.read()
                s = re.findall(r"\[.+?]\(\/display.+?\)", textFromMd)
                print(s)
                for i in s:
                    textFromMd = textFromMd.replace(i, "")

            with open(f'{file_md}', 'w', encoding='utf-8') as f:
                f.write(textFromMd)
def remove_others5(item):
    list = os.listdir(f'data/{item["name"]}')
    print(list)
    for file_md in glob.glob(f'data/{item["name"]}/*.md'):
        print(file_md)
        if os.path.isfile(file_md):
            print(file_md)
            with open(f'{file_md}', 'r', encoding='utf-8') as md_file:
                textFromMd = md_file.read()
                s = re.findall(r".+\[.+?]\(\/viewpage.+?\)", textFromMd)
                print(s)
                for i in s:
                    textFromMd = textFromMd.replace(i, "")

            with open(f'{file_md}', 'w', encoding='utf-8') as f:
                f.write(textFromMd)

def remove_others6(item):
    list = os.listdir(f'data/{item["name"]}')
    print(list)
    for file_md in glob.glob(f'data/{item["name"]}/*.md'):
        print(file_md)
        if os.path.isfile(file_md):
            print(file_md)
            with open(f'{file_md}', 'r', encoding='utf-8') as md_file:
                textFromMd = md_file.read()
                s = re.findall(r"!\[.+?]\(\/s.+?\)", textFromMd)
                print(s)
                for i in s:
                    textFromMd = textFromMd.replace(i, "")

            with open(f'{file_md}', 'w', encoding='utf-8') as f:
                f.write(textFromMd)

def remove_others7(item):
    list = os.listdir(f'data/{item["name"]}')
    print(list)
    for file_md in glob.glob(f'data/{item["name"]}/*.md'):
        print(file_md)
        if os.path.isfile(file_md):
            print(file_md)
            with open(f'{file_md}', 'r', encoding='utf-8') as md_file:
                textFromMd = md_file.read()
                s = re.findall(r"\[.+?]\(\/plugins.+?\)", textFromMd)
                print(s)
                for i in s:
                    textFromMd = textFromMd.replace(i, "")

            with open(f'{file_md}', 'w', encoding='utf-8') as f:
                f.write(textFromMd)

#\[\!\[\]\(.+?\)](.+)
if __name__ == '__main__':
    counter = 0
    for item in dict['spaces']:
        counter += 1
        if counter > 17:
            break
        #replace_from_imgs2(item)
        replace_from_imgs(item)
        replace_from_assets(item)
        remove_others(item)
        remove_others2(item)
        remove_others3(item)
        remove_others4(item)
        remove_others5(item)
        remove_others6(item)
        remove_others7(item)