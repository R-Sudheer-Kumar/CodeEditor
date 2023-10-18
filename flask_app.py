import os
import subprocess
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('abc.html')

@app.route('/checkf' , methods=["POST"])  
def check():
    if request.method=='POST':
        filepath='static/'

        a = request.form['code'] 
        # if not os.path.exists(filepath+'try.c'):
        #     os.open(filepath+'try.c',os.O_CREAT)

        # fd = os.open(filepath+"try.c",os.O_WRONLY)   
        # fileadd = str.encode(str(a))
        # os.write(fd,fileadd)
        # os.close(fd)
        
        # s = subprocess.run(['gcc' , '-o',filepath+'new',filepath+'try.c'] )
        # r = subprocess.run([filepath+'new.exe'] , stdout=subprocess.PIPE) 
        # output = r.stdout.decode('utf-8')
        # return output

        if not os.path.exists(filepath+'ty.py'):
            os.open(filepath+'ty.py',os.O_CREAT)

        fd = os.open(filepath+'ty.py' , os.O_WRONLY)
        os.truncate(fd,0)
        fileadd = str.encode(str(a))
        os.write(fd,fileadd)
        os.close(fd)
        i =os.open(filepath+'test1.txt' , os.O_RDONLY)
        ib = os.read(i,100)
        print(ib)
        s = subprocess.run(['python',filepath+'ty.py'],input=ib,stdout=subprocess.PIPE)
        # r=subprocess.run([filepath+'ty.py'])
        # output = s.stdout.decode("utf-8")
        os.close(i)
        return s.stdout.decode("utf-8")
if __name__ == '__main__':
    app.run(debug=True)
