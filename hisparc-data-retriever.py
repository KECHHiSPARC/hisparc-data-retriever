import urllib.request

response = urllib.request.urlopen('http://data.hisparc.nl/data/download/')
html = str(response.read()).split('\\n')

#print(html)

locations={}

for i in html:
    if '<option' in i:
        loc = i.replace('<','>').split('>')[2]
        if len(loc.split(':')) < 2:
               pass
        else:
               locations[loc.split(':')[0]] = loc.split(':')[1]
print(locations)

for i in locations:
    print(i,locations[i])
    

'''
response = urllib.request.urlopen('http://data.hisparc.nl/show/source/eventtime/4/2018/1/24/')
html = response.read()
print('%s%s%s' % ('a','b','c'))
'''
