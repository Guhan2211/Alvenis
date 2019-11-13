import urllib.request
from datetime import datetime
from pytz import timezone
import googlemaps
import ast

class data:

    #req = urllib.request.Request('https://api.thingspeak.com/channels/591147/feeds.json?results=100')  #guhan
    req = urllib.request.Request('https://api.thingspeak.com/channels/600627/feeds.json?minutes=180')   #manoj  results=100,minutes=180
    with urllib.request.urlopen(req) as response:
        the_page = response.read()

    x=str(the_page)
    x=x[2:-1]
    text_dic = ast.literal_eval(x)

    dat=text_dic

    strfeed=dat['feeds']

    no=len(strfeed)
    #print(no)
    if(no!=0):
        ty=strfeed[no-1]
        ty=ty['created_at']

        firstentryid=dat['feeds'][0]['entry_id']
        lastentryid=dat['feeds'][no-1]['entry_id']
        #print(firstentryid,lastentryid)
        entrycount=(lastentryid-firstentryid)+1


        #print(entrycount)
        #print(no)
        #print(ty)


        ty=ty[0:10]+ " "+ty[11:19]
        #print(ty)
        dt_obj = datetime.strptime(ty,'%Y-%m-%d %H:%M:%S')
        #print(str(dt_obj))
        format = "%Y-%m-%d %H:%M:%S"
        tym=dt_obj.astimezone(timezone('Asia/Calcutta'))
        #tym=dt_obj.astimezone(timezone('UTC'))


        #xyzd=tym+timedelta(hours=11)

        tym=str(tym)
        tym=tym[:-6]
        #print(tym)


        #-----------------------------------------------------------------
        #-----------------multimarker----------------------------------------

        tymapx=[]


        if(no==1):
            tymx=strfeed[0]['created_at']

            tymx=tymx[0:10]+ " "+tymx[11:19]
            dt_obj = datetime.strptime(tymx,'%Y-%m-%d %H:%M:%S')
            format = "%Y-%m-%d %H:%M:%S"
            tym=dt_obj.astimezone(timezone('Asia/Calcutta'))
            tym=str(tym)
            #tymx=tymx[:-6]
            tymapx.append(tymx)

        else:
            for ix in range(0,no-1):
                tymx=strfeed[ix]['created_at']

                tymx=tymx[0:10]+ " "+tymx[11:19]
                dt_obj = datetime.strptime(tymx,'%Y-%m-%d %H:%M:%S')
                format = "%Y-%m-%d %H:%M:%S"
                tym=dt_obj.astimezone(timezone('Asia/Calcutta'))
                tym=str(tym)
                #tymx=tymx[:-6]
                tymapx.append(tymx)

            #print(tymapx)




        #--------------------------------------------------------------------


        #print(no)
        chlis=[]
        for i in range(0,entrycount):#changes.........no........
            ch=strfeed[i]
            ch=(ch['field1'],ch['field2'])
            if ch==None:
                pass
            else:
                chlis.append(ch)

        noentry=dat['channel']['last_entry_id']
        #print(noentry,"noentry")
        #print(entrycount,"entrycount")
    ##    print(chlis,"chlis")
    ##    print("lat:",chlis[0][0])
    ##    print("lng:",chlis[0][1])

        #----------------list to str-----------------------------------------
        stri="["
        for i in range (0,entrycount):#noentry...changes
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
        #print(latpass,lngpass)
        #print(fradd)




        lis=stri
        lastcord=las

        gmaps = googlemaps.Client(key='AIzaSyCBomZqjzkNGH8jWT4ULH8R25NuluqhjUY')


        reverse =gmaps.reverse_geocode(fradd)
        li=reverse

        fr1=li[2]
        fr1=fr1['formatted_address']

        info=tym+" "+fr1



        #print(info)
    else:



        lis="[{lat:11.061960,lng:77.037069}]"
        lastcord="{lat:11.061960,lng:77.037069}"
        info="Not started"


obj=data()



