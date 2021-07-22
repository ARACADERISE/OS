from colorama import Fore, Style
import sys

KEYWORDS = [
    'import',
    'print',
    'def',
    'class',
    '__init__',
    'with',
    'open',
    'file',
    'from',
    'for',
    'in',
    'is',
    'if',
    'while',
    'else',
    'elif',
    'True',
    'False',
    'None',
    'as',
    'not',
    'self',
    'pass',
    'range'
]
COLORS = {
    'import': Fore.RED,
    'from': Fore.RED,
    'print': Fore.CYAN,
    'file': Fore.CYAN,
    'with': Fore.YELLOW,
    'as': Fore.YELLOW,
    'open': Fore.CYAN,
    'for': Fore.YELLOW,
    'in': Fore.YELLOW,
    'is': Fore.YELLOW,
    'not': Fore.YELLOW,
    'while': Fore.CYAN,
    'if': Fore.GREEN,
    'else': Fore.GREEN,
    'elif': Fore.GREEN,
    'True': Fore.BLUE,
    'False': Fore.BLUE,
    'None': Fore.BLUE,
    '__init__': Fore.CYAN,
    'def': Fore.MAGENTA,
    'class': Fore.MAGENTA,
    'self': Fore.YELLOW,
    'pass': Fore.RED,
    'range': Fore.CYAN
}

with open(sys.argv[1], 'r') as file:
    data = file.read()
    
    data = data.split(' ')
    #print(data)
    #sys.exit()
    for k in data:
        if '\n' in k:
            times = 0
            for i in range(len(k)):
                if i == len(k) - 1: break
                if k[i] == '\n': times+=1

            if times == 0: times = 1
            k = k.split('\n')
            #print(k)
            for i in range(len(k)):
                if k[i] == '':
                    for t in range(times): print()
                else:
                    for a in range(len(KEYWORDS)):
                        if KEYWORDS[a] in k[i]:
                            s_f = False
                            for t in k[i]:
                                if t == ')' or t == ']':
                                    print(Fore.WHITE + t + Style.RESET_ALL, end = '')
                                    continue
                                if t == '(' or t == '[':
                                    s_f = True
                                    print(Fore.WHITE + t + Style.RESET_ALL, end = '')
                                    continue
                                if s_f:
                                    print(Fore.WHITE + t + Style.RESET_ALL, end = '')

                                    if t == ')' or t == ']' or t == ':': s_f = False
                                else: print(COLORS[KEYWORDS[a]] + t + Style.RESET_ALL, end = '')
                            print(' ', end = '')
                            #print(COLORS[KEYWORDS[a]] + k[i] + Style.RESET_ALL, end = ' ')
                            break
                        else:
                            if a == len(KEYWORDS) - 1:
                                print(Fore.WHITE + k[i] + Style.RESET_ALL, end = ' ')
                                break
        else:
            for a in range(len(KEYWORDS)):
                if KEYWORDS[a] in k:
                    for t in k:
                        if t == '(' or t == ')' or t == ':': print(Fore.WHITE + t + Style.RESET_ALL, end = '')
                        else: print(COLORS[KEYWORDS[a]] + t + Style.RESET_ALL, end = '')
                    print(' ', end = '')
                    #print(COLORS[KEYWORDS[a]] + k + Style.RESET_ALL, end = ' ')
                    break
                else:
                    if a == len(KEYWORDS) - 1: 
                        print(Fore.WHITE + k + Style.RESET_ALL, end = ' ')
                        break
    file.close()
    print()
