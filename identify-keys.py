import subprocess
from enum import Enum

# TODO: Figure out what the rest of these are

class Keycode(Enum):
    ESC = 9
    ONE = 10
    TWO = 11
    THREE = 12
    FOUR = 13
    FIVE = 14
    SIX = 15
    SEVEN = 16
    EIGHT = 17
    NINE = 18
    ZERO = 19
    MINUS = 20
    EQUALS = 21
    BACKSPACE = 22
    TAB = 23
    Q = 24
    W = 25
    E = 26
    R = 27
    T = 28
    Y = 29
    U = 30
    I = 31
    O = 32
    P = 33
    RIGHTBRACE = 34
    LEFTBRACE = 35
    ENTER = 36
    LEFTCTRL = 37
    A = 38
    S = 39
    D = 40
    F = 41
    G = 42
    H = 43
    J = 44
    K = 45
    L = 46
    COLON = 47
    QUOTE = 48
    GRAVE = 49
    LEFTSHIFT = 50
    HASH = 51
    Z = 52
    X = 53
    C = 54
    V = 55
    B = 56
    N = 57
    M = 58
    COMMA = 59
    PERIOD = 60
    SLASH = 61
    RIGHTSHIFT = 62
    LEFTALT = 64
    SPACE = 65
    CAPSLOCK = 66
    F1 = 67
    F2 = 68
    F3 = 69
    F4 = 70
    F5 = 71
    F6 = 72
    F7 = 73
    F8 = 74
    F9 = 75
    F10 = 76
    SCROLLLOCK = 78
    F11 = 95
    F12 = 96
    RIGHTCTRL = 105
    PRTSCN = 107
    ALTGR = 108
    HOME = 110
    UP = 111
    PGUP = 112
    LEFT = 113
    RIGHT = 114
    END = 115
    DOWN = 116
    PGDOWN = 117
    INSERT = 118
    DELETE = 119
    PAUSE = 127
    LEFTSUPER = 133
    MENU = 135


proc = subprocess.Popen(['xinput', 'test-xi2', '--root'],
                        stdout=subprocess.PIPE)

inkeypressevent = False
inkeyreleaseevent = False

while True:
    line = proc.stdout.readline()
    if line != '':
        if line == b'EVENT type 2 (KeyPress)\n':
            inkeypressevent = True
        elif line.startswith(b'    detail:') and inkeypressevent:
            code = int(line.split()[1])
            try:
                key = Keycode(code)
                print(key, end='')
                print(' - ', end='')
                print(code)
            except ValueError:
                print('unknown key - ' + code)
            inkeypressevent = False
