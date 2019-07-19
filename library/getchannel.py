import urllib3
import json
from datetime import *
from pytz import timezone
from tzlocal import get_localzone
import certifi
import googlemaps
#import geocoder

class data:

    http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED',ca_certs=certifi.where())
    r = http.request('GET', 'https://api.thingspeak.com/channels/591147/feeds.json?results=100')#results=100,days=1
    dat=json.loads(r.data.decode('utf-8'))
    #print(dat)
    #print(type(dat))
    
    strfeed=dat['feeds']

    no=len(strfeed)

    ty=strfeed[no-1]
    ty=ty['created_at']


    ty=ty[0:10]+ " "+ty[11:19]
    #print(ty)
    dt_obj = datetime.strptime(ty,'%Y-%m-%d %H:%M:%S')

    format = "%Y-%m-%d %H:%M:%S"
    tym=dt_obj.astimezone(timezone('UTC'))
    tym=str(tym)
    tym=tym[:-6]
    #print(tym)





    #print(no)
    chlis=[]
    for i in range(0,no):
        ch=strfeed[i]
        ch=(ch['field1'],ch['field2'])
        if ch==None:
            pass
        else:
            chlis.append(ch)

    noentry=dat['channel']['last_entry_id']
    #print(noentry)
    #print(chlis)
    #print("lat:",chlis[0][0])
    #print("lng:",chlis[0][1])

    #----------------list to str-----------------------------------------
    stri="["
    for i in range (0,noentry):
        stri=stri+"{"
        stri=stri+"lat:%s,lng:%s"%(chlis[i][0],chlis[i][1])
        stri=stri+"},"
    stri=stri[:-1]
    stri=stri+"]"
    #print(stri)
    #--------------------identfying last cord pos----------------------
    z=0
    for i in range (0,len(stri)):
        if stri[i]=="}" and stri[i+1]=="]":
            z=i
    #print(z)
    s=0
    s=z
    while stri[s]!="{":
        s=s-1

    #print(s,"s")

    las=stri[s:z+1]
    #print(las)

    #----------------lastcrd in tuple------------------------

    #{lat:13.056062,lng:81.046547}

    latpass=float(las[5:14])
    lngpass=float(las[-10:-1])
    fradd=(latpass,lngpass)
    #print(fradd,str(datetime.now()))




    lis=stri
    lastcord=las

    gmaps = googlemaps.Client(key='AIzaSyCBomZqjzkNGH8jWT4ULH8R25NuluqhjUY')


    reverse =gmaps.reverse_geocode(fradd)
    li=reverse
    #print(li)
    #fr1=li[2]
    fr1=li[1]
    #print(fr1)
    fr1=fr1['formatted_address']

    info=tym+" "+fr1



    print(info)


obj=data()        
        
