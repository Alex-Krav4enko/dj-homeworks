from django.shortcuts import render

from csv import reader

inflation_list = None

with open('inflation_russia.csv', 'r', encoding='utf-8') as csv_file:
    inflation_list = list(reader(csv_file))

head_item_list = inflation_list.pop(0)[0].split(';')
body_item_list = [year[0].split(';') for year in inflation_list]


def inflation_view(request):
    template_name = 'inflation.html'

    # чтение csv-файла и заполнение контекста
    context = {
        'head': head_item_list,
        'body': body_item_list
    }

    return render(request, template_name,
                  context)
