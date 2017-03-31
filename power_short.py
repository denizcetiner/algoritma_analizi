# -*- coding: utf-8 -*-


def power(a, b):
    toplam_carpma_islemi = 0
    powers = [a] #a^1,a^2,a^4,a^8,a^16,a^32,a^64,a^128,a^256......
    while(True):
        last_element = powers[len(powers)-1]
        powers.append(last_element * last_element)
        toplam_carpma_islemi += 1
        if(2 ** len(powers) > b):
            break
    power_counter = 0
    result = 1
    index = len(powers)-1
    while(power_counter < b):
        if(power_counter + (2 ** index) > b):
            index=index-1
            continue
        result = result * powers[index]
        toplam_carpma_islemi += 1
        power_counter = power_counter + (2 ** index)
        index=index-1
    print("sonuc " + str(result))
    return toplam_carpma_islemi

print(power(3,62))
