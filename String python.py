#def double_word(word):
#    return((2*word)+str(len(2*(word)))

#print(double_word("hello"))
#print(double_word("abc"))   # Should return abcabc6
#print(double_word("0"))      # Should return 0ef double_word(word):
###############################Rightdown &wrongup###############################################\
def double_word(word):
    return word + word + str(len((word) * 2))

print(double_word("hello")) # Should return hellohello10
print(double_word("abc"))   # Should return abcabc6
print(double_word(""))      # Should return 0


print("example "*3)
name="Jaylen"
print(name[1])
print(name[0])
text="random text with"
print(text[-1])
print(text[-2])

def first_and_last(message):
    if (message[0])==(message[-1]):
       return True
    else:
        return False
print(first_and_last("else"))
print(first_and_last("tree"))
#############################################################################
color="orange"
print(color[1:4])
print(color[:3])
print(color[3:])
new_color=color[:3]+"cle"
print(new_color)
pets = "Cats & Dog"
print(pets.index("&"))
print(pets.index("Cats"))
print(pets.index("Dog"))
word = "supercalifragilisticexpialidocious"
print(word.index("x"))
print("Dragons" in pets)
print("Cats" in pets)
#############################################################################
def Replace_Domain(email,old_domain, new_domain):
    if "@"+old_domain in email:
        index=email.index("@"+old_domain)
        new_email=email[:index]+"@"+new_domain
        return new_email
    return email#otherwise return old email if (if) condition failed
#############################################################################
answer='YES'
if answer.lower() == "yes":
    print("User Said Yes")
##########################################################################
print("No. of e in this string is 1-".count("e"))
#############################################################################
print("Forest".endswith("rest"))
print(int("123")+int("100"))
print(" ".join(["this", "is", "a", "bat"]))#joined by space
print("-".join(["date", "is", "31","Dec","2021"]))#joined by "-"
print("This is another example".split())
#We've covered a bunch of String class methods already, so let's keep building on those and run down some more advanced methods.

#The string method lower will return the string with all characters changed to lowercase. The inverse of this is the upper method, which will return the string all in uppercase. Just like with previous methods, we call these on a string using dot notation, like "this is a string".upper(). This would return the string "THIS IS A STRING". This can be super handy when checking user input, since someone might type in all lowercase, all uppercase, or even a mixture of cases.

#You can use the strip method to remove surrounding whitespace from a string. Whitespace includes spaces, tabs, and newline characters. You can also use the methods  lstrip and rstrip to remove whitespace only from the left or the right side of the string, respectively.

#The method count can be used to return the number of times a substring appears in a string. This can be handy for finding out how many characters appear in a string, or counting the number of times a certain word appears in a sentence or paragraph.

#If you wanted to check if a string ends with a given substring, you can use the method endswith. This will return True if the substring is found at the end of the string, and False if not.

#The isnumeric method can check if a string is composed of only numbers. If the string contains only numbers, this method will return True. We can use this to check if a string contains numbers before passing the string to the int() function to convert it to an integer, avoiding an error. Useful!

#We took a look at string concatenation using the plus sign, earlier. We can also use the join method to concatenate strings. This method is called on a string that will be used to join a list of strings. The method takes a list of strings to be joined as a parameter, and returns a new string composed of each of the strings from our list joined using the initial string. For example, " ".join(["This","is","a","sentence"]) would return the string "This is a sentence".

#The inverse of the join method is the split method. This allows us to split a string into a list of strings. By default, it splits by any whitespace characters. You can also split by any other characters by passing a parameter.
########################################IMP#################################
name="Manny"
number=len(name)*3
print("Hello {}, your lucky number is {}".format(name,number))
############################################################################
print("Your lucky number is {number}, {name}".format(name=name,number=len(name)*3))
#############################################################################
price = 7.5
with_tax=price * 1.09
print(price, with_tax)
#############################################################################
print("Base price: ${:.2f} with tax:${:.2f}".format(price, with_tax))
##############################################################################
def to_celsius(x):
    return(x-32)*5/9
for x in range(0,101,10):
    print("{:>3} F | {:>6.2f} C".format(x,to_celsius(x)))