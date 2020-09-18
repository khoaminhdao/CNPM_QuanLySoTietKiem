import sqlite3
from datetime import datetime
from monthdelta import monthdelta, timedelta

from flask_login import current_user
from sqlalchemy import func, desc
from sqlalchemy.orm import load_only

from app import db
from app.models import SavingType, Saving, DepositForm, Employee, Customer, Regulation, RegulationDetail, WithdrawalForm


def read_Type():
    return SavingType.query.all()


def read_Saving():
    return Saving.query.filter(Saving.balanceAmount > 0).all()


def read_NoTerm_Saving():
    return Saving.query.filter(Saving.savingTypeID == 1, Saving.balanceAmount > 0).all()


def read_WithdrawAllowed_Saving():
    return Saving.query.filter(Saving.balanceAmount > 0, Saving.allowWithdrawDate <= datetime.now()).all()


def read_HasTerm_Saving():
    return Saving.query.filter(Saving.savingTypeID != 1, Saving.balanceAmount > 0,
                               Saving.allowWithdrawDate <= datetime.now()).all()


def read_Saving_By_ID(savingID):
    return Saving.query.filter(Saving.savingID == savingID).all()


def read_Saving_By_Type(savingTypeID):
    return Saving.query.filter(Saving.savingTypeID == savingTypeID).all()


def add_Saving(customerName, identityNumber, address, amount, savingType):
    customer = Customer.query.get(identityNumber)
    if not customer:
        customer = Customer(identityNumber=identityNumber, customerName=customerName, address=address)
        db.session.add(customer)
        db.session.commit()

    wDate = datetime.now()
    term = SavingType.query.get(savingType).term
    if term == 0:
        regu = RegulationDetail.query.filter(RegulationDetail.regulationID == 2, RegulationDetail.applyDate <=
                                             datetime.now()).order_by(desc(RegulationDetail.applyDate)).limit(1).first()
        wDate += timedelta(days=int(regu.value))
    else:
        wDate += monthdelta(term)

    saving = Saving(savingTypeID=savingType, customerID=identityNumber, balanceAmount=amount, allowWithdrawDate=wDate)
    db.session.add(saving)
    db.session.commit()
    return wDate + timedelta(days=1)


def add_DepositForm(savingID, amount):
    if savingID == "undefined":
        return False

    depositForm = DepositForm(savingID=savingID, depositDate=datetime.now(), amount=amount,
                              employeeCreated=current_user.identityNumber)
    db.session.add(depositForm)
    db.session.commit()

    saving = Saving.query.get(savingID)
    saving.balanceAmount += float(amount)
    db.session.add(saving)
    db.session.commit()
    return saving.balanceAmount


def add_WithdrawalForm(savingID, amount):
    if savingID == "undefined":
        return False

    withdrawalForm = WithdrawalForm(savingID=savingID, withdrawDate=datetime.now(), amount=amount,
                                    employeeCreated=current_user.identityNumber)
    db.session.add(withdrawalForm)
    db.session.commit()

    saving = Saving.query.get(savingID)
    saving.balanceAmount -= float(amount)
    db.session.add(saving)
    db.session.commit()
    return saving.balanceAmount


def save_Activity():
    employee = Employee.query.get(current_user.identityNumber)
    employee.lastActive = datetime.now()
    db.session.add(employee)
    db.session.commit()


def changePass(newPass):
    employee = Employee.query.get(current_user.identityNumber)
    employee.password = newPass
    db.session.add(employee)
    db.session.commit()


def extendTerm(savingID):
    saving = Saving.query.get(savingID)
    saving.allowWithdrawDate += monthdelta(saving.savingtype.term)
    saving.balanceAmount += saving.balanceAmount * saving.savingtype.term * saving.savingtype.interestRate
    monthNoTerm = (datetime.now().timestamp() - saving.allowWithdrawDate.timestamp()) / (24 * 60 * 60 * 30)
    saving.balanceAmount += saving.balanceAmount * (saving.savingtype.term * saving.savingtype.interestRate +
                                                        SavingType.query.get(1).interestRate * monthNoTerm)
    db.session.add(saving)
    db.session.commit()
    return saving.allowWithdrawDate + timedelta(days=1)
