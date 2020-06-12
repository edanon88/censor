# These are the emails you will be censoring. 
#The open() function is opening the text file that the emails are contained in
#the .read() method is allowing us to save their contexts to the following variables:

email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()

# arguments all str
def censor(input_text, phrase):
	censored_text=input_text.replace(phrase,("X"*len(phrase)))
	return censored_text

print(censor(email_one,"learning algorithms"))
