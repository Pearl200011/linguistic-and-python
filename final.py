import sys
def count_alphabets(in_str):
    alphabet_count_dict = {}
    for alphabet in in_str:
        if str not in alphabet_count_dict.keys():
            alphabet_count_dict[alphabet]=1
        else:
            alphabet_count_dict[alphabet]=alphabet_count_dict[alphabet]+1
    return alphabet_count_dict
def sortdic(indic):
    sortlist=[]
    
    sortlist=sorted(indic.items(),key=lambda pair:pair[1],reverse = True)
    return(sortlist)
def Convert(tup, di):
    di = dict(tup)
    return di
    
str2 = ""
for line in sys.stdin.readlines():
    s = line.strip()
    index = 0
    index1 = 0
    str = ""
    for alphabet in s:
        str +=alphabet
        if (alphabet == "b" ):
            index = len(str)
            stri = alphabet + s[index]
            str2 += stri + " "
a = str2.strip()
v = a.split(" ")
alphabet_count_dict = count_alphabets(v)
sortL=sortdic(alphabet_count_dict)
diction={}
sortlist2=Convert(sortL,diction)
keylist=list(sortlist2.keys())
print(keylist)