bitmap = """
                    ***  ***
   *   *  *          *** ***           * *
     *    *******  ** ** ****     * *    * * *
        *                                   *
        * * *                                 * * *
         * * *
            * * 
              *** 
"""
print('enter some thing')
message = input('> ')
if message == '':
    exit()

for line in bitmap.splitlines():
    for index, pixel in enumerate(line):
        if pixel == ' ':
            print(' ', end='')
        else:
            print(message[index % len(message)], end='')
    print()
