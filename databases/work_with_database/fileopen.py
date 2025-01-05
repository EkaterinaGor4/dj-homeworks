def open_file():

    res = []
    for i in open('C:\\Users\\User\\Documents\\GitHub\\dj-homeworks\\databases\\work_with_database\\phones.csv'):
        #print(i)
        ls = i.strip().split(';')
        #ls.pop()
        res.append(ls)
        #print(ls)
    res.pop(0)
    #print(res)
    dic = {}
    for i in res:
        dic[int(i[0])] = {'name': i[1], 'image': i[2], 'price': int(i[3]), 'release_date': i[4], 'lte_exists': i[5]}
    return dic
print(open_file())