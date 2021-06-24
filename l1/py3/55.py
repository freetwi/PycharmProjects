import sys

Zero = ['  ***  ',
        ' *   * ',
        '*     *',
        '*     *',
        '*     *',
        ' *   * ',
        '  ***  ']
One = ['  *  ',
       ' **  ',
       '* *  ',
       '  *  ',
       '  *  ',
       '  *  ',
       '*****']
Two = [' *** ',
       '*   *',
       '*   *',
       '   * ',
       '  *  ',
       ' *   ',
       '*****']
Three = ['  ***  ',
         ' *   * ',
         '      *',
         '     * ',
         '      *',
         ' *   * ',
         '  ***  ']
Four = ['  ***  ',
        ' *   * ',
        '*     *',
        '*     *',
        '*     *',
        ' *   * ',
        '  ***  ']
Five = [' ***** ',
        ' *     ',
        '   *   ',
        '     * ',
        ' *    *',
        ' *   * ',
        '  ***  ']
Six = ['  ***  ',
       ' *   * ',
       '*      ',
       '* * *  ',
       '*     *',
       ' *   * ',
       '  ***  ']
Seven = ['******',
         '*    *',
         '    * ',
         '   *  ',
         '  *   ',
         ' *    ',
         '*     ']
Еight = ['  ***  ',
         ' *   * ',
         '*     *',
         '  * *  ',
         '*     *',
         ' *   * ',
         '  ***  ']
Nine = [' **** ',
        '*    *',
        '*    *',
        ' **** ',
        '     *',
        '*    *',
        ' ***  ']
Digits = [Zero, One, Two, Three, Four, Five, Six, Seven, Еight, Nine]
try:
    digits = sys.argv[1]
    row = 0
    while row < 7:
        line = ""
        column = 0
        while column < len(digits):
            namber = int(digits[column])
            digit = Digits[number]
            line += digit[row] + "  "
            colum += 1
        print(line)
        row += 1
except IndexError:
    print('usage: biGGdik <777>')
except ValueError as err:
    print(err, "in", digits)