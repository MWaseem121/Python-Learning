print("...Password Checker...")
password = input("Enter password: ")
print("Password:", password)
if len(password) >= 12:
  print("Strong Password")
elif len(password) >= 8:
  print("Middiam Password")
else:
 print("Weak Password")


print("...Password Checker...")
password = input("Enter password number: ")
condition = password_with_number = any(char.isdigit() for char in password)
if condition:
  print("your password has number")
elif not condition:
  print("your password has no number")

if len(password) >= 8:
  print("your password is more than 8 characters")
elif len(password) < 8:
  print("your password is less than 8 characters")
else:
  print("your password is less than 8 characters")


print("...Password Checker...")
password = input("Enter password number: ")
condition = password_with_number = any(char.isdigit() for char in password)
if condition and len(password) >= 8:
  print("your password has number and more than 8 characters")
elif condition and len(password) < 8:
  print("your password has number and less than 8 characters")
elif not condition and len(password) >= 8:
  print("your password has no number and more than 8 characters")
  