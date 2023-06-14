#!/usr/bin/python3
def roman_to_int(roman_string):
    """
    Converts a Roman numeral to an integer
    :param roman_string:
    :return:
    """
    translation = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    if type(roman_string) is not str or roman_string is None:
        return 0
    dec_num_list = []
    for i in roman_string:
        if i in translation:
            dec_num = translation[i]
            dec_num_list.append(dec_num)

    if len(dec_num_list) > 1:

        for j, k in enumerate(dec_num_list[:-1]):
            if k < dec_num_list[j + 1]:
                dec_num_list[j] = dec_num_list[j + 1] - dec_num_list[j]
                dec_num_list[j + 1] = 0
                rom_numb = sum(dec_num_list)
                # print(rom_numb)

            else:
                rom_numb = sum(dec_num_list)
                # print(rom_numb)

        return rom_numb
    else:
        return dec_num_list[0]
