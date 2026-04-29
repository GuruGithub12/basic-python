my_dictionary = { 
    "Guru": 85,
    "Lucky": 78,
    "Adya": 92
}

def  fn_CheckKey(my_dictionary, key):
    if key in my_dictionary:
        return key + " is present in the dictionary"
    else:
        return key +" is not present in the dictionary"
print(fn_CheckKey(my_dictionary, "Guru"))