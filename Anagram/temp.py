str1 = "zone"
str2 = "noze"
part_anagram = []
two_word_anagrams = []
q = 0
input1 = "sailing"
def anagram(str1,str2):
    str1 = str1.lower()
    str2 = str2.lower()
    savestr2 = str2
    savestr1 = str1
    str1 = ''.join(sorted(str1))
    str2 = ''.join(sorted(str2))
    searchlength1 = len(str1)
    searchlength2 = len(str2)
    z = searchlength1  
    v = 0 
    if searchlength1 == searchlength2:
        while searchlength1 > 0 and searchlength2 > 0 and v < z:
            try:
                for x in range(0, z):
                    v = 0
                    for y in range(0, z):
                        if str1[y] == str2[x]:
                            str1 = str1[0:y] + str1[y+1:len(str1)]
                            str2 = str2[0:x] + str2[x+1:len(str2)]
               #             print(str1)
            #                print(str2)
                            searchlength1 = len(str1)
                            searchlength2 = len(str2)
                        else: v = v + 1
            except: z = z - 1
        if searchlength1 == 0 and searchlength2 == 0 and savestr1 != savestr2:
           # print("The words are anagrams of one another: True")
            print(savestr2 + " is an anagram of " + savestr1 +"!")
            if len((sub_anagram.part_anagram[q]) + " " + savestr2) - 1 == len(input1):
                Add = True
                for i in range(0,len(two_word_anagrams)):
                    if ((sub_anagram.part_anagram[q]) + " " + savestr2) == two_word_anagrams[i]:
                        Add = False                        
                    else: pass
                if Add == False:
                   pass
                elif Add == True:
                   two_word_anagrams.append((sub_anagram.part_anagram[q]) + " " + savestr2)
        else:
            pass
         #   print("They words contain different characters: False")
    else: 
        pass
   #     print("The lenghts of the words are not the same: False")
    
    
def test_anagram():
    try:
        print("Testing...")        
        str1 = ""
        str2 = ""        
        anagram(str1,str2)
        
        str1 = ""
        str2 = ""        
        anagram(str1,str2)
        
        str1 = ""
        str2 = ""        
        anagram(str1,str2)
        
        print("The tests were all passed and the anagram checker is working properly")    
    except: print("The test was a failure and the anagram checker is not working properly")
    

def get_dictionary_wordlist():
    path = "C:/Users/Greg/Documents/University/Computing/dictionary.txt"
    text_file = open(path, 'r')
    lines = text_file.readlines()
    print(len(lines))
    text_file.close()
    get_dictionary_wordlist.lines = lines
    
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
    for p in range(0,len(lines)):
        str3 = lines[p][0:len(lines[p])-1]
        anagram(str1,str3)

def find_anagrams(word):
    str1 = word
    get_dictionary_wordlist()            
    find_anagrams_in_wordlist(str1,get_dictionary_wordlist.lines)
    
def test_find_anagrams():
    print("Testing, 1 2 3...")
    try:
        print("Test 1: nine")
        word = "nine"
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
    z = searchlength1
    v = 0 

    while (searchlength1 > 0 or searchlength2 > 0) and v < z:
        try:
            for x in range(0, z):
                v = 0
                for y in range(0, z):
                    if str1[y] == str2[x]:
                        str1 = str1[0:y] + str1[y+1:len(str1)]
                        str2 = str2[0:x] + str2[x+1:len(str2)]
                       # print(str1)
                       # print(str2)                      
                        searchlength1 = len(str1)
                        searchlength2 = len(str2)
                    else: 
                        v = v + 1
        except: z = z - 1
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
        print("Test 1: nine")
        find_sub_anagram_in_wordlist("zno",lines)
        print("Working!")
        print("Test 2: hit/z8er£")
        find_sub_anagram_in_wordlist("hit/z8er£",lines)
        print("Working!")
        print("Test 3: testingground")
        find_sub_anagram_in_wordlist("testingground",lines)
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
    z = searchlength1
    v = 0 

    while (searchlength1 > 0 or searchlength2 > 0) and v < z:
        try:
            for x in range(0, z):
                v = 0
                for y in range(0, z):
                    if str1[y] == str2[x]:
                        str1 = str1[0:y] + str1[y+1:len(str1)]
                        str2 = str2[0:x] + str2[x+1:len(str2)]                    
                        searchlength1 = len(str1)
                        searchlength2 = len(str2)
                    else: 
                        v = v + 1
        except: z = z - 1
    print(str1)
    remove_letters.remaining = str1

def find_two_wrod_anagrams(str1):
    get_dictionary_wordlist()
    lines = get_dictionary_wordlist.lines
    find_sub_anagram_in_wordlist(str1,lines)
    print(sub_anagram.part_anagram)
    for q in range(0,len(sub_anagram.part_anagram)):
        remove_letters(str1,sub_anagram.part_anagram[q])
        find_anagrams_in_wordlist(remove_letters.remaining,lines)
    print(two_word_anagrams)

find_two_wrod_anagrams(input1)     
