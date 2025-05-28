## Version : 4

from datetime import date
from dateutil import relativedelta
from G2_01_2 import Account
import time

class CheckingAccount(Account):
    
    _overdraft_credits_fee = 0.20
    _over_draft_limit = 500
    
    def __init__(self, full_name: str, username: str, password: str, email: str, phone: str, balance: float = 0\
        , account_number: str = None, credit_spend: float = 0, repayment_deadline: str = None) -> None:
        Account.__init__(self, full_name, username, password, email, phone, balance, account_number)
        self._credit_amount_spend = credit_spend
        self._repayment_deadline = repayment_deadline
        
    
    
    @classmethod
    def existingAccountHolder(cls, data: dict) -> object:
        return cls(full_name = data["Name"], username = data["Username"], password = data["Password"]\
            , email = data["Email"], phone = data["Phone"], balance = data["Balance"], account_number = data["AccountID"]\
            , credit_spend = data["CreditAmountSpend"], repayment_deadline = data["RepaymentDeadline"])
    
    
    def _creditsAccumaleted(self):
        self._overdraft_due = self.__overDraftLimit()
        
        if self._over_draft_limit == 0:
            return None
        
        is_due_already_added = self.dataclass_obj.getUsersTransactionHistory(self._username)
        
        for details in is_due_already_added:
            if details["OperationType"] == "DueFee" and \
                self.dataclass_obj.strToDateObj(details["Date"]) >= Account.today.month:
                return None
            
        self._balance -= self._overdraft_due
        data: dict = {"Username": self._username, "Balance": self._balance}
        self.dataclass_obj.updateUserData(data, "CheckingAccount")
        self.dataclass_obj.addTransaction(self._username, self._account_number, None, None, "DueFee", self._overdraft_due, Account.today())    
        
        
    def __overDraftLimit(self)->float:
        return self._credit_amount_spend*CheckingAccount._overdraft_credits_fee
  
  
    
    def deposit(self, amount: float) -> bool:
        if amount < 0:
            return False
        
        
        self._credit_amount_spend -= amount
        self._balance += amount
        
        if self._credit_amount_spend < 0: 
            self._credit_amount_spend = 0
                       
        data: dict = {"Username": self._username, "Balance": self._balance, "CreditAmountSpend": self._credit_amount_spend}
        return Account.deposit(self, "CheckingAccountUsers", amount, acc_details = data)
    
   
    
    def repaymentDate(self) -> None:
        self._repayment_deadline = Account.today + relativedelta.relativedelta(months = 1 )    
 
 
        
    def withdraw(self, amount) -> str:
        if amount < 0 :
            return "Invalid Amount"
        
        if amount < self._balance:
            self._balance -= amount
        
        elif amount < (self._balance + self._over_draft_limit) and self._over_draft_limit >= self._credit_amount_spend:
            temp_var_1 = amount - self._balance
            temp_var_2 = self._credit_amount_spend + temp_var_1
            if self._over_draft_limit < temp_var_2 :
                return "Not Enough Funds, Credit Limit reached. Can't Proccess the request."
    
            self._balance = -amount
            self._credit_amount_spend = temp_var_2
            
        data: dict = {"Username": self._username, "Balance": self._balance, "CreditAmountSpend": self._credit_amount_spend}
        return Account.withdraw(self, "CheckingAccountUsers", amount, data)
    
    
    def moneyTransfer(self, receiver_acc_type:str, receiver_acc_id: str, receiver_username: str, amount: float):
        if amount <= 0:
            return "Invalid Amount."

        return Account.moneyTransfer(self, receiver_acc_type, receiver_acc_id, receiver_username, amount)


    def isANewUser(self):
        if self._account_number == None:
            self._account_number = Account.generateAccountNumber(self)
            
        return self.dataclass_obj.addCheckingAccountUser(self._full_name, self._username, self._password, self._email, self._phone\
            , self._account_number, self._balance, self._credit_amount_spend, self._repayment_deadline)


    

