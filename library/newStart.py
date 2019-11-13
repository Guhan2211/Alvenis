from flask import Flask
from flask import render_template,abort
import sys

import library.alias as ali
import library.logSession as logs
from flask import *
app=Flask(__name__) 

busList=['22','23','24','26','28','29','30','32']
sessobj=None


@app.route('/',methods=['GET','POST'])


def basic():


    global sessobj
    if(not sessobj):
        if (request.method =='POST'):
            email=request.form['email']
            password=request.form['password']


            sessobj=logs.session(email,password)
            if(sessobj.loggedIn==False):
                auth_check=sessobj.login()
                if (auth_check is None and sessobj.loggedIn):
                    
                    return render_template('start_Nandha.html')
                else:

                    return render_template('homepage.html',us=auth_check)
            else:
                return render_template('start_Nandha.html')  
    elif(sessobj.loggedIn):
        return render_template('start_Nandha.html')

                
    return render_template('homepage.html')

@app.route('/getid')
def getid():
    return render_template('getid.html') 


@app.route('/pswdreset',methods=['GET','POST'])

def pswdreset():
    if (request.method =='POST'):

        email=request.form['email']
        #print(email)
        resetobj=logs.session(email)
        wh=resetobj.pswdreset()
        if(wh=='1'):
            message="password verfication mail has been sent to your mail id!"
            inf="succ"
        else:
            message="EMAIL_NOT_FOUND,RETRY AGAIN!"
            inf="fail"
        print(message,inf)
        return render_template('reset.html',message=message,inf=inf)


    


@app.route('/<busNo>')

def draw_lines(busNo):

    global sessobj
    if busNo not in busList:
        abort(404) 
    print("Reloading occurrs!")
    obj=""
    del sys.modules['library.alias']
    del obj
    import library.alias as ali
    
    obj=ali.data(busNo)
    try:
        obj.initdata()
    except:
        abort(400)
    #-------------------------------------------------------
    #print(busNo)
    if(sessobj):
        if(sessobj.loggedIn):
            return render_template('draw_lines.html', coord=obj.lis,
                                    lst=obj.lastcord,addr=obj.info,tymapx=obj.tymapx)
    else:
        abort(401)


@app.route('/logout')
def logout():
    global sessobj
    #print("Logout")
    #sessobj.loggedIn=False
    sessobj=None
    return redirect(url_for('basic'))
    
@app.route('/info')

def info():
    return render_template('credits.html')

       
    


@app.errorhandler(404)

def not_found(error):
    return render_template('404.html',code="404"), 404                        
 
@app.errorhandler(401)

def not_found(error):
    return render_template('404.html',code="401"), 401                        
  
@app.errorhandler(400)

def not_found(error):
    return render_template('404.html',code="400"), 400                        
 



if __name__ == '__main__':
    app.run()

