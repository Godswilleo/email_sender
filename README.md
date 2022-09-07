# EMAIL SENDER

## INTRODUCTION
This program is used to send emails using the python inbuilt
smtp library. In this program the, the email is routed through
the gmail smtp server.

It can send message to multiple recipients at once.

Also a custom Sender name different from the sender's email address can be specified

## REQUIREMENTS

### DEPENDENCIES
The following modules are required
* smtplib
  This is used to access the SMTP Server
* SSL
   This is used to ensure that the SMTP Server is accessed in a secured way

Both libraries are inbuilt in python and so doesn't required any installation

### GMAIL LOGIN
Also the logon details to the gmail to be used for sending the email are required
* The email address
* password

The password to be used here is not the usual password used to access the gmail account.
Gmail allows third party access into the account using a seperate password. 
The password can be gotten by logging into the gmail account 
Click Settings > Security > App Passwords > Select App, 
in the input provided enter "python" or anything you choose, then click Generate.

This will generate a password. This is the password that should be used for the app.

During the process above, gmail may prompt you to re-login into the email account, go ahead and do it.

## EXPANDING THE PROGRAM
### PASSWORD
For more security, the password can be passed in as an environment variable so as not to input it directly as a plain string in the program.

### FRONT END
A frontend can be created from where the email addresses of the sender both the sender and the recipients along with the required password 
are passed into the program