class SavingAccount(Account):
    
    interest_rate = 0.018
        
    def __init__(self, full_name: str, username: str, password: str, email: str, phone: str, balance: float = 0\
        , account_number: str = None) -> None:
        Account.__init__(self, full_name, username, password, email, phone, balance, account_number)    
        self.isANewUser()
        self.__interestAdder()
        
        
    @classmethod
    def existingAccountHolder(cls, data: dict) -> object:
        return cls(full_name = data["Name"], username = data["Username"], password = data["Password"], email = data["Email"]\
            , phone = data["Phone"], balance = data["Balance"], account_number = data["AccountID"])
    

    def deposit(self, amount: float) -> bool:
        if amount<=0:
            return False
            
        self._balance += amount
        data = {"Username": self._username, "Balance": self._balance}
        return Account.deposit(self, "SavingAccountUsers", amount, data)
        
            
    def withdraw(self, amount: float) -> str:
        if amount <= 0:
            return "Invalid Amount."

        if self._balance < amount:
            return "Not Sufficient Funds."

        self._balance -= amount
        data: dict = {"Username": self._username, "Balance": self._balance}
        return Account.withdraw(self, "SavingAccountUsers", amount, data)



    def interestCalculator(self):
        return round(self._balance*SavingAccount.interest_rate,2)


    def __interestAdder(self) -> None:
        funds = self.dataclass_obj.getUsersTransactionHistory(self._username)
        for fund in funds:
            if fund["OperationType"] == "InterestDeposit" \
                and self.dataclass_obj.strToDateObj(fund["Date"]).month >= Account.today.month:
                return None
            
        interest = self.interestCalculator()    
        if interest > 0:
            self._balance += interest
            data: dict = {"Username": self._username, "Balance": self._balance}
            self.dataclass_obj.updateUserData(data, "SavingAccountUsers")
            self.dataclass_obj.addTransaction(self._username, self._account_number, None, None, "InterestDeposit", interest, Account.today)
            
            
    def moneyTransfer(self, receiver_acc_type:str, receiver_acc_id: str, receiver_username: str, amount: float):
        if amount <= 0:
            return "Invalid Amount."

        return Account.moneyTransfer(self, receiver_acc_type, receiver_acc_id, receiver_username, amount)
    
            
    def isANewUser(self):
        return self.dataclass_obj.addSavingAccountUser(self._full_name, self._username, self._password, self._email\
            , self._phone, self._account_number, self._balance)
        




class LoanAccount(Account):
    
    __due_charges = 0.023
    
    
    def __init__(self, full_name: str, username: str, password: str, email: str, phone: str, loan_amount: float\
        , account_number: str = None, repayment_deadline: str = 0, amount_repayed: float = 0) -> None:
        
        Account.__init__(self, full_name, username, password, email, phone, -loan_amount, account_number)
        repayment_date = repayment_deadline or self.__loanDeadlineCalculator(3)
        self._repayment_deadline: date = self.dataclass_obj.strToDateObj(repayment_date)
        self._amount_repayed: float = amount_repayed 
        self.isANewUser()
        self.dealineExpired()
        
                
    @classmethod
    def existingAccountHolder(cls, data: dict) -> object:
        return cls(full_name = data["Name"], username = data["Username"], password = data["Password"], email = data["Email"]\
            , phone = data["Phone"], loan_amount = data["LoanTaken"], account_number = data["AccountID"]\
            , repayment_deadline = data["RepaymentDeadline"], amount_repayed = data["AmountRepayed"])
    


    
    def withdraw(self) -> str:
        return "No withdrawal function for Loan Account Users."

    
    
    def deposit(self, amount):
        if amount < 0:
            return False
        
        self._amount_repayed += amount
        data: dict = {"Username": self._username, "AmountRepayed": self._amount_repayed}
        return Account.deposit(self, "LoanAccountUsers", amount, data)
    
    
    
    def __loanDeadlineCalculator(self, loan_time) -> None:
        return Account.today + relativedelta.relativedelta(months = loan_time)
        

    
    def dealineExpired(self) -> bool:
        is_due_already_added: list = self.dataclass_obj.getUsersTransactionHistory(self._username)
        
        if Account.today > self._repayment_deadline:
        
            for details in is_due_already_added:
                if details["OperationType"] == "LoanNotRepayed"\
                    and self.dataclass_obj.strToDateObj(details["RepaymentDeadline"]).month >= Account.today.month:
                        return False
                    
            self._due_charges = self._balance*LoanAccount.__due_charges
            self._balance -= self._due_charges
                  
            data: dict = {"Username": self._username, "LoanTaken": self._balance}   
            self.dataclass_obj.updateUserData(data,"LoanAccountUsers")
            self.dataclass_obj.addTransaction(self._username, self._account_number, None, None, "LoanNotRepayed", self.__due_charges, Account.today)
            return True
        
        return False
        
     
     
    def moneyTransfer(self) -> str:
        return "No Money Transfer Method for Loan Account Users"
     
    
    def seeTransactions(self):
        return super().seeTransactions()
     
     
    def isANewUser(self):
        return self.dataclass_obj.addLoanAccountUser(self._full_name, self._username, self._password, self._email\
            , self._phone, self._account_number, self._balance, self._amount_repayed, self._repayment_deadline)