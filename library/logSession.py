import pyrebase
     
config={
    "apiKey": "AIzaSyApM-4zT2QXArZpjtr3tlTQtUAjiDM_ql0",
    "authDomain": "result-analysis-27931.firebaseapp.com",
    "databaseURL":" https://result-analysis-27931.firebaseio.com",
    "projectId": "result-analysis-27931",
    "storageBucket": "result-analysis-27931.appspot.com",
    "messagingSenderId": "55363811459"
}

firebase = pyrebase.initialize_app(config)
auth=firebase.auth()


class session:

    def __init__(self,email="",password=""):
        #print(busNo,"init")  
        self.loggedIn = False
        self.err=""
        self.email=email
        self.password=password

    def pswdreset(self):
        global auth
        try:
            x=auth.send_password_reset_email(self.email)
            return '1'
        except Exception as x:
            
            return "0"
            




    def login(self):
        global auth
        try:
            ec=auth.sign_in_with_email_and_password(self.email,self.password)
            self.loggedIn=True
            #print(ec)
        except Exception as ex:
            
        # except Exception as ex:
        
           xyz=str(ex)
           #print('xyz',xyz)
           messpos=xyz.find('message')
           #print(messpos,'messpos')
           xyz2=xyz[messpos:]
           errpos=xyz2.find(',')
           #print(errpos,'errpos')
           errpos=errpos+messpos
           #print('$'+xyz[messpos+11:errpos-1]+'$')
           errmsg=xyz[messpos+11:errpos-1]
           self.err=errmsg
           #print(errmsg)
           if(len(self.err)>15):
               self.err="PASSWORD_INCORRECT"
           return self.err
            


#obj=session("mailmeguhan98@gmail.cm","990190")
#msg=obj.login()
#print(msg,type(msg))


     
