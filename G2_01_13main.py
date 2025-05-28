## Admin Username : asta
## Admin Password : shinobu
## Don't Select Any accout type for admin


import sys
import time
from G2_01_3 import CheckingAccount, SavingAccount, LoanAccount
from G2_01_1 import DataHandler
from G2_01_06 import PDF
from PySide6.QtCore import QTimer, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QStackedWidget, QDialog, QMessageBox\
    , QTableWidgetItem
from G2_01_09UI import Ui_SplashWindow
from G2_01_07UI import Ui_SignIn
from G2_01_08UI import Ui_SignUp   
from G2_01_04UI import Ui_InitialMoney   
from G2_01_11UI import Ui_UserDashboard
from G2_01_05UI import Ui_MoneyTransfer
from G2_01_12UI import Ui_Admin
from G2_01_10UI import Ui_Transactions
        

class SplashScreen(QMainWindow):
    def __init__(self) -> None:
        QMainWindow.__init__(self)
        self.count = 0
        self.splash_screen = Ui_SplashWindow()
        self.splash_screen.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.splashScreen()
        self.show()

    def splashScreen(self):
        """
        Displays the loading bar and main screen during startup.
        """
        self.timer_1 = QTimer()
        self.timer_1.setInterval(30)
        self.timer_1.start()
        
        self.splash_screen.AppLoadingBar.setValue(self.count)
        self.timer_1.timeout.connect(self.counter)
        
        
    def counter(self):
        """
        Update the loading bar value and switch to the login screen when the loading is complete.
        """
        self.count += 1
        self.splash_screen.AppLoadingBar.setValue(self.count)
        if self.count == 100:
            self.timer_1.stop()
            self.signin()
            self.close()
            
    
    def signin(self):
        """
        Switch to the sign-in screen.
        """
        # Making the the variable global to manage all the UI screens across the code.
        global MainApplication  
        MainApplication = BankApplication()
       
       
class SignIN(QMainWindow):

    def __init__(self, stacked_widget) -> None:
        QMainWindow.__init__(self)
        self.stacked_widget = stacked_widget
        self.sign_in = Ui_SignIn()
        self.sign_in.setupUi(self)
        self.sign_in.close_btn.clicked.connect(lambda: MainApplication.close())
        self.sign_in.login_btn.clicked.connect(self.userVerify)
        self.sign_in.register_btn.clicked.connect(self.signup)
        self.show()


    def userVerify(self):
        """
        Verify the user credentials and switch to the user dashboard if the credentials are correct.
        Displays messagebox errors if not.
        """
        account_type_checker: dict = {"CHECKING ACCOUNT": ["CheckingAccountUsers", CheckingAccount],
                              "SAVINGS ACCOUNT": ["SavingAccountUsers", SavingAccount],
                              "LOAN ACCOUNT": ["LoanAccountUsers", LoanAccount]}
        
        self.data_verify = DataHandler()
        username = self.sign_in.username_field.text()
        password = self.sign_in.password_field.text()
        account = self.sign_in.account_type_comboBox.currentText()
        
        if username == "" or password == "":
            self.messageboxInfo("Username or Password not entered.")
            
        elif username == "asta" and password == "shinobu":
            self.adminboard()
            
        else:
            try:
                user_account_type = account_type_checker[account]
                is_a_user = self.data_verify.isAnExistingUser(username, user_account_type[0])
            except KeyError:
                is_a_user = False
                SignIN.messageboxError("User not found..!")
            except IndexError:
                is_a_user = False
                SignIN.messageboxError("User not found..!")
            
            else:
                if is_a_user:
                    try:
                        data = self.data_verify.getUsersData(username, user_account_type[0])[0]
                    
                    except KeyError:
                        self.messageboxInfo("Username and Password doesnot match")
                    except IndexError:
                        self.messageboxInfo("Username and Password doesnot match")    
                    
                    if password == data["Password"]:
                        self.dashboard(username, user_account_type)

                else:
                    self.messageboxInfo("Username and Password doesnot match")

            
    @staticmethod
    def messageboxInfo(text: str):
        """
        Display an information message box with the given text.
        
        Args:
            text (str): The text to display in the message box.
        """
        msg = QMessageBox()
        msg.setWindowTitle("Info")
        msg.setText(text)
        msg.setIcon(QMessageBox.Information)
        msg.exec()


    def messageboxError(text: str):
        """
        Display an error message box with the given text.
        
        Args:
            text (str): The text to display in the message box.
        """
        msg = QMessageBox()
        msg.setWindowTitle("Error")
        msg.setText(text)
        msg.setIcon(QMessageBox.Critical)
        msg.exec()
    

    def signup(self):
        """
        Switch to the sign-up screen.
        """
        self.sign_in.username_field.clear()
        self.sign_in.password_field.clear()
        self.stacked_widget.setCurrentIndex(1)
        # widget.setCurrentIndex(widget.currentIndex() + 1)


    def dashboard(self, username, account_type):
        """
        Switch to the user dashboard screen.
        
        Args:
            username (str): The username of the user.
            account_type (list): A list containing the account type and its corresponding class.
        """
        self.user_board = UserDashBoard(self.stacked_widget, username, account_type)
        x = self.stacked_widget.addWidget(self.user_board)
        self.stacked_widget.setCurrentIndex(x)
        self.sign_in.username_field.clear()
        self.sign_in.password_field.clear()


    def adminboard(self):
        """
        Switch to the admin dashboard screen.
        """
        self.sign_in.username_field.clear()
        self.sign_in.password_field.clear()
        self.stacked_widget.setCurrentIndex(2)


