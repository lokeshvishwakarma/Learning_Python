#!/usr/bin/python

# Title: Conditional Statements

user_list = ['loki', 'datta', 'sid', 'mayur']
admin_users = ['admin']

user_id = input("Please enter your login ID: ")
if user_id in admin_users:
    print("You have access to ADMIN account")
elif user_id in user_list:
    print("You are a regular user")
else:
    print("User not found !! Contact your System Admin.")
