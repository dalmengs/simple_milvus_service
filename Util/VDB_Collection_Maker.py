import torch
from torch.utils.data import Dataset, DataLoader
from sentence_transformers import SentenceTransformer
import pandas as pd
import numpy as np
from pymilvus import connections, FieldSchema, CollectionSchema, DataType, Collection, utility
from config import *

"""
    -----------------[NOTE]-----------------------------------------
    Basic Setting of Collection is 'Create'.
    So, If you run this file, contents of collection will be reset.
    Please notify that and be careful.
    ----------------------------------------------------------------
"""

# Try to connect with host and port.
connections.connect(host=VDB_HOST, port=VDB_PORT)

# Collection Reset
if utility.has_collection(VDB_COLLECTION_NAME):
    utility.drop_collection(VDB_COLLECTION_NAME)

# Field and Schema define
fields = [
    FieldSchema(name='id', dtype=DataType.INT64, is_primary=True, auto_id=True),
    FieldSchema(name='username', dtype=DataType.VARCHAR, max_length=50),
    FieldSchema(name='date', dtype=DataType.INT64, max_length=10),
    FieldSchema(name='chat_text', dtype=DataType.VARCHAR, max_length=1000),
    FieldSchema(name='chat_embedding', dtype=DataType.FLOAT_VECTOR, dim=EMBEDDING_DIMENSION)
]

schema = CollectionSchema(fields=fields)
collection = Collection(name=VDB_COLLECTION_NAME, schema=schema)

# Index Part
index_params = {
    'metric_type': VDB_METRIC,
    'index_type': VDB_INDEX_TYPE,
    'params':{"nlist":1536}
}

# Make collection with upper settings
collection.create_index(field_name=VDB_COLLECTION_NAME, index_params=index_params)
collection.load()