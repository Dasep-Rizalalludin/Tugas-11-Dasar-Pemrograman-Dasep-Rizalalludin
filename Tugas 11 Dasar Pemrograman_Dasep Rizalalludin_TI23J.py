#!/usr/bin/env python
# coding: utf-8

# In[11]:


#Buatlah Fungsi untuk menjumlahkan total nilai dari list
data = [1, 2, 3, 4, 12, 9,10]
def total(data):
    total=0
    for i in range(len(data)) :
        total += data[i]    
    print("Total dari jumlah list adalah", total)
total(data)


# In[5]:


#BUatlah fungsi untuk mencari nilai terbesar dari sekumpulan list
data = [12, 4, 5, 23, 7, 50]
def nilai(data):
    return max(data)
print("Nilai terbesar dari list tersebut adalah :",nilai(data))


# In[20]:


#Buatlah fungsi untuk menjumlahkan 2 buah list
data1 = [5, 10, 5]
data2 = [10, 30, 20]
def jumlah(data1, data2):
    total=0
    for data1, data2 in zip(data1, data2):
        total +=data1 + data2
    return total

result = jumlah(data1, data2)
print(f"total sum:{result}")     