class SignUP(QWidget):
    def __init__(self, stacked_widget):
        QWidget.__init__(self)
        self.stacked_widget = stacked_widget
        self.sign_up = Ui_SignUp()
        self.sign_up.setupUi(self)
        self.sign_up.close_btn.clicked.connect(lambda: MainApplication.close())
        self.sign_up.sign_up_btn.clicked.connect(self.createAccount)
        self.sign_up.back_btn.clicked.connect(self.backLogin)
       
        
    def createAccount(self):
        """
        Create a new user account.
        """
        account_checker: dict = {"CHECKING ACCOUNT": ["CheckingAccountUsers", CheckingAccount],
                              "SAVINGS ACCOUNT": ["SavingAccountUsers", SavingAccount],
                              "LOAN ACCOUNT": ["LoanAccountUsers", LoanAccount]}
        
        self.data_verify = DataHandler()        
        fullname = self.sign_up.fullname_field.text()
        username = self.sign_up.username_field.text()
        email = self.sign_up.email_field.text()
        password = self.sign_up.password_field.text()
        phone = self.sign_up.phone_field.text()
        account = self.sign_up.account_type_comboBox.currentText()
        
        if fullname == "" or username == "" or email == "" or password == ""\
            or phone == "" or account == "ACCOUNT TYPE":
                print("Field is Empty")
                
        else:
            self.data_check = DataHandler()
            account_type = account_checker[account]
            
            data = self.data_check.isAnExistingUser(username, account_type[0])
                    
            if data:
                SignIN.messageboxInfo("Username Already Exist.")
        
            else:
                self.initial_money = InitialDeposit(fullname, username, email, phone, password, account_type)
                self.initial_money.show()
                
                
    def backLogin(self):
        self.stacked_widget.setCurrentIndex(0)

        

class InitialDeposit(QWidget):
    """
        Args:
        full_name (str): The full name of the user.
        username (str): The username of the user.
        email (str): The email address of the user.
        password (str): The password of the user.
        phone (str): The phone number of the user.
    """
    def __init__(self, fullname, username, email, phone, password, account_type):
        QWidget.__init__(self)
        self.full_name = fullname
        self.username = username
        self.email = email
        self.phone = phone
        self.password = password
        self.account_type = account_type
        self.initial_deposit = Ui_InitialMoney()
        self.initial_deposit.setupUi(self)
        self.initial_deposit.create_account_btn.clicked.connect(self.accountCreation)

     
    def accountCreation(self):
        """
        Create a new account with an initial deposit.
        """
        try:
            starting_balance = float(self.initial_deposit.initial_balance_field.text())
        except ValueError:
            starting_balance = 0
        except TypeError:
            starting_balance = 0       
        finally:
            self.account_creator = self.account_type[1](self.full_name, self.username, self.password, self.email, self.phone, starting_balance)
            self.account_creator.isANewUser()
            SignIN.messageboxInfo("Your Account is created, go to the login page.")           
            time.sleep(2)
            self.close()
            

