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
