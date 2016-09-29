
# coding: utf-8

# In[1]:


get_ipython().magic(u'matplotlib inline')
import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(0,50)

alfa=20
beta=70

def f(x,alfa,beta):
    if (x<=alfa):
        
        p=1
   
    if (alfa<=x)&(x<=beta):
        p=(x-alfa)/(beta-alfa)
    
    if (x>=beta):
        p=0
   
    return p

plt.xlabel('Valores de X')
plt.ylabel('Valores de Y')
plt.title('Funcion Tipo Hombro  o Saturacion Izquierda')

f_vec = np.vectorize(f)
func=f_vec(x,alfa,beta)
plt.plot(x,f_vec(x,alfa,beta),'g:o')


# In[ ]:



