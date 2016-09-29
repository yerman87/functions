
# coding: utf-8

# In[1]:


get_ipython().magic(u'matplotlib inline')
import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(0,100)

a=10
b=30
c=60
d=70

def f(x,a,b,c,d):
    
    if (x<a)|(x>=c):
        m=0;
   
    if (x>=a)&(x<b):
        m=(x-a)/(b-a)
    
    if (x>=b)&(x<d):
        m=1
    
    if (x>=d)&(x<c):
        m=1-(x-d)/(c-d)
    return m

plt.xlabel('Valores de X')
plt.ylabel('Valores de Y')
plt.title('Funcion Tipo Saturacion Izquierda (PI)')


f_vec = np.vectorize(f)
func=f_vec(x,a,b,c,d)
plt.plot(x,f_vec(x,a,b,c,d),'y:o')



# In[ ]:



