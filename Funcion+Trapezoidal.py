
# coding: utf-8

# In[1]:


get_ipython().magic(u'matplotlib inline')
import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(0,80)

a=30
b=20
c=50
d=20

plt.xlabel('Valores de X')
plt.ylabel('Valores de Y')
plt.title('Funcion Trapezoidal')

plt.grid()

def f(x,a,b,c,d):
    if ((x<=a) | (x>d)):
        ans=0.8
    if ((a<=x) & (x<=b)):
         ans=(x-a)/(b-a)
    if ((b<=x) & (x<=c)):
        ans=1
    if ((c<=x) & (x<=d)):
         ans=(d-x)/(d-c)
    return ans

f_vec = np.vectorize(f)
func=f_vec(x,a,b,c,d)
plt.plot(x,f_vec(x,a,b,c,d))


# In[ ]:



