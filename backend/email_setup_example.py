#               *** NEED TO STUDY THIS AND UNDERSTAND IT ***

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import formataddr

def send_email(sender_email, sender_name, receiver_email, subject, body, smtp_server, smtp_port, smtp_username, smtp_password):
    # Create a MIMEText object for the email body
    email_body = MIMEText(body, "plain")

    # Create a MIMEMultipart message and add the sender, receiver, subject, and body
    message = MIMEMultipart()
    message["From"] = formataddr((sender_name, sender_email))
    message["To"] = receiver_email
    message["Subject"] = subject
    message.attach(email_body)

    try:
        # Establish a connection to the SMTP server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Upgrade the connection to a secure TLS connection
        server.login(smtp_username, smtp_password)  # Authenticate with the SMTP server

        # Send the email
        server.sendmail(sender_email, receiver_email, message.as_string())

        # Close the connection
        server.quit()

        print("Email sent successfully!")
    except Exception as e:
        print(f"Error sending email: {e}")

# Example usage
sender_email = "your_email@example.com"
sender_name = "Your Name"
receiver_email = "recipient@example.com"
subject = "Test Email"
body = "This is a test email."
smtp_server = "smtp.example.com"
smtp_port = 587  # Default SMTP port for TLS
smtp_username = "your_smtp_username"
smtp_password = "your_smtp_password"

send_email(sender_email, sender_name, receiver_email, subject, body, smtp_server, smtp_port, smtp_username, smtp_password)
