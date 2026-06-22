import yagmail

sender = "your_email@gmail.com"
password = "app_password"

receiver = "supervisor@gmail.com"

subject = "SafetyEye Alert"

body = """
Worker without Helmet detected.
Check dashboard immediately.
"""

yag = yagmail.SMTP(
    sender,
    password
)

#yag.send(
 #   receiver,
  #  subject,
  #  body
#)
print("Email alerts disabled")