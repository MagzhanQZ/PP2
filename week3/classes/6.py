def fillt(listik):
    print(list(filter(lambda x : all( x % i !=0  
                                    for i in range(2,x)),listik)))  