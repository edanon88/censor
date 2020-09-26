# The open() function is opening the text file that the emails are contained in
# The .read() method is allowing us to save their contexts to the following variables:

alphabet=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "'", "#"]

punctuation = [" ", "\n", ".", ",", "s", "'", "(", ")", "!"]

email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()

phrase = "learning algorithms"
proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her", "herself"]
negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmingly", "alarmed", "out of control", "help", "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distress", "concerning", "horrible", "horribly", "questionable"]

# Sort terms list longest to shortest
def sort_long_to_short(phrase_list):
	long_to_short = sorted(phrase_list, key=len, reverse=True)
	return long_to_short


def split_into_characters(text):
	return [character for character in text]


def censor(email, phrase):
	email_characters = split_into_characters(email)
	phrase_characters = split_into_characters(phrase)
	# Work through the email letter by letter
	for i in range(len(email_characters)):
		# If the current letter is the same as the first of the phrase... 
		if email_characters[i] == phrase_characters[0].upper()\
		or email_characters[i] == phrase_characters[0].lower():
			# Word starts at current i
			# Initialise boolean
			match = False
			# Work through the length of the phrase
			for n in range(len(phrase_characters)):
				if email_characters[i+n] == phrase_characters[n].upper()\
				or email_characters[i+n] == phrase_characters[n].lower():
					match = True
				else:
					match = False
					break
					#This should leave the boolean as false
			if match and email_characters[i-1] in punctuation and email_characters[i+n+1] in punctuation:
				for n in range(len(phrase_characters)):
					email_characters[i+n] = "#"
	return "".join(email_characters)

######
# Task: Remove "Learning Algorithms" (phrase) from email_one
######

print("Remove the phrase 'Learning Algorithms' from email one.")
print()
print(censor(email_one,"Learning Algorithms"))

######
# Task: Remove list of proprietary_terms from email_two
######

def censor_phrase_list(email, phrase_list):
	# Phrase list must be sorted big to small
	sorted_phrase_list = sort_long_to_short(phrase_list)

	censored_email = email
	for phrase in sorted_phrase_list:
		phrase_characters = split_into_characters(phrase)
		censored_email = censor(censored_email, phrase)
	return censored_email

print("Take a list of proprietary terms out of email two")
print()
print(censor_phrase_list(email_two, proprietary_terms))

######
# Task: Censor email 3
# Remove negative words from negative list after 2nd occurrance
######

def email_as_list(email):
	email_as_list = []
	i=0
	while i < len(email):
		if email[i].lower() in alphabet:
			word = ""
			while email[i].lower() in alphabet:
				word = word + email[i]
				i += 1
				if i == len (email):
					email_as_list.append(word)
					return email_as_list
			email_as_list.append(word)
			email_as_list.append(email[i])
			i += 1
		else:
			email_as_list.append(email[i])
			i += 1
	return email_as_list


def censor_negative(email, negative_words):
	count=0
	words_removed = []
	text_as_list = email_as_list(email)
	# Goes through text word by word
	for i in range(len(text_as_list)):
		# for each word in the text, goes through all negative words
		for negative_word in negative_words:
			# use of .lower takes care of caps
			if (negative_word in text_as_list[i].lower()):
				if (count>=2) :
					words_removed.append(text_as_list[i])
					text_as_list[i] = "#"*len(text_as_list[i])
					count+=1
				else:
					count+=1
	print("Words removed:")
	print(words_removed)
	return ("".join(text_as_list))

print("Remove negative terms from email three after the second occurrance.")
print()
print(censor_negative(email_three, negative_words))


######
# Task: Censor all prop terms, neg words, and words either side for email 4
######

banned_list = proprietary_terms + negative_words

censored_email_four = censor_phrase_list(email_four, banned_list)
print(censored_email_four)

#Take a censored email, find the terms already censored and censor the words before and after

def censor_before_and_after(censored_email):
	cd_email_as_list = email_as_list(censored_email)
	i = 0
	while i < len(cd_email_as_list)-2:
		if "#" in cd_email_as_list[i]:
			# Working backwards to find the previous word (not punctuation)
			n = i-1
			while len(cd_email_as_list[n]) <= 1:
				n -= 1
			cd_email_as_list[n] = "#" * len(cd_email_as_list[n])
			# Working forwards likewise
			n = i+1
			while len(cd_email_as_list[n]) <= 1:
				n += 1
			cd_email_as_list[n] = "#" * len(cd_email_as_list[n])
			# Moving the function counter forwards to skip newly censored words
			i = n + 1
		else:
			i = i + 1
	return("".join(cd_email_as_list))

print(censor_before_and_after(censored_email_four))