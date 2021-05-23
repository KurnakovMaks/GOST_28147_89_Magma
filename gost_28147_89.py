from math import *

plain_text = "81ddb2a8fac76d12"
L0 = "81ddb2a8"
R0 = "fac76d12"

def convert_base(num, to_base=10, from_base=10):
    # first convert to decimal number
    if isinstance(num, str):
        n = int(num, from_base)
    else:
        n = int(num)
    # now convert decimal to 'to_base' base
    alphabet = "0123456789abcdefgABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if n < to_base:
        return alphabet[n]
    else:
        return convert_base(n // to_base, to_base) + alphabet[n % to_base]










key1 = "13a170cf"
key2 = "4764cb9b"
key3 = "cf55b828"
key4 = "08fae737"
key5 = "e802eee0"
key6 = "b3eb590a"
key7 = "77e1b970"
key8 = "99ca3d21"
key9 = "13a170cf"
key10 = "4764cb9b"
key11 = "cf55b828"
key12 = "08fae737"
key13 = "e802eee0"
key14 = "b3eb590a"
key15 = "77e1b970"
key16 = "99ca3d21"
key17 = "13a170cf"
key18 = "4764cb9b"
key19 = "cf55b828"
key20 = "08fae737"
key21 = "e802eee0"
key22 = "b3eb590a"
key23 = "77e1b970"
key24 = "99ca3d21"
key25 = "99ca3d21"
key26 = "77e1b970"
key27 = "b3eb590a"
key28 = "e802eee0"
key29 = "08fae737"
key30 = "cf55b828"
key31 = "4764cb9b"
key32 = "13a170cf"

S_boxes = ["4a92d80e6b1c7f53", "eb4c6dfa23810759", "581da342efc7609b", "7da1089fe46cb253", "6c715fd84a9e03b2", "4ba0721d36859cfe", "db413f590ae7682c", "1fd057a4923e6b8c"]
S1 = "4a92d80e6b1c7f53"
S2 = "eb4c6dfa23810759"
S3 = "581da342efc7609b"
S4 = "7da1089fe46cb253"
S5 = "6c715fd84a9e03b2"
S6 = "4ba0721d36859cfe"
S7 = "db413f590ae7682c"
S8 = "1fd057a4923e6b8c"

'''round_key = key1
rou_key_2 = convert_base(round_key, from_base=16, to_base=2)
rou_key_10 = convert_base(rou_key_2, from_base=16, to_base=10)
R = convert_base(R0, from_base=16, to_base=10)
k1=rou_key_10
rk=(int(R))+(int(k1))

rk_mod_2_32 = (int(rk)) // (int(big))



'''

k1 = key1
R = R0
key_10 = convert_base(k1, from_base=16, to_base=10)
R_10 = convert_base(R, from_base=16, to_base=10)

rk = key_10 + R_10

big = pow(2, 32)
rk_mod_2_32 = (int(rk)) % (int(big))
print("rk_mod_2_32 = ", rk_mod_2_32)

rk_mod_2_32_16 = convert_base(rk_mod_2_32, from_base=10, to_base=16)
len_rk_mod_2_32_16 = len(rk_mod_2_32_16)

print("len_rk_mod_2_32_16 = ", len_rk_mod_2_32_16)

if len_rk_mod_2_32_16 == 8:
    rk_mod_2_32_16_10 = rk_mod_2_32_16
elif len_rk_mod_2_32_16 == 7:
    rk_mod_2_32_16_10 = "0" + rk_mod_2_32_16
elif len_rk_mod_2_32_16 == 6:
    rk_mod_2_32_16_10 = "00" + rk_mod_2_32_16

print("rk_mod_2_32_16_10 = ", rk_mod_2_32_16_10)

i = 0
print(f"S_boxes[{i}] = ", S_boxes[i])

print("len(rk_mod_2_32_16_10) = ", len(rk_mod_2_32_16_10))
new_data = ""
for i in range(len(rk_mod_2_32_16_10)):
    new_data += S_boxes[i][int(convert_base(rk_mod_2_32_16_10[i], from_base=16, to_base=10))]

print("new_data = ", new_data)

new_data_2 = ""
i = 0
for i in range(len(new_data)):
    if len(convert_base(new_data[i], from_base=16, to_base=2)) == 4:
        new_data_2 += convert_base(new_data[i], from_base=16, to_base=2)
    elif len(convert_base(new_data[i], from_base=16, to_base=2)) == 3:
        new_data_2 += "0" + convert_base(new_data[i], from_base=16, to_base=2)
    elif len(convert_base(new_data[i], from_base=16, to_base=2)) == 2:
        new_data_2 += "00" + convert_base(new_data[i], from_base=16, to_base=2)
    elif len(convert_base(new_data[i], from_base=16, to_base=2)) == 1:
        new_data_2 += "000" + convert_base(new_data[i], from_base=16, to_base=2)

print("new_data_2 = ", new_data_2)

i = 0
new_data_2_x = ""

for i in range(len(new_data_2)-11):
    new_data_2_x += new_data_2[i+11]
for i in range(11):
    new_data_2_x += new_data_2[i]

print("new_data_2_x = ", new_data_2_x)


L = L0
L_2 = convert_base(L0, from_base=16, to_base=2)

L_2_xor_new_data_2_x = ""

for i in range(len(new_data_2_x)):
    L_2_xor_new_data_2_x += "1" if L_2[i] != new_data_2_x[i] else "0"

print("L_2_xor_new_data_2_x = ", L_2_xor_new_data_2_x)


new_answer = ""
i = 0
new_answer = convert_base(L_2_xor_new_data_2_x, from_base=2, to_base=16)
print("new_answer = ", new_answer)
print("new_answer_R0 = ", new_answer+R)

print("1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1")
print("-----------------------------------------------------------------------------------")

for j in range(31):
    k1 = key2
    R = new_answer
    key_10 = convert_base(k1, from_base=16, to_base=10)
    R_10 = convert_base(R, from_base=16, to_base=10)


    rk = key_10 + R_10

    big = pow(2, 32)
    rk_mod_2_32 = (int(rk)) % (int(big))
    print("rk_mod_2_32 = ", rk_mod_2_32)

    rk_mod_2_32_16 = convert_base(rk_mod_2_32, from_base=10, to_base=16)
    len_rk_mod_2_32_16 = len(rk_mod_2_32_16)

    print("len_rk_mod_2_32_16 = ", len_rk_mod_2_32_16)

    if len_rk_mod_2_32_16 == 8:
        rk_mod_2_32_16_10 = rk_mod_2_32_16
    elif len_rk_mod_2_32_16 == 7:
        rk_mod_2_32_16_10 = "0" + rk_mod_2_32_16
    elif len_rk_mod_2_32_16 == 6:
        rk_mod_2_32_16_10 = "00" + rk_mod_2_32_16

    print("rk_mod_2_32_16_10 = ", rk_mod_2_32_16_10)

    i = 0
    print(f"S_boxes[{i}] = ", S_boxes[i])

    print("len(rk_mod_2_32_16_10) = ", len(rk_mod_2_32_16_10))
    new_data = ""
    for i in range(len(rk_mod_2_32_16_10)):
       new_data += S_boxes[i][int(convert_base(rk_mod_2_32_16_10[i], from_base=16, to_base=10))]

    print("new_data = ", new_data)

    new_data_2 = ""
    i = 0
    for i in range(len(new_data)):
        if len(convert_base(new_data[i], from_base=16, to_base=2)) == 4:
            new_data_2 += convert_base(new_data[i], from_base=16, to_base=2)
        elif len(convert_base(new_data[i], from_base=16, to_base=2)) == 3:
            new_data_2 += "0" + convert_base(new_data[i], from_base=16, to_base=2)
        elif len(convert_base(new_data[i], from_base=16, to_base=2)) == 2:
            new_data_2 += "00" + convert_base(new_data[i], from_base=16, to_base=2)
        elif len(convert_base(new_data[i], from_base=16, to_base=2)) == 1:
            new_data_2 += "000" + convert_base(new_data[i], from_base=16, to_base=2)

    print("new_data_2 = ", new_data_2)

    i = 0
    new_data_2_x = ""

    for i in range(len(new_data_2)-11):
        new_data_2_x += new_data_2[i+11]
    for i in range(11):
        new_data_2_x += new_data_2[i]

    print("new_data_2_x = ", new_data_2_x)


    L = L0
    L_2 = convert_base(L0, from_base=16, to_base=2)

    L_2_xor_new_data_2_x = ""

    for i in range(len(new_data_2_x)):
        L_2_xor_new_data_2_x += "1" if L_2[i] != new_data_2_x[i] else "0"

    print("L_2_xor_new_data_2_x = ", L_2_xor_new_data_2_x)


    new_answer = ""
    i = 0
    new_answer = convert_base(L_2_xor_new_data_2_x, from_base=2, to_base=16)
    print("new_answer = ", new_answer)
    print("new_answer_R0 = ", new_answer+R)

    print("j = ", j)
    print("2-2-2-2-2-2-2-2-2-2-2-2-2-2-2-2-2-2-2-2-2-2-2-2-2-2-2-2-2-2-2-2-2-2-2-2-2-2-2-2-2-2")

