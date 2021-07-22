# Script to reverse words in a string
def reverse(str1):
    words_list = str1.split(' ')
    reversed_word_list = list(reversed(words_list))
    reversed_string = ' '.join(reversed_word_list)
    print(reversed_string)
    return words_list


print(reverse("You are in amazon"))

# Script to Search and replace:
string = "You are in Amazon forest, again Amazon, again Amazon"
print(string.replace("Amazon", "it"))  # Replaces all the occurrence of Amazon with it
print(string.replace("Amazon", "it", 2))  # Replaces two occurrences of Amazon
print(string.replace("zon", "xyz", 2))  # Replaces certain characters of the string

# script to Search and replace, with case insensitivity
import re

src_str = re.compile("this", re.IGNORECASE)  # Means ignore case of "this"
str_replaced = src_str.sub("that",
                           "This is a test sentence. this is a test sentence. THIS")  # replace 'that' with 'this'
print(str_replaced)


# Script to read a file with contents as shown below, and find the total cost of expenditure by comp1:
# comp1 200
# comp2 100
# comp3 300
# comp1 200
cost = 0
with open('input_file.txt') as text_file:
	for line in text_file:
		first_word = line.split(' ', 1)[0] #splits the words in a line delimited by space, makes 1 split, takes first element of the list
		if first_word == 'comp1':
			cost += int(line.split(' ', 1)[1])
		
		print(line, end='')
	print(cost)
    
 
#script to read a file with contents as shown below, and find the total occurance of the word "comp1":
# comp1 44 comp1
# comp2 500 comp2
# comp3 600
# comp2 150
# comp1 350 comp1

count = 0
with open('input_file.txt') as text_file:
	for line in text_file:
		line = line.rstrip('\n')  # strips each file of the new line char '\n'
		word_list = line.split(' ')
		for i in range(len(word_list)):
			
			if word_list[i] == 'comp1':
				count += 1
		
	print(count)
