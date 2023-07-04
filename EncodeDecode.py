import random
import os
#Some lovely variables
running = 0
encodednum = []
encodedlet = []
decodednum = []
decodedlet = []
placement = 0
filenum = '1'
create = 0
decoding = 0
keysize = [1,3,2]
masterkeysplit = []
index = 0

#Starting Questions
while running == 0:
    while running == 0:
        masterkey = 0
        create = 0
        txtfile = ''
        start = input('Would you like to Encrypt or Decrypt. Type E or D or RULES or EXIT: ').upper()

        if start == 'E':
            process = 'E'
            running = 1
        elif start == 'D':
            process = 'D'
            running = 2
        elif start == 'RULES':
            print('''For your message/data to encode and decode properlly only use "!", ".", "?" and ":" for punctuation. 
Using ENTER will not show up in your messagaes either. Also do not use Latin/Accents in your message. 
And always remember your key, without it you will not be able to recover your message.''')
        elif start == 'EXIT':
            exit()
        else:
            print('I am sorry, I do not understand. Try typeing "E" or "D" or "EXIT".')
    #Encrypt
    while running == 1:
        while running == 1:
            txtfile = input('Input .txt file location for Encryption. type "HELP" if you need help with formating: ').lower()
            if txtfile == 'help':
                print('To enter the file location use the file address for your OS. On windows you can open file explorer and copy the file address once you have found the file')
                pass
            else:
                try:
                    with open(txtfile.lower(), 'r', encoding='utf-8') as file:
                        contents = file.read()
                    break
                except FileNotFoundError:
                    print('File not found.')
    #Create Key
        key1 = random.randint(6,9)
        key2 = random.randint(97,122)
        key3 = random.randint(1,99)
        if key2 < 100:
            key2 = '0' + str(key2)
        if key3 < 10:
            key3 = '0' + str(key3)
        masterkey = str(key1) + str(key2) + str(key3)
        print(f'your key is - {masterkey}')
    #Encrypting contents
        #Turns Characters to Numbers
        for item in contents:
            character = ord(item)
            encodednum.append(character)
        #Random Letter to Accent - Key2 picks character. Key3 Offsets
        for item in range(len(encodednum)):
            if encodednum[item] == int(key2):
                encodednum[item] = 192 + int(key3)
        #Offset All Key1
        for item in range(len(encodednum)):
            encodednum[item] = int(encodednum[item]) + key1
        #Lowers all Characters
        for item in range(len(encodednum)):
            if encodednum[item] > 126 and encodednum[item] < 191:
                encodednum[item] = encodednum[int(item)] - 95
        #Make spaces a random accent.
        for item in range(len(encodednum)):
            if encodednum[item] == 32:
                encodednum[item] = 300 + random.randint(1,50)
        #Changes Numbers Back to Characters
        for item in encodednum:
            encodedlet.append(chr(item))
        encodedstr = ''.join(map(str, encodedlet))
        running = 3
        break
    #Decrypt (Uncrypt)
    while running == 2:
        while decoding == 0:
            txtfile = input('Input .txt file location for Decryption. type "HELP" if you need help with formating: ').lower()
            if txtfile == 'help':
                print('To enter the file location use the file address for your OS. On windows you can open file explorer and copy the file address once you have found the file')
                pass
            else:
                try:
                    with open(txtfile.lower(), 'r', encoding='utf-8') as file:
                        contents = file.read()
                    decoding = 1
                    break
                except FileNotFoundError:
                    print('File not found.')
    #Getting Key from User
        masterkey = input('What is your key: ')
        start = input(f'You input {masterkey}. Is this correct. Type Y or N: ').upper()
        if start == 'Y':
            pass
        elif start == 'N':
            print('Retype your key.')
        else:
            print('I am sorry, I do not understand.')
        for keysize in keysize:
            masterkeysplit.append(int(masterkey[index:index+keysize]))
            index += keysize
        key1, key2, key3 = masterkeysplit
    #Decrypting Contents
        contents = [*contents]
        for item in contents:
            character = ord(item)
            decodednum.append(character)
        #Change spaces(32) back to 32 from accent
        for item in range(len(decodednum)):
            if decodednum[item] > 299:
                decodednum[item] = 32
        #Change offset back
        for item in range(len(decodednum)):
            decodednum[item] = int(decodednum[item]) - key1
        #Change random accent back
        for item in range(len(decodednum)):
            if decodednum[item] > 130:
                decodednum[item] = key2
        #Raises all Characters
        for item in range(len(decodednum)):
            if decodednum[item] < 32:
                decodednum[item] = decodednum[int(item)] + 95
        #Change Numbers to Characters
        for item in decodednum:
            decodedlet.append(chr(item))
        decodedstr = ''.join(map(str, decodedlet))
        running = 3
        #Encrypted File Creation
    while running == 3:
        try:
            filename = f'{os.path.splitext(txtfile)[0] + str(filenum) + str(process)}.txt'
            with open(filename, 'x', encoding='utf-8') as file:
            #Note - "utf-8" allows letters with accents to go into the file. Accents caused by key3
                if process == 'E':
                    file.write(encodedstr)
                elif process == 'D':
                    file.write(decodedstr)
            print(filename.lower())
            create = 1
            running = 0
        except FileExistsError:
            filenum = int(filenum) + 1