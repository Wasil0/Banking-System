## Version : 8

import json
from datetime import date

class DataHandler:
    user_file: str = "Users.json"
    transaction_file: str = "Transactions.json"
    
    def addSavingAccountUser(self, full_name: str, username: str, password: str, email: str, phone:str\
        , account_id: str, balance: float):
        
        if not self.isAnExistingUser(username, "SavingAccountUsers"):
            data : dict = { 
                            "Name": full_name,
                            "Username": username,
                            "Password": password,
                            "Email": email,
                            "Phone": phone,
                            "AccountID": account_id,
                            "Balance": balance,
                            }
            return self.__addData(DataHandler.user_file, "SavingAccountUsers", data)
        
      
    def addCheckingAccountUser(self, full_name: str, username: str, password: str, email: str, phone:str\
        , account_id: str, balance: float, credit_amount_spend: float, repayment_deadline: str,):
        
        if not self.isAnExistingUser(username, "CheckingAccountUsers"):
            data : dict = { 
                            "Name": full_name,
                            "Username": username,
                            "Password": password,
                            "Email": email,
                            "Phone": phone,
                            "AccountID": account_id,
                            "Balance": balance,
                            "CreditAmountSpend": credit_amount_spend,
                            "RepaymentDeadline": self.dateToStrObj(repayment_deadline)
                            }
            return self.__addData(DataHandler.user_file, "CheckingAccountUsers", data)
             
    
    def addLoanAccountUser(self, full_name: str, username: str, password: str, email: str, phone:str\
        , account_id: str, loan_taken: float, amount_repayed: float, repayment_deadline: str):
        
        if not self.isAnExistingUser(username, "LoanAccountUsers"):
            data : dict = { 
                            "Name": full_name,
                            "Username": username,
                            "Password": password,
                            "Email": email,
                            "Phone": phone,
                            "AccountID": account_id,
                            "LoanTaken": loan_taken,
                            "RepaymentDeadline": amount_repayed,
                            "AmountRepayed": self.dateToStrObj(repayment_deadline)
                            }
            return self.__addData(DataHandler.user_file, "LoanAccountUsers", data)

    def addTransaction(self, sender: str, s_account_id: str, receiver: str, r_account_id: str\
        , operation_type: str, amount: float, date: str):
        data: dict = {  
                        "SenderAccountID": s_account_id,
                        "SenderUsername": sender,
                        "OperationType": operation_type,
                        "Amount": amount,
                        "ReceiverAccountID": r_account_id,
                        "ReceiverUsername": receiver,
                        "Date": self.dateToStrObj(date)
                    }
        return self.__addTransactions(DataHandler.transaction_file, "Transactions", data)
 
 
       
    def isAnExistingUser(self, username: str, account_type: str) -> bool:
        if self.__dataChecker(DataHandler.user_file, "LoanAccountUsers", "Username", username)\
            or self.__dataChecker(DataHandler.user_file, "SavingAccountUsers", "Username", username)\
            or self.__dataChecker(DataHandler.user_file, "CheckingAccountUsers", "Username", username):
            return True
        else:
            return False
            
  
                             
    def getUsersData(self, username: str, account_type: str):
        return self.__dataChecker(DataHandler.user_file, account_type, "Username", username)


    def updateUserData(self, data: dict, account_type: str)->str:
        with open(DataHandler.user_file, "r+") as file:
            database = json.load(file)
            for user in database[account_type]:
                if data.get("Username") == user.get("Username"):
                    modified_data: dict = user
                    database[account_type].remove(user)
                    break
                    
            for change in data:
                modified_data[change] = data[change]
            

            database[account_type].extend([modified_data])
            file.seek(0)
            json.dump(database, file, indent=4)
                
            return "Successfully Changed."

                   
    def getUsersTransactionHistory(self, username: str) -> list:
        _ : list = self.__dataChecker("Transactions.json", "Transactions", "SenderUsername", username)
        _.extend(self.__dataChecker("Transactions.json", "Transactions", "ReceiverUsername", username))
        return _ 



    def __addTransactions(self, file_name: str, table: str, details: dict)->str:
        with open(file_name, "r+") as file:         
            data = json.load(file)
            data[table].append(details)
            file.seek(0)
            json.dump(data, file, indent=4)
            return True        



    def __addData(self, file_name: str, table: str, details: dict)->str:
        
        if self.isAnExistingUser(details["Username"], table):
            return False
        
        with open(file_name, "r+") as file:         
            data = json.load(file)
            data[table].extend([details])
            file.seek(0)
            json.dump(data, file, indent=4)
            return True


    def __dataChecker(self, file_name: str, table: str, key: str, value: str) -> list:
        with open(file_name, "r") as file:
            database: dict = json.load(file)
            results: list = []
            for data in database[table]:
                if value == data[key]:
                    results.append(data)
            
        return results



    def getAllTheUsers(selfstr, table: str) -> list:
        with open(DataHandler.user_file, "r") as file:
            database: dict = json.load(file)
        
        return database[table]


    def strToDateObj(self, str_date: str) -> date:
        if isinstance(str_date, date):
            return str_date
        
        temp1 = str_date.split("-")
        temp2 = []
        for i in temp1:
            temp2.append(int(i))
        
        return date(*temp2)


    def dateToStrObj(self, date_obj: date) -> str:
        return str(date_obj)    
    
    
    
    