
# coding: utf-8

# In[1]:


get_ipython().magic(u'matplotlib inline')
import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(0,100)

alfa=0.935
beta=50

def f(x,alfa,beta):
    if (x<=alfa):
        
        p=0
   
    if (alfa<=x)&(x<=beta):
        p=(x-beta)/(alfa-beta)
    
    if (x>=beta):
        p=1
   
    return p

plt.xlabel('Valores de X')
plt.ylabel('Valores de Y')
plt.title('Funcion Tipo Hombro o Saturacion Derecha')

f_vec = np.vectorize(f)
func=f_vec(x,alfa,beta)
plt.plot(x,f_vec(x,alfa,beta),'c:>')


# In[ ]:



