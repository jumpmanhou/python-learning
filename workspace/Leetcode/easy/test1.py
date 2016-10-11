def stringEnoc(s):
    ls = list(s)
    for i in range(len(ls)//2):
        if ls[i] == 'a':
            ls[i] = 'z'
        else:
            ls[i] = chr(ord(ls[i])-1)
        if ls[len(ls)-1-i] == 'z':
            ls[len(ls)-1-i] ='a'
        else :
            ls[len(ls)-1-i] = chr(ord(ls[len(ls)-1-i])+1)
        
        ss = "".join(ls)
    
    return ss


if __name__ == "__main__":
    
    s = input("please input a string in lower case:")
    
    print(stringEnoc(s))