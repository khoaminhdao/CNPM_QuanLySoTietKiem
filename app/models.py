from flask_admin import BaseView, expose
from flask_admin.contrib.sqla import ModelView
from flask_login import UserMixin, logout_user, current_user
from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import relationship
from werkzeug.utils import redirect
from datetime import datetime

from app import db, admin


class AuthenticatedView(ModelView):
    column_display_pk = True
    def is_accessible(self):
        return current_user.is_authenticated


class SavingType(db.Model):
    savingTypeID = Column(Integer, primary_key=True, autoincrement=True)
    savingName = Column(String(50), nullable=False)
    term = Column(Integer, nullable=False)
    interestRate = Column(Float, nullable=False)
    applyDate = Column(DateTime, nullable=False)
    saving = relationship('Saving', backref='savingtype', lazy=False)

    def __str__(self):
        return self.savingName


class Customer(db.Model):
    identityNumber = Column(String(12), primary_key=True)
    customerName = Column(String(50), nullable=False)
    address = Column(String(100), nullable=False)
    saving = relationship('Saving', backref='customer', lazy=False)

    def __str__(self):
        return self.identityNumber + "\t" + self.customerName


class Saving(db.Model):
    savingID = Column(Integer, primary_key=True, autoincrement=True)
    savingTypeID = Column(Integer, ForeignKey(SavingType.savingTypeID), nullable=False)
    customerID = Column(String(50), ForeignKey(Customer.identityNumber),  nullable=False)
    createDate = Column(DateTime, default=datetime.now(), nullable=False)
    balanceAmount = Column(Float, nullable=False)
    allowWithdrawDate = Column(DateTime, nullable=False)
    withdrawal = relationship('WithdrawalForm', backref='saving', lazy=True)
    deposit = relationship('DepositForm', backref='saving', lazy=True)

    def __str__(self):
        return str(self.savingID)


class Position(db.Model):
    posID = Column(Integer, primary_key=True, autoincrement=True)
    posName = Column(String(50), nullable=False)
    pos = relationship('Employee', backref='position', lazy=True)

    def __str__(self):
        return self.posName


class Employee(db.Model, UserMixin):
    identityNumber = Column(String(12), primary_key=True)
    employeeName = Column(String(50), nullable=False)
    account = Column(String(20), nullable=False)
    password = Column(String(255), default='e10adc3949ba59abbe56e057f20f883e', nullable=False)
    positionID = Column(Integer, ForeignKey(Position.posID), nullable=False)
    lastActive = Column(DateTime, nullable=True)
    depositForm = relationship('DepositForm', backref='employee', lazy=True)
    withdrawalForm = relationship('WithdrawalForm', backref='employee', lazy=True)
    regulation = relationship('RegulationDetail', backref='employee', lazy=True)

    def __str__(self):
        return self.employeeName

    def get_id(self):
        return self.identityNumber


class Regulation(db.Model):
    regulationID = Column(Integer, primary_key=True, autoincrement=True)
    regulationName = Column(String(50), nullable=False)
    regulationDetail = relationship('RegulationDetail', backref='regulation', lazy=False)

    def __str__(self):
        return self.regulationName


class RegulationDetail(db.Model):
    regulationID = Column(Integer, ForeignKey(Regulation.regulationID), primary_key=True)
    value = Column(Float, nullable=False)
    applyDate = Column(DateTime, primary_key=True,)
    employeeCreated = Column(String(12), ForeignKey(Employee.identityNumber), nullable=False)


class WithdrawalForm(db.Model):
    formID = Column(Integer, primary_key=True, autoincrement=True)
    savingID = Column(Integer, ForeignKey(Saving.savingID), nullable=False)
    withdrawDate = Column(DateTime, default=datetime.now(), nullable=False)
    amount = Column(Float, nullable=False)
    employeeCreated = Column(String(12), ForeignKey(Employee.identityNumber), nullable=False)


class DepositForm(db.Model):
    formID = Column(Integer, primary_key=True, autoincrement=True)
    savingID = Column(Integer, ForeignKey(Saving.savingID), nullable=False)
    depositDate = Column(DateTime, default=datetime.now(), nullable=False)
    amount = Column(Float, nullable=False)
    employeeCreated = Column(String(12), ForeignKey(Employee.identityNumber), nullable=False)


class SavingTypeView(AuthenticatedView):
    column_labels = dict(savingName='Saving Name', term='Term', interestRate='Interest Rate', applyDate='Apply Date')
    column_exclude_list = ('savingTypeID', )
    form_columns = ('savingName', 'term', 'interestRate', 'applyDate')


class SavingView(AuthenticatedView):
    column_labels = dict(savingID='Saving ID', customer='Customer', createDate='Create Date',
                         balanceAmount='Balance Amount', allowWithdrawDate='Allowed Withdraw Date', savingtype='Saving Type')
    form_columns = ('customer', 'balanceAmount', 'allowWithdrawDate', 'savingtype')


class DepositFormView(AuthenticatedView):
    column_labels = dict(formID='Form ID', depositDate='Date', amount='Amount')
    form_columns = ('saving', 'amount', 'employee')


class WithdrawalFormView(AuthenticatedView):
    column_labels = dict(formID='Form ID', withdrawDate='Date', amount='Amount')
    form_columns = ('saving', 'amount', 'employee')


class EmployeeView(AuthenticatedView):
    column_labels = dict(identityNumber='Identity Number', employeeName='Employee Name', account='Account',
                         lastActive='Last Active')
    column_exclude_list = ('password', )
    form_columns = ('identityNumber', 'employeeName', 'account', 'position')


class PositionView(AuthenticatedView):
    column_labels = dict(posID='ID', posName='Position Name')
    form_columns = ('posName', )


class RegulationView(AuthenticatedView):
    column_labels = dict(applyDate='Apply Date')
    form_columns = ('regulation', 'value', 'applyDate', 'employee')


class CustomerView(AuthenticatedView):
    column_labels = dict(identityNumber='Identity Number', customerName='Customer Name')
    form_columns = ('identityNumber', 'customerName', 'address')


class LogoutView(BaseView):
    @expose('/')
    def index(self):
        logout_user()
        return redirect("/admin")

    def is_accessible(self):
        return current_user.is_authenticated


admin.add_view(SavingTypeView(SavingType, db.session, name='Saving Type'))
admin.add_view(SavingView(Saving, db.session))
admin.add_view(DepositFormView(DepositForm, db.session, name="Deposit Form"))
admin.add_view(WithdrawalFormView(WithdrawalForm, db.session, name="Withdrawal Form"))
admin.add_view(EmployeeView(Employee, db.session))
admin.add_view(PositionView(Position, db.session))
admin.add_view(CustomerView(Customer, db.session))
admin.add_view(RegulationView(RegulationDetail, db.session, name="Regulation"))
admin.add_view(LogoutView(name="Logout"))
#admin.add_view(ModelView(Regulation, db.session))

if __name__ == "__main__":
    db.create_all()
