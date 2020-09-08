from flask_admin import BaseView, expose
from flask_admin.contrib.sqla import ModelView
from flask_login import UserMixin, logout_user, current_user
from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import relationship
from werkzeug.utils import redirect

from app import db, admin


class AuthenticatedView(ModelView):
    column_display_pk = True
    def is_accessible(self):
        return current_user.is_authenticated


class LoaiTietKiem(db.Model):
    maLoaiTK = Column(Integer, primary_key=True, autoincrement=True)
    tenLoaiTK = Column(String(50), nullable=False)
    kyHan = Column(Integer, nullable=False)
    laiSuat = Column(Float, nullable=False)
    ngayApDung = Column(DateTime, nullable=False)
    loaiTietKiem = relationship('SoTietKiem', backref='loaitietkiem', lazy=False)


class SoTietKiem(db.Model):
    maSo = Column(Integer, primary_key=True, autoincrement=True)
    loaiTietKiem = Column(Integer, ForeignKey(LoaiTietKiem.maLoaiTK), nullable=False)
    khachHang = Column(String(50), nullable=False)
    CMND = Column(String(12), nullable=False)
    diaChi = Column(String(100), nullable=False)
    ngayMoSo = Column(DateTime, nullable=False)
    soTienGui = Column(Float, nullable=False)
    soLanDaoHan = Column(Integer, nullable=False, default=1)
    soRut = relationship('PhieuRutTien', backref='sotietkiem', lazy=True)
    soGui = relationship('PhieuGuiTien', backref='sotietkiem', lazy=True)


class ChucVu(db.Model):
    maCv = Column(Integer, primary_key=True, autoincrement=True)
    tenCV = Column(String(50), nullable=False)
    chucVu = relationship('NhanVien', backref='chucvu', lazy=True)


class NhanVien(db.Model, UserMixin):
    maNV = Column(Integer, primary_key=True, autoincrement=True)
    CMND = Column(String(12), nullable=True)
    tenNV = Column(String(50), nullable=False)
    taiKhoan = Column(String(20), nullable=False)
    matKhau = Column(String(255), nullable=False)
    chucVu = Column(Integer, ForeignKey(ChucVu.maCv), nullable=False)
    lanTruyCapGanNhat = Column(DateTime, nullable=True)
    nhanVienRut = relationship('PhieuRutTien', backref='nhanvien', lazy=True)
    nhanVienGui = relationship('PhieuGuiTien', backref='nhanvien', lazy=True)
    nhanVienTaoQuyDinh = relationship('QuyDinh', backref='nhanvien', lazy=True)


    def get_id(self):
        return self.maNV


class QuyDinh(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    tenQuyDinh = Column(String(50), nullable=False)
    giaTriQuyDinh = Column(Float, nullable=False)
    ngayApDung = Column(DateTime, nullable=True)
    nhanVienTao = Column(Integer, ForeignKey(NhanVien.maNV), nullable=False)


class PhieuRutTien(db.Model):
    maPhieu = Column(Integer, primary_key=True, autoincrement=True)
    maSo = Column(Integer, ForeignKey(SoTietKiem.maSo), nullable=False)
    ngayRut = Column(DateTime, nullable=False)
    soTienRut = Column(Float, nullable=False)
    nhanVien = Column(Integer, ForeignKey(NhanVien.maNV), nullable=False)


class PhieuGuiTien(db.Model):
    maPhieu = Column(Integer, primary_key=True, autoincrement=True)
    maSo = Column(Integer, ForeignKey(SoTietKiem.maSo), nullable=False)
    ngayGui = Column(DateTime, nullable=False)
    soTienGui = Column(Float, nullable=False)
    nhanVien = Column(Integer, ForeignKey(NhanVien.maNV), nullable=False)

    def __str__(self):
        return self.name


class LoaiTietKiemView(AuthenticatedView):
    column_labels = dict(maLoaiTK='Mã loại tiết kiệm', tenLoaiTK='Tên loại tiết kiệm', kyHan='Kỳ hạn', laiSuat='Lãi suất', ngayApDung='Ngày áp dụng')
    column_exclude_list = ('loaiTietKiem', )

class SoTietKiemView(AuthenticatedView):
    column_labels = dict(maSo='Mã sổ', khachHang='Tên khách hàng', CMND='Số CMND', diaChi='Địa chỉ', ngayMoSo='Ngày mở sổ', soTienGui='Số tiền gửi', soLanDaoHan='Số lần đáo hạn')


class PhieuGuiTienView(AuthenticatedView):
    column_labels = dict(maPhieu='Mã phiếu', ngayGui='Ngày gửi', soTienGui='Số tiền gửi')


class PhieuRutTienView(AuthenticatedView):
    column_labels = dict(maPhieu='Mã phiếu', ngayRut='Ngày rút', soTienRut='Số tiền rút')


class NhanVienView(AuthenticatedView):
    column_labels = dict(maNV='Mã nhân viên', tenNV='Tên nhân viên', CMND='Số CMND', taiKhoan='Tên tài khoản', matKhau='Mật khẩu', lanTruyCapGanNhat='Lần truy cập gần nhất')


class ChucVuView(AuthenticatedView):
<<<<<<< HEAD
    column_labels = dict(maCv='Mã chức vụ', tenCV='Tên chức vụ')
=======
    column_labels = dict(maCV='Mã chức vụ', tenCV='Tên chức vụ')
>>>>>>> master


class QuyDinhView(AuthenticatedView):
    column_labels = dict(id='Mã quy định', tenQuyDinh='Mã quy định', giaTriQuyDinh='Giá trị quy định', ngayApDung='Ngày áp dụng')


class LogoutView(BaseView):
    @expose('/')
    def index(self):
        logout_user()
        return redirect("/admin")

    def is_accessible(self):
        return current_user.is_authenticated


admin.add_view(SoTietKiemView(SoTietKiem, db.session, name="Sổ tiết kiệm"))
admin.add_view(LoaiTietKiemView(LoaiTietKiem, db.session, name="Loại tiết kiệm"))
admin.add_view(PhieuGuiTienView(PhieuGuiTien, db.session, name="Phiếu gửi tiền"))
admin.add_view(PhieuRutTienView(PhieuRutTien, db.session, name="Phiếu rút tiền"))
admin.add_view(NhanVienView(NhanVien, db.session, name="Nhân viên"))
admin.add_view(ChucVuView(ChucVu, db.session, name="Chức vụ"))
admin.add_view(QuyDinhView(QuyDinh, db.session, name="Quy định"))
admin.add_view(LogoutView(name="Đăng xuất"))

if __name__ == "__main__":
    db.create_all()
