#Random Module
import random
import sys, time, os
import datetime
import pytz

#Type animation
def cool_type(msg, speed = 0.1):
  for char in msg:
      sys.stdout.write(char)
      sys.stdout.flush()
      time.sleep(speed)

#username and password
def username_verify():
    global new_user
    new_user = True
    global user_number
    user_number = 0
    username_read = open('username.txt', 'r')
    enter_username = input("Username: ")
    existing_user = username_read.read().splitlines()
    for usernames in existing_user:
        if usernames == enter_username:

            def password_verify():
                password_read = open('password.txt', 'r')
                user_passwords = password_read.read().splitlines()
                enter_password = input("Password: ")
                if user_passwords[user_number] == enter_password:
                    print("-" * 40)
                    cool_type(f"welcome, {enter_username} \n")
                    print("-" * 40)
                    global new_user
                    new_user = False
                else:
                    print("-" * 40)
                    cool_type("Wrong Password.\n")
                    print("-" * 40)
                    password_verify()

            password_verify()
        if new_user == True:
            user_number += 1
    if new_user == True:
        print("-" * 40)
        cool_type("Username does not exist. Try again.\n")
        print("-" * 40)
        username_verify()


#storing user data
def store_new_data():
    data_add = open('stored.txt', 'a')
    new_data = input("Type the data you would like to store:\n\n ")
    print("\n" + "-" * 40)
    data_add.write("\n" + new_data)


#CreateNewUser
def create_user():
    username_taken = False
    username_add = open('username.txt', 'a')
    new_username_add = input("Username: ")
    username_read = open('username.txt', 'r')
    existing_user = username_read.read().splitlines()
    for usernames in existing_user:
        if usernames == new_username_add:
            cool_type("Username is taken.\n")
            print("-" * 40)
            create_user()
            username_taken = True
            continue
    if username_taken == False:
        username_add.write("\n" + new_username_add)
        password_add = open("password.txt", "a")
        new_password_add = input("Password: ")
        print("-" * 40)
        password_add.write("\n" + new_password_add)
        store_new_data()
    cool_type("Your new account has been created.\n")
    print("-" * 40)


#getting stored data
def get_user_data():
    get_data = open('stored.txt', 'r')
    data = get_data.read().splitlines()
    print("STORED DATA:\n")
    print(data[user_number])
    print("\n" + "-" * 40)


#login/signup
end = False
while True:

    def user_decide():
        print("-" * 40)
        choice = input("""
   _____________________________________________
  |Enter '1' if you are a new user.             |
  |Enter '2' if you are an existing user.       |
  |Enter 'exit' if you want the program to end. |                                
  |_____________________________________________|

  ------------------------------------------

  Enter: """)
        print("\n" + "-" * 40)
        if choice == "2":
            username_verify()
            get_user_data()
            global end
            end = True
        if choice == "1":
            create_user()
        if choice == "exit":
            end = True

    user_decide()
    if end == True:
        break


#More Animation.
def animate_type(msg_frame1, msg_frame2, msg_frame3, repeat = 1):
    while repeat != 0:
        sys.stdout.write('\r' + msg_frame1)
        time.sleep(0.5)
        sys.stdout.write('\r' + msg_frame2)
        time.sleep(0.5)
        sys.stdout.write('\r' + msg_frame3)
        time.sleep(0.5)
        sys.stdout.flush()
        repeat -= 1


#animate_type("(-_-)", "(o_o)", "(O-O)", 3)
#print("\n" + "-" * 40)


def bigger_animation(frames, repeat, speed = 0.1):
    print("\n")
    while repeat != 0:
        for frame in frames:
            sys.stdout.write('\r' + frame)
            time.sleep(speed)
            repeat -= 1
            sys.stdout.flush()


animation_frames = [
    "~~~~ ~~~~ ~~~~ ~~~~ ~~~~ ~~~~ |WELCOME TO VAULT|~~~~ ~~~~ ~~~~ ~~~~ ~~~~ ~~~~ ",
    "~~~ ~~~~ ~~~~ ~~~~ ~~~~ ~~~~ ~|WELCOME TO VAULT|~~~ ~~~~ ~~~~ ~~~~ ~~~~ ~~~~ ~",
    "~~ ~~~~ ~~~~ ~~~~ ~~~~ ~~~~ ~~|WELCOME TO VAULT|~~ ~~~~ ~~~~ ~~~~ ~~~~ ~~~~ ~~",
    "~ ~~~~ ~~~~ ~~~~ ~~~~ ~~~~ ~~~|WELCOME TO VAULT|~ ~~~~ ~~~~ ~~~~ ~~~~ ~~~~ ~~~",
    " ~~~~ ~~~~ ~~~~ ~~~~ ~~~~ ~~~~|WELCOME TO VAULT| ~~~~ ~~~~ ~~~~ ~~~~ ~~~~ ~~~~",
]

bigger_animation(animation_frames, 10)