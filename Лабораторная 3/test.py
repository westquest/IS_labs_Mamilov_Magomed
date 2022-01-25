res = 30
sub = 11
while sub != 0:
    tmp = sub
    sub = res % sub
    res = tmp

print(res)