# Build an Email Simulator
# Description:
'''
# 📧 Email Simulator (Python OOP Project)

## 📌 Overview
This project is a simple **Email Simulator** built using Python and Object-Oriented Programming (OOP). It models a basic email system where users can send emails, receive them in an inbox, read messages, and delete them.

---

## 🧱 Features

- Create users with individual inboxes
- Send emails between users
- Automatically timestamp emails
- Track read/unread status
- View inbox with formatted email list
- Read full email details
- Delete emails from inbox

---

## 🏗️ Project Structure

### 📩 Email Class
Represents a single email message.

**Attributes:**
- sender
- receiver
- subject
- body
- timestamp (auto-generated)
- read status

**Methods:**
- `mark_as_read()` → Marks email as read
- `display_full_email()` → Shows full email details
- `__str__()` → Returns formatted email summary

---

### 📥 Inbox Class
Manages all received emails for a user.

**Methods:**
- `receive_email(email)` → Adds email to inbox
- `list_emails()` → Displays all emails
- `read_email(index)` → Opens a specific email
- `delete_email(index)` → Removes an email

---

### 👤 User Class
Represents a system user.

**Methods:**
- `send_email(receiver, subject, body)` → Sends email to another user
- `check_inbox()` → Displays inbox
- `read_email(index)` → Reads a specific email
- `delete_email(index)` → Deletes an email

---

## 🔄 How It Works

1. A user sends an email using `send_email()`
2. An `Email` object is created with sender, receiver, subject, and body
3. The email is delivered to the receiver’s inbox
4. The receiver can:
   - View emails
   - Read emails
   - Delete emails
'''

# Source code:
import datetime

class Email:
    def __init__(self, sender, receiver, subject, body):
        self.sender = sender
        self.receiver = receiver
        self.subject = subject
        self.body = body
        self.timestamp = datetime.datetime.now()
        self.read = False

    def mark_as_read(self):
        self.read = True

    def display_full_email(self):
        self.mark_as_read()
        print('\n--- Email ---')
        print(f'From: {self.sender.name}')
        print(f'To: {self.receiver.name}')
        print(f'Subject: {self.subject}')
        print(f"Received: {self.timestamp.strftime('%Y-%m-%d %H:%M')}")
        print(f'Body: {self.body}')
        print('------------\n')

    def __str__(self):
        status = 'Read' if self.read else 'Unread'
        return f"[{status}] From: {self.sender.name} | Subject: {self.subject} | Time: {self.timestamp.strftime('%Y-%m-%d %H:%M')}"
class Inbox:
    def __init__(self):
        self.emails = []

    def receive_email(self, email):
        self.emails.append(email)

    def list_emails(self):
        if not self.emails:
            print('Your inbox is empty.\n')
            return
        print('\nYour Emails:')
        for i, email in enumerate(self.emails, start=1):
            print(f'{i}. {email}')


    def read_email(self, index):
        if not self.emails:
            print('Inbox is empty.\n')
            return
        actual_index = index - 1
        if actual_index < 0 or actual_index >= len(self.emails):
            print('Invalid email number.\n')
            return
        self.emails[actual_index].display_full_email()

    def delete_email(self, index):
        if not self.emails:
            print('Inbox is empty.\n')
            return
        actual_index = index - 1
        if actual_index < 0 or actual_index >= len(self.emails):
            print('Invalid email number.\n')
            return
        del self.emails[actual_index]
        print('Email deleted.\n')
        
class User:
    def __init__(self, name):
        self.name = name
        self.inbox = Inbox()

    def send_email(self, receiver, subject, body):
        email = Email(sender=self, receiver=receiver, subject=subject, body=body)
        receiver.inbox.receive_email(email)
        print(f'Email sent from {self.name} to {receiver.name}!\n')

    def check_inbox(self):
        print(f"\n{self.name}'s Inbox:")
        self.inbox.list_emails()

    def read_email(self, index):
        self.inbox.read_email(index)

    def delete_email(self, index):
        self.inbox.delete_email(index)

def main():
    tory = User('Tory')
    ramy = User('Ramy')        
    
    tory.send_email(ramy, 'Hello', 'Hi Ramy, just saying hello!')
    ramy.send_email(tory, 'Re: Hello', 'Hi Tory, hope you are fine.')
    
    ramy.check_inbox()
    ramy.read_email(1)
    ramy.delete_email(1)
    ramy.check_inbox()

    
if __name__ == '__main__':
    main()