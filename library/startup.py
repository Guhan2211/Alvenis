from flask import Flask
from flask import render_template
import sys


#either or methods----------

#from library.getchannel import obj
from library.alias import obj


#-------------------------

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('start.html')
    
@app.route('/bus_1')

def draw_lines():

    #----------------------------------------------------
                       
    #del sys.modules['library.getchannel']
    #from library.getchannel import obj
                       
    del sys.modules['library.alias']
    from library.alias import obj

    #-------------------------------------------------------
    return render_template('draw_lines.html', coord=obj.lis,lst=obj.lastcord,addr=obj.info,tymapx=obj.tymapx)

         
       
 
        
      
    


