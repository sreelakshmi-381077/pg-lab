def replace_char(s):
    first=s[0]
    modified=s.replace(first,"$")
    return first+modified[1:]
print(replace_char("onion"))