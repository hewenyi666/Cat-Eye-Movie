import requests
from bs4 import BeautifulSoup
import xlsxwriter
def get_score(soup):#获取电影评分
    score1=[]
    score2=[]
    score = []  # 存放评分
    score_1 = soup.find_all(class_='integer')  # 获取评分前半部分
    score_2 = soup.find_all(class_='fraction')  # 获取后半部分
    for b in score_1:
        score1.append(b.string)
    for c in score_2:
        score2.append(c.string)
    for r in range(len(score_1)):
        score.append(score1[r] + score2[r])
    return score
def get_releasetime(soup):#获取上映时间
    releasetime=[]
    time = soup.find_all(class_='releasetime')  # 获取上映时间
    for cc in time:
        releasetime.append(cc.string)
    return releasetime
def get_actor_name(soup):#获取演员名称
    actor_name=[]
    actor = soup.find_all(class_='star')  # 获取演员名字
    for bb in actor:
        actor_name.append(bb.string)
    return actor_name
def get_file_name(soup):#获取电影名称
    file_name=[]
    name = soup.find_all(class_='name')  # 获取电影名称
    for aa in name:
        file_name.append(aa.string)
    return file_name
def save_to_excel(file_name,actor_name,releasetime,score):#保存数据至Excel中
    workbook = xlsxwriter.Workbook("F:\\maoyan.xlsx")
    worksheet = workbook.add_worksheet('爬取的数据')
    head = ['排名', '电影名称', '演员', '上映时间', '评分']
    worksheet.write_row('A1', head)
    num = []
    for yy in range(100):
        num.append(yy + 1)
    worksheet.write_column('A2', num)
    worksheet.write_column('B2', file_name)
    worksheet.write_column('C2', actor_name)
    worksheet.write_column('D2', releasetime)
    worksheet.write_column('E2', score)
    workbook.close()
if __name__=='__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
    i = 0
    score3=[]
    time=[]
    actor=[]
    file=[]
    for a in range(10):
        url = 'https://maoyan.com/board/4?offset=' + str(i)
        i = i + 10
        r = requests.get(url, headers=headers)
        html = r.text
        soup = BeautifulSoup(html, 'html.parser')
        score3+=get_score(soup)
        time+=get_releasetime(soup)
        actor+=get_actor_name(soup)
        file+=get_file_name(soup)
    save_to_excel(file, actor, time, score3)
    print('OK!')
