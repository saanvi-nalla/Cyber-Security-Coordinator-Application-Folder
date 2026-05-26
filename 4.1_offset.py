from pwn import *

libc = ELF('./libc.so.6')

print(hex(libc.sym['system']))
print(hex(libc.sym['__libc_start_main']))
print(next(libc.search(b'/bin/sh')))
