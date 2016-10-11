def isSameString(s1,s2,s3):
    s1.replace(s3,'').strip()
    s2.replace(s3,'').strip()
    
    return s1 is s2


if __name__ == "__main__":

    s1 = raw_input()
    s2 = raw_input()
    s3 = raw_input()
    
    print isSameString(s1, s2, s3)