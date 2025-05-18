import math

# 1

input1 = "python"
output1 = input1.capitalize()
print(output1)

# 2
input2 = "ananas"
output2 = input2.count("a")
print(output2)

# 3
input3 = "kot"
output3 = input3[::-1]
print(output3)

# 4
input4 = "kajak"
revinput4 = input4[::-1]
output4 = input4 == revinput4
print(output4)

# 5
input5 = "Ala ma kota"
output5 = input5.replace(" ","-")
print(output5)

# 6
input6 = 1234
input6str = str(input6)
output6 = int(input6str[0])+int(input6str[1])+int(input6str[2])+int(input6str[3])
print(output6)

# 7
input7 = 42
output7 = input7.__mod__(2) == 0
print(output7)

# 8
input8 = 5
output8 = math.factorial(input8)
print(output8)

# 9
input9 = 9582
output9 = max(str(input9))
print(output9)

# 10
input10 = 10
output10 = bin(input10)[2:]
print(output10)

# 11
input11 = "To jest przykładowe zdanie"
input11strip = input11.strip()
output11 = input11strip.count(" ")+1
print(output11)

# 12
input12 = "abc123def456"
output12 = input12[:3]+input12[6:9:]
print(output12)

# 13
input13j = "Python3"
input13d = "Python"
output13j = input13j.isalpha()
output13d = input13d.isalpha()
print(output13j)
print(output13d)