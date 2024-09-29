# capitalize all first character of each word of msg1 

msg1 = "welcome to aws python 101 class:strings"
print (msg1.title())

# reverse msg2
msg2 = "The instructor here is Claudio"

print (msg2[::-1])

# write msg1 in lower case
print (msg1.lower())

# write msg2 in upper case
print (msg2.upper())

# find how many "e" character was used in msg 2

print (msg2.count("e"))

# Replace 'python" by 'java' in msg1
print(msg1.replace("python", "java"))

# write a new message 'python is great" using msg1 characters
new_msg = msg1[15:21]+' '+msg1[-4]+msg1[-1]+' '+msg1[-2]+msg1[-5]+msg1[1]+msg1[11]+msg1[-6]
print(new_msg)

# create a new message "java is well done" using msg1 characters
new_msg2 = "java"+ ' '+ msg1[-4]+msg1[-1]+ ' '+ msg1[0]+msg1[1]+msg1[2]+msg1[2]+' '+ "done"
print (new_msg2)
