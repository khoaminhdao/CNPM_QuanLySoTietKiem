import sqlite3
from datetime import datetime

from flask_login import current_user
from sqlalchemy import or_

from app import db
from app.models import LoaiTietKiem, SoTietKiem, PhieuGuiTien, PhieuRutTien


def read_Loai():
    return LoaiTietKiem.query.all()

def read_STK():
    return SoTietKiem.query.all()

def read_STK_KKH():
    return SoTietKiem.query.filter(SoTietKiem.loaiTietKiem == 1).all()

def read_STK_DuocRut():
    return SoTietKiem.query.filter(SoTietKiem.loaiTietKiem == 1)

def them_STK(name, CMND, address, amount, loaitietkiem):
    stk = SoTietKiem(loaiTietKiem=loaitietkiem, khachHang=name, CMND=CMND, diaChi=address, ngayMoSo=datetime.now(), soTienGui=amount)
    db.session.add(stk)
    db.session.commit()

def them_PhieuGuiTien(maSo, name, amount):
    pgt = PhieuGuiTien(maSo=maSo, ngayGui=datetime.now(), soTienGui=amount, nhanVien=current_user.maNV)
    db.session.add(pgt)
    db.session.commit()

    stk = SoTietKiem.query.get(maSo)
    stk.soTienGui += float(amount)
    db.session.add(stk)
    db.session.commit()

def them_PhieuRutTien(maSo, name, amount):
    pgt = PhieuRutTien(maSo=maSo, ngayRut=datetime.now(), soTienRut=amount, nhanVien=current_user.maNV)
    db.session.add(pgt)
    db.session.commit()

    stk = SoTietKiem.query.get(maSo)
    stk.soTienGui -= float(amount)
    db.session.add(stk)
    db.session.commit()
