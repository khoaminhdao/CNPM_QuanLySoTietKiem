import hashlib

from flask import render_template, request, session, redirect
from flask_login import login_user, login_required

from app import app, login, dao
from app.models import *


@login.user_loader
def user_load(identityNumber):
    return Employee.query.get(identityNumber)


@app.route("/", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get("username")
        password = request.form.get("password")
        password = str(hashlib.md5(password.strip().encode("utf-8")).hexdigest())
        user = Employee.query.filter(Employee.account == username.strip(),
                                     Employee.password == password.strip()).first()
        if user:
            login_user(user=user)
            dao.save_Activity()
        else:
            pass
    return render_template("index.html")


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
@login_required
def create_saving():
    notification = ""
    if request.method == 'POST':
        if dao.add_Saving(**dict(request.form)):
            notification = "Created successfully!"
        else:
            notification = "Cannot create!!"
    return render_template("create-saving.html", savingtype=dao.read_Type(),  notification=notification)


@app.route("/create_deposit_form", methods=['GET', 'POST'])
@login_required
def create_deposit():
    notification = ""
    if request.method == 'POST':
        if dao.add_DepositForm(**dict(request.form)):
            notification = "Created successfully!"
        else:
            notification = "Cannot create!!"

    return render_template("create-deposit.html", savingList=dao.read_NoTerm_Saving(), notification=notification)


@app.route("/create_withdrawal_form", methods=['GET', 'POST'])
@login_required
def create_withdrawal():
    notification = ""
    if request.method == 'POST':
        if dao.add_WithdrawalForm(**dict(request.form)):
            notification = "Created successfully!"
        else:
            notification = "Cannot create!!"

    return render_template("create-withdrawal.html", savingList=dao.read_WithdrawAllowed_Saving(), notification=notification)


@app.route("/tracuu", methods=['GET', 'POST'])
@login_required
def tracuu():
    if request.method == 'POST':
        if dao.them_PhieuRutTien(**dict(request.form)):
            return redirect("/tracuu")

    return render_template("tracuu.html", dsso=dao.read_STK())


@app.route("/thongke", methods=['GET'])
@login_required
def thongke():
    return render_template("thongke.html")


if __name__ == "__main__":
    app.run(debug=False)
