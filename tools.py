def dictToStr(dictionary, seperator, optionalSeperator, trimLast=True):
    concat = ""
    for key, value in dictionary.items():
        concat = concat + key + seperator + str(value) + optionalSeperator
    if trimLast == True:
        concat = concat.strip(optionalSeperator)
    return concat