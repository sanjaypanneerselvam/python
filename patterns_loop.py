n=5 
for i in range(n):                        # * * * * * 
    for j in range(n):                    # * * * * * 
        print('*' , end=" " )             # * * * * *
                                          # * * * * *
    print("")                             # * * * * *

print()

for i in range(n):                        # *
    for j in range(i+1):                  # * *
        print('*' , end=" " )             # * * *
                                          # * * * *
    print("")                             # * * * * *

print()

for i in range(n):                        # * * * * *
    for j in range(n-i):                  # * * * *
        print('*' , end=" " )             # * * *
                                          # * * 
    print("")                             # *

print()

for i in range(n):                        #     *
    for j in range(n-i):                  #    * *
        print('',end=' ')                 #   * * *
    for j in range (i+1):                 #  * * * *
        print('*',end=' ')                # * * * * *
    print()                              

print()

for i in range(n):                        # * * * * *
    for j in range(i+1):                  #  * * * *
        print('',end=' ')                 #   * * *
    for j in range (i,n):                 #    * *
        print('*',end=' ')                #     *
    print()
