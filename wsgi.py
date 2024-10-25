from app import app 
from app1 import app as app1

if __name__ == '__main__':  
    app.run() 
    app1.run()