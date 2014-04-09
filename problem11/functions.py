# Source Generated with Decompyle++
# File: functions.pyc (Python 2.7)


def hori_right(tab):
    maxHR = 0
    i = 0
    j = 0
    while i < len(tab):
        j = 0
        while j < len(tab[i]) - 3:
            n = tab[i][j] * tab[i][j + 1] * tab[i][j + 2] * tab[i][j + 3]
            if n > maxHR:
                maxHR = n
            j += 1
        i += 1
    return maxHR


def hori_left(tab):
    maxHL = 0
    i = 0
    j = 3
    while i < len(tab):
        j = 3
        while j < len(tab):
            n = tab[i][j] * tab[i][j - 1] * tab[i][j - 2] * tab[i][j - 3]
            if n > maxHL:
                maxHL = n
            j += 1
        i += 1
    return maxHL


def vert_up(tab):
    maxVU = 0
    i = 3
    j = 0
    while i < len(tab):
        j = 0
        while j < len(tab):
            n = tab[i][j] * tab[i - 1][j] * tab[i - 2][j] * tab[i - 3][j]
            if n > maxVU:
                maxVU = n
            j += 1
        i += 1
    return maxVU


def vert_down(tab):
    maxVD = 0
    i = 0
    j = 0
    while i < len(tab) - 3:
        j = 0
        while j < len(tab):
            n = tab[i][j] * tab[i + 1][j] * tab[i + 2][j] * tab[i + 3][j]
            if n > maxVD:
                maxVD = n
            j += 1
        i += 1
    return maxVD


def diag_up_left(tab):
    maxUL = 0
    i = 3
    j = 3
    while i < len(tab):
        j = 3
        while j < len(tab):
            n = tab[i][j] * tab[i - 1][j - 1] * tab[i - 2][j - 2] * tab[i - 3][j - 3]
            if n > maxUL:
                maxUL = n
            j += 1
        i += 1
    return maxUL


def diag_up_right(tab):
    maxUR = 0
    i = 3
    j = 0
    while i < len(tab):
        j = 0
        while j < len(tab) - 3:
            n = tab[i][j] * tab[i - 1][j + 1] * tab[i - 2][j + 2] * tab[i - 3][j + 3]
            if n > maxUR:
                maxUR = n
            j += 1
        i += 1
    return maxUR


def diag_down_left(tab):
    maxDL = 0
    i = 0
    j = 3
    while i < len(tab) - 3:
        j = 3
        while j < len(tab):
            n = tab[i][j] * tab[i + 1][j - 1] * tab[i + 2][j - 2] * tab[i + 3][j - 3]
            if n > maxDL:
                maxDL = n
            j += 1
        i += 1
    return maxDL


def diag_down_right(tab):
    maxDR = 0
    i = 0
    j = 0
    while i < len(tab) - 3:
        j = 0
        while j < len(tab) - 3:
            n = tab[i][j] * tab[i + 1][j + 1] * tab[i + 2][j + 2] * tab[i + 3][j + 3]
            if n > maxDR:
                maxDR = n
            j += 1
        i += 1
    return maxDR

