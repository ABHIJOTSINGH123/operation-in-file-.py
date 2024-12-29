fn=open('text.txt', 'r')
fn1=open('codingal.txt','w')
cont=fn.readlines()
type(cont)
for r in range(1, len(cont)+1):
    if r%2!=0:
        fn1.write(cont[r-1])
    else:
        pass
fn1.close()
fn1=open('codingal.txt','r')
cont1=fn1.read()
print(cont1)

fn.close()

fn1.close()