s = "All is well"
rev = s[::-1]
print(rev)

a = ["1","2","3","4","4","5","6","6","7","8","9","10","10"]
a = list(dict.fromkeys(a))
print(a)

a = [1, 2]
b = [1, 2]
print(a == b)  
print(a is b) 

string= input("Enter string:")
vowels=0
for i in string:
      if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
            vowels=vowels+1
print("Number of vowels are:")
print(vowels)
