#paramtype:  str
#return type: str
def stringSplite(s):
    
    return ",".join(s.split())+','



if __name__ == "__main__":
    
    s = input("please input a string in lower case:")
    
    print(stringSplite(s))
    