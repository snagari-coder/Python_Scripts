# Write a Python program to read an entire text file
def file_operations(fileName):
    with open(fileName, 'r') as file1:
        lines = file1.readlines()
        # print(lines) # prints each line as an element in list

        def all_lines(lines):
            content_array = []
            count = 0
            for line in lines:
                count += 1
                print(line) # prints all lines
                content_array.append(line)
            print(content_array)
            print('Number of lines in file', count)

        def first_n(lines,n):
            for i in range(n):
                print(lines[i])  # prints first 5 lines

        def last_n(lines,n):
            for i in range(len(lines) - n, len(lines)):
                print(lines[i]) # prints last 5 lines

        def file_append(fileName):
            list1 = [1,2,3]
            list2=['a','b','c']
            with open(fileName, 'a+') as myfile:
                myfile.write('\nhello1')
                myfile.write('\nhello2')
                myfile.write('\n'+str(list1))
                for char in list2:
                    myfile.write('\n'+char)
            txt = open(fileName)
            print(txt.read())

        def max_length_word(fileName):
            max_length = 0
            with open(fileName,'r') as f1:
                words = f1.read().split()
            for word in words:
                max_length = max(max_length,len(word))
            for word in words:
                if len(word) == max_length:
                    longest_word = word
            return longest_word

        def count_freq_of_words(fileName):
            hashmap = {}
            with open(fileName, 'r') as f1:
                words = f1.read().split()
            for word in words:
                if word in hashmap:
                    hashmap[word] += 1
                else:
                    hashmap[word] = 1
            print(hashmap)

        def file_size(fileName):
            import os
            stats_info = os.stat(fileName)
            return stats_info.st_size

        def copy_fileA_to_fileB(fileName):
            with open(fileName,'r') as fileA:
                with open('test2.txt','w+') as fileB:
                    lines = fileA.readlines()
                    for line in lines:
                        fileB.writelines(line)
            with open('test2.txt', 'r') as fileB:
                txt = fileB.read()
                print(txt)

        def copy_srcfile_to_desfile(fileName):
            from shutil import copyfile
            copyfile(fileName,'test3.txt')

        def zip_file1_file2():
            with open('fileA.txt','r') as fileA, open('fileB.txt','r') as fileB:
                for line1,line2 in zip(fileA,fileB):
                    print(line1+line2)

        def random_line(fileName):
            import random
            with open(fileName,'r') as file1:
                lines = file1.readlines()
            return random.choice(lines)

        def closedOrOpen(fileName):
            f = open(fileName,'r')
            print(f.closed)
            f.close()
            print(f.closed)

        def removeNewLineCharsFromFile(fileName):
            lines = open(fileName).readlines()
            print(lines)
            return [line.rstrip('\n') for line in lines]

        def numsOfWords(fileName):
            with open(fileName, 'r') as f:
                data = f.read()
                data.replace(',', ' ')
                return len(data.split(" "))

        # Write a Python program to extract characters
        # from various text files and puts them into a list.
        def combineChars():
            import glob
            fileList = glob.glob("*.txt")
            char_list = []
            for file in fileList:
                with open(file,'r') as f:
                    char_list.append(f.read())
            print(char_list)

        # Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt
        def createFiles():
            list = ['A','B','C','D','E']
            for char in list:
                open(f'{char}.txt','w+')

        #first_n(lines,5)
        #last_n(lines, 5)
        #all_lines(lines)
        #file_append(fileName)
        #print(max_length_word(fileName))
        #count_freq_of_words(fileName)
        #print("File size in bytes: ",file_size(fileName))
        #copy_fileA_to_fileB(fileName)
        #copy_srcfile_to_desfile(fileName)
        #zip_file1_file2()
        #print(random_line(fileName))
        #closedOrOpen(fileName)
        #print(removeNewLineCharsFromFile(fileName))
        #print(numsOfWords(fileName))
        #combineChars()
        createFiles()

file_operations('test.txt')
#file_operations('fileA.txt')
