import urllib3
import json
http = urllib3.PoolManager()
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
r = http.request('GET', 'https://api.thingspeak.com/channels/591147/fields/2.json?days=1')
dat=json.loads(r.data.decode('utf-8'))
print(dat)
strfeed=dat['feeds']
no=len(strfeed)
print(no)
lnglis=[]
for i in range(0,no):
    lng=strfeed[i]
    lng=lng['field2']
    if lng==None:
        pass
    else:
        lnglis.append(lng)

print(lnglis)
    
