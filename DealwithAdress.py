
def check_if_chinese(input_str):
    chk_result = True
    for ch in input_str:
        if u'\u4e00' >= ch or ch >= u'\u9fff':
            chk_result = False
    return chk_result

testAddr = "台中市北屯區軍榮五街181~210號"
print("地號 position = ", testAddr.find("地號"))
print("Skip [地號] = ", testAddr[0:testAddr.index("地號")])
i = 0
for tmpChar in testAddr:
    ch_check = "-"
    if check_if_chinese(tmpChar):
        ch_check = "Y"
    else:
        ch_check = "N"

    print(i, ". ", tmpChar, "(", ch_check, ")")
    i = i +1
    if tmpChar=="地號":
        print("到我就結束了-", tmpChar)
print("===============倒著印=========", j)

run_flag = True
while run_flag:
    tmpChar = testAddr[j-1]
    print(j, ". ", tmpChar)
    if check_if_chinese(tmpChar):
        print("Final String = ", testAddr[0:j])
        run_flag = False
    j = j-1


