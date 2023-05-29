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

#  با کمک ترتل، شش ضلعی بکش
# که هر یک از خط های آن فقط رنگ های
# سبز قرمز آبی را داشته باشند

COLOR = ['red', 'green', 'blue']
