# Python Password Manager

---

#### This is a basic password manager written in python

## By Giancarlo Vigneri

---

## Technologies used

- _Python_
  - _Tkinter_
  - _secrets 😉_
  - _random_
- _JSON_

## Description

_This program allows the user to create and save fairly secure passwords and save them locally on their machines via a custom GUI._

## Setup/Installation Requirements

1. Navigate to (https://github.com/vigneriCodes/python-password-manager)
2. Clone or download 'python-password-manager'
3. Open a command prompt window, navigate to the directory where your Python script is located, and type "python" followed by the filename of your Python script (with the ".py" extension) and press 'Enter'.

   - for example; "python main.py" to run the script "main.py" in the current directory.

## Basic Usage

1. Enter the name of the website in the "Website:" entry field.
2. Adjust the email/username you would like to associate with the new password in the "Email/Username:" entry field. (_Optionally; change the email in line '132' of 'main.py' to be your chosen email for this to populate automatically with your preferred email._)
3. Press the 'Generate Password' button.
4. Press the 'Add'.
5. A messagebox will appear asking if you are satisfied with the information entered/password generated. Click 'OK' if you are 'Cancel' if not satisfied.
6. A file called "data.json" will be generated on your machine with the information saved in the JSON format. _**Conversely if that file already exists; the file will be updated with the new information.**_
7. Your new password will be saved to the clipboard and be availabale to paste if wanted ('ctrl-v').
8. Repeat steps 1-6 to add more websites and passwords.

## Search Functionality

_You may also use the GUI to search for saved passwords:_

1. Enter the name of the website you wish to search for in the "Website:" entry field.
2. Press the 'Search' button.
3. If found; a messagebox will appear with the relevant information displayed as well as the password saved to the clipboard for easy pasting ('ctrl-v').

---

## Known Bugs

- no known bugs

## License [GPL] (https://choosealicense.com/licenses/gpl-3.0/)

_if you do run into any issues or have questions, ideas, or concerns; I would greatly encourage you to send feedback or make a contribution to the code_

## Contact Information

_Contact Giancarlo Vigneri at: vignericodes@gmail.com_
