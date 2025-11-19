import smtplib

# send email alert
def send_mail_alert():
    sender_email = "stellamic1998@gmail.com"
    sender_password = "zzqj gfiv gowb mctz"
    receiver_email = "stellamic1998@gmail.com"

    subject = "ATM Alert: Wrong PIN Attempts"
    body = "Warning! Your ATM PIN was entered incorrectly more than 3 times."

    message = f"Subject: {subject}\n\n{body}"

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, message)
        server.quit()
        print("⚠️ Email alert sent!")

    except Exception as e:
        print("Error sending email:", e)

# ATM PROGRAM

PIN = 4576
attempts = 0
MAX_attempts = 3
balance = 8200

while attempts < MAX_attempts:
    user_pin = int(input("Enter your ATM PIN: "))

    if user_pin == PIN:
        print("PIN verified! Welcome.")
        print(f"Your current balance is: ₹{balance}")
        amount = int(input("Enter amount to withdraw: "))

    if amount <= 0:
        print("Invalid amount!")
    elif amount > balance:
        print("Insufficient balance!")
    elif amount % 100 != 0:
        print("ATM can dispense only multiples of 100.")
    else:
        balance -= amount
        print(f"Please collect your cash: ₹{amount}")
        print(f"Remaining balance: ₹{balance}")
        print("Thank you for using the ATM!")
        break
else:
        attempts += 1
        print(f"Wrong PIN! Attempts left: {MAX_attempts - attempts}")

# If exceeded attempts
if attempts >= MAX_attempts:
    print("❌ ATM Card Blocked! Too many wrong attempts.")
    send_mail_alert()
