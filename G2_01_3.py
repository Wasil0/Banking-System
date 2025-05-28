from datetime import date
from dateutil import relativedelta
from G2_01_2 import Account

class CheckingAccount(Account):
    """
    A class representing a checking account.
    """

    _overdraft_credits_fee = 0.20
    _over_draft_limit = 500

    def __init__(self, full_name: str, username: str, password: str, email: str, phone: str, balance: float = 0\
                 , account_number: str = None, credit_spend: float = 0, repayment_deadline: str = None) -> None:
        """
        Initializes an instance of the CheckingAccount class.

        Args:
            full_name (str): The full name of the account holder.
            username (str): The username for the account.
            password (str): The password for the account.
            email (str): The email address of the account holder.
            phone (str): The phone number of the account holder.
            balance (float, optional): The initial account balance. Defaults to 0.
            account_number (str, optional): The account ID. If not provided, a random account number will be generated.
                Defaults to None.
            credit_spend (float, optional): The amount of credit spent. Defaults to 0.
            repayment_deadline (str, optional): The repayment deadline. Defaults to None.
        """
        Account.__init__(self, full_name, username, password, email, phone, balance, account_number)
        self._credit_amount_spend = credit_spend
        self._repayment_deadline = repayment_deadline

    @classmethod
    def existingAccountHolder(cls, data: dict) -> object:
        """
        Class method for creating an instance of CheckingAccount from existing account holder data.

        Args:
            data (dict): The account holder's data.

        Returns:
            object: An instance of the CheckingAccount class.
        """
        return cls(full_name=data["Name"], username=data["Username"], password=data["Password"]\
                   ,email=data["Email"], phone=data["Phone"], balance=data["Balance"], account_number=data["AccountID"]\
                    ,credit_spend=data["CreditAmountSpend"], repayment_deadline=data["RepaymentDeadline"])

    def _creditsAccumaleted(self):
        """
        Calculates and accumulates the overdraft charges.

        Returns:
            None
        """
        self._overdraft_due = self.__overDraftLimit()

        if self._over_draft_limit == 0:
            return None

        is_due_already_added = self.dataclass_obj.getUsersTransactionHistory(self._username)

        for details in is_due_already_added:
            if (details["OperationType"] == "DueFee" and self.dataclass_obj.strToDateObj(details["Date"]) >= Account.today.month):
                return None

        self._balance -= self._overdraft_due
        data: dict = {"Username": self._username, "Balance": self._balance}
        self.dataclass_obj.updateUserData(data, "CheckingAccount")
        self.dataclass_obj.addTransaction(self._username, self._account_number, None, None\
                                          , "DueFee", self._overdraft_due, Account.today())

    def __overDraftLimit(self) -> float:
        """
        Calculates the overdraft limit based on the credit amount spent.

        Returns:
            float: The overdraft limit.
        """
        return self._credit_amount_spend * CheckingAccount._overdraft_credits_fee


    def deposit(self, amount: float) -> bool:
        """
        Deposits funds into the account.

        Args:
            amount (float): The amount to be deposited.

        Returns:
            bool: True if the deposit is successful, False otherwise.
        """
        if amount < 0:
            return False

        self._credit_amount_spend -= amount
        self._balance += amount

        if self._credit_amount_spend < 0:
            self._credit_amount_spend = 0

        data: dict = {
            "Username": self._username,
            "Balance": self._balance,
            "CreditAmountSpend": self._credit_amount_spend,
        }
        return Account.deposit(self, "CheckingAccountUsers", amount, acc_details=data)

    def repaymentDate(self) -> None:
        """
        Sets the repayment date for the account.

        Returns:
            None
        """
        self._repayment_deadline = Account.today + relativedelta.relativedelta(months=1)

    def withdraw(self, amount) -> str:
        """
        Withdraws funds from the account.

        Args:
            amount (float): The amount to be withdrawn.

        Returns:
            str: The result of the withdrawal operation.
        """
        if amount <= 0:
            return False

        if amount < self._balance:
            self._balance -= amount

        elif (amount < (self._balance + self._over_draft_limit) and self._over_draft_limit >= self._credit_amount_spend):
            amount_to_be_deduced_from_credits = amount - self._balance
            total_credits_spend = self._credit_amount_spend + amount_to_be_deduced_from_credits
            if self._over_draft_limit < total_credits_spend:
                return False

            self.repaymentDate()
            self._balance = -total_credits_spend
            self._credit_amount_spend = total_credits_spend

        data: dict = {
            "Username": self._username,
            "Balance": self._balance,
            "CreditAmountSpend": self._credit_amount_spend,
            "RepaymentDeadline" : self.dataclass_obj.dateToStrObj(self._repayment_deadline)
            }
        return Account.withdraw(self, "CheckingAccountUsers", amount, data)

    def moneyTransfer(self, receiver_acc_type: str, receiver_acc_id: str, receiver_username: str, amount: float):
        """
        Transfers money from the account to another account.

        Args:
            receiver_acc_type (str): The type of the receiver account.
            receiver_acc_id (str): The ID of the receiver account.
            receiver_username (str): The username of the receiver.
            amount (float): The amount to be transferred.

        Returns:
            bool: True if the transfer is successful, False otherwise.
        """
        if self.withdraw(amount):
            return Account.moneyTransfer(self, receiver_acc_type, receiver_acc_id, receiver_username, amount)

        return False

    def isANewUser(self):
        """
        Checks if the user is a new user.

        Returns:
            bool: True if the user is a new user, False otherwise.
        """
        if self._account_number == None:
            self._account_number = Account.generateAccountNumber(self)

        return self.dataclass_obj.addCheckingAccountUser(self._full_name, self._username, self._password\
            , self._email, self._phone, self._account_number, self._balance, self._credit_amount_spend, self._repayment_deadline)


