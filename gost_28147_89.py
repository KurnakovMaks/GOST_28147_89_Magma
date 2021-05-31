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


plain_text = "81ddb2a8fac76d12"
L0 = "81ddb2a8"
R0 = "fac76d12"

key = ["13a170cf", "4764cb9b", "cf55b828", "08fae737",
       "e802eee0", "b3eb590a", "77e1b970", "99ca3d21",
       "13a170cf", "4764cb9b", "cf55b828", "08fae737",
       "e802eee0", "b3eb590a", "77e1b970", "99ca3d21",
       "13a170cf", "4764cb9b", "cf55b828", "08fae737",
       "e802eee0", "b3eb590a", "77e1b970", "99ca3d21",
       "99ca3d21", "77e1b970", "b3eb590a", "e802eee0",
       "08fae737", "cf55b828", "4764cb9b", "13a170cf"]

'''plain_text = "9a0573bd4b2d295c"
L0 = "9a0573bd"
R0 = "4b2d295c"

key =  ["18a75dcf", "2c1ee560", "14621875", "7206bfba",
        "358ea8f4", "e36ed553", "18fb69db", "0ec9b5b9",
        "18a75dcf", "2c1ee560", "14621875", "7206bfba",
        "358ea8f4", "e36ed553", "18fb69db", "0ec9b5b9",
        "18a75dcf", "2c1ee560", "14621875", "7206bfba",
        "358ea8f4", "e36ed553", "18fb69db", "0ec9b5b9",
        "0ec9b5b9", "18fb69db", "e36ed553", "358ea8f4",
        "7206bfba", "14621875", "2c1ee560", "18a75dcf"]'''

S_boxes = ["4a92d80e6b1c7f53", "eb4c6dfa23810759",
           "581da342efc7609b", "7da1089fe46cb253",
           "6c715fd84a9e03b2", "4ba0721d36859cfe",
           "db413f590ae7682c", "1fd057a4923e6b8c"]


j = 0
while (j < 32):
    round_key = key[j]
    print(f"round key = {round_key}")
    R_start = R0
    round_key_10 = convert_base(round_key, from_base=16, to_base=10)
    print("round_key in 10 = ", round_key_10)
    R_10 = convert_base(R_start, from_base=16, to_base=10)
    print("R = ", R_10)
    k1 = (int(round_key_10)) + (int(R_10))
    print("K1 = ", k1)
    big = pow(2, 32)
    k1_mod_2_32 = (int(k1)) % (int(big))
    print("R + K mod 2^32 = ", k1_mod_2_32)
    if len(convert_base(k1_mod_2_32, from_base=10, to_base=2)) < 32:
        print("0"*(32-len(convert_base(k1_mod_2_32, from_base=10, to_base=2))
                   ) + convert_base(k1_mod_2_32, from_base=10, to_base=2))

    rk_mod_2_32_16 = convert_base(k1_mod_2_32, from_base=10, to_base=16)
    len_rk_mod_2_32_16 = len(rk_mod_2_32_16)

    '''print("len_rk_mod_2_32_16 = ", len_rk_mod_2_32_16)'''

    if len_rk_mod_2_32_16 == 8:
        rk_mod_2_32_16_10 = rk_mod_2_32_16
    elif len_rk_mod_2_32_16 == 7:
        rk_mod_2_32_16_10 = "0" + rk_mod_2_32_16
    elif len_rk_mod_2_32_16 == 6:
        rk_mod_2_32_16_10 = "00" + rk_mod_2_32_16

    '''print("rk_mod_2_32_16_10 = ", rk_mod_2_32_16_10)'''

    i = 0
    '''print(f"S_boxes[{i}] = ", S_boxes[i])'''

    '''print("len(rk_mod_2_32_16_10) = ", len(rk_mod_2_32_16_10))'''
    SR = ""
    for i in range(len(rk_mod_2_32_16_10)):
        SR += S_boxes[i][int(convert_base(rk_mod_2_32_16_10[i],
                                          from_base=16, to_base=10))]

    '''print("SR = ", SR)'''
    print("S ( R ) = ", SR)
    if len(convert_base(SR, from_base=16, to_base=2)) < 32:
        '''print("SR_2 = ", "0"*(32-len(convert_base(SR, from_base=16, to_base=2))) + convert_base(SR, from_base=16, to_base=2))'''
        print("\tS ( R ) = ", "0" * (32 - len(convert_base(SR, from_base=16,
                                                           to_base=2))) + convert_base(SR, from_base=16, to_base=2))

    new_data_2 = ""
    i = 0
    for i in range(len(SR)):
        if len(convert_base(SR[i], from_base=16, to_base=2)) == 4:
            new_data_2 += convert_base(SR[i], from_base=16, to_base=2)
        elif len(convert_base(SR[i], from_base=16, to_base=2)) == 3:
            new_data_2 += "0" + convert_base(SR[i], from_base=16, to_base=2)
        elif len(convert_base(SR[i], from_base=16, to_base=2)) == 2:
            new_data_2 += "00" + convert_base(SR[i], from_base=16, to_base=2)
        elif len(convert_base(SR[i], from_base=16, to_base=2)) == 1:
            new_data_2 += "000" + convert_base(SR[i], from_base=16, to_base=2)

    '''print("new_data_2 = ", new_data_2)'''

    i = 0
    new_data_2_x = ""

    for i in range(len(new_data_2)-11):
        new_data_2_x += new_data_2[i+11]
    for i in range(11):
        new_data_2_x += new_data_2[i]

    '''print("new_data_2_x = ", new_data_2_x)'''
    print("Shift = ", new_data_2_x)

    L = L0
    L_2 = convert_base(L, from_base=16, to_base=2)
    if (len(L_2)) < 32:
        old_L2 = L_2
        L_2 = ""
        L_2 += "0" * (32 - len(old_L2)) + \
            convert_base(L0, from_base=16, to_base=2)

    L_2_xor_new_data_2_x = ""

    print(len(new_data_2_x))
    print(len(L_2))

    for i in range(len(new_data_2_x)):
        L_2_xor_new_data_2_x += "1" if L_2[i] != new_data_2_x[i] else "0"

    '''print("L_2_xor_new_data_2_x = ", L_2_xor_new_data_2_x)'''
    print("L ( + ) F ( R ) = ", L_2_xor_new_data_2_x)

    new_answer = ""
    i = 0
    new_answer = convert_base(L_2_xor_new_data_2_x, from_base=2, to_base=16)
    '''print("new_answer = ", new_answer)'''
    if (len(new_answer)) < 8:
        old_newans = new_answer
        new_answer = ""
        new_answer += "0" * (8 - len(old_newans)) + old_newans

    '''print("new_answer_R0 = ", R+new_answer)'''
    print(f"L1 = {R_start} || R1 = {new_answer}")
    print(f"{R_start} = {convert_base(R_start,10,16)}")
    print(f"{new_answer} = {convert_base(new_answer,10,16)}")

    print(f"-{j+1}"*23)
    j += 1

    L0 = R_start
    R0 = new_answer
    print("-------------------------------------------------------------------")

    print("-------------------------------------------------------------------")

    print("-------------------------------------------------------------------")
