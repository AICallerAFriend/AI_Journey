print("Hello \nworld")
print("AI\tEngineering")
print("uttam \"Dongre\"")
# print("C:\newfolder\test.txt") # it will give error because \n and \t are escape characters
#print("C:\\newfolder\\test.txt") # to print the above path we need to
print("hello\bworld") # it will remove the last character before \b
print("hellothis\rworld") # it will replace the first 5 characters with world
print("hello\0world") # it will print hello and ignore the rest of the string after \0
print("hello\aworld") # it will print hello and make a beep sound
print("hello\N{GREEK SMALL LETTER ALPHA}world") # it will print helloαworld
print("hello\U0001F600world") # it will print hello😀world
print("hello\nworld, ai \t engineering, is the \"future")
