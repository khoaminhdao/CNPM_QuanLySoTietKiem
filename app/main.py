import hashlib

from flask import render_template, request
from flask_login import login_user, login_required
from werkzeug.utils import redirect

from app import app, login
from app.models import *

@app.route("/")
def index():
    return render_template("index.html")

@login.user_loader
def user_load(maNV):
    return NhanVien.query.get(maNV)

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

if __name__ == "__main__":
    app.run()