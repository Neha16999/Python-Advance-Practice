import re

pass_pattern= re.compile(r"[A-Za-z0-9$%#@]{8,}\d")
password= input("Enter your password: ")

a=pass_pattern.fullmatch(password)
print(a)