class SavingAccount(Account):
    """
    A class representing a savings account.
    """

    interest_rate = 0.018

    def __init__(self, full_name: str, username: str, password: str, email: str, phone: str, balance: float = 0\
                 , account_number: str = None) -> None:
        """
        Initializes an instance of the SavingAccount class.

        Args:
            full_name (str): The full name of the account holder.
            username (str): The username for the account.
            password (str): The password for the account.
            email (str): The email address of the account holder.
            phone (str): The phone number of the account holder.
            balance (float, optional): The initial account balance. Defaults to 0.
            account_number (str, optional): The account ID. If not provided, a random account number will be generated.
                Defaults to None.
        """
        Account.__init__(self, full_name, username, password, email, phone, balance, account_number)
        self.isANewUser()
        self.__interestAdder()

    @classmethod
    def existingAccountHolder(cls, data: dict) -> object:
        """
        Class method for creating an instance of SavingAccount from existing account holder data.

        Args:
            data (dict): The account holder's data.

        Returns:
            object: An instance of the SavingAccount class.
        """
        return cls(full_name=data["Name"], username=data["Username"], password=data["Password"]\
                   , email=data["Email"], phone=data["Phone"], balance=data["Balance"], account_number=data["AccountID"])

    def deposit(self, amount: float) -> bool:
        """
        Deposits funds into the account.

        Args:
            amount (float): The amount to be deposited.

        Returns:
            bool: True if the deposit is successful, False otherwise.
        """
        if amount <= 0:
            return False

        self._balance += amount
        data = {"Username": self._username, "Balance": self._balance}
        return Account.deposit(self, "SavingAccountUsers", amount, data)

    def withdraw(self, amount: float) -> bool:
        """
        Withdraws funds from the account.

        Args:
            amount (float): The amount to be withdrawn.

        Returns:
            bool: The result of the withdrawal operation.
        """
        if amount <= 0:
            return False

        if self._balance < amount:
            return False

        self._balance -= amount
        data: dict = {"Username": self._username, "Balance": self._balance}
        return Account.withdraw(self, "SavingAccountUsers", amount, data)

    def interestCalculator(self):
        """
        Calculates the interest amount.

        Returns:
            float: The interest amount.
        """
        return round(self._balance * SavingAccount.interest_rate, 2)

    def __interestAdder(self) -> None:
        """
        Adds interest to the account.

        Returns:
            None
        """
        funds = self.dataclass_obj.getUsersTransactionHistory(self._username)
        for fund in funds:
            if (fund["OperationType"] == "InterestDeposit" and self.dataclass_obj.strToDateObj\
                (fund["Date"]).month >= Account.today.month):
                return None

        interest = self.interestCalculator()
        if interest > 0:
            self._balance += interest
            data: dict = {"Username": self._username, "Balance": self._balance}
            self.dataclass_obj.updateUserData(data, "SavingAccountUsers")
            self.dataclass_obj.addTransaction(self._username, self._account_number, None, None\
                , "InterestDeposit", interest, Account.today)

    def moneyTransfer(self, receiver_acc_type: str, receiver_acc_id: str, receiver_username: str, amount: float) -> bool:
        """
        Transfers money from the account to another account.

        Args:
            receiver_acc_type (str): The type of the receiver account.
            receiver_acc_id (str): The ID of the receiver account.
            receiver_username (str): The username of the receiver.
            amount (float): The amount to be transferred.

        Returns:
            bool: True if the transfer is successful, False otherwise.
        """
        if self.withdraw(amount):
            return Account.moneyTransfer(self, receiver_acc_type, receiver_acc_id, receiver_username, amount)

        return False

    def isANewUser(self):
        """
        Checks if the user is a new user.

        Returns:
            bool: True if the user is a new user, False otherwise.
        """
        return self.dataclass_obj.addSavingAccountUser(self._full_name, self._username, self._password, self._email\
                , self._phone, self._account_number, self._balance)


