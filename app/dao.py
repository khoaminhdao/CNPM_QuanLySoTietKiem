import sqlite3
from datetime import datetime

from app import db
from app.models import LoaiTietKiem, SoTietKiem

def read_Loai():
    return LoaiTietKiem.query.all()

def read_STK():
    return SoTietKiem.query.all()

def them_STK(name, CMND, address, amount, loaitietkiem):
    stk = SoTietKiem(loaiTietKiem=loaitietkiem, khachHang=name, CMND=CMND, diaChi=address, ngayMoSo=datetime.now(), soTienGui=amount)
    db.session.add(stk)
    db.session.commit()