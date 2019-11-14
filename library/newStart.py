from flask import *
import sys
import os

import library.alias as ali
import library.logSession as logs

app=Flask(__name__) 
app.secret_key=os.urandom(24)
busList=['22','23','24','26','28','29','30','32']
active_users=[]


@app.route('/',methods=['GET','POST'])


def basic():
    global active_users
    if not g.user:
        if (request.method =='POST'):
            session.pop ('user',None)
            email=request.form['email']
            
            password=request.form['password']


            sessobj=logs.session(email,password)
            
            auth_check=sessobj.login()
            if (auth_check is None and sessobj.loggedIn):
                session['user']=email
                active_users.append(email)
                return redirect(url_for('select')) 
            else:
                return render_template('homepage.html',us=auth_check)
        

        return render_template('homepage.html')
    else:
        return redirect(url_for('select')) 
        

@app.route('/getUsers')
def getUsers():
    global active_users
    if g.user:
        return render_template("getUsers.html",active_users=active_users,length=len(active_users)) 





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


@app.route('/select')
def select():
    if g.user:
        return render_template('start_Nandha.html')   


@app.route('/<busNo>')

def draw_lines(busNo):


    #-------------------------------------------------------
    #print(busNo)
    if g.user:
    
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
        
        return render_template('draw_lines.html', coord=obj.lis,
                                lst=obj.lastcord,addr=obj.info,tymapx=obj.tymapx)
    else:
        abort(401)



@app.before_request
def before_request():
    g.user=None
    if 'user' in session:
        g.user=session['user']


@app.route('/logout')
def logout():
    global active_users
    print(g.user,type(g.user))
    active_users.remove(g.user)
    session.pop('user',None)
   

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

