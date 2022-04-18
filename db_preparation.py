import glob
import json
import os
import shutil


def md_replace(directory):
    if not os.path.exists('dataObsidian'):
        os.mkdir('dataObsidian')

    list = os.listdir(directory)
    print(list)
    json_f = glob.glob(os.path.join(directory, '*.json'))[0]
    print(json_f)

    with open(json_f, 'r', encoding='utf-8') as file:
        json_str = file.read()
        dic = json.loads(json_str)
        print(dic)

    files = glob.glob(os.path.join(directory, '*.md'))
    print(files)
    for file in files:
        if file.split('\\')[1] in dic['path']:
            if not os.path.exists(f'dataObsidian/{dic["name"]}'):
                os.mkdir(f'dataObsidian/{dic["name"]}')
            os.rename(file, f'dataObsidian/{dic["name"]}/{dic["name"]}.md')
        else:
            for elem in dic['pages']:
                try:
                    if elem['pages']:

                        for elem_2 in elem['pages']:
                            try:
                                if elem_2['pages']:
                                    for elem_3 in elem_2['pages']:
                                        try:
                                            if elem_3['pages']:
                                                if not os.path.exists(f'dataObsidian/{dic["name"]}/{elem["name"]}/{elem_2["name"]}/{elem_3["name"]}'):
                                                    os.mkdir(f'dataObsidian/{dic["name"]}/{elem["name"]}/{elem_2["name"]}/{elem_3["name"]}')
                                                if file.split('\\')[1] in elem['path']:
                                                    os.rename(file, f'dataObsidian/{dic["name"]}/{elem["name"]}/{elem_2["name"]}/{elem_3["name"]}/{elem_3["name"]}.md')
                                                else:
                                                    c = 0
                                                    for child3 in elem_3['pages']:
                                                        c += 1
                                                        if file.split('\\')[1] in child3['path']:
                                                            os.rename(file,
                                                                      f'dataObsidian/{dic["name"]}/{elem["name"]}/{elem_2["name"]}/{elem_3["name"]}/{str(c).zfill(2)}_{child3["name"]}.md')

                                        except Exception as exc:
                                            print(f"Нет вложений 3ий слой {exc}")
                                            if file.split('\\')[1] in elem_3['path']:
                                                os.rename(file, f'dataObsidian/{dic["name"]}/{elem["name"]}/{elem_2["name"]}/{elem_3["name"]}.md')
                                    if not os.path.exists(
                                            f'dataObsidian/{dic["name"]}/{elem["name"]}/{elem_2["name"]}'):
                                        os.mkdir(f'dataObsidian/{dic["name"]}/{elem["name"]}/{elem_2["name"]}')
                                    if file.split('\\')[1] in elem_2['path']:
                                        os.rename(file,
                                                  f'dataObsidian/{dic["name"]}/{elem["name"]}/{elem_2["name"]}/{elem_2["name"]}.md')
                                    else:
                                        b = 0
                                        for child2 in elem_2['pages']:
                                            b += 1
                                            if file.split('\\')[1] in child2['path']:
                                                os.rename(file,
                                                          f'dataObsidian/{dic["name"]}/{elem["name"]}/{elem_2["name"]}/{str(b).zfill(2)}_{child2["name"]}.md')
                            except Exception as exc:
                                print(f"Нет вложений 2ой слой {exc}")

                        if not os.path.exists(f'dataObsidian/{dic["name"]}/{elem["name"]}'):
                            os.mkdir(f'dataObsidian/{dic["name"]}/{elem["name"]}')
                        if file.split('\\')[1] in elem['path']:
                            os.rename(file, f'dataObsidian/{dic["name"]}/{elem["name"]}/{elem["name"]}.md')
                        else:
                            a = 0
                            for child in elem['pages']:
                                a += 1
                                if file.split('\\')[1] in child['path']:
                                    os.rename(file, f'dataObsidian/{dic["name"]}/{elem["name"]}/{str(a).zfill(2)}_{child["name"]}.md')

                except Exception as exc:
                    print(f"Нет вложений {exc}")
                    if file.split('\\')[1] in elem['path']:
                        os.rename(file, f'dataObsidian/{dic["name"]}/{elem["name"]}.md')
    other_files = glob.glob(os.path.join(directory, '*'))
    print(other_files)
    for ofile in other_files:
        shutil.move(ofile, f'dataObsidian/{dic["name"]}')





if __name__ == '__main__':

    directory = os.listdir('data')
    for item in directory:
        dir = 'data/'+ item
        print(dir)
        md_replace(dir)
