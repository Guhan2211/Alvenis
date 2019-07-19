import urllib3
import json
http = urllib3.PoolManager()
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
r = http.request('GET', 'https://api.thingspeak.com/channels/591147/fields/1.json?days=1')
dat=json.loads(r.data.decode('utf-8'))
print(dat)
strfeed=dat['feeds']
no=len(strfeed)
latilis=[]
for i in range(0,no):
    lati=strfeed[i]
    lati=lati['field1']
    if lati==None:
        pass
    else:
        latilis.append(lati)

print(latilis)
    
