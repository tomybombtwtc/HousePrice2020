import pandas as pd

def check_if_chinese(input_str):
    chk_result = True
    for ch in input_str:
        if u'\u4e00' >= ch or ch >= u'\u9fff':
            chk_result = False
    return chk_result

def trunc_address_no(testAddr):
    result_str = ""
    if testAddr.find("地號") > 0:
        j = testAddr.index("地號")
    else:
        j = testAddr.index("號")

    run_flag = True
    while run_flag:
        tmp_char = testAddr[j - 1]
        #print(j, ". ", tmp_char)
        if check_if_chinese(tmp_char):
            #print("Final String = ", testAddr[0:j])
            result_str = testAddr[0:j]
            run_flag = False
        j = j - 1

    return result_str

addressALLData = pd.read_csv("2019_OrgTC_BUY_V7_ForPython.csv")
addressData = addressALLData['Adress']
new_address_rawdata = []
print(addressData[0])
print(type(new_address_rawdata))
i = 0
while i < len(addressData):
    tmp_new_address = trunc_address_no(addressData[i])
    #print(i, " = ", tmp_new_address)
    new_address_rawdata.append(tmp_new_address)
    i = i + 1
#print("new_address_rawdata[100] = ",  new_address_rawdata[100])
finalDataframe = pd.DataFrame(new_address_rawdata, columns=["Address"])
#print(finalDataframe.head())
print(addressALLData['Adress'].head())
addressALLData.insert(5, 'Address', finalDataframe)
print(addressALLData['Address'].head())
addressALLData.to_csv("test0412.csv", index=False, sep=',', encoding='utf-8-sig' )
