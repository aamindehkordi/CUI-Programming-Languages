def remove_duplicates(plaintext): #Converts the plain text to all lower case alphabet letters only and removes duplicate characters
        plaintext = plaintext.lower()
        text_alpha = ""
        for i in range(len(plaintext)):#alphbet letters
            if plaintext[i].isalpha():
                text_alpha += plaintext[i]
        final = ""
        for i in range(len(text_alpha)):#removes duplicate characters
            if final.find(text_alpha[i]) == -1:
                final += text_alpha[i]
        return final

def create_playfair_grid(key):#Creates a 5x5 key grid by removing duplicates of the key compared to the alphabet - 'j' to insure a max of 5x5
    while key.find('j') != -1:
        key.replace('j','i')
    key = remove_duplicates(key)#Format the key
    alphabet = 'abcdefghiklmnopqrstuvwxyz'
    for i in range(len(alphabet)):
        if key.find(alphabet[i]) == -1:
            key += alphabet[i]            
    final = [key[:5],key[5:10],key[10:15],key[15:20],key[20:]]#Grid Creation
    return final

def everybody_pair_up(plaintext):#Turns the message into lowercase, separates them into groups of two, and inserts an x inbetween two of the same concurrent characters or at the very end to ensure an even length
    plaintext = plaintext.lower()
    textAlpha = ''
    for i in range(len(plaintext)):#formats text
        if plaintext[i].isalpha():
            textAlpha += plaintext[i]
    temp = ''
    i = 0
    while i < len(textAlpha):#adds the x 
        ch1 = textAlpha[i]
        ch2 = textAlpha[i+1] if i+1 < len(textAlpha) else 'x'

        if ch1 == ch2:
            ch2 = 'x'
            i+=1
        else:
            i+=2
        temp += ch1+ch2+' ' #groups of two

    return temp

def decode_playfair_digrams(eText):#removes the x from the decrypted message
     dText = eText[0]  # first (to avoid indexing errors with i-1) 
     for i in range(1, len(eText)-1):
        if eText[i] == 'x' and eText[i-1] == eText[i+1]:
            pass
        else:
            dText += eText[i]
     dText += eText[-1] # last (to avoid indexing errors with i+1)
     return dText

def playfair_encrypt(key, plaintext):#Encrypts the message using the playfair method
    digrams = everybody_pair_up(plaintext)
    keyTable = create_playfair_grid(key)
    key = remove_duplicates(key)
    alphabet = 'abcdefghiklmnopqrstuvwxyz'
    for i in range(len(alphabet)):
        if key.find(alphabet[i]) == -1:
            key += alphabet[i]#key grid but in a string rather than an array

    saltytext = ''
    i = 0
    while i < len(digrams):#run through the groups of two, two at a time and encrypts
        target1 = digrams[i]
        target2 = digrams[i+1]
        keyIdx1 = key.find(target1)
        keyIdx2 = key.find(target2)

        row1 = keyIdx1//5
        col1 = keyIdx1%5
        row2 = keyIdx2//5
        col2 = keyIdx2%5
        row3 = row1+1
        row4 = row2+1
        col3 = col1+1
        col4 = col2+1
        if col3 > 4:
            col3 = 0
        if row3 > 4:
            row3 = 0
        if col4 > 4:
            col4 = 0
        if row4 > 4:
            row4 = 0
        if(row1 == row2):# if they are in the same row
            saltytext += keyTable[row2][col2] + keyTable[row1][col4]
        elif(col1 == col2):#if they are in the same column
            saltytext += keyTable[row3][col2] + keyTable[row4][col1]
        else:
            saltytext += keyTable[row1][col2] + keyTable[row2][col1]
        i+=3
    return saltytext

def playfair_decrypt(key, saltytext):#decrypt encrypted message using playfair method
    digrams = everybody_pair_up(saltytext)
    keyTable = create_playfair_grid(key)
    key = remove_duplicates(key)
    alphabet = 'abcdefghiklmnopqrstuvwxyz'
    for i in range(len(alphabet)):
        if key.find(alphabet[i]) == -1:
            key += alphabet[i]

    plaintext = ''
    i = 0
    while i < len(digrams):
        target1 = digrams[i]
        target2 = digrams[i+1]
        keyIdx1 = key.find(target1)
        keyIdx2 = key.find(target2)

        row1 = keyIdx1//5
        col1 = keyIdx1%5
        row2 = keyIdx2//5
        col2 = keyIdx2%5
        row3 = row1-1
        row4 = row2-1
        col3 = col1-1
        col4 = col2-1

        if col4 < 0:
            col4 = 4
        if row3 < 0:
            row3 = 4
        if col4 < 0:
            col4 = 4
        if row4 < 0:
            row4 = 4
        if(row1 == row2):
            plaintext += keyTable[row2][col3] + keyTable[row1][col4]
        elif(col1 == col2):
            plaintext += keyTable[row3][col2] + keyTable[row4][col1]
        else:
            plaintext += keyTable[row1][col2] + keyTable[row2][col1]
        i+=3
    plaintext = decode_playfair_digrams(plaintext)
    return plaintext

key = input("please enter a secure alpha-non-numeric key")
message = input("what would you like decrypted?")
encrypted = playfair_encrypt(key,message)
print("Here is the encrypted message:", encrypted)
print('decryption starting')
print('.')
print('..')
print('...')
decrypted = playfair_decrypt(key, encrypted)
print('Decrypted message ( you will need to add spaces logically):', decrypted)