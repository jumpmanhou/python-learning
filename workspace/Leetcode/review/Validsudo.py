# -*- coding: utf-8 -*-

#验证一个数独是不是有效的：遍历所有表格中的数，把坐标记录到一个list中，最后比较list 和set长度。


def isValidSudoku(board):
    seen = []
    
    for i ,row in enumerate(board):
        for j,c in enumerate(row):
            if c !='.':
                seen +=[(c,j),(i,c),(i/3,j/3,c)]
                
    return len(seen)==len(set(seen))


board = [".87654321","2........","3........","4........","5........","6........","7........","8........","9........"]

print (isValidSudoku(board))
