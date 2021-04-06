from flask import Flask,render_template,request,session
from sqlalchemy import create_engine
from flask_session import Session
import sqlalchemy
from sqlalchemy import create_engine
engine = sqlalchemy.create_engine('postgresql://bythxcskwmhcdl:597c29264c730f03283d5765f10a263b343e643e4626371b87faa8dff29019ba@ec2-34-225-103-117.compute-1.amazonaws.com:5432/d8fc0jk561kh8p')
db=engine.connect()

app=Flask(__name__,template_folder='sign_up')
value=False
value1=False
value2=False
value3=False
message=0
f_name=' '
m_name=' '
l_name=' '
username=' '
password=' '
r_password=' '
sex=' '
country=' '
city=' '
pincode=' '
message=' '
biap=" "
biap1=" "

global name
global books
books=[]
app1=Flask(__name__,template_folder="sign_up")
app1.config["SESSION_PERMANENT"]=False
app1.config["SESSION_TYPE"]="filesystem"
Session(app1)

@app1.route("/")

def sign_up():
    session["values"]=[]
    session["values"].append(False)
    session["values"].append(False)
     
    return render_template("index.html")
@app1.route("/log")
def log():
    
   
    print("values",session["values"])
    return render_template("logout.html")
@app1.route("/servicesout1")
def servicesout1():
    return render_template("servicesout1.html")
@app1.route("/contactout")
def contactout():
    return render_template("contactout.html")            
@app1.route("/login1")
def login1():
    return render_template('login.html')
@app1.route("/sign_up1")
def sign_up1():
    return render_template('sign_up.html')        
@app1.route("/index1")
def index1():
    session["values"]=[]
    session["values"].append(False)
    session["values"].append(False)
    return render_template("index.html")    
@app1.route("/team1")
def team1():
    return render_template("team.html")
@app1.route("/services1")
def services1():
    return render_template("services.html")      
@app1.route("/contact1")
def contact1():
    return render_template("contact.html")
@app1.route("/logout")
def logout():
    print("logout")
    return render_template("index.html")   
@app1.route('/datacheck',methods=["POST","GET"])
def datacheck():
    
    last=' '
    username=' '
    password=' '
    if request.method=="POST":
        username=request.form.get('username')
        password=request.form.get('password')
        print(username+" "+password)
        last=db.execute('Select'+' "user_id","password"'+ ' from "readers"')
    for i in last:
        value=False
        value1=False
        if username==i.user_id:
            
            value=True
        if password==i.password:
            
            value1=True
        if value==True and value1==True:
            break
    

    session["values"][0]=value
    session["values"][1]=value1

    print(value,value1)
    if value==True and value1==True:
        return render_template("logout.html")
    else:
        value2=False
        value3=False
        last=db.execute('Select'+' "user_id","password"'+ ' from "readers"')
        for i in last:
            if username==i.user_id:
                value2=True
                break
        last=db.execute('Select'+' "user_id","password"'+ ' from "readers"')    
        for i in last:
           if password==i.password:
                value3=True
                break
        print(value2,value3)
        if value2==False and value3==True:
            message=1
            return render_template("login.html",message=message)
        elif (value2==True and value3==False) or (value1==True and value==True):
            message=2
            return render_template("login.html",message=message)
        elif value2==False and value3==False:
            message=3
            return render_template("login.html",message=message)
        else:
            message=0
            return render_template("login.html",message=message)
@app1.route("/datastore1",methods=["POST","GET"])


def datastore1():
    if request.method=="POST":
        f_name=request.form.get("f_name")
        m_name=request.form.get("m_name")
        l_name=request.form.get("l_name")
        username=request.form.get("username")
        password=request.form.get("password")
        r_password=request.form.get("r_password")
        sex=request.form.get("option")
        country=request.form.get("country")
        city=request.form.get("city")
        pincode=request.form.get("pincode")
    if r_password==password:
        db.execute("insert into"+' "readers"('+'"first_name","middle_name","last_name","sex","user_id","password","country","city","pincode") '+f"values('{f_name}','{m_name}','{l_name}','{sex}','{username}','{password}','{country}','{city}','{pincode}')")
        return render_template('login.html')
@app1.route("/ec")
def ec():
    if(session["values"][0]==True and session["values"][1]==True):
        return render_template("entreprenuership_course.html")
    else:
        return render_template("index.html")     
@app1.route("/courses")
def courses():
    if(session["values"][0]==True and session["values"][1]==True):
        print("in",session["values"][0]==True)
        return render_template("courses.html")
    else:
        return render_template("index.html")      

@app1.route("/ai")
def ai():
    if(session["values"][0]==True and session["values"][1]==True):
        return render_template("AI & ML course.html")
    else:
        return render_template("index.html")      
@app1.route("/data")
def data():
    if(session["values"][0]==True and session["values"][1]==True):
        return render_template("Data Science Course.html")
    else:
        return render_template("index.html")      
@app1.route("/stack")
def stack():
    if(session["values"][0]==True and session["values"][1]==True):
        return render_template("Full Stack Developer Course.html")
    else:
        return render_template("index.html")      
@app1.route("/buisness")
def buisness():
    if(session["values"][0]==True and session["values"][1]==True):
        return render_template("Business Management_course.html")
    else:
        return render_template("index.html")                                      

@app1.route("/account")
def account():
    if(session["values"][0]==True and session["values"][1]==True):
        return render_template("Management Accounting_course.html")
    else:
        return render_template("index.html")      

@app1.route("/soft")
def soft():
    if(session["values"][0]==True and session["values"][1]==True):
        return render_template("Soft Skills Course.html")
    else:
        return render_template("index.html")      

@app1.route("/deduct")
def deduct():
    if(session["values"][0]==True and session["values"][1]==True):
        return render_template("Deductive Logic Course.html")
    else:
        return render_template("index.html")      

@app1.route("/admin")
def admin():
    if(session["values"][0]==True and session["values"][1]==True):
        return render_template("Constitution of India and Environmental Governance_Course.html")
    else:
        return render_template("index.html")      

@app1.route("/finan")
def finan():
    if(session["values"][0]==True and session["values"][1]==True):
        return render_template("Financial Accounting_course.html")
    else:
        return render_template("index.html")      

@app1.route("/stock")
def stock():
    if(session["values"][0]==True and session["values"][1]==True):
        return render_template("Stock Market_course.html")
    else:
        return render_template("index.html")      

@app1.route("/quant")
def quant():
    if(session["values"][0]==True and session["values"][1]==True):
        return render_template("Quantitive Finance_course.html")
    else:
        return render_template("index.html")      

 
if __name__=="__main__":
    app1.debug=True
    app1.run(host="127.0.0.1",port=5000)