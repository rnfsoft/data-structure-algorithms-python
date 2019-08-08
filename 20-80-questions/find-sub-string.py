def substring_changer(str1, str2):
    idx = str1.find(str2)
    if idx is not -1:
        rev_str2 = str2[::-1]
        return str1.replace(str2, rev_str2)
    else:
        return None



str1 = "this is string example....wow!!!"
str2 = "exam"
print(substring_changer(str1, str2))


