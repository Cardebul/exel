from time import sleep
import os


def valid_data(request):
    project_name = request.POST.get('ProjectName')
    price = request.POST.get('Price')
    start_date = request.POST.get('Start')
    time_period = request.POST.get('time-period')

    item_names = request.POST.getlist('itemName[]')
    item_names1 = request.POST.getlist('itemName1[]')
    item_names2 = request.POST.getlist('itemName2[]')
    item_names3 = request.POST.getlist('itemName3[]')

    data1 = {
            'Имя': project_name,
            'Тариф': price,
            'Дата': start_date,
            'Дни/Недели': time_period,
        }

    data2 = {
            'Этап': item_names,
            'Работы': item_names1,
            'Количество': item_names2,
            'Временной лаг': item_names3,
        }
    data = {'data1': data1, 'data2': data2}
    return data, project_name


def deleter(path):
    try:
        sleep(22)
        os.remove(path)
    except OSError as e:
        print(f'Ошибка удаления файла {path}', e)
    return
