import struct

e = input()

d = e
e = e.split()
a = e[0]
b = e[1]
c = e[2]
d = d.replace(a + ' ' + b + ' ' + c + ' ', "")

a = int(a)
b = float(b)
b = struct.unpack('f', struct.pack('f', b))[0]

print("{}{:f}{}{}".format(a, b, c, d))
print("{}	{:f}	{}	{}".format(a, b, c, d))
print("{:>10d}{:>10f}{:>10s}{:>10s}".format(a, b, c, d))
