str1 = "never2"
str2 = "2veenr"
part_anagram = []
two_word_anagrams = []
q = 0
input1 = ""

def anagrams(str1,str2):
    is_anagram = False #(re)sets the condition of the strings being anagrams as false
    anagram.is_anagram = is_anagram # allow it to be accessed outside of the function
    str1 = str1.lower() #these two peices of code turn the capitals into lower case as they are the form of the text in dictionary.txt
    str2 = str2.lower()
    savestr2 = str2     #this saves the values of the two input strings so they can be called back later after being edited
    savestr1 = str1
    str1 = ''.join(sorted(str1)) #this peice of code sorts the strings alphabetically
    str2 = ''.join(sorted(str2))
    searchlength1 = len(str1) #saves the lenght of the strings as a different variable
    searchlength2 = len(str2) 
    errorcount = searchlength1  #sets the counting value errorcount as the lenghth of the first string, this stops an error occuring where the functions gets stuck in a loop of trying processes that do not work error. it is also used as a variable to hold the lenght of string 1
    compare_error = 0  # compare_error is a variable used to stop more letters being compared than there are in the string
    if searchlength1 == searchlength2:  #this compares the lenghts of the string to make sure they are the same
        while searchlength1 > 0 and searchlength2 > 0 and compare_error < errorcount: # this stops the loop when one or both of the words have had all the letters cancelled out or when there have been more loops round the string to check the characters than there are characters 
            try: #this helps stop errors occuring or allows it to continue the process if one does
                for x in range(0, errorcount): # x is just a temporary counting value for the cycles, it cycles round the first word until it has compared all its letters
                    compare_error = 0 #this resets the value of compare_error for each loop as compare_error
                    for y in range(0, errorcount): # y is just a temporary counting value for the cycles, it cycles round the second word until it has compared all its letters
                        if str1[y] == str2[x]: #this compares specific characters to see if they are the same
                            str1 = str1[0:y] + str1[y+1:len(str1)] #this removes the characters form the strings when they have been identifies as being the same
                            str2 = str2[0:x] + str2[x+1:len(str2)]
               #             print(str1)               # this was used ot check the values being processed were correct
            #                print(str2)
                            searchlength1 = len(str1)  # this updates the string lenghts with the new lenghts of the string
                            searchlength2 = len(str2)
                        else: compare_error = compare_error + 1 #this is in case the letters do not match
            except: errorcount = errorcount - 1 # this is incase there is an error
        if searchlength1 == 0 and searchlength2 == 0 and savestr1 != savestr2: #these are conditions for the strings to be an anagram
           # print("The words are anagrams of one another: True")    #prints that the anagram is true, marked out to reduce congestion in console
            is_anagram = True #telling the program the anagram is true for the sake of marks, not really relavent
            anagram.is_anagram = is_anagram #same as previous statement but allows the value to be accessed outside of the function
            print(savestr2 + " is an anagram of " + savestr1 +"!") #tells you what is an anagram of what depeninding on the order of the strings
            try: #this will run is the right function is releavent such as the two anagram process
               if len((sub_anagram.part_anagram[q]) + " " + savestr2) - 1 == len(input1): #this code verifies that later on when finding two anagrams that the word is the right lenght
                    Add = True
                    for i in range(0,len(two_word_anagrams)):
                        if ((sub_anagram.part_anagram[q]) + " " + savestr2) == two_word_anagrams[i]: #this code stops a word being added to a string array twice
                            Add = False                        
                        else: pass
                        if Add == False:
                            pass
                        elif Add == True:
                            two_word_anagrams.append((sub_anagram.part_anagram[q]) + " " + savestr2) #this adds the word to the arrat
            except: pass
        else:
            pass
         #   print("They words contain different characters: False")
    else: 
        pass
   #     print("The lenghts of the words are not the same: False")
    
    
def test_anagram():
    try:
        print("Testing...")     
        str1 = "never2"
        str2 = "2veenr"        
        anagram(str1,str2)
        str1 = "ace"
        str2 = "cae"        
        anagram(str1,str2)
        str1 = "filing"
        str2 = "toolong"        
        anagram(str1,str2)
        str1 = "diff"
        str2 = "difi"        
        anagram(str1,str2)
        print("The tests were all passed and the anagram checker is working properly") 
    except: print("The test was a failure and the anagram checker is not working properly")
    

def get_dictionary_wordlist():
    try:
        path = "C:/Users/Greg/Documents/University/Computing/dictionary.txt" # notes the paths for the resource
        text_file = open(path, 'r') # this opens the file
        lines = text_file.readlines() #creates an array with all of the words of the text file
        print(len(lines)) #prints the number of words in the file
        text_file.close() # closes the file
        get_dictionary_wordlist.lines = lines #makes the variable available outside of the function
    except: # placed in case an error occurs where the recource is not available
        print("Resource not found")
    
def test_get_dictionary_wordlist():
    try:
        get_dictionary_wordlist()
        print("")
    except:
        print("")

    path = "C:/Users/Greg/Documents/University/Computing/dictionary.txt"
    text_file = open(path, 'r')
    lines = text_file.readlines()
    print("The number of words is: " + str(len(lines)))
    #print(lines)
    text_file.close()
    print("The first 10 words are as follows:")
#    tenwords = []
   # w = 0
    for i in range(0,10):
        print(lines[i])
  #  while w < 11:
   #     for i in range(0,500):
    #        if lines[i] == "'":
     #           startchar = i
      #          print(w)
       #     if lines[i] == "n":
        #        tenwords[w] =  lines[startchar:i]
         #       w = w + 1
   # print(tenwords)
        
