a = [1,2,3,4,5,6,7,8]

for i in range(0,len(a),2):
    print(a[i],end='\t')


b = a[0:len(a):2]
print(b)


