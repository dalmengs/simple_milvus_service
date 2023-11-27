import torch
from torch.utils.data import Dataset, DataLoader
from sentence_transformers import SentenceTransformer
import pandas as pd
import numpy as np
from pymilvus import connections, FieldSchema, CollectionSchema, DataType, Collection, utility
from tqdm.auto import tqdm
import re
import datetime
from config import *
from Util.Embedder import Embedder
import pprint

# Managed by Singleton Pattern
class VectorDB:
    __collection = None
    __embedder: None

    def __init__(self):
        self.__embedder = Embedder()
        connections.connect(host=VDB_HOST, port=VDB_PORT)
        self.__collection = Collection(name=VDB_COLLECTION_NAME)
    
    def insertData(self, username, texts):
        data = []
        for text in texts:
            data.append({
                "username": username,
                "date": int(datetime.datetime.now().timestamp()),
                "chat_text": text,
                "chat_embedding": self.__embedder.encode(text)
            })
        self.__collection.insert(data)
        self.__collection.flush()
        return self.__collection.num_entities
    
    def searchData(self, username, texts):
        result = self.__collection.search(
            data = self.__embedder.encode(texts),
            anns_field = "chat_embedding",
            param = VDB_PARAM,
            limit = VDB_LIMIT,
            output_fields = ["username", "date", "chat_text"],
            expr = "username == '{}'".format(username)
        )

        ret = []
        for hits in result:
            for hit in hits:
                ret.append(hit.to_dict())
        return ret

if __name__ == "__main__":
    vectorDB = VectorDB()

    while True:
        mode = int(input("1 : Insert Data\n2 : Find Data\n"))
        if mode not in [1, 2]:
            print("Invalid Input")
            continue

        if mode == 1:
            username = "dalmeng"
            msg = input("Input message that you want to store : ")

            result = vectorDB.insertData(username, [msg])
            if result:
                print("Succeed to store data | The number of Entities : {}".format(result))
        else:
            username = "dalmeng"
            msg = input("Input message that you want to find : ")

            result = vectorDB.searchData(username, [msg])
            print("[Query Result of Message '{}']".format(msg))
            pprint.pprint(result)