class UserDashBoard(QWidget):
    def __init__(self, stacked_widget, username, account_type):
        QWidget.__init__(self)
        self.username = username
        self.account_type = account_type
        self.stacked_widget = stacked_widget
        self.user_dashboard = Ui_UserDashboard()
        self.user_dashboard.setupUi(self)
        self.user_dashboard.close_btn.clicked.connect(lambda: MainApplication.close())
        self.user_dashboard.logout_btn.clicked.connect(self.logout)
        self.user_dashboard.helpdesk_btn.clicked.connect(self.helpdeskNumber)
        self.user_dashboard.money_transfer_btn.clicked.connect(self.moneytransferpage)
        self.user_dashboard.show_transactions_btn.clicked.connect(self.transactionPage)
        self.accountConnected()
        self.show()
    
          
    def helpdeskNumber(self):
        """
        Display the helpdesk number in a message box.
        """
        
        # A QDialog Box showing the email.
        SignIN.messageboxInfo("You can contact us on our whatsapp number: 03403489016")
             
        
    def accountConnected(self):
        """
        Connect the user account to the user dashboard screen.
        """
        gui_functions: dict = {"CheckingAccountUsers": self.checkingGUI, 
                               "SavingAccountUsers": self.savingsGUI,
                               "LoanAccountUsers": self.loanGUI}
        self.__data_handler = DataHandler()
        self.account_data = self.__data_handler.getUsersData(self.username, self.account_type[0])[0]
        self.connected_account = self.account_type[1].existingAccountHolder(self.account_data)
        gui_functions[self.account_type[0]]()
       
    
    def checkingGUI(self):
        """
        Display the checking account details on the user dashboard screen.
        """
        self.user_dashboard.username_lbl.setText(self.connected_account._username)
        self.user_dashboard.account_number_lbl.setText(f"ACCOUNT NUMBER : {self.connected_account._account_number}")
        self.user_dashboard.balance_lbl.setText(f"BALANCE : ${self.connected_account._balance}")
        self.user_dashboard.time_period_lbl.setText(f"RETURN PERIOD : {self.connected_account._repayment_deadline}")
        self.user_dashboard.different_balance_scheme_lbl.setText(f"CREDIT AMOUNT SPEND: ${self.connected_account._credit_amount_spend}")
        self.user_dashboard.account_type_lbl.setText("CHECKING ACCOUNT")
        self.user_dashboard.deposit_btn.clicked.connect(self.checkingDeposit)
        self.user_dashboard.withdraw_btn.clicked.connect(self.checkingWithdraw)
    
    
    def savingsGUI(self):
        """
        Display the savings account details on the user dashboard screen.
        """
        self.user_dashboard.username_lbl.setText(self.connected_account._username)
        self.user_dashboard.account_number_lbl.setText(f"ACCOUNT NUMBER : {self.connected_account._account_number}")
        self.user_dashboard.balance_lbl.setText(f"BALANCE : ${self.connected_account._balance}")
        self.user_dashboard.time_period_lbl.setText(f"INTEREST PERIOD : 1 Month")
        self.user_dashboard.different_balance_scheme_lbl.setText(f"ESTIMATED INTEREST: ${self.connected_account.interestCalculator()}")
        self.user_dashboard.account_type_lbl.setText("SAVING ACCOUNT")
        self.user_dashboard.deposit_btn.clicked.connect(self.savingDeposit)
        self.user_dashboard.withdraw_btn.clicked.connect(self.savingWithdraw)
           
    
    def loanGUI(self):
        """
        Display the loan account details on the user dashboard screen.
        """
        self.user_dashboard.username_lbl.setText(self.connected_account._username)
        self.user_dashboard.account_number_lbl.setText(f"ACCOUNT NUMBER : {self.connected_account._account_number}")
        self.user_dashboard.balance_lbl.setText(f"LOAN TAKEN : ${self.connected_account._balance}")
        self.user_dashboard.time_period_lbl.setText(f"REPAYMENT DEADLINE : {self.connected_account._repayment_deadline}")
        self.user_dashboard.different_balance_scheme_lbl.setText(f"AMOUNT REPAYED : ${self.connected_account._amount_repayed}")
        self.user_dashboard.account_type_lbl.setText("LOAN ACCOUNT")
        self.user_dashboard.deposit_btn.clicked.connect(self.loanRepayment)
        self.user_dashboard.withdraw_btn.setDisabled(True)
        self.user_dashboard.money_transfer_btn.setDisabled(True)

    
    def deposit(self):
        """
        Perform a deposit into the connected account.
        """
        self.user_dashboard.deposit_btn.setDisabled(True)
        try:
            amount = float(self.user_dashboard.amount_field.text())
        except ValueError or TypeError:
            self.user_dashboard.amount_field.clear()
        else:
            self.user_dashboard.amount_field.clear()
            self.connected_account.deposit(amount)
            
        self.timerBtnDeposit()
        
        
    def savingDeposit(self):
        """
        Perform a deposit into the savings account.
        """
        self.deposit()
        self.user_dashboard.balance_lbl.setText(f"BALANCE : ${self.connected_account._balance}")
        self.user_dashboard.different_balance_scheme_lbl.setText(f"ESTIMATED INTEREST: ${self.connected_account.interestCalculator()}")
               
                
    def savingWithdraw(self):
        """
        Perform a withdrawal from the savings account.
        """
        self.withdraw()
        self.user_dashboard.different_balance_scheme_lbl.setText(f"ESTIMATED INTEREST: ${self.connected_account.interestCalculator()}")
            
    
    def loanRepayment(self):
        """
        Perform a repayment into the loan account.
        """
        self.deposit()
        self.user_dashboard.balance_lbl.setText(f"LOAN TAKEN : ${self.connected_account._balance}")
        self.user_dashboard.different_balance_scheme_lbl.setText(f"AMOUNT REPAYED : ${self.connected_account._amount_repayed}")
        self.user_dashboard.time_period_lbl.setText(f"REPAYMENT DEADLINE : {self.connected_account._repayment_deadline}")
        if self.connected_account._balance == self.connected_account._amount_repayed:
            self.user_dashboard.deposit_btn.clicked.connect(lambda: SignIN.messageboxInfo("Your Loan is repayed. Can't deposit Money."))
            SignIN.messageboxInfo("Hurray You have repayed all the loan amount.")
 
    
    def checkingDeposit(self):
        """
        Perform a deposit into the checking account.
        """
        self.deposit()
        self.user_dashboard.balance_lbl.setText(f"BALANCE : ${self.connected_account._balance}")
        self.user_dashboard.different_balance_scheme_lbl.setText(f"CREDIT AMOUNT SPEND: ${self.connected_account._credit_amount_spend}")
        self.user_dashboard.time_period_lbl.setText(f"RETURN PERIOD : {self.connected_account._repayment_deadline}")

        
    def checkingWithdraw(self):
        """
        Perform a withdrawal from the checking account.
        """
        self.withdraw()
        self.user_dashboard.different_balance_scheme_lbl.setText(f"CREDIT AMOUNT SPEND: ${self.connected_account._credit_amount_spend}")
        self.user_dashboard.time_period_lbl.setText(f"RETURN PERIOD : {self.connected_account._repayment_deadline}")
        
                
    def withdraw(self):
        """
        Perform a withdrawal from the connected account.
        """
        self.user_dashboard.withdraw_btn.setDisabled(True)
        try:
            amount = float(self.user_dashboard.amount_field.text())
        except ValueError:
            self.user_dashboard.amount_field.clear()
        except TypeError:
            self.user_dashboard.amount_field.clear()
        else:
            self.connected_account.withdraw(amount)
            self.user_dashboard.amount_field.clear()
            self.user_dashboard.balance_lbl.setText(f"BALANCE : ${self.connected_account._balance}")
        
        
        self.timerBtnWithdraw()
           
                
    def moneytransferpage(self):
        """
        Switch to the money transfer page.
        """
        self.moneytransfer = MoneyTranfer(self.connected_account)
        self.moneytransfer.show()


    def transactionPage(self):
        """
        Switch to the transaction history page.
        """
        self.transaction_screen = TransactionScreen(self.stacked_widget, self.connected_account._username)
        self.stacked_widget.addWidget(self.transaction_screen)
        self.stacked_widget.setCurrentIndex(self.stacked_widget.currentIndex() + 1)
              
        
    def logout(self):
        """
        Switch back to the sign-in screen.
        """
        self.stacked_widget.setCurrentIndex(0)    
        
        
    def timerBtnDeposit(self):
        """
        Enable the deposit button after a specified time interval.
        """
        self.timer = QTimer()
        self.timer.setInterval(300)
        self.timer.start()
        self.timer.timeout.connect(lambda: self.user_dashboard.deposit_btn.setEnabled(True))
        if self.user_dashboard.deposit_btn.isEnabled():
            self.timer.stop()
       
    
    def timerBtnWithdraw(self):
        """
        Enable the withdraw button after a specified time interval.
        """
        self.timer = QTimer()
        self.timer.setInterval(300)
        self.timer.start()
        self.timer.timeout.connect(lambda: self.user_dashboard.withdraw_btn.setEnabled(True))
        if self.user_dashboard.withdraw_btn.isEnabled():
            self.timer.stop()
 
        
class MoneyTranfer(QDialog):
    def __init__(self, account_cennected):
        QDialog.__init__(self)
        self.money_transfer = Ui_MoneyTransfer()
        self.account_connected = account_cennected
        self.money_transfer.setupUi(self)
        self.money_transfer.tranfer_money_btn.clicked.connect(self.transfer)
        self.show()
        

    def transfer(self):
        """
        Perform a money transfer from the connected account to another account.
        """
        self.money_transfer.tranfer_money_btn.setDisabled(True)
        r_username = self.money_transfer.receiver_username_field.text()
        r_id = self.money_transfer.receiver_account_id_field.text()
        r_account_type = self.money_transfer.receiver_account_type_comboBox.currentText()
        
        if r_username == "" or r_id == "" or r_account_type == "ACCOUNT TYPE":
            SignIN.messageboxError("Fill All the Fields")

        try:
            amount = float(self.money_transfer.transfer_amount_field.text())
        except ValueError:
            amount = 0
        except TypeError:
            amount = 0
             
        self.account_connected.moneyTransfer(r_account_type, r_id, r_username, amount)
        SignIN.messageboxInfo("Money is Transferred.")
        self.timerbtn()
            
             
    def timerbtn(self):
        """
        Enable the transfer button after a specified time interval.
        """
        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.start()
        self.timer.timeout.connect(lambda: self.money_transfer.tranfer_money_btn.setEnabled(True))
        if self.money_transfer.tranfer_money_btn.isEnabled():
            self.timer.stop()


