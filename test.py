import getpass

newUser = input('Are you a new user? ')
newUser = newUser.casefold()
print(newUser)
isNewUser = False
if newUser == 'yes':
    isNewUser = True

username = input('Username: ')
password = getpass.getpass('Password: ')
userNames = open('userNames', 'r+')
usedUserNames = userNames.read().split('\n')
for userName in usedUserNames:
    if username == userName:
        isNewUser = False
        print('sorry this username is taken')
if isNewUser:
    credentials = open('credentials:' + username, 'w')
    credentials.write(username + '\n' + password)
    credentials.close()
    userNames.write(username + '\n')
    print('Hello ' + username)
else:
    try:
        credentials = open('credentials:' + username, 'r')
        userpass = credentials.read().split('\n')
        if userpass[1] == password:
            print('Hello ' + username)
    except FileNotFoundError:
        print("sorry that user doesn't exist")

print('Hi there')
