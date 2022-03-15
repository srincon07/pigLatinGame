""" Program to translate an English word to the pig latin game. """

def makeList(word):
    """Function to make a list from a given word

    Args:
        word (str): word to be converted into a list

    Returns:
        list (list): List with each character in the word as its elements
    """
    iterable = []
    
    for i in word:
        iterable.append(i)
    return iterable

def countCons(list):
    """Function to count consonants in a word

    Args:        
        list (list): List with each character into the word as its elements

    Returns:
        cons (int): Amount of consonants into the word before first vowel
    """
    vowels = ['A', 'E', 'I', 'O', 'U']
    cons = 0
    for letter in list:
        if letter not in vowels:
            cons += 1
        else:
            break
    return cons

def pigLatin(cons, list):
    """Function to translate a word to pig latin

    Args:
        cons (int): Amount of consonants in the word before first vowel
        list (list): List with each character in the word as its elements

    Returns:
        translation (str): word translated to pig latin
    """
    if cons == 0:
        list.append('WAY') # Adding suffix 
    else:
        for i in range(cons): 
            list.append(list[0]) # Moving consonants to the end of the list
            list.pop(0) # Deleting first element of the list
        list.append('AY') # Adding suffix 

    # Transforming resulting list into a word 
    translation = ''.join(list)
    return translation

def run():
    start = """
        Welcome to Pig Latin Translator. Please type the word to be translated.
        To exit type F.
    """
    print(start)
    
    finish = ''
    
    while finish != 'Y':    
        # Getting data introduced by the user
        data = input('Please type a word: ')
        # Deleting blank spaces into the word
        data = data.replace(' ', '')
        # Capitalising the word
        data = data.upper()
        
        if data != 'F':
            list = makeList(data)
            
            num_cons = countCons(list)
            
            translation = pigLatin(num_cons, list)
            
            print('Your word in pig latin is: ' + translation)

        else:
            finish = 'Y'
    
if __name__=='__main__':
    run()