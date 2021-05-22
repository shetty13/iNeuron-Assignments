# Solution-1

def equalValueCheck(a, b, c):

    l = [a,b,c]

    for i in l:
        if not type(i) == int:
            raise TypeError ("Please enter all arguments as integers")

    counter = 0

    if a==b or b==c or a==c:
        counter+=2

    if a==b and b==c:
        counter = 3

    print(counter)
    return counter

    

# Solution-2
def dictToList(dictionary):

    if not type(dictionary) == dict:
        raise TypeError ("Please provide a dictionary")

    else:
        list_items = [item for item in dictionary.items()]
        list_items.sort()
        return list_items


        
        
# Solution-3
def mappingUpperCase(alphabet_list):
    
    if not type(alphabet_list) == list:
        raise TypeError ('Please provide a list of alphabets')

    else:
        alphabet_dict = {alphabet : alphabet.upper() for alphabet in alphabet_list}
        return(alphabet_dict)


# Solution-4

def vowelReplace(string_a, vowel):

    if vowel not in ['a', 'e', 'i', 'o', 'u']:
        raise ValueError ("Please enter a vowel")

    else:
        string_a = string_a.replace('a', vowel).replace('e', vowel).replace('i', vowel).replace('o', vowel).replace('u', vowel)
        return string_a

# Solution-5

def capitalizeASCII(string_b):

    if not type(string_b) == str:
        raise TypeError ("Please provide string as argument.")

    else:   
        list_ascii = [i.upper() if ord(i) % 2 == 0 else i.lower() for i in string_b]
        new_string = ''.join(list_ascii)
        return new_string

