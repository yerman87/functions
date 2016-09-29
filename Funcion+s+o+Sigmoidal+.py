
# coding: utf-8

# In[2]:


get_ipython().magic(u'matplotlib inline')
import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(0,100)

a=10
b=30
c=60

def f(x,a,b,c):
    
   
    if (x<a):
        p=0
  
    if (x>=a)&(x<b):
        p=2*(((x-a)/(c-a))**2)
    
    if (x>=b)&(x<=c):
        p=1-2*(((x-c)/(c-a))**2)
   
    if (x>c):
        p=1

    return p

plt.xlabel('Valores de X')
plt.ylabel('Valores de Y')
plt.title('Funcion Forma S o Sigmoidal')

f_vec = np.vectorize(f)
func=f_vec(x,a,b,c)
plt.plot(x,f_vec(x,a,b,c),'r:o')


# In[ ]:



