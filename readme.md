------------Bank Application using PySide6---------------

# Nova Banking

- The Bank Application is a graphical user interface (GUI) application built using PySide6, a Python binding for the Qt framework. 
- This application provides users with a convenient and intuitive way to manage their banking activities.

## Requirements

- Minimum Screen Resolution should be 1080p or higher.
- Python and its interpreter should be set up.
- PY Modules including [PySide6, dateutil, fpdf2] should also be installed for this application to run.


## Admin Access - Instructions

- Username: asta
- Password: shinobu
- Don't select any account type for Admin access, otherwise, you won't be able to log in.
- Select one of the Account Types to print the Database of that Account type.
- Printed database will be saved in the form of a PDF, with the folder named of the Account type.( eg: SavingAccountUsers.pdf )


## User Access

- A User can create one of the types of Account: Loan, Checking, or Saving.
- Try to choose a unique username, as the application does not allow redundant usernames.
- Fill all the fields and click signup. Then, enter the initial amount which will be added to their created account.
- For Loan Account Users, that amount will be considered as the Taken Loan.
- Money Transfer is available between Checking and Saving Account Users.
- By entering the amount on the right input field in the Dashboard, Checking and Saving Account holders can deposit or withdraw.
- Loan Account Users can only use the Deposit option to repay their loans.
- Users can also see their Transaction Histories.


## Files

- Files named with UI contain GUI Layout and Styling of the Application Screens.
- Files named with rc are the resource files used for icons and background stuff.
- The file named `G2_01_13main.py` is the main file that uses the Modules and runs the GUI application.
- The `Backend` folder contains the data handling and Account classes implemented for CLI testing.
- The `DataFiles` folder contains the data files for CLI implementations.
- G2_01_1 : DataHandling File
- G2_01_2 : Account File
- G2_01_3 : BankClasses File
- G2_01_6 : Report Generator File
- G2_01_13main : Main File containing all the GUI driver classses and application.
- All the other files are used to create the layout and UI.

## GUI

- For GUI, run the `G2_01_1.py` file with the above requirements.
- Files inside the Main Folder are modified to handle the GUI implementation.


## Warning

- Don't mess with the following files:
  - Files named with UI contain GUI Layout and Styling of the Application Screens.
  - Files named with rc are the resource files used for icons and background stuff.


## About Us
- Main Developer - asta - khan4530215@cloud.neduet.edu.pk
- Debugging - Prototype - +92 330 3148501
- Docstrings and Ideas - sahil - wasil4506229@cloud.neduet.edu.pk