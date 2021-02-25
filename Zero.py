# -.-encoding utf-8 -.-#
import os
import random
import time
import webbrowser
import ctypes
from time import time as timer
from colorama import *

init()
init(autoreset = True)
red = Fore.LIGHTRED_EX
green = Fore.GREEN
lgrn = Fore.LIGHTGREEN_EX
blue = Fore.BLUE
lblue = Fore.LIGHTBLUE_EX
cyan = Fore.CYAN
mag = Fore.LIGHTMAGENTA_EX
white = Fore.WHITE
yellow = Fore.LIGHTYELLOW_EX

try:
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
except:
    print('Use windows plz')

contact_us = 'https://discord.gg/GE46n8baWf'

init()
red = Fore.LIGHTRED_EX
green = Fore.LIGHTGREEN_EX
blue = Fore.LIGHTBLUE_EX
cyan = Fore.CYAN
yellow = Fore.YELLOW
lgrn = Fore.GREEN
white = Fore.LIGHTWHITE_EX

init(autoreset = True)


def logo():
    x = (f'''
    {green} M""""""""`M                            MM""""""""`M                   dP       M""""""""M 
    {lgrn} Mmmmmm   .M                            MM  mmmmmmmM                   88       Mmmm  mmmM 
    {yellow} MMMMP  .MMM .d8888b. 88d888b. .d8888b. M'      MMMM dP    dP .d8888b. 88  .dP  MMMM  MMMM 
    {yellow} MMP  .MMMMM 88ooood8 88'  `88 88'  `88 MM  MMMMMMMM 88    88 88'  `"" 88888"   MMMM  MMMM 
    {yellow} M' .MMMMMMM 88.  ... 88       88.  .88 MM  MMMMMMMM 88.  .88 88.  ... 88  `8b. MMMM  MMMM 
    {cyan} M         M `88888P' dP       `88888P' MM  MMMMMMMM `88888P' `88888P' dP   `YP MMMM  MMMM 
    {cyan} [][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][]
    ''')
    ctypes.windll.kernel32.SetConsoleTitleW(r"https://t.me/xConKronos || https://sellix.io/TearzZ || https://discord.gg/GE46n8baWf")
    print(x)
    desc = '\t\tThis module will obfuscate the strings in your letters in order to make your content \nmore difficult '\
           'to detect by spam filters. The technique is called ZeroFont. \nWhich will look something like this: \n\n'
    desc2 = [rf'{white} </span>,', rf'{cyan}P',
             f'{white} <span style="font-size: 0.0000000000000000000000000000008349vh;">Farmer \n',
             rf'{white} </span>,', rf'{cyan}a',
             f'{white} <span style="font-size: 0.00000000000000000000000000000039632%;">soutien \n'
             rf'{white} </span>,', rf'{cyan}y',
             f'{white} <span style="font-size: 0.00000000000000000000000000000056979em;">océans \n'
             rf'{white} </span>,', rf'{cyan}P',
             f'{white} <span style="font-size: 0.0000000000000000000000000000005243%;">debout, \n'
             rf'{white} </span>,', rf'{cyan}a',
             f'{white} <span style="font-size: 0.00000000000000000000000000000067519vw;">enseignants, \n'
             rf'{white} </span>,', rf'{cyan}l',
             f'{white} <span style="font-size: 0.00000000000000000000000000000091066vw;">celui-ci \n\n']
    for char in desc:
        time.sleep(0.05)
        print(green + char, end = '', flush = True)
    for line in desc2:
        time.sleep(0.175)
        print(line, end = '', flush = True)


