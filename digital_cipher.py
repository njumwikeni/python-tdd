import math

alpha_numeric = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,
                 'j':10,'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,
                 'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26}

def encode(word,key):
    coded=[]
    coded_final=[]
    #print(len(word))
    key_iterations = math.ceil(len(word)/len(str(key)))
    key_to_add = str(key)*key_iterations

    #print(key_to_add)
    for x in word:
        coded.append(alpha_numeric[x])

    for y in range(len(coded)):
        coded_final.append(coded[y]+int(key_to_add[y]))

    return coded_final

def decode(word,key):
    level_one_decode=[]
    level_two_decode = ''
    key_iterations = math.ceil(len(word)/len(str(key)))
    key_to_subtract = str(key)*key_iterations

    for y in range(len(word)):
        level_one_decode.append(word[y]-int(key_to_subtract[y]))

    for x in range(len(level_one_decode)):
        level_two_decode+=get_dict_key(level_one_decode[x],alpha_numeric)

    return level_two_decode


def get_dict_key(val,a_dict):
    for k, value in a_dict.items():
        if val== value:
            return k
        else:
            pass

print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")

print (encode("scout",1939))
print (encode("masterpiece",1939))


print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")

print (decode([ 20, 12, 18, 30, 21],1939))
print (decode([ 14, 10, 22, 29, 6, 27, 19, 18, 6, 12, 8],1939))

print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
