def is_isogram(string):
    string = string.lower()
    string = string.replace(" ","")
    string = string.replace("-","")
    return len(set(string)) == len(string)
