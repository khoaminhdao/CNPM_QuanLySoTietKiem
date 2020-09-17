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
    return Saving.query.all()


def read_NoTerm_Saving():
    return Saving.query.filter(Saving.savingTypeID == 1).all()


def read_WithdrawAllowed_Saving():
    return Saving.query.filter(Saving.allowWithdrawDate <= datetime.now())


def add_Saving(customerName, identityNumber, address, amount, savingType):
    customer = Customer.query.get(identityNumber)
    if not customer:
        customer = Customer(identityNumber=identityNumber, customerName=customerName, address=address)
        db.session.add(customer)
        db.session.commit()

    wDate = datetime.now()
    term = SavingType.query.get(savingType).term
    if term == 0:
        regu = RegulationDetail.query.filter(RegulationDetail.regulationID == 2 and RegulationDetail.applyDate <=
                                                datetime.now()).order_by(desc(RegulationDetail.applyDate)).limit(1).first()
        wDate += timedelta(days=int(regu.value))
    else:
        wDate += monthdelta(term)

    saving = Saving(savingTypeID=savingType, customerID=identityNumber, balanceAmount=amount, allowWithdrawDate=wDate)
    db.session.add(saving)
    db.session.commit()
    return True


def add_DepositForm(savingID, amount):
    depositForm = DepositForm(savingID=savingID, depositDate=datetime.now(), amount=amount,
                              employeeCreated=current_user.identityNumber)
    db.session.add(depositForm)
    db.session.commit()

    saving = Saving.query.get(savingID)
    saving.balanceAmount += float(amount)
    db.session.add(saving)
    db.session.commit()
    return True


def add_WithdrawalForm(savingID, amount):
    withdrawalForm = WithdrawalForm(savingID=savingID, depositDate=datetime.now(), amount=amount, employeeCreated=current_user.identityNumber)
    db.session.add(withdrawalForm)
    db.session.commit()

    saving = Saving.query.get(savingID)
    saving.balanceAmount -= float(amount)
    db.session.add(saving)
    db.session.commit()
    return True


def save_Activity():
    employee = Employee.query.get(current_user.identityNumber)
    employee.lastActive = datetime.now()
    db.session.add(employee)
    db.session.commit()

