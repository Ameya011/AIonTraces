#!/usr/bin/env python
# coding: utf-8
# In[11]:


# Import relevant packages
import json
import sklearn
from readtrace import readFileData
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer


# In[12]:


# read the data set

dataset = []
fns = []
chunks = []
for line in open('dataset-example.csv', encoding='utf-8'):
    fn, txt, chunk = line.strip().split('|')
    fns.append(fn)
    dataset.append(txt)
    chunks.append(chunk)


# In[13]:


# Perform tfidf vecotrization

count_vect = CountVectorizer()
X_train_counts = count_vect.fit_transform(dataset)
tf = TfidfVectorizer(norm=None)
tfidf_matrix = tf.fit_transform(dataset)


# In[14]:


# Feature score for a document
def tfidfscores(doc):
    feature_names = np.array(tf.get_feature_names())
    feature_index = tfidf_matrix[doc,:].nonzero()[1]
    tfidf_scores = list(zip(feature_names[feature_index], [tfidf_matrix[doc, x] for x in feature_index]))
    return sorted(tfidf_scores, reverse=True, key=lambda x:x[1])


# In[15]:


# sum of feature scores for multiple documents
def tfidfsum(docs, tf, tfidf_matrix):
    feature_names = np.array(tf.get_feature_names())
    feature_sum = np.zeros(tfidf_matrix[0,:].shape)
    for doc in docs:
        feature_sum += 1.0/len(docs) *tfidf_matrix[doc,:]
    
    mindist, mindoc = 1e9,-1
    for doc in docs:
        dist = np.linalg.norm(tfidf_matrix[doc,:] - feature_sum)
        if dist < mindist:
            mindist = dist
            mindoc = doc
        
    feature_index = feature_sum.nonzero()[1]
    tfidf_scores = list(zip(feature_names[feature_index], [float(feature_sum[:,x]) for x in feature_index]))
    return sorted(tfidf_scores, reverse=True, key=lambda x:x[1]), fns[mindoc]


# In[16]:


def chunk_tfidf_sum(chunk, tf, tfidf_matrix):
    docs = []
    for i,c in enumerate(chunks):
        if chunks[i] == chunk:
            docs.append(i)
    return tfidfsum(docs,tf,tfidf_matrix)


# In[17]:


chunk_tfidf_sum('1546453200',tf,tfidf_matrix)


# In[21]:


def labelvecchunks():
    jres = []
    for i in range(len(chunknrs)):
        res, fn = chunk_tfidf_sum(chunknrs[i],tf, tfidf_matrix)
        dat = readFileData(fn)
        jrow = {}
        jrow['chunk'] = chunknrs[i]
        jrow['filename'] = fn
        jrow['tracename'] = dat['name']
        jrow['tracepath'] = dat['path']
        jrow['filename'] = fn
        jrow['tokens'] = [x for x,y in res][:10]
        print (chunknrs[i]+"|"+fn+"|", ",".join([x for x,y in res][:10]))
        print (jrow)
        jres.append(jrow)
    return jres


# In[22]:


chunktxt = dict()
chunkdocs = dict()
revchunknrs = dict()
for i,c in enumerate(chunks):
    chunktxt[c] = chunktxt.get(c,'') + ' ' + dataset[i]
    l = chunkdocs.get(c)
    if l:
        l.append(i)
    else:
        chunkdocs[c] = [i]
        
chunknrs = list(chunktxt.keys())
chunkdataset = list(chunktxt.values())
revchunknrs = dict([(v,k) for k,v in enumerate(chunknrs)] )

# Perform tfidf vecotrization
chunktf = TfidfVectorizer(norm=None)
chunktfidf_matrix = chunktf.fit_transform(chunkdataset)


# In[23]:


# Feature score for a document
def tfidfscores(doc,tf, tfidf_matrix):
    feature_names = np.array(tf.get_feature_names())
    feature_index = tfidf_matrix[doc,:].nonzero()[1]
    tfidf_scores = list(zip(feature_names[feature_index], [tfidf_matrix[doc, x] for x in feature_index]))
    return sorted(tfidf_scores, reverse=True, key=lambda x:x[1])


# In[24]:


[x for x,y in tfidfscores(revchunknrs['1546404900'],chunktf, chunktfidf_matrix)][:10]


# In[25]:


def labelchunks():
    for i in range(len(chunknrs)):
        print (chunknrs[i], [x for x,y in tfidfscores(i,chunktf, chunktfidf_matrix)][:10])

#labelchunks()
json.dump(labelvecchunks(), open('chunkinfo.json','w'))


# In[26]:







# In[ ]:




