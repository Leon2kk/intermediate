import datetime

def getTimeNow():
    return datetime.datetime.strptime(datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S"),"%Y-%m-%d %H:%M:%S") 

def add(head, body):
    with open('data.txt', 'a+', encoding='UTF-8') as file:
        file.write(f'{head} | {body} | {getTimeNow()}\n')

def readAll(showfile = 'data.txt'):
    with open(showfile, 'r', encoding='UTF-8') as file:
        lines = file.readlines()
        file.close()
        return lines 

def edit(head, body, index):
    data = readAll()
    data[int(index)-1] = f'{head} | {body} | {getTimeNow()}\n'
    with open('data.txt', 'w+', encoding='UTF-8') as txt:
        for i in range(len(data)):
            txt.write(f"{data[i]}")
        txt.close()
   
        