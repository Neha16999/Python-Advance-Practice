import re

pattern= re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
string = input("Enter your email address: ")

a=pattern.search(string)
print(a)
