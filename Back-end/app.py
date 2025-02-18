#建立伺服器
from flask import *

app = Flask(__name__,
            static_folder= "public",
            static_url_path="/"
            )
#使用者session 密碼
app.secret_key = "123456"


#初始資料庫連線
import pymongo as py
client = py.MongoClient("mongodb+srv://s920201lin87:zxc19961208ZXC@database.2psro.mongodb.net/")
print("連線資料庫")
db= client.member_system
collection = db.memberINFO



#首頁
@app.route("/")
def index():
    return render_template("index.html")

#會員登入註冊網頁
@app.route("/sign_in")
def sign_in():
    return render_template("sign_in.html")

#會員註冊網頁
@app.route("/register")
def register():
    return render_template("register.html")

#取得會員登入資訊
@app.route("/sign_in_info",methods= ["POST"])
def sign_in_info():
    signInEmail =request.form["email"] 
    signInPwd = request.form["pwd"]
    result = collection.find_one({
        "email": signInEmail
        })
    if result is None:
        return redirect("/sign_in_error")

    # 如果找到使用者，但密碼不相符，也導向錯誤頁面
    if result["pwd"] != signInPwd:
        return redirect("/sign_in_error")
    
    # 如果都正確，就把使用者資訊存入 session，導向首頁或個人頁面
    session["userName"] = result["name"]
    return redirect("/member")
    
#取得會員註冊資料
@app.route("/register_info",methods= ["POST"])
def register_info():
    registerName = request.form["name"]
    registerEmail = request.form["email"]
    registerpwd = request.form["pwd"]
    # registerPwdConfirm = request.form["pwdConfirm"]
    print(registerName,registerEmail,registerpwd) 

#檢查會員集合中是否有相同信箱
    result = collection.find_one(
        {
        "email":registerEmail
        })
    if result != None:
        return redirect("/sign_in_error")
    collection.insert_one({
        "name":registerName,
        "email":registerEmail,
        "pwd":registerpwd
    })
    return redirect("/")

#會員登入錯誤訊息
@app.route("/sign_in_error")
def sign_in_error():
    return render_template("sign_in_error.html")


@app.route("/member")
def member_login():
    if "userName" in session:
        return render_template("member.html", name=session["userName"])
    else:
        return redirect("/sign_in")

@app.route("/log_out")
def log_out():
    session.clear()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True,port= 7890)