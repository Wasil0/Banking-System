## Version : 7;

import random
from abc import ABC, abstractmethod
from datetime import date
from DataClass import DataHandler
        
        
class Account(ABC):

    today: date = date.today()
    
    def __init__(self, full_name: str, username: str, password: str, email: str, phone:str, balance: float = 0\
        , account_id: str = None) -> None:
        self._account_number: str = account_id or self.generateAccountNumber()
        self._full_name: str = full_name
        self._username: str = username
        self._password: str = password
        self._email: str = email
        self._phone: str = phone
        self._balance: float = balance
        self.dataclass_obj: DataHandler = DataHandler()
        

            
    def balanceEnquiry(self):
        return self._balance


    
    @property
    def AccountNumber(self):  
        return self._account_number


    @abstractmethod
    def deposit(self, account_type: str, amount:float, acc_details: dict)->bool:
        self.dataclass_obj.updateUserData(data = acc_details, account_type = account_type)
        self.dataclass_obj.addTransaction(self._username, self._account_number, None, None, "Deposit", amount, Account.today)
        return True


            
    def seeTransactions(self):
        return self.dataclass_obj.getUsersTransactionHistory(self, self._username)



    def generateAccountNumber(self):
        temp: str = ""        
        for i in range(0,8):
            temp += str(random.randint(0,9))
        return temp


    @abstractmethod
    def withdraw(self, account_type: str, amount: float, details: dict)->str:
        self.dataclass_obj.updateUserData(data = details, account_type = account_type)
        self.dataclass_obj.addTransaction(self._username, self._account_number, None, None, "Withdraw", amount, Account.today)
        return f"${amount}/- is Successfully withdrawed."
    

            
    @abstractmethod
    def moneyTransfer(self, receiver_acc_type:str, receiver_acc_id: str, receiver_username: str, amount: float):
        receiver_data = self.dataclass_obj.getUsersData(receiver_username, receiver_acc_type)
        receiver_data[0]["Balance"] += amount
        self.dataclass_obj.updateUserData(receiver_data, receiver_acc_type)
        self.dataclass_obj.addTransaction(self._username, self._account_number, receiver_username, receiver_acc_id\
            , "MoneyTranfer", amount, Account.today)

    
  
    @classmethod
    @abstractmethod
    def existingAccountHolder(cls):         
        ...
   
    
    @abstractmethod
    def isANewUser(self):
        ...
        
        