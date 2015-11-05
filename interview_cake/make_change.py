amount = 5
denom = [2,3,5]

def make_change(n, m):
    if n < 0 or m < 0:
        return 0
    if n == 0:
        return 1
    return make_change(n - denom[m], m) + make_change(n, m-1)

def make_change_2(n, m):
    change_table = [[0] * m for _ in xrange(n+1)] 
    change_table[0] = [1] * m
    for i in range(1,n+1):
        if i % denom[0] == 0:
        	change_table[i][0] = 1
        
        for j in range(1,m):
            if i >= denom[j]:
            	change_table[i][j] = change_table[i-denom[j]][j] + change_table[i][j-1]
            else:
                change_table[i][j] = change_table[i][j-1]
    return change_table[n][m-1]

print make_change(amount, len(denom)-1)
print make_change_2(amount, len(denom))
