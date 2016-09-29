
# coding: utf-8

# In[2]:


get_ipython().magic(u'matplotlib inline')
import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(0,100)
a=8
b=50
c=90

plt.xlabel('Valores de X')
plt.ylabel('Valores de Y')
plt.title('Funcion Triangular')

plt.grid()

def f(x,a,b,c):
    if ((x<a) | (x>=c)):
        ans=0
    if ((a<=x) & (x<b)):
         ans=(x-a)
    if ((b<=x) & (x<=c)):
        ans=(c-x)
    return ans

f_vec = np.vectorize(f)
func=f_vec(x,a,b,c)
plt.plot(x,f_vec(x,a,b,c),'y:<')


# In[ ]:



