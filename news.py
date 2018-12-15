from datetime import datetime
import xlrd
import xlwt
import jieba
data = xlrd.open_workbook(r'./shiyansi.xls')
news = data.sheet_by_name('news')
comment1 = data.sheet_by_name('1')
comment2 = data.sheet_by_name('2')
comment3 = data.sheet_by_name('3')
comment4 = data.sheet_by_name('4')
wenben = news.col_values(1)
source_date = news.col_values(2)
source_list = []
date_list = []
for i in range(1,7):
    a = source_date[i].split(' ')
    source_list.append(a[0])
    date_list.append(a[1]+' '+a[2])
def create_news(m,comment1):
    # m:xinwenbianhao comment1:pinglunbiao
    news1 = dict.fromkeys(['title', 'date', 'source', 'comment'])
    news1['comment'] = []
    news1['title'] = wenben[m]
    news1['date'] = date_list[m-1]
    news1['source'] = source_list[m-1]
    if m >4:
      return news1
    else:
        for i in range(1, comment1.nrows):
            keys = ['user', 'area', 'date', 'content']
            u = comment1.row_values(i)
            del u[0]
            u[2] += ':00'
            c = jieba.lcut(u[1])
            u[1] = c[1]
            a = dict(zip(keys, u))
            news1['comment'].append(a)
        return news1
news1 = create_news(1,comment1)
news2 = create_news(2,comment2)
news3 = create_news(3,comment3)
news4 = create_news(4,comment4)
news5 = create_news(5,comment4)
news6 = create_news(6,comment4)
d1 = datetime.strptime(news1['date'],'%Y-%m-%d %H:%M:%S')
d2 = datetime.strptime(news2['date'],'%Y-%m-%d %H:%M:%S')
d3 = datetime.strptime(news3['date'],'%Y-%m-%d %H:%M:%S')
d4 = datetime.strptime(news4['date'],'%Y-%m-%d %H:%M:%S')
d5 = datetime.strptime(news5['date'],'%Y-%m-%d %H:%M:%S')
d6 = datetime.strptime(news6['date'],'%Y-%m-%d %H:%M:%S')
news_list = list(zip([news1,news2,news3,news4,news5,news6],[d1,d2,d3,d4,d5,d6]))
print(type(news_list[1][1]))
def sort_days(d):
    #d is a time list
    a = d.copy()
    for j in range(len(a)):
        for i in range(len(a)):
            delta = a[j][1] - a[i][1]
            if delta.days >0:
                a[j],a[i] = a[i],a[j]
    return a
a = sort_days(news_list)
f = open('./news.txt','w')
for i in range(len(a)):
    f.write(str(a[i][0]))