class LoanAccount(Account):
    """
    A class representing a loan account.
    """

    __due_charges = 0.23

    def __init__(self, full_name: str, username: str, password: str, email: str, phone: str, loan_amount: float\
                 , account_number: str = None, repayment_deadline: str = 0, amount_repayed: float = 0) -> None:
        """
        Initializes an instance of the LoanAccount class.

        Args:
            full_name (str): The full name of the account holder.
            username (str): The username for the account.
            password (str): The password for the account.
            email (str): The email address of the account holder.
            phone (str): The phone number of the account holder.
            loan_amount (float): The loan amount.
            account_number (str, optional): The account ID. If not provided, a random account number will be generated.
                Defaults to None.
            repayment_deadline (str, optional): The repayment deadline. Defaults to 0.
            amount_repayed (float, optional): The amount repaid. Defaults to 0.
        """
        Account.__init__(self, full_name, username, password, email, phone, -loan_amount, account_number)
        repayment_date = repayment_deadline or self.__loanDeadlineCalculator(3)
        self._repayment_deadline: date = self.dataclass_obj.strToDateObj(repayment_date)
        self._amount_repayed: float = amount_repayed
        self.isANewUser()
        self.dealineExpired()

    def isANewUser(self):
        """
        Checks if the user is a new user.

        Returns:
            bool: True if the user is a new user, False otherwise.
        """
        return self.dataclass_obj.addLoanAccountUser(self._full_name, self._username, self._password, self._email\
                , self._phone, self._account_number, self._balance, self._amount_repayed, self._repayment_deadline)

    @classmethod
    def existingAccountHolder(cls, data: dict) -> object:
        """
        Class method for creating an instance of LoanAccount from existing account holder data.

        Args:
            data (dict): The account holder's data.

        Returns:
            object: An instance of the LoanAccount class.
        """
        return cls(full_name=data["Name"], username=data["Username"], password=data["Password"], email=data["Email"]\
                , phone=data["Phone"], loan_amount=data["LoanTaken"], account_number=data["AccountID"]\
                , repayment_deadline=data["RepaymentDeadline"], amount_repayed=data["AmountRepayed"])

    def withdraw(self) -> str:
        """
        Withdraws funds from the account.

        Returns:
            str: The result of the withdrawal operation.
        """
        pass

    def deposit(self, amount):
        """
        Deposits funds into the account.

        Args:
            amount (float): The amount to be deposited.

        Returns:
            bool: True if the deposit is successful, False otherwise.
        """
        if amount <= 0:
            return False

        self._amount_repayed += amount
        data: dict = {"Username": self._username, "AmountRepayed": self._amount_repayed}
        if self._amount_repayed >= self._balance:
            data["LoanTaken"] = 0
            data["RepaymentDeadline"] = None

        return Account.deposit(self, "LoanAccountUsers", amount, data)

    def __loanDeadlineCalculator(self, loan_time) -> None:
        """
        Calculates the repayment deadline for the loan.

        Args:
            loan_time (int): The loan time in months.

        Returns:
            None
        """
        return Account.today + relativedelta.relativedelta(months=loan_time)

    def dealineExpired(self) -> bool:
        """
        Checks if the repayment deadline has expired and adds due charges.

        Returns:
            bool: True if the repayment deadline has expired, False otherwise.
        """
        is_due_already_added: list = self.dataclass_obj.getUsersTransactionHistory(self._username)

        if Account.today >= self._repayment_deadline:
            for details in is_due_already_added:
                try:
                    if (details["OperationType"] == "LoanNotRepayed" and
                        self.dataclass_obj.strToDateObj(details["Date"]).month >= Account.today.month):
                        return False
                
                except KeyError:
                    break
                except ValueError:
                    break
                except IndexError:
                    break
                
            self._due_charges = self._balance * LoanAccount.__due_charges
            self._balance -= self._due_charges

            data: dict = {"Username": self._username, "LoanTaken": self._balance}
            self.dataclass_obj.updateUserData(data, "LoanAccountUsers")
            self.dataclass_obj.addTransaction(self._username, self._account_number, None, None\
                    , "LoanNotRepayed", self.__due_charges, Account.today)
            return True

        return False

    def moneyTransfer(self) -> bool:
        """
        No Money Transfer Method for Loan Account Users.

        Returns:
            bool: False
        """
        pass
