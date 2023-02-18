import datetime

def showToScreen(data):
   data = [i.replace('|', '').rstrip('\n') for i in data]
   print()
   for i in range(len(data)):
        print(f"{i+1}) {data[i]}")

def showToScreenABC(data):
   data = [i.rstrip('\n').split('|') for i in data]
   print("Упорядоченный вывод по дате")
   data = sorted(data, key=lambda x: datetime.datetime.strptime(x[2].strip(), '%Y-%m-%d %H:%M:%S'), reverse=True)
   for i in range(len(data)):
        print(f"{i+1}) {data[i][0]} {data[i][1]} {data[i][2]}")

def saveToTXT(data):
    data = [i.replace('|', '') for i in data]
    with open('export.txt', 'w+', encoding='UTF-8') as txt:
        for i in range(len(data)):
            txt.write(f"{i+1}) {data[i]}")
        txt.close()

def saveToHTML(data):
    data = [i.replace('|', '').rstrip('\n') for i in data]
    html = '<html>\n  <head></head>\n  <body style="font-size:14px;">\n'
    for i in range(len(data)):
        html += '<div><p>{}) {}</p></div>\n'.format(i+1, data[i])
    html += ' </body>\n</html>'    
    with open('export.html', 'w', encoding='UTF-8') as page:
        page.write(html)
        page.close()

def saveToXML(data):
    data = [i.replace('|', '').rstrip('\n') for i in data]
    xml = '<xml>\n'
    for i in range(len(data)):
        xml += '<p>{}) {}</p>\n'.format(i+1, data[i])
    xml += '</xml>'
    with open('export.xml', 'w', encoding='UTF-8') as page:
        page.write(xml)
        page.close()

def saveToCSV(data):
    data = [i.replace('|', ';') for i in data]
    with open('export.csv', 'w', encoding='UTF-8-sig') as csv:
        for i in range(len(data)):
            csv.write(f"{i+1}; {data[i]}")
        csv.close()


