Python 3.8.2 (v3.8.2:7b3ab5921f, Feb 24 2020, 17:52:18) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> year = int(input('Enter year:\n'))

if year < 1962:
    print('Car did not exist yet!')
elif year <= 1964:
    print('$', 18500)
elif year <= 1968:
    print('$', 6000)
elif year <= 1971:
    print('$', 12000)
elif year <= 1975:
    print('$', 48000)
elif year <= 1980:
    print('$', 200000)
elif year <= 1985:
    print('$', 650000)
elif year <= 2012:
    print('$', 35000000)
elif year <= 2014:
    print('$', 52000000)