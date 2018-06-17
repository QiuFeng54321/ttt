print("hello world!")
def encodeCaecar(s,key):
    for i in s[:]:
        s[i]+=key
    return s
print(encodeCaecar("h",2))