def find_anagrams_in_wordlist(str1,lines):
    for count in range(0,len(lines)): #this loops over the number of words in the function using count as a counting variable
        str3 = lines[count][0:len(lines[count])-1] #reterives the word one at a time from the text file lines, and makes it compatible my removing the last empty character
        anagram(str1,str3) # this runs anagram for it for the word from lines and the inputed word

def find_anagrams(word): 
    str1 = word
    get_dictionary_wordlist()            
    find_anagrams_in_wordlist(str1,get_dictionary_wordlist.lines)
    
def test_find_anagrams():
    print("Testing, 1 2 3...")
    try:
        print("Test 1: noze")
        word = "noze"
        find_anagrams(word)
        print("Working!")
        print("Test 2: hit/z8er£")
        word = "hit/z8er£"
        find_anagrams(word)
        print("Working!")
        print("Test 3: EPSILON")
        word = "EPSILON"
        find_anagrams(word)
        print("Working!")
        print("TESTS PASSED")
    except:
        print("CRITICAL FAILUrE, ab@RT, ABoR4...") 
    
def sub_anagram(str1,str2):
    if len(str2) > len(str1):
        str3 = str2
        str2 = str1
        str1 = str3
    str1 = str1.lower()
    str2 = str2.lower()
    savestr2 = str2
    savestr1 = str1
    str1 = ''.join(sorted(str1))
    str2 = ''.join(sorted(str2))
    searchlength1 = len(str1)
    searchlength2 = len(str2)
    errorcount = searchlength1
    compare_error = 0 

    while (searchlength1 > 0 or searchlength2 > 0) and compare_error < errorcount:
        try:
            for x in range(0, errorcount):
                compare_error = 0
                for y in range(0, errorcount):
                    if str1[y] == str2[x]:
                        str1 = str1[0:y] + str1[y+1:len(str1)]
                        str2 = str2[0:x] + str2[x+1:len(str2)]
                       # print(str1)
                       # print(str2)                      
                        searchlength1 = len(str1)
                        searchlength2 = len(str2)
                    else: 
                        compare_error = compare_error + 1
        except: errorcount = errorcount - 1
    if (searchlength1 == 0 or searchlength2 == 0) and savestr1 != savestr2:
           # print("The words are anagrams of one another: True")
        print(savestr2 + " is a sub anagram of " + savestr1 + "!")
        part_anagram.append(savestr2)
        sub_anagram.part_anagram = part_anagram
    else: pass
  #          print("They words contain different characters: False")

def find_sub_anagram_in_wordlist(str1,lines):
       for p in range(0,len(lines)):
        str3 = lines[p][0:len(lines[p])-1]
        if len(str1) > len(str3):
            sub_anagram(str1,str3)

def test_find_sub_anagram_in_wordlist():
    get_dictionary_wordlist()  
    lines = get_dictionary_wordlist.lines        
    print("Testing, 1 2 3...")
    try:
        print("Test 1: hinoze")
        find_sub_anagram_in_wordlist("hinoze",lines)
        print("Working!")
        print("Test 2: hit/z8er£")
        find_sub_anagram_in_wordlist("hit/z8er£",lines)
        print("Working!")
        print("Test 3: testingground")
        find_sub_anagram_in_wordlist("testingground",lines)
        print("")
        print("Working!")
        print("Test 4: 4")
        find_sub_anagram_in_wordlist("4",lines)
        print("")
        print("Working!")
        print("TESTS PASSED")
    except:
        print("CRITICAL FAILUrE, ab@RT, ABoR4...") 
        
def remove_letters(str1,str2):
    str1 = str1.lower()
    str2 = str2.lower()
    str1 = ''.join(sorted(str1))
    str2 = ''.join(sorted(str2))
    searchlength1 = len(str1)
    searchlength2 = len(str2)
    errorcount = searchlength1
    compare_error = 0 

    while (searchlength1 > 0 or searchlength2 > 0) and compare_error < errorcount:
        try:
            for x in range(0, errorcount):
                compare_error = 0
                for y in range(0, errorcount):
                    if str1[y] == str2[x]:
                        str1 = str1[0:y] + str1[y+1:len(str1)]
                        str2 = str2[0:x] + str2[x+1:len(str2)]                    
                        searchlength1 = len(str1)
                        searchlength2 = len(str2)
                    else: 
                        compare_error = compare_error + 1
        except: errorcount = errorcount - 1
    print(str1)
    remove_letters.remaining = str1
    
def test_remove_letters():    
    print("Testing, 1 2 3...")
    try:
        print("Test 1: empty")
        remove_letters("","")
        print("Working!")
        
        print("Test 2:str1 empty")
        remove_letters("","safe")
        print("Working!")
        
        print("Test 3:str2 empty")
        remove_letters("testingground","")
        print("")
        print("Working!")
        
        print("Test 4:same")
        remove_letters("gh","gh")
        print("")
        print("Working!")
        
        print("Test 5: str 1 in str2")
        remove_letters("gh","ghlemon")
        print("")
        print("Working!")
        
        print("Test 4: different")
        remove_letters("gh","jk")
        print("")
        print("Working!")
        
        print("TESTS PASSED")
    except:
        print("CRITICAL FAILUrE, ab@RT, ABoR4...") 

def find_two_wrod_anagrams(str1):
    get_dictionary_wordlist()
    lines = get_dictionary_wordlist.lines
    find_sub_anagram_in_wordlist(str1,lines)
    print(sub_anagram.part_anagram)
    for q in range(0,len(sub_anagram.part_anagram)):
        remove_letters(str1,sub_anagram.part_anagram[q])
        find_anagrams_in_wordlist(remove_letters.remaining,lines)
    print(two_word_anagrams)