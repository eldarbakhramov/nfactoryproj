#import PyTorch

biname = []
numb = []
newnumb = []
with open('names.txt','r') as f:
    lines = f.readlines()
    for i in range(len(lines)):
   # for i in range(10):
        a = lines[i]
        for i in range(len(a)):
            if i == 0:
                biname.append('^' +  str(a[i]))
            elif i != 0 and i != len(a)-1:
                biname.append(str(a[i-1]) +  str(a[i]))
            else:
                biname.append(str(a[i-2]) +  '$')
for i in biname:
    numb.append(str(i)+ str(biname.count(i)))
newnumb = set(numb)