class TransactionScreen(QWidget):
    def __init__(self, stacked_widget, username):
        QWidget.__init__(self)
        self.username = username
        self.stack_widget = stacked_widget
        self.transaction_screen = Ui_Transactions()
        self.transaction_screen.setupUi(self)
        self.transaction_screen.close_btn.clicked.connect(lambda: MainApplication.close())
        self.transaction_screen.back_to_userdashboard_btn.clicked.connect(self.backToDashboard)
        self.showTransaction()

    def showTransaction(self):
        """
        Display the transaction history of the user.
        """
        data = DataHandler()
        transactions = data.getUsersTransactionHistory(self.username)
        row = 0
        self.transaction_screen.tableWidget.setRowCount(len(transactions))
        for transaction in transactions:
            self.transaction_screen.tableWidget.setItem(row, 0, QTableWidgetItem(transaction["SenderAccountID"]))
            self.transaction_screen.tableWidget.setItem(row, 1, QTableWidgetItem(transaction["SenderUsername"]))
            self.transaction_screen.tableWidget.setItem(row, 2, QTableWidgetItem(transaction["OperationType"]))
            self.transaction_screen.tableWidget.setItem(row, 3, QTableWidgetItem(str(transaction["Amount"])))
            self.transaction_screen.tableWidget.setItem(row, 4, QTableWidgetItem(transaction["ReceiverAccountID"]))
            self.transaction_screen.tableWidget.setItem(row, 5, QTableWidgetItem(transaction["ReceiverUsername"]))
            self.transaction_screen.tableWidget.setItem(row, 6, QTableWidgetItem(transaction["Date"]))
            row += 1
    
    
    def backToDashboard(self):
        """
        Switch back to the user dashboard.
        """
        self.stack_widget.setCurrentIndex(self.stack_widget.currentIndex()-1)
       
    
