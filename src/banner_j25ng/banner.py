from pyfiglet import Figlet
import random

def show():
    f = Figlet(font='slant')
    print(f.renderText('j25ng'))

def pic():
    p = """
    -------------:------::--:::-=#@@%+--------=--===-=
    -----=---:----:--:--------:--=@@@@*-------------=-
    ---=======--------*@@+--==-:--*@@@%*++=---=-:----=
    -=====-=----------=%@@%*++*****#%%%%%#+==--::.:-==
    ====+=========--=-=@@@@@@@@@@@%%%@@@%%#*=-=====-==
    ====+===+++========@@@@%%%@%*%@%%@@@%%%%+==+======
    ===++====++==++-===%@@%%#@@+.#@##%@@%%%%*===-=====
    +=+++++============+@@@%##+:.*##%%%%%%%%#++=====++
    ++====++===========+#@%%%+.::.-#@%%%%@@%%*+===++==
    +=-=-=++==========++%%%#*::=-:.=*#%%@@@%%*===+++=+
    =-===+=====++==--=*%%%*----::--+##%@@@%%*=-=++*++=
    =====---==+++**+++#@@@%+:::::-#%%%@@%*=:.-=+=--===
    +++=======+++***+#%@@@%*:..:=*%@@%@@#++:.:==+++++=
    ==++++=====+++=+*%@@@@@%#-:+%@@@@@@%#**+:-=+*+==+=
    +*+++*==**=++++*#@@@@@@%#+=*#%@@@@@%#*****+**+=---
    =+++++==++===+*#%@@@@##*++++*#@%@@%#**===+++===-==
    -=++**++=====*%@@@%##**+=###%@@@@@*****##*++++===+
    """
    print(p)

def lotto():
    l = random.sample(range(1,46),6)
    print(l)
