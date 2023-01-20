# 01100111 01110010 01100001 01110100 01110101 01101100 01100001 01100011 01101010 01100101
# gratulacje

# binary = '01100111 01110010 01100001 01110100 01110101 01101100 01100001 01100011 01101010 01100101'
binary = '01100111011100100110000101110100011101010110110001100001011000110110101001100101'
# binary_wo_spc = binary.replace(" ", "")
# binary_wo_spc = binary.split()
# print(binary_wo_spc)
for spaces in binary:
    if spaces.isspace():
        result = [binary[i:i + 8] for i in range(0, len(binary), 8)]
        print(result)
    else:
        # for byte in range(0, len(binary), 7):
        break
binary_wo_spc = binary.split()
print(binary_wo_spc)

# if not binary.isspace():
#     binary_wo_spc = binary.split()
#     print(binary_wo_spc)
# else:
#     for b in range(0, len(binary), 7):
#         print(b)
    # binary_wo_spc = binary.split()
    # for i in range(0, len(binary_wo_spc)):
    #     # print(binary_wo_spc[i])
    #
    #     data = int(binary_wo_spc[i], 2)
    #     print(chr(data), end="")



#data = int('0b01100111', 2)
# datastring = chr(data)
# print(datastring)