# write a program to remove a word from the string and strip at the same time 

def removeAndStrip(string,word) :
   resultString = string.replace(word,"")
   return resultString.strip()


mystring= removeAndStrip("    Hello how are you doing Arian    ",'Hello')
print(f"string after removing the word  :{mystring}")