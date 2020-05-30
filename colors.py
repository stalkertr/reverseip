"""

  _____             _    _            _                   ____            
 / ____|           | |  | |          | |                 / __ \           
| (___  _ __  _   _| |__| | __ _  ___| | _____ _ __ ____| |  | |_ __ __ _ 
 \___ \| '_ \| | | |  __  |/ _` |/ __| |/ / _ \ '__|_  /| |  | | '__/ _` |
 ____) | |_) | |_| | |  | | (_| | (__|   <  __/ |   / / | |__| | | | (_| |
|_____/| .__/ \__, |_|  |_|\__,_|\___|_|\_\___|_|  /___(_)____/|_|  \__, |
       | |     __/ |                                                 __/ |
       |_|    |___/                                                 |___/ 
"""

from colorama import init,Fore,Back,Style
import os


if os.name == "posix":
    # colors foreground text:
    fc = "\033[0;96m"
    fg = "\033[0;92m"
    fw = "\033[0;97m"
    fr = "\033[0;91m"
    fb = "\033[0;94m"
    fy = "\033[0;33m"
    fm = "\033[0;35m"

    # colors background text:
    bc = "\033[46m"
    bg = "\033[42m"
    bw = "\033[47m"
    br = "\033[41m"
    bb = "\033[44m"
    by = "\033[43m"
    bm = "\033[45m"

    # colors style text:
    sd = Style.DIM
    sn = Style.NORMAL
    sb = Style.BRIGHT

    c = fc + sb
    g = fg + sb
    w = fw + sb
    r = fr + sb
    b = fb + sb
    y = fy + sb
    m = fm + sb
else:
    ## ----------------------------------------------------------------------------------------------------------------------  ##
    init(autoreset=True)
    # colors foreground text:
    fc = Fore.CYAN
    fg = Fore.GREEN
    fw = Fore.WHITE
    fr = Fore.RED
    fb = Fore.BLUE
    fy = Fore.YELLOW
    fm = Fore.MAGENTA
    

    # colors background text:
    bc = Back.CYAN
    bg = Back.GREEN
    bw = Back.WHITE
    br = Back.RED
    bb = Back.BLUE
    by = Fore.YELLOW
    bm = Fore.MAGENTA

    # colors style text:
    sd = Style.DIM
    sn = Style.NORMAL
    sb = Style.BRIGHT

    c = fc + sb
    g = fg + sb
    w = fw + sb
    r = fr + sb
    b = fb + sb
    y = fy + sb
    m = fm + sb
    ## ----------------------------------------------------------------------------------------------------------------------  ##
