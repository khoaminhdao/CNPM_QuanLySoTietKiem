import hashlib

from flask import render_template, request, session, redirect
from flask_login import login_user, login_required

from app import app, login, dao
from app.models import *

@login.user_loader
def user_load(maNV):
    return NhanVien.query.get(maNV)

@app.route("/", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get("username")
        password = request.form.get("password")
        password = str(hashlib.md5(password.strip().encode("utf-8")).hexdigest())
        user = NhanVien.query.filter(NhanVien.taiKhoan == username.strip(), NhanVien.matKhau == password.strip()).first()
        if user:
            login_user(user=user)
        else:
            pass
    return render_template("index.html")

@app.route("/login-admin", methods=['GET', 'POST'])
def login_admin():
    if request.method == 'POST':
        username = request.form.get("username")
        password = request.form.get("password")
        password = str(hashlib.md5(password.strip().encode("utf-8")).hexdigest())
        user = NhanVien.query.filter(NhanVien.taiKhoan == username.strip(), NhanVien.matKhau == password.strip(), NhanVien.chucVu == 1).first()
        if user:
            login_user(user=user)
    return redirect("/admin")

@app.route("/logout")
def logout():
    logout_user()
    return redirect("/")

@app.route("/moso", methods=['GET', 'POST'])
def moso():
    if request.method == 'POST':
       if dao.them_STK(**dict(request.form)):
         return redirect("/moso")

    return render_template("moso.html", loaitietkiem=dao.read_Loai())

@app.route("/guitien", methods=['GET', 'POST'])
def guitien():
    if request.method == 'POST':
       if dao.them_PhieuGuiTien(**dict(request.form)):
         return redirect("/guitien")

    return render_template("guitien.html", dsso=dao.read_STK_KKH())

@app.route("/ruttien", methods=['GET', 'POST'])
def ruttien():
    if request.method == 'POST':
       if dao.them_PhieuRutTien(**dict(request.form)):
         return redirect("/ruttien")

    return render_template("ruttien.html", dsso=dao.read_STK_DuocRut())

if __name__ == "__main__":
    app.run()