#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().system('pip install autoscraper')


# In[3]:


from autoscraper import AutoScraper


# In[4]:


amazon_url="https://www.amazon.in/s?k=iphones&crid=1NCETJ898WCE7&sprefix=iphone%2Caps%2C340&ref=nb_sb_noss_1"
wanted_list=["₹61,999","Apple iPhone 13 (128GB) - (Product) RED","14,835"]


# In[5]:


scraper=AutoScraper()
result=scraper.build(amazon_url,wanted_list)
print(result)


# In[6]:


scraper.get_result_similar(amazon_url,grouped=True) 


# In[7]:


scraper.set_rule_aliases({'rule_e7us':'Title'})
scraper.keep_rules(['rule_e7us'])
scraper.save('amazon-search')


# In[11]:


result=scraper.get_result_similar('https://www.amazon.in/s?k=mi+phones+under+10000&crid=1SAC3RWYS6URT&sprefix=mi++phones+%2Caps%2C2821&ref=nb_sb_ss_ts-doa-p_2_10',group_by_alias=True)


# In[14]:


result['Title']


# In[ ]:




