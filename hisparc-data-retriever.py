import urllib.request

def get_server_locations():
    ''' Returns All The HiSPARC Server Names With Their Corresponding Numbers'''
    
    try:
        response = urllib.request.urlopen('http://data.hisparc.nl/data/download/') # Downloads html of the hisparc data download page
    except urllib.error.HTTPError:
        return False
    
    html = str(response.read()).split('\\n')

    locations={}

    try:
        for i in html:                                          # Removes unnecessary data and keeps the location data. Puts it in a dictionary.
            if '<option' in i:
                loc = i.replace('<','>').split('>')[2]
                if len(loc.split(':')) < 2:
                       pass
                else:
                       locations[loc.split(':')[0]] = loc.split(':')[1]
        return locations
    
    except: # Hehe
        return False


if __name__ == '__main__':
    server_locations = get_server_locations()
    print(server_locations)

'''
Ignore This Stuff

print(locations)

for i in locations:
    print(i,locations[i])
    


response = urllib.request.urlopen('http://data.hisparc.nl/show/source/eventtime/4/2018/1/24/')
html = response.read()
print('%s%s%s' % ('a','b','c'))
'''
