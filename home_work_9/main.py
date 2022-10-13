# --------- Simple database about countries --------- #

import json
from uuid import uuid4


def add_group_list_by_uid(main_data: dict, second_list: dict, group: str):
    """
        Функция группировки по введенной группе для записи в файл. ПараметрыЖ
        --- main_data : словарь, список данных из главного JSON файла
        --- second_list: словарь, в который будут записаны/находятся сгрупированные данные из main_data
        --- group : строка, название групы из main_data

        return : список с сгрупированными данными
    """

    if main_data[group] in part_of_the_world_index:
        second_list[country_data[group]].append(main_data['UID'])
    else:
        second_list[main_data[group]] = list()
        second_list[main_data[group]].append(main_data['UID'])
    return second_list


if __name__ == "__main__":

    part_of_the_world_json = "part_of_the_world.json"
    language_json = "language.json"
    countries_json = "countries.json"

    with open(countries_json) as CJ:
        load_data = json.load(CJ)

        uid_index = dict()
        part_of_the_world_index = dict()
        language_index = dict()

        for country_data in load_data["country"]:
            country_data['UID'] = str(uuid4())

            uid_index[country_data['UID']] = country_data

            part_of_the_world_index = add_group_list_by_uid(country_data, part_of_the_world_index, 'part_of_the_world')

            language_index = add_group_list_by_uid(country_data, language_index, 'language')

    # Запись UID в главный файл и запись сгрупированных данных
    json.dump({'country': list(uid_index.values())}, open(countries_json, 'w'), indent=4)
    json.dump(part_of_the_world_index, open(part_of_the_world_json, 'w'), indent=4)
    json.dump(language_index, open(language_json, 'w'), indent=4)

    print('Done')
