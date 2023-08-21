def filter_data(result):
    text = ""
    num = ''
    joined = False

    for res in result:
        print(res[1])
    print('\n')

    # getting if text part has length of 3
    for res in result:
        try:
            _text = res[1][:3].upper()
            count = 0
            for chr in _text:
                if chr.isalpha():
                    count += 1
                if count >= 2:
                    _text = _text.replace('0','O')
            if _text.isalpha():# and res[1][:3].isupper():
                
                if (res[1][3] == ' ' or res[1][3] == '-' or res[1][3] == ':' or res[1][3] == ';') and 'ISL' not in res[1].upper() and 'ICT' not in res[1].upper() and 'MABAD' not in res[1].upper()  and 'PUNJAB' not in res[1].upper():
                    text = _text
                    try:
                        temp = res[1][4::]
                        temp = temp.replace("&", "8")
                        temp = temp.replace("]", "1")
                        _temp = int(temp)
                        if num == '' or _temp > int(num):
                            text = _text
                            num = temp
                            joined = True
                            # ans = _text + '-' + temp
                            # print(1)
                            # print(ans)
                            # return ans
                    except:
                        pass
                else:
                    try:
                        _temp = res[1][3::]
                        temp = int(_temp)
                        if num == '' or temp > int(num):
                            joined = True
                            text = _text
                            num = _temp
                            # ans = _text + '-' + str(temp)
                            # print(2)
                            # print(ans)
                            # return ans
                    except:
                        pass

        except:
            pass
     # getting if text part has length of 2
    if not text:
        for res in result:
            try:
                if res[1][:2].isalpha():
                    _text = res[1][:2].upper()
                    if (res[1][2] == ' ' or res[1][2] == '-' or res[1][2] == ':' or res[1][2] == ';' or res[1][2].islower()) and 'ISL' not in res[1] and 'ICT' not in res[1] and 'MABAD' not in res[1] and 'PUNJAB' not in res[1].upper():
                        try:
                            temp = res[1][3::]
                            temp = temp.replace("&", "8")
                            temp = temp.replace("]", "1")
                            _temp = int(temp)
                            if num == '' or _temp > int(num):
                                joined = True
                                text = _text
                                num = temp
                                # ans = _text + '-' + temp
                                # print(3)
                                # print(ans)
                                # return ans
                        except:
                            pass
            except:
                pass
    if not text:
        for res in result:
            if res[1].isalpha() and res[1].isupper() and len(res[1]) == 3  and 'ISL' not in res[1] and 'PUNJAB' not in res[1]:
                text = res[1]
            try:
                temp = int(res[1])
                if num == '' or temp > int(num):
                    num = res[1]
            except:
                pass
    if not text:
        for res in result:
            if res[1].isalpha() and res[1].isupper() and len(res[1]) == 2  and 'IS' not in res[1] and 'PUNJAB' not in res[1].upper():
                text = res[1]
    if not text:
        for res in result:
            _text = "".join(ch for ch in res[1] if ch.isalnum())
            try:
                int(_text)
                break
            except:
                pass
            if len(_text) < 4 and ('ISL' not in _text) and ('ABAD' not in _text) and ('PUNJAB' not in _text):
                text = _text
    if not text:
        for res in result:
            if res[1].isalpha() and res[1].isupper()  and 'IS' not in res[1] and 'PUNJAB' not in res[1].upper():
                text = res[1][:3]
    # filtering integer part
    for res in result:
        try:
            temp = int(res[1][:4])
            if num == '' or temp > int(num):
                num = res[1][:4]
        except:
            try:
                temp = int(res[1][:3])
                if num == '' or temp > int(num):
                    num = res[1][:3]
            except:
                pass
        try:
            _temp = res[1].replace(' ', '')
            temp = int(_temp)
            if num == '' or temp > int(num):
                num = _temp
        except:
            pass
    if not joined:
        for res in result:
            count = 0
            for chr in res[1]:
                try:
                    int(chr)
                    count += 1
                except:
                    pass
            if count > len(res[1])/2:
                _num = res[1].replace('C', '0')
                _num = res[1].replace('.', '')
            try:
                if not num:
                    int(_num)
                    num = _num
            except:
                pass

    if num:
        if len(num) > 4:
            text = text + '-' + str(num[:4])
        else:
            text = text + '-' + str(num)
    found = False
    for res in result:
        if 'PUNJAB' in res[1].upper() or (res[1][0].upper() == 'P' and res[1][-1].upper() == 'B'):
            text = text + '@PUNJAB'
            found = True
            break
        if 'ISLAMABAD' in res[1].upper() or 'AMABAD' in res[1].upper() or 'ABAD' in res[1].upper() or 'ISLA' in res[1].upper():
            text = text + '@ISLAMABAD'
            found = True
            break
        if 'SINDH' in res[1].upper():
            text = text + '@SINDH'
            found = True
            break

    if not found:
        text = text + '@Not found'
    return text