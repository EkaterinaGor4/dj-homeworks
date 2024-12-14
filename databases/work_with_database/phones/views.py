from django.shortcuts import render

d = {'1': {'name': 'Samsung Galaxy Edge 2',
         'image': 'https://avatars.mds.yandex.net/get-mpic/364668/img_id5636027222104023144.jpeg/orig',
         'price': 73000,
         'release_date': '2016-12-12',
         'lte_exists': 'True'},
     '2': {'name': 'Iphone X',
         'image': 'https://avatars.mds.yandex.net/get-mpic/200316/img_id270362589725797013.png/orig',
         'price': 80000,
         'release_date': '2017-06-01',
         'lte_exists': 'True'},
     '3': {'name': 'Nokia 8',
         'image': 'https://avatars.mds.yandex.net/get-mpic/397397/img_id6752445806321208103.jpeg/orig',
         'price': 20000,
         'release_date': '2013-01-20',
         'lte_exists': 'False'}}


def open_file():
    res = []
    for i in open('C:\\Users\\User\\Documents\\GitHub\\dj-homeworks\\databases\\work_with_database\\phones.csv'):
        # print(i)
        ls = i.strip().split(';')
        # ls.pop()
        res.append(ls)
        # print(ls)
    res.pop(0)
    # print(res)
    dic = {}
    for i in res:
        dic[int(i[0])] = {'name': i[1], 'image': i[2], 'price': int(i[3]), 'release_date': i[4], 'lte_exists': i[5]}
    return dic

def show_catalog(request):
    template = 'catalog.html'

    context = {'data': d.values()}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    context = {}
    return render(request, template, context)
