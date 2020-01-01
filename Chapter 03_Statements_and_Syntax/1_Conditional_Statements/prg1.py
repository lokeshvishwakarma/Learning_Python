#!/usr/bin/python

# Title: Conditional Statements

db_login = "admin"
db_password = "adminpower"

login_id = input("Please enter your login ID: ")
password = input("Please enter your Password: ")

if login_id == db_login and password == db_password:
    print("Login Successful !!")
else:
    print("Login Failed !!")
    print("Please contact your System Administrator !!")

