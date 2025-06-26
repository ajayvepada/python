letter = 'P'#single line comment
print(letter)
print(len(letter))
greeting = 'Hello world!'
print(greeting)
print(len(greeting))
sentence = "I learn python in 30 days"
print(sentence)
print(len(sentence))
#multiline string
multiline_string = ''' I am a student and enjoy the class.
 I learining python language in  naresh i techonologies in hyderabad.
 i  regularly attend the class'''
print(multiline_string)
# another way of multiline string
multiline_string = """ I am a student and enjoy the class.
 I learining python language in  naresh i techonologies in hyderabad.
 i  regularly attend the class"""
print(multiline_string)
#string concentation
first_name = 'ajay'
last_name = 'vepada'
space = ' '
full_name = first_name + space + last_name
print(full_name)
# checking the length of string use len() inbuild function
print(len(first_name))
print(len(last_name))
print(len(full_name))
print(len(first_name) < len(last_name))
# unpacking characters
language = 'software'
a,b,c,d,f,g,h,i = language
print(a)
print(b)
print(c)
print(d)
print(f)
print(g)
print(h)
print(i)
#Accessing character in string of index
language = 'software'
print(language[0])
print(language[0])
print(language[-1])
print(language[-4])
#slicing
language = 'software'
print(language[0:5])
print(language[-5:-2])
print(language[:6])
print(language[2:])
#skipping characters while splitting strings
print(language[0:6:2])
print(language[0:5:3])
#string method
#captialize(): convert the first character the string the capital letter
outline = 'thirty one'
print(outline.capitalize())
#count(): 
print(outline.count('t'))
#endswitch(): return occures the string end with specified
print(outline.endswith('ne'))
print(outline.endswith('ty'))
#expandtabs(): replace the tab characters with space,default size is 8.it take tab agurment
challenge = 'thirty\tdays\tof\tpython'
print(challenge.expandtabs())
print(challenge.expandtabs(9))
#find(): return the  index of first occurance of substring
print(outline.find('ty'))
print(outline.find('t'))
#index(): return of substrings
print(outline.find('o'))
#format () format string into nicer output
name = 'Ajay'
name1 = 'vepada'
job = 'student'
country = 'india'
sentence = 'I am {}{}.I am {}. I live in {}.'.format(name,name1,job,country)
print(sentence)
radius = 10
pi = 3.14
result = 'the area of circle is {} is {}.'.format(str(radius),str(pi))
print(result)
#iaalphnum(): check alphanumeric characters
challenge = 'thirtyone'
print(challenge.isalnum())
challenge = '30one'
print(challenge.isalnum())
challenge = ' thirty one'
print(challenge.isalnum())
#isalph(): check the if all characters are alphbets
print(challenge.isalpha())
num = '123'
print(num.isalpha())
#isdigit(): check digit character
challenge = 'thirty one'
print(challenge.isdigit())
num2 = '23'
print(num2.isdigit())
#isdecimal(): check dicimal character
num = '10'
num3 = '10.5'
print(num.isdecimal())
print(num3.isdecimal())
#islower(): check the if all alphabets are lower case
challenge = 'THIRTY ONE'
print(challenge.islower())
#isupper(): check if all character of string are upper case are not
challenge = 'forthy one'
print(challenge.isupper())
print(challenge.islower())
#isidentifier():check valid identifier mean if string is valid for variable name
challenge = '30days of python'
print(challenge.isidentifier())#because its start with numbers
challenge = 'thirty_one_number'
print(challenge.isidentifier())
#join():return a concatented string
web_tech = ['HTML','CSS','JAVA']
result = '#,'.join(web_tech)
print(result)
#strip(): remove the both leading and trailing characters
challenge = 'thirty days of python'
print(challenge.strip('y'))
#replace(): replace the string value
challenge = 'i learn python'
print(challenge.replace('python','javascript'))
#split():
print(challenge.split())
#title():
print(challenge.title())
#swapcase(): check if string start with specified string
print(challenge.swapcase())
challenge = 'Thirty One'
print(challenge.swapcase())
# starswith(): check if string start with specified string
challenge = 'thirty days of python'
print(challenge.startswith('t'))