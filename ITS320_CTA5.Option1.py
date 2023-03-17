Python 3.8.2 (v3.8.2:7b3ab5921f, Feb 24 2020, 17:52:18) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> user_str = str(input('Enter three string values:\n'))

def main_method(user_str):
    return reversed(user_str)

print('String values in reverse order is:', main_method)