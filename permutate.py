out=[]
def permute(msg, i, length):
    if i==length:
        out.append("".join(msg))
    else:
        for j in range(i, length):
            msg[i], msg[j] = msg[j], msg[i]
            permute(msg, i+1, length)
            msg[j], msg[i] = msg[i], msg[j]

msg="12345"
permute(list(msg), 0, len(msg))
for i in range(len(out)):
    print(out[i])  
print(len(out))