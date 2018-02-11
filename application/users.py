# This module  manages the userlogin and signup

USERS = {}

class Users(object):
    #Create a constructor with user args
    def __init__(self, email=None, username=None, Password=None):

        self.email = email
        self.username = username
        self.Password = Password

        def add_users(self,email,username,password):
            #add users to the app
            if email not in USERS:
                USERS[email] = {"email":email, "username":username, "password":password}
                return "user added successfully"

            return "Sorry, Email already registered"


        def get_user (self,email,Password):
            #get user from the list
            if email in USERS:
                current_user = USERS[email]
                #authenticate password
                if current_user["password"] == Password:
                    return current_user
                return "passowrd error"
            return "users not found"    