def main():
    logo()
    letter = input(yellow + 'Please enter the path to your letter (if it is not in this directory) \n>>>>>>>  ' + cyan +
                   ' ')
    with open(letter, 'r', encoding = 'utf-8') as (new):
        x = str(new.read())
    x = x.replace('\n', '')
    x = x.replace('\r', '')
    x = x.replace('\t', '')
    x = x.replace('  ', '')
    fontword = ('***************************************************',
                '##################################################################',
                '-----------------------------------------------------------------------',
                '___________________________________________________________________',
                '_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-',
                '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    worderx = random.choice(fontword)
    bite = ('%', 'vw', 'vh', 'em', 'ex')
    bites = random.choice(bite)
    forx = input(
            red + 'Pick a number between 1 and 3! \nThis only decides what alphabet will be used to hide your strings '
                  'examples below: \n\n1. French/English/Latin  \n2. Russian/Cryillic \n3. Arabic \n4. Hindu \n5. '
                  'Japanese \n\n'
                  'You may make your '
                  'selection '
                  'now: ')
    if forx == '1':
        types = 'FRW.txt'
    elif forx == '2':
        types = 'RUW.txt'
    elif forx == '3':
        types = 'ARW.txt'
    elif forx == '4':
        types = 'HIW.txt'
    elif forx == '4':
        types = 'JPW.txt'
    else:
        types = 'FRW.txt'
    lvl = input(f'{red}Choose your level of obfuscation {white}(1-10):  ')
    lvl = int(lvl)
    if lvl > 10:
        lvl = 10
    else:
        if lvl < 1:
            lvl = 1
        i = 0
        ch = ''
        rp = 0
        while i <= len(x) - 1:
            if x[i:i + 6].lower() == '<style':
                ff = ''
                while x[i:i + 7].lower() != '</style':
                    ff += x[i]
                    i += 1

                ff += '</style>'
                i += 8
                ch += ff
            elif x[i:i + 3] == '<!-':
                ff = ''
                while x[i:i + 3] != '-->':
                    ff += x[i]
                    i += 1

                ff += '-->'
                ch += ff
                i += 3
            elif x[i] == '<':
                ch1 = ''
                ch1 = ch1 + '<'
                while x[i] != '>':
                    i = i + 1
                    ch1 = ch1 + x[i]

                if i < len(x) - 1:
                    i = i + 1
                ch = ch + ch1
            elif ord(x[i]) > 127:
                ee = ''
                while ord(x[i]) >= 127:
                    ee += x[i]
                    i += 1

                if random.randint(lvl, 10) == 10:
                    if rp == 0:
                        ch = ch + '<span style="font-size: 0.000000000000000000000000000000' + str(random.randint(100, 100000)) + random.choice(bite) + ';">' + worderx + '</span>' + ee + '<span style="font-size: 0.000000000000000000000000000000' + str(random.randint(100, 100000)) + random.choice(bite) + ';">' + random.choice(list(open(types, encoding = 'utf8'))) + '</span>'
                        rp += 10
                    else:
                        ch = ch + ee + '<span style="font-size: 0.000000000000000000000000000000' + str(random.randint(
                                100, 100000)) + random.choice(bite) + ';">' + random.choice(list(open(types, encoding = 'utf8'))) + '</span>'
                elif rp == 0:
                    ch = ch + '<span style="font-size: 0.000000000000000000000000000000' + str(random.randint(100, 100000)) + random.choice(bite) + ';">' + worderx + '</span>' + ee
                    rp += 10
                else:
                    ch = ch + ee
            elif x[i] == '&' and x[i] != '<' and (
                    x[(i + 3)] == ';' or x[(i + 4)] == ';' or x[(i + 5)] == ';' or x[(i + 6)] == ';' or x[(i + 7)] == ';' or
                    x[(i + 8)] == ';' or x[(i + 9)] == ';' or x[(i + 10)] == ';'):
                ch3 = ''
                ch3 = ch3 + x[i]
                while x[i] != ';':
                    i = i + 1
                    ch3 = ch3 + x[i]

                i = i + 1
                if random.randint(lvl, 10) == 10:
                    if rp == 0:
                        ch = ch + '<span style="font-size: 0.000000000000000000000000000000' + str(random.randint(100, 100000)) + random.choice(bite) + ';">' + worderx + '</span>' + ch3 + '<span style="font-size: 0.000000000000000000000000000000' + str(random.randint(100, 100000)) + random.choice(bite) + ';">' + random.choice(list(open(types, encoding = 'utf8'))) + '</span>'
                        rp += 10
                    else:
                        ch = ch + ch3 + '<span style="font-size: 0.000000000000000000000000000000' + str(random.randint(100, 100000)) + random.choice(bite) + ';">' + random.choice(list(open(types, encoding = 'utf8'))) + '</span>'
                elif rp == 0:
                    ch = ch + '<span style="font-size: 0.000000000000000000000000000000' + str(random.randint(100, 100000)) + random.choice(bite) + ';">' + worderx + '</span>' + ch3
                    rp += 10
                else:
                    ch = ch + ch3
            elif i <= len(x) and x[i] != '<' and x[i] != '&' and ord(x[i]) < 127:
                if random.randint(lvl, 10) == 10:
                    if rp == 0:
                      ch = ch + '<span style="font-size: 0.000000000000000000000000000000' + str(random.randint(100, 100000)) + random.choice(bite) + ';">' + worderx + '</span>' + x[i] + '<span style="font-size: 0.000000000000000000000000000000' + str(random.randint(100, 100000)) + random.choice(bite) + ';">' + random.choice(list(open(types, encoding = 'utf8'))) + '</span>'
                      i = i + 1
                      rp += 10
                    else:
                        ch = ch + x[i] + '<span style="font-size: 0.000000000000000000000000000000' + str(random.randint(100, 100000)) + random.choice(bite) + ';">' + random.choice(list(open(types, encoding = 'utf8'))) + '</span>'
                        i = i + 1
                elif rp == 0:
                    ch += '<span style="font-size: 0.000000000000000000000000000000' + str(random.randint(100, 100000)) + random.choice(bite) + ';">' + worderx + '</span>' + x[i]
                    i += 1
                    rp += 10
                else:
                    ch += x[i]
                    i += 1
    ch2 = ch
    ch2 = ch2.replace('>>', '>')
    ch2 = ch2.replace('> <', '>\xad&nbsp;<')
    ch2 = ch2.replace('> ', '>&shy;&nbsp;')
    f = open('encrypted.html', 'w')
    f.write(str(ch2.encode('utf8')))
    f.close()
    return start


if __name__ == '__main__':
    start = timer()
    main()
    print(
            f'{cyan}Thank you for waiting\n'
            f'Done in: {white}{str(timer() - start)}.\n'
            f' {cyan}You can find your '
            f'letter in your '
            f'CWD, '
            f'titled {red}"encrypted.html"')
    print(lgrn + '''
    \t[1] - Exit tool\n
    [2] - Obfuscate another letter\n
    [3] - Contact Support\n''')
    lastchoice = input(red + 'Make your selection now:   ')
    if lastchoice == '1':
        os.exit()
    elif lastchoice == '2':
        main()
    elif lastchoice == '3':
        webbrowser.open_new(contact_us)
