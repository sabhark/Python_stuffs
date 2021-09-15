#--------------Python String Programms----------------------

#-----------https://www.geeksforgeeks.org/python-programming-examples/#string--------------

#-------------Python program to check if a string is palindrome or not--------

#-------way-1-------------------------------
# value = input('enter any string : ')
# if value[::] == value[::-1]:
	# print('it is a palindrome')
# else:
	# print('its not a palindrome')


#-------way-2-------------------------------
def isPalindrome(str):

	# Run loop from 0 to len/2
	for i in range(0, int(len(str)/2)):
		if str[i] != str[len(str)-i-1]:
			return False
	return True

# main function
s = input('enter values : ')
ans = isPalindrome(s)

if (ans):
	print("Yes, its palindrome")
else:
	print("No, its not a palindrome")
	
#-------way-3-------------------------------

# value = input('enter any string : ')
# rev_value = reversed(value)
# output = ''.join(rev_value)
# if value==output:
	# print('it is a palindrome')
# else:
	# print('its not a palindrome')

#-------way-4-------------------------------	

# value = input('enter any string : ')
# get_length = int(len(value)/2)
# if len(value)%2==0:
	# First_Value = value[0:get_length]
	# Second_Value = value[get_length:(len(value))]
	# if First_Value[::] == Second_Value[::-1]:
		# print('it is a palindrome')
	# else:
		# print('its not a palindrome')
# else:
	# First_Value = value[0:get_length]
	# Second_Value = value[get_length+1:(len(value))]
	# if First_Value[::] == Second_Value[::-1]:
		# print('it is a palindrome')
	# else:
		# print('its not a palindrome')

#-------way-5-------------------------------
# x = "malayalam"
 
# w = ""
# for i in x:
    # w = i + w
 
# if (x == w):
    # print("Yes")
# else:
    # print("No")

#JUST TO CHECK

#-----to get the length count------------

s = 'test'
print('way_1 to get length : ',len(s))
count=0
for i in s:
	count = count+1
print('way_2 to get length : ',count)


#------Python – Avoid Spaces in string length--------
s= 'test new'
print(len(s))
s1=s.replace(' ','')
print(len(s1))
res = sum(not chr.isspace() for chr in s)
print(res)

#---Python program to print even length words in a string
#---------way-1-------------------------------
s = 'this is a programming test'
s1 = s.split(' ')
print('s1 values are : ', s1)
out = ''
for i in range(len(s1)):
	if (len(s1[i]) %2 == 0):
		out = (s1[i])
		print(out,end=' ')

#-------------way-2-------------------------------
def printWords(s):
    s = s.split(' ')
    for word in s: 
        if len(word)%2==0:
            print(word) 
s = "i am muskan" 
printWords(s)

#------Python – Uppercase Half String-------
#--------way-1-------------------------------
def upperhalf(s):
	upperh = len(s)//2
	s1=s[:upperh]
	print('first half', s1)
	s2=s[upperh::]
	print('second half', s2)
	s2=s2.upper()
	print(s2)
	s3=s1+s2
	print('Uppercase Half String are : ',s3)
upperhalf('sabhashiva')

#------way-2-------------------------------
# initializing string
test_str = 'geeksforgeeks'
  
# printing original string
print("The original string is : " + str(test_str))
  
# computing half index
hlf_idx = len(test_str) // 2
  
# join() used to create result string 
res = ''.join([test_str[idx].upper() if idx >= hlf_idx else test_str[idx]
         for idx in range(len(test_str)) ])
          
# printing result 
print("The resultant string : " + str(res)) 

#---Python program to capitalize the first and last character of each word in a string------

def capitalize_first_last(s):
	s=s.split(' ')
	for word in s:
		print((word[0].upper())+word[1:len(word)-1]+(word[-1].upper()))
		
capitalize_first_last('first and last')

#---Python program to check if a string has at least one letter and one number------
#---way-1-------------------------------
s='test123'
values='abcdefghijklmnopqrstuvwyz'
digits='0123456789'
out1=''
out2=''
for ch in s:
	if ch in values:
		out1=out1+ch
	elif ch in digits:
		out2=out2+ch			
print(out1)
print(out2)
if len(out1)!=0 and len(out2)!=0:
	print('the given string has atleast one letter and one number')

#--way-2-------------------------------
def checkString(str):
	
	# intializing flag variable
	flag_l = False
	flag_n = False
	
	# checking for letter and numbers in
	# given string
	for i in str:
		
		# if string has letter
		if i.isalpha():
			flag_l = True

		# if string has number
		if i.isdigit():
			flag_n = True
	
	# returning and of flag
	# for checking required condition
	return flag_l and flag_n


# driver code
print(checkString('while29'))
print(checkString('geeksforgeeks'))

#-------------way-3-------------------------------
def checkString(str):
	
	# intializing flag variable
	flag_l = False
	flag_n = False
	
	# checking for letter and numbers in
	# given string
	for i in str:
		
		# if string has letter
		if i.isalpha():
			flag_l = True

		# if string has number
		if i.isdigit():
			flag_n = True
	
	if flag_l and flag_n == True:
		print('the given string is having both alpha and digits')


# driver code
checkString('while29')

#--Python | Program to accept the strings which contains all vowels----
vowels = 'aeiou'
out=''
def vowelscheck(s):
	s=s.lower()
	for ch in vowels:
		if ch not in s:
			global out
			out= out+ch
	if len(out)!=0:
		print('The given string does not contain all vowels')
	else:
		print('Accepted !!! because given string contain all vowels')

vowelscheck('aiOuE')
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	