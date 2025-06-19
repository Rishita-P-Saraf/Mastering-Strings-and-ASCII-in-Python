def capitalize(text):
    if (len(text) != 0):
        return text[0].upper() + text[1:].lower()
    else:
        return None
    
def upper(txt):
    string=""
    for char in txt:
        if(ord(char)>=97 and ord(char)<=122): # 97 -122 (Lowercase)
            string+=chr(ord(char)-32)        # Add 32 to make it uppercase
        else:
            string+=char
    return string

def lower(txt):
    string=""
    for char in txt:
        if(ord(char)>=65 and ord(char)<=90): # 65 -90 (Uppercase)
            string+=chr(ord(char)+32)        # Add 32 to make it lowercase
        else:
            string+=char
    return string

def capitalize(text):
    if (len(text) != 0):
        return upper(text[0]) + lower(text[1:])
    else:
        return None
    
def isalpha(text):
    c=0
    for char in text:
        if(ord(char)>=65 and ord(char)<=90) or (ord(char)>=97 and ord(char)<=122):
            c+=1

    if (len(text)==c):
        return True
    else:
        return False
    
def isdigit(text):
    c=0
    for char in text:
        if(ord(char)>=48 and ord(char)<=57):
            c+=1

    if (len(text)==c):
        return True
    else:
        return False
    
def isalnum(text):
    c=0
    for char in text:
        if(ord(char)>=65 and ord(char)<=90) or (ord(char)>=97 and ord(char)<=122) or (ord(char)>=48 and ord(char)<=57):
            c+=1

    if (len(text)==c):
        return True
    else:
        return False

def title(txt):
    string=[]
    for word in txt.split():
        string.append(upper(word[0])+ lower(word[1:]))
    return " ".join(string)

