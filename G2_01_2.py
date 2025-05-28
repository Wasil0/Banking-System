import random
from abc import ABC, abstractmethod
from datetime import date
from G2_01_1 import DataHandler


class Account(ABC):
    """
    Abstract base class representing a generic account.
    """

    today: date = date.today()

    def __init__(self, full_name: str, username: str, password: str, email: str, phone: str, balance: float = 0, account_id: str = None) -> None:
        """
        Initializes an instance of the Account class.

        Args:
            full_name (str): The full name of the account holder.
            username (str): The username for the account.
            password (str): The password for the account.
            email (str): The email address of the account holder.
            phone (str): The phone number of the account holder.
            balance (float, optional): The initial account balance. Defaults to 0.
            account_id (str, optional): The account ID. If not provided, a random account number will be generated.
                Defaults to None.
        """
        self._account_number: str = account_id or self.generateAccountNumber()
        self._full_name: str = full_name
        self._username: str = username
        self._password: str = password
        self._email: str = email
        self._phone: str = phone
        self._balance: float = balance
        self.dataclass_obj: DataHandler = DataHandler()

    def balanceEnquiry(self):
        """
        Retrieves the account balance.

        Returns:
            float: The account balance.
        """
        return self._balance

    @property
    def AccountNumber(self):
        """
        Property representing the account number.

        Returns:
            str: The account number.
        """
        return self._account_number

    @abstractmethod
    def deposit(self, account_type: str, amount: float, acc_details: dict) -> bool:
        """
        Abstract method for depositing funds into the account.

        Args:
            account_type (str): The type of the account.
            amount (float): The amount to be deposited.
            acc_details (dict): The account details.

        Returns:
            bool: True if the deposit is successful, False otherwise.
        """
        self.dataclass_obj.updateUserData(data=acc_details, account_type=account_type)
        self.dataclass_obj.addTransaction(self._username, self._account_number, None, None, "Deposit", amount, Account.today)
        return True

    def generateAccountNumber(self):
        """
        Generates a random account number.

        Returns:
            str: The generated account number.
        """
        temp: str = ""
        for i in range(0, 8):
            temp += str(random.randint(0, 9))
        return temp

    @abstractmethod
    def withdraw(self, account_type: str, amount: float, details: dict) -> str:
        """
        Abstract method for withdrawing funds from the account.

        Args:
            account_type (str): The type of the account.
            amount (float): The amount to be withdrawn.
            details (dict): The account details.

        Returns:
            str: The result of the withdrawal operation.
        """
        self.dataclass_obj.updateUserData(data=details, account_type=account_type)
        self.dataclass_obj.addTransaction(self._username, self._account_number, None, None, "Withdraw", amount, Account.today)
        return True

    @abstractmethod
    def moneyTransfer(self, receiver_acc_type: str, receiver_acc_id: str, receiver_username: str, amount: float):
        """
        Abstract method for transferring money to another account.

        Args:
            receiver_acc_type (str): The type of the receiver account.
            receiver_acc_id (str): The ID of the receiver account.
            receiver_username (str): The username of the receiver.
            amount (float): The amount to be transferred.

        Returns:
            bool: True if the transfer is successful, False otherwise.
        """
        receiver_data = self.dataclass_obj.getUsersData(receiver_username, receiver_acc_type)
        receiver_data[0]["Balance"] += amount
        self.dataclass_obj.updateUserData(receiver_data[0], receiver_acc_type)
        self.dataclass_obj.addTransaction(self._username, self._account_number, receiver_username, receiver_acc_id\
                , "MoneyTransfer", amount, Account.today)

        return True

    @classmethod
    @abstractmethod
    def existingAccountHolder(cls):
        """
        Abstract class method for handling existing account holders.
        """
        ...
        

    @abstractmethod
    def isANewUser(self):
        """
        Abstract method for checking if the user is a new user.

        Returns:
            bool: True if the user is a new user, False otherwise.
        """
        ...
