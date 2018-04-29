import random
import sys
import os
import datetime
import getpass
import yaml

new_user = False
#(print = essentialy text, ""('') = string, can store numbers or letters)
print("\nHomework Schedule!\n")

  #(username = variable, input = user can type in whatever, () = string w question)
have_username = input("Do you have a username?: \n")
if have_username == "yes".lower():
    username = input("Who is the user?: \n").lower()
else:
    print("Why don't you create a username!")
    username = input("Enter Here: ").lower()
    print("Now create a password!")
    password = input("Enter Here: ")
    print("Great " + username + ", now you can schedule your homework! Your password is: " + password)
    
    new_user = True
    if not os.path.exists('./users'):
        os.makedirs("./users")
    filename = username + ".txt"
    f = open('./users/'+filename,'w')
    f.write("User: \"" + username + "\"\n" + "Password: \"" + password + "\"\n")
    f.close()
    
#(if = if my name is entered do below, .lower() = lower or uppercase sensitive)
# Here, check to see if the user is in the Users folder

if new_user == True or os.path.exists("./Users/"+username+".txt"):
    with open("./Users/"+username+".txt", 'r') as stream:
        try:
            user_password = yaml.load(stream)["Password"]
        except yaml.YAMLError as exc:
            print(exc)
    input_password = getpass.getpass("What is the password " + username + "?:\n")
    
    if new_user == True or input_password == user_password:
        target_class = input("What class is giving you new work?: \n").lower()
        schoolwork_list = ["humanities", "science", "drama", "math"]
    
        if target_class in schoolwork_list:
            work = input("Do you have a test, homework, or project in " + target_class + "?: ").lower()
            due = input("\nWhen " + ("are" if work.endswith('s') else 'is') + " your " + work + ":" "\n")
            if work == "test":
                print("\nGood Luck, study. Remember you have a test: " + due + "\n")
            if work == "homework"  or work == "project":
                print("\nGreat! Make sure you get it done by: " + due + "\n")
            if not os.path.exists('./homework'):
                os.makedirs("./homework")
            filename = '{:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())
            f = open('./homework/'+filename,'w')
            f.write("User: \"" + username + "\"\n" + "Class: \"" + target_class + "\"\n" + "Homework: \"" + work + "\"\n" + "Due Date: \"" + due + "\"\n")
            f.close()
            
        else:
            print("Class not found! Exiting")
    else:
        print("Password is Incorrect! Get out!")
else:
    print("User not found! Bye")

# Commands (command k = clear, command spacebar = searchbar, command s = save)

