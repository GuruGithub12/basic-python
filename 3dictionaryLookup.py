my_StatesAndCApitalDictionary = { "NSW": "Sydney",
                                  "VIC": "Melbourne",
                                    "ACT": "Canberra",
                                      "QLD": "Brisbane",
                                        "SA": "Adelaide",
                                        "WA": "Perth",
                                          "TAS": "Hobart",
                                            "NT": "Darwin" }

def fn_LookupCapital(state):
    if state in my_StatesAndCApitalDictionary:
        return "The capital of " + state + " is " + my_StatesAndCApitalDictionary[state]
    else:
        return "State not found in the dictionary"
    
print(fn_LookupCapital("NSW"))
print(fn_LookupCapital("NSW1"))