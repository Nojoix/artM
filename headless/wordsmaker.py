# genwords.py
# find corresponding words from random letters

from multiprocessing import Pool

dico = "/Users/vvaysse/Downloads/words.txt"


def sort_letters(tstr):
    str_array = {"": 0}
    nstr = tstr.replace('\n', '')
    i = 0
    while i < len(nstr):

        if nstr[i] in str_array:
            str_array[nstr[i]] = str_array[nstr[i]] + 1
        else:
            str_array[nstr[i]] = 1

        i = i + 1

    return str_array


def lineParser(line):
    fword = ""
    line = line.lower()
    line = line.replace('\n', '')
    buf = sort_letters(line)
    # print buf
    o = 0
    while o < len(line):
        if line[o] in ulet:
            fword += line[o]
        else:
            fword = ""
        o = o + 1

    if len(fword) == len(line):
        print(fword)
        return fword
        #n = n + 1


def run(ustr):
    global ulet
    ulet = sort_letters(ustr)
    print ulet
    #n = 0
    file = open(dico, 'r')
    p = Pool(20)
    warr = p.map(lineParser,file)
    warr = list(filter(None, warr))
    p.close()
    p.join()
    file.close()
    warr.sort(key=len, reverse=True)
    return warr

# get images from google

# create new image

# send to server

#
