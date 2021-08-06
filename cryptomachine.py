def machine():
    keys = 'abcdefghijklmnopqrstuvwxyz !'
    value = keys[-1] + keys[0:-1]


    encryptDict = dict(zip(keys, value))
    decryptDict = dict(zip(value, keys))

    message = input("please enter your secret message:")
    mode = input("please enter the mode : Encode(E) OR decode(D)")

    if mode.upper() == 'E':
        newMessage = ''.join([encryptDict[letter]
                               for letter in message.lower()])

    elif mode.upper() == 'D':
        newMessage = ''.join([decryptDict[letter]
                               for letter in message.lower()])                           
    
    else:
        print("please enter a correct choice")

    return newMessage

print(machine())        