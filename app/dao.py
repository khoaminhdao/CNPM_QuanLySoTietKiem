import sqlite3
from datetime import datetime

from flask_login import current_user
from sqlalchemy import or_

from app import db
from app.models import SavingType, Saving, DepositForm, Employee


def read_Type():
    return SavingType.query.all()


def read_Saving():
    return Saving.query.all()


def read_NoTerm_Saving():
    return Saving.query.filter(Saving.savingTypeID == 1).all()


def read_WithdrawAllowed_Saving():
    return Saving.query.filter(Saving.savingTypeID == 1)

#def add_Saving(customerName, identityNumber, address, amount, savingType):
#    saving = Saving(savingTypeID=savingType, customerID=name, CMND=CMND, diaChi=address, ngayMoSo=datetime.now(), soTienGui=amount)
#    db.session.add(stk)
#    db.session.commit()


def add_DepositForm(savingID, amount):
    depositForm = DepositForm(savingID=savingID, depositDate=datetime.now(), amount=amount, employeeCreated=current_user.identityNumber)
    db.session.add(depositForm)
    db.session.commit()

    saving = Saving.query.get(savingID)
    saving.balanceAmount += float(amount)
    db.session.add(saving)
    db.session.commit()


def add_WithdrawalForm(savingID, amount):
    withdrawalForm = DepositForm(savingID=savingID, depositDate=datetime.now(), amount=amount, employeeCreated=current_user.identityNumber)
    db.session.add(withdrawalForm)
    db.session.commit()

    saving = Saving.query.get(savingID)
    saving.balanceAmount -= float(amount)
    db.session.add(saving)
    db.session.commit()


def save_Activity():
    employee = Employee.query.get(current_user.identityNumber)
    employee.lastActive = datetime.now()
    db.session.add(employee)
    db.session.commit()

