import hashlib

from flask import render_template, request
from flask_login import login_user

from app import app, login, dao
from app.models import *


def changePass():
    password = str(hashlib.md5(request.form.get("password_change").strip().encode("utf-8")).hexdigest())
    newpass = str(hashlib.md5(request.form.get("new_password").strip().encode("utf-8")).hexdigest())
    confirm = str(hashlib.md5(request.form.get("confirm_password").strip().encode("utf-8")).hexdigest())
    if current_user.password == password:
        if newpass == confirm:
            dao.changePass(newpass)
            return "Change successfully!!"
        else:
            return "Confirm password is wrong!!"
    else:
        return "Password is wrong!!"


def loginEmp():
    username = request.form.get("username")
    password = request.form.get("password")
    password = str(hashlib.md5(password.strip().encode("utf-8")).hexdigest())
    user = Employee.query.filter(Employee.account == username.strip(),
                                 Employee.password == password.strip()).first()
    if user:
        login_user(user=user)
        dao.save_Activity()
        return ""
    else:
        return "Account or password is wrong!!"


@login.user_loader
def user_load(identityNumber):
    return Employee.query.get(identityNumber)


@app.route("/", methods=['GET', 'POST'])
def home():
    notification_pass = ""
    if request.method == 'POST':
        if not current_user.is_authenticated:
            notification_pass = loginEmp()
        else:
            notification_pass = changePass()
    return render_template("index.html", notification_pass=notification_pass)


@app.route("/login-admin", methods=['GET', 'POST'])
def login_admin():
    if request.method == 'POST':
        username = request.form.get("username")
        password = request.form.get("password")
        password = str(hashlib.md5(password.strip().encode("utf-8")).hexdigest())
        user = Employee.query.filter(Employee.account == username.strip(), Employee.password == password.strip(),
                                     Employee.positionID == 1).first()
        if user:
            login_user(user=user)
            dao.save_Activity()
    return redirect("/admin")


@app.route("/logout")
def logout():
    dao.save_Activity()
    logout_user()
    return redirect("/")


@app.route("/create_saving", methods=['GET', 'POST'])
def create_saving():
    notification = ""
    notification_pass = ""
    if not current_user.is_authenticated:
        notification_pass = "You must login!!"
    if request.method == 'POST':
        if not current_user.is_authenticated:
            notification_pass = loginEmp()
        elif request.form.get("password_change"):
            notification_pass = changePass()
        else:
            date = dao.add_Saving(**dict(request.form))
            notification = "Created successfully, you can withdraw on \n" + date.strftime("%d/%m/%Y")
    return render_template("create_saving.html", savingtype=dao.read_Type(), notification=notification,
                           notification_pass=notification_pass)


@app.route("/create_deposit_form", methods=['GET', 'POST'])
def create_deposit():
    notification = ""
    notification_pass = ""
    if not current_user.is_authenticated:
        notification_pass = "You must login!!"
    if request.method == 'POST':
        if not current_user.is_authenticated:
            notification_pass = loginEmp()
        elif request.form.get("password_change"):
            notification_pass = changePass()
        else:
            result = dao.add_DepositForm(**dict(request.form))
            if result is False:
                notification = "Cannot create!!"
            else:
                notification = "Successful, your balance amount: " + str(result) + "VNĐ"

    return render_template("create_deposit_form.html", savingList=dao.read_NoTerm_Saving(), notification=notification,
                           notification_pass=notification_pass)


@app.route("/create_withdrawal_form", methods=['GET', 'POST'])
def create_withdrawal():
    notification = ""
    notification_pass = ""
    if not current_user.is_authenticated:
        notification_pass = "You must login!!"
    if request.method == 'POST':
        if not current_user.is_authenticated:
            notification_pass = loginEmp()
        elif request.form.get("password_change"):
            notification_pass = changePass()
        else:
            result = dao.add_WithdrawalForm(**dict(request.form))
            if result is False:
                notification = "Cannot create!!"
            else:
                notification = "Successful, your balance amount: " + str(result) + "VNĐ"

    return render_template("create_withdrawal_form.html", savingList=dao.read_WithdrawAllowed_Saving(),
                           notification=notification,
                           notification_pass=notification_pass)


@app.route("/extend_term", methods=['GET', 'POST'])
def extendTerm():
    notification = ""
    notification_pass = ""
    if not current_user.is_authenticated:
        notification_pass = "You must login!!"
    if request.method == 'POST':
        if not current_user.is_authenticated:
            notification_pass = loginEmp()
        elif request.form.get("password_change"):
            notification_pass = changePass()
        else:
            date = dao.extendTerm(**dict(request.form))
            notification = "Extended successfully, you can withdraw on " + date.strftime("%d/%m/%Y")

    return render_template("extend_term.html", savingList=dao.read_HasTerm_Saving(),
                           notification=notification, notification_pass=notification_pass)


@app.route("/search", methods=['GET', 'POST'])
def search():
    notification = ""
    notification_pass = ""
    savingList = dao.read_Saving()
    if not current_user.is_authenticated:
        notification_pass = "You must login!!"
    if request.method == 'POST':
        if not current_user.is_authenticated:
            notification_pass = loginEmp()
        elif request.form.get("password_change"):
            notification_pass = changePass()
        elif request.form.get("savingID"):
            savingList = dao.read_Saving_By_ID(request.form.get("savingID"))
        else:
            savingList = dao.read_Saving_By_Type(request.form.get("savingType"))

    return render_template("search.html", savingTypeList=dao.read_Type(), savingList=savingList,
                           notification=notification, notification_pass=notification_pass)


@app.route("/report", methods=['GET', 'POST'])
def report():
    notification_pass = ""
    if not current_user.is_authenticated:
        notification_pass = "You must login!!"
    if request.method == 'POST':
        if not current_user.is_authenticated:
            notification_pass = loginEmp()
        else:
            notification_pass = changePass()
    return render_template("report.html", notification_pass=notification_pass)


@app.route('/postmethod', methods=['POST'])
def get_post_javascript_data():
    jsdata = request.form['javascript_data']
    return jsdata


if __name__ == "__main__":
    app.run(debug=False)
