def DecimalToBinaryR1(test_num):
    return  [int(i) for i in list('{0:04b}'.format(test_num))]
def DecimalToBinaryR2(test_num):
    return  [int(i) for i in list('{0:08b}'.format(test_num))]
def binaryToDecimal(binary):
    return sum(val*(2**idx) for idx, val in enumerate(reversed(binary)))

def combine(buff1,buff):
    for i in buff1:
        buff.append(i)


def raw_angle(l):
    L1 = []
    L2 = []
    buff = []
    buff1 = []
    buff2 = []
    i=0
    L1.append(l[0])
    L1.append(l[1])
    buff1 = DecimalToBinaryR1(L1[0])
    buff2 = DecimalToBinaryR2(L1[1])
    combine(buff1,buff)
    combine(buff2,buff)
    print((360/4096)*binaryToDecimal(buff))
    return((360/4096)*binaryToDecimal(buff))