class Admin(QWidget):
    """
        Admin class represents the admin dashboard in the application.

        Args:
            stacked_widget (QStackedWidget): Reference to the stacked widget for managing UI navigation.
    """
    def __init__(self, stacked_widget):
        QWidget.__init__(self)
        self.admin = Ui_Admin()
        self.stacked_widget = stacked_widget
        self.admin.setupUi(self)
        self.admin.logout_btn.clicked.connect(self.logout)
        self.admin.close_btn.clicked.connect(lambda : MainApplication.close())
        self.admin.print_users_btn.clicked.connect(self.printUsers)
    
    
    def printUsers(self):
        """
        Prints the users of the selected account type in a PDF file.
        """
        self.admin.print_users_btn.setDisabled(True)
        
        if not self.admin.loan_users_radio_btn.isChecked() and not self.admin.saving_users_radio_btn.isChecked()\
            and not self.admin.checking_users_radio_btn.isChecked():
            SignIN.messageboxInfo("Select an account type, to print the users of that account type.")
        
        else:
            if self.admin.loan_users_radio_btn.isChecked():
                self.users_account = "LoanAccountUsers"
                self.headers = ["Name","Username","Email","Phone","AccountID","LoanTaken","RepaymentDeadline","AmountRepayed"]
                
            elif self.admin.saving_users_radio_btn.isChecked():
                self.users_account = "SavingAccountUsers"
                self.headers = ["Name","Username","Email","Phone","AccountID","Balance"]
                
            elif self.admin.checking_users_radio_btn.isChecked():
                self.users_account = "CheckingAccountUsers"
                self.headers = ["Name","Username","Email","Phone","AccountID","Balance","CreditAmountSpend","RepaymentDeadline"]
                
                
            data = DataHandler()
            self.get_users_data = [self.headers] + data.getAllTheUsers(self.users_account)
            self.pdfMaker()
            self.timerbtn()

        
    def timerbtn(self):
        """
        Enables the print users button after a timeout and stops the timer.
        """
        self.timer = QTimer()
        self.timer.setInterval(3000)
        self.timer.start()
        self.timer.timeout.connect(lambda: self.admin.print_users_btn.setEnabled(True))
        if self.admin.print_users_btn.isEnabled():
            self.timer.stop()
   
   
    def pdfMaker(self):
        """
        Creates a PDF file with the user data in a table format.
        """
        self.pdf = PDF(format="letter")
        self.pdf.add_page()
        self.pdf.create_table(self.users_account, self.get_users_data)
 
   
    def logout(self):
        """
            Logs out the admin user and switches to the sign-in screen.
        """
        self.close()
        self.stacked_widget.setCurrentIndex(0)


class BankApplication(QMainWindow):
    """
        Main driver class. Basically runs the whole program.
    """
    def __init__(self):
        QMainWindow.__init__(self)       
        self.widget = QStackedWidget()
        self.setCentralWidget(self.widget)
        self.signin = SignIN(self.widget)
        self.signup = SignUP(self.widget)
        self.admin_board = Admin(self.widget)

        self.widget.addWidget(self.signin)
        self.widget.addWidget(self.signup)
        self.widget.addWidget(self.admin_board)
        self.setMinimumSize(1000,680)
        self.setMaximumSize(1000,680)
        self.setStyleSheet("background-color: qlineargradient(spread:reflect, x1:0.392, y1:0.836, x2:1, y2:0, stop:0 rgba(151,150,240, 255), stop:1 rgba(251, 199, 212, 255));")
        self.setWindowFlag(Qt.FramelessWindowHint)

        
        self.setWindowTitle("Banking System")
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SplashScreen()
    # window.show()
    sys.exit(app.exec())

   
   
   
   
   
   