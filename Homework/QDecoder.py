def decode_playfair_digrams(eText):
    dText = ""
    i = eText.find('Q')
    while(i>-1):        
        if eText[i-1] == eText[i+1]:
            dText = eText[:i-1] + eText[i+1:]
        if i == -1:
            return "not encrypted"
        else:
            i = eText.find('Q', i)
            if i == -1:
                return "not encrypted"
            dText = eText[:i-1] + eText[i+1:]
            i = eText.find('Q')
    return dText

print(decode_playfair_digrams('misQsisQsipQpi'))