import json
from datetime import date

class DataHandler:
    user_file: str = "Users.json"
    transaction_file: str = "Transactions.json"

    
    def addSavingAccountUser(self, full_name: str, username: str, password: str, email: str, phone:str, account_id: str, balance: float):
        """
        Add a new saving account user to the database.

        Args:
            full_name (str): Full name of the user.
            username (str): Username of the user.
            password (str): Password of the user.
            email (str): Email of the user.
            phone (str): Phone number of the user.
            account_id (str): Account ID of the user.
            balance (float): Account balance of the user.

        Returns:
            bool: True if the user is added successfully, False otherwise.
        """
        if not self.isAnExistingUser(username, "SavingAccountUsers"):
            data: dict = {
                "Name": full_name,
                "Username": username,
                "Password": password,
                "Email": email,
                "Phone": phone,
                "AccountID": account_id,
                "Balance": balance,
            }
            return self.__addData(DataHandler.user_file, "SavingAccountUsers", data)
        
      
    def addCheckingAccountUser(self, full_name: str, username: str, password: str, email: str, phone:str, account_id: str\
                               , balance: float, credit_amount_spend: float, repayment_deadline: str):
        """
        Add a new checking account user to the database.

        Args:
            full_name (str): Full name of the user.
            username (str): Username of the user.
            password (str): Password of the user.
            email (str): Email of the user.
            phone (str): Phone number of the user.
            account_id (str): Account ID of the user.
            balance (float): Account balance of the user.
            credit_amount_spend (float): Credit amount spent by the user.
            repayment_deadline (str): Repayment deadline of the user.

        Returns:
            bool: True if the user is added successfully, False otherwise.
        """
        if not self.isAnExistingUser(username, "CheckingAccountUsers"):
            data: dict = {
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
             
    
    def addLoanAccountUser(self, full_name: str, username: str, password: str, email: str, phone:str, account_id: str\
                           , loan_taken: float, amount_repayed: float, repayment_deadline: str):
        """
        Add a new loan account user to the database.

        Args:
            full_name (str): Full name of the user.
            username (str): Username of the user.
            password (str): Password of the user.
            email (str): Email of the user.
            phone (str): Phone number of the user.
            account_id (str): Account ID of the user.
            loan_taken (float): Loan amount taken by the user.
            amount_repayed (float): Amount repaid by the user.
            repayment_deadline (str): Repayment deadline of the user.

        Returns:
            bool: True if the user is added successfully, False otherwise.
        """
        if not self.isAnExistingUser(username, "LoanAccountUsers"):
            data: dict = {
                "Name": full_name,
                "Username": username,
                "Password": password,
                "Email": email,
                "Phone": phone,
                "AccountID": account_id,
                "LoanTaken": loan_taken,
                "RepaymentDeadline": self.dateToStrObj(repayment_deadline),
                "AmountRepayed": amount_repayed
            }
            return self.__addData(DataHandler.user_file, "LoanAccountUsers", data)

    def addTransaction(self, sender: str, s_account_id: str, receiver: str, r_account_id: str, operation_type: str\
                       , amount: float, date: str):
        """
        Add a transaction to the transaction history.

        Args:
            sender (str): Sender's username.
            s_account_id (str): Sender's account ID.
            receiver (str): Receiver's username.
            r_account_id (str): Receiver's account ID.
            operation_type (str): Type of operation.
            amount (float): Amount of the transaction.
            date (str): Date of the transaction.

        Returns:
            bool: True if the transaction is added successfully.
        """
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
        """
        Check if a user already exists in the given account type.

        Args:
            username (str): Username of the user to check.
            account_type (str): Account type to check.

        Returns:
            bool: True if the user exists, False otherwise.
        """
        if self.__dataChecker(DataHandler.user_file, "LoanAccountUsers", "Username", username) or \
           self.__dataChecker(DataHandler.user_file, "SavingAccountUsers", "Username", username) or \
           self.__dataChecker(DataHandler.user_file, "CheckingAccountUsers", "Username", username):
            return True
        else:
            return False

    def getUsersData(self, username: str, account_type: str):
        """
        Get user's data from the database.

        Args:
            username (str): Username of the user.
            account_type (str): Account type of the user.

        Returns:
            list: List of user data.
        """
        return self.__dataChecker(DataHandler.user_file, account_type, "Username", username)

    def updateUserData(self, data: dict, account_type: str) -> str:
        """
        Update user's data in the database.

        Args:
            data (dict): Updated user data.
            account_type (str): Account type of the user.

        Returns:
            str: Success message if the data is updated successfully.
        """
        with open(DataHandler.user_file, "r+") as file:
            database = json.load(file)
            for user in database[account_type]:
                if user["Username"] == data["Username"]:
                    modified_data: dict = user
                    database[account_type].remove(user)
                    break
                    
            for change in data:
                modified_data[change] = data[change]
            
            database[account_type].extend([modified_data])
            file.seek(0)
            file.truncate()
            json.dump(database, file, indent=4)
            
            return "Successfully Changed."

    def getUsersTransactionHistory(self, username: str) -> list:
        """
        Get the transaction history of a user.

        Args:
            username (str): Username of the user.

        Returns:
            list: List of user's transaction history.
        """
        transactions: list = self.__dataChecker("Transactions.json", "Transactions", "SenderUsername", username)
        transactions.extend(self.__dataChecker("Transactions.json", "Transactions", "ReceiverUsername", username))
        return transactions

    def __addTransactions(self, file_name: str, table: str, details: dict) -> str:
        """
        Add transaction details to the transaction file.

        Args:
            file_name (str): Name of the transaction file.
            table (str): Name of the table in the file.
            details (dict): Transaction details to add.

        Returns:
            str: Success message.
        """
        with open(file_name, "r+") as file:         
            data = json.load(file)
            data[table].extend([details])
            file.seek(0)
            json.dump(data, file, indent=4)
            return True

    def __addData(self, file_name: str, table: str, details: dict) -> str:
        """
        Add user details to the user file.

        Args:
            file_name (str): Name of the user file.
            table (str): Name of the table in the file.
            details (dict): User details to add.

        Returns:
            str: Success message.
        """
        if self.isAnExistingUser(details["Username"], table):
            return False
        
        with open(file_name, "r+") as file:         
            data = json.load(file)
            data[table].extend([details])
            file.seek(0)
            json.dump(data, file, indent=4)
            return True

    def __dataChecker(self, file_name: str, table: str, key: str, value: str) -> list:
        """
        Check if a data entry exists in the given table.

        Args:
            file_name (str): Name of the file to check.
            table (str): Name of the table to check.
            key (str): Key to compare.
            value (str): Value to compare.

        Returns:
            list: List of matching entries.
        """
        with open(file_name, "r") as file:
            database: dict = json.load(file)
            results: list = []
            for data in database[table]:
                if value == data[key]:
                    results.append(data)
            
        return results

    def getAllTheUsers(self, table: str) -> list:
        """
        Get all users' data from the given table.

        Args:
            table (str): Name of the table to retrieve data from.

        Returns:
            list: List of all users' data.
        """
        with open(DataHandler.user_file, "r") as file:
            database: dict = json.load(file)
            result: list = []
            for data in database[table]:
                temp = list(data.values())
                del temp[2]  # Deletes the Password
                result.append(temp)
        
        return result

    def strToDateObj(self, str_date: str) -> date:
        """
        Convert a string date to a date object.

        Args:
            str_date (str): String date to convert.

        Returns:
            date: Date object.
        """
        if isinstance(str_date, date):
            return str_date
        
        temp1 = str_date.split("-")
        temp2 = []
        for i in temp1:
            temp2.append(int(i))
        
        return date(*temp2)

    def dateToStrObj(self, date_obj: date) -> str:
        """
        Convert a date object to a string.

        Args:
            date_obj (date): Date object to convert.

        Returns:
            str: String representation of the date.
        """
        return str(date_obj)
