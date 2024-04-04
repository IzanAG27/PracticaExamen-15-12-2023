"""
   Izan Arnáiz Gallego
   ITB Institut Tecnològic de Barcelona
   ASIXc M03 UF2 A2
   04/04/2024

   EXEMPLE: System Colors
   FONT: https://stackoverflow.com/questions/287871/how-to-print-colored-text-to-the-terminal
   US:
        Per imprimir amb colors al terminal ----------
        print('\x1b[6;30;42m' + 'Success!' + '\x1b[0m')
"""

# region #Definició de colors --------------------------
# Formats
FEND = '\33[0m'
FBOLD = '\33[1m'
FITALIC = '\33[3m'
FURL = '\33[4m'
BLINK = '\33[5m'
BLINK2 = '\33[6m'
SELECTED = '\33[7m'

# Colors
BLACK = '\33[30m'
RED = '\33[31m'
GREEN = '\33[32m'
YELLOW = '\33[33m'
BLUE = '\33[34m'
VIOLET = '\33[35m'
BEIGE = '\33[36m'
WHITE = '\33[37m'

BLACKBG = '\33[40m'
REDBG = '\33[41m'
GREENBG = '\33[42m'
YELLOWBG = '\33[43m'
BLUEBG = '\33[44m'
VIOLETBG = '\33[45m'
BEIGEBG = '\33[46m'
WHITEBG = '\33[47m'

GREY = '\33[90m'
RED2 = '\33[91m'
GREEN2 = '\33[92m'
YELLOW2 = '\33[93m'
BLUE2 = '\33[94m'
VIOLET2 = '\33[95m'
BEIGE2 = '\33[96m'
WHITE2 = '\33[97m'

GREYBG = '\33[100m'
REDBG2 = '\33[101m'
GREENBG2 = '\33[102m'
YELLOWBG2 = '\33[103m'
BLUEBG2 = '\33[104m'
VIOLETBG2 = '\33[105m'
BEIGEBG2 = '\33[106m'
WHITEBG2 = '\33[107m'
# endregion

# region Joc de Proves ---
# print(CBLUE + CBOLD + 'Have a lot of fun BITXOS ;-)!')
# print(CGREEN + CSELECTED + 'Success!')
# endregion
