__author__ = 'gary'
import matplotlib.pyplot as plt



f = open('sb','r')
b = []
i=0
c=[]
a = f.readline()
b.append(a)
c.append(i)

while(a!=''):

    a = f.readline()

    if a != '':
        b.append(a)
        i+=1
        c.append(i)
    #print "a", a
    #print "i", i
print "c", len(c)
print "b", len(b)
plt.plot(c,b,'-')
plt.show()