# genwords.py
# find corresponding words from random letters

dico = "/usr/share/dict/words"
ustr = "ccfeaceafbddfcfaebecdaedabdaab"


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


warr = list()
fword = ""
ulet = sort_letters(ustr)
print ulet
n = 0

file = open(dico, 'r')
for line in file:
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
        warr.append(fword)
        n = n + 1

file.close()

warr.sort(key=len, reverse=True)
print warr[0]


# get images from google

# create new image

# send to server

#
