#!/usr/bin/python
# -*- coding: utf-8 -*-
from pymemcache.client import base
from pymemcache import fallback
import uuid


class GeoDistributedLRU:

    #Varible initialized after an object of this class has been instanciated
    def __init__(self,host,port,cacheExpirationTime):
        """ Variables for client, backup Clients, fallbackClient instances, cache Expiration Time and old Client Cache """
        self.client = base.Client((host, port))
        self.fallbackClient = None 
        self.backupClients = None
        self.cacheExpirationTime = cacheExpirationTime
        self.oldClient = None

    #Sets intances of Clients in which cache data must be replicated
    def setBackupClients(self,clientsList):
        self.backupClients = clientsList

    #Used to provide a client instance as a fallback client for the current client
    def setFallbackClient(self,fallbackClient):
        self.fallbackClient = fallbackClient

    #Can be used to prevent the thundering herd problem
    def initializeFallbackClient(self):
        if(self.fallbackClient is not None):
            self.oldClient = self.client
            self.client = fallback.FallbackClient((self.fallbackClient, self.client))
        else:
            print("Initialization Failed: Please define a fallback client first")

    #Used to write the new cache data to other clients as well
    def replicateDataCacheKey(self,cacheKey,cacheData):
        for client in self.backupClients:
            result = client.get(cacheKey)
            if result is None:
                client.set(cacheKey, cacheData, self.cacheExpirationTime)
            else:
                modifyCacheData(cacheKey,cacheData)
            
    
    #Generate a unique cache Key
    def generateCacheKey(self):
        newKey = str(uuid.uuid4())
        return newKey

    #Get cache data by providing cache Key
    def getCacheData(self,cacheKey):
        cacheData = self.client.get(cacheKey)
        
        if cacheData is None:
            cacheData = {}

        return cacheData
    
    #add data to the cache
    def setCacheData(self,cacheKey, dataToCache):
        self.client.set(cacheKey, dataToCache,self.cacheExpirationTime)
 
    #Used to modify the content of a cache
    def modifyCacheData(self,cacheKey,newCacheData):
        #For concurrent cache access
        while True:
            cacheData, cas = self.client.gets(cacheKey)
            if cacheData is None:
                cacheData = newCacheData
                replicateDataCacheKey(cacheKey,newCacheData)
            else:
                cacheData = newCacheData
            if self.client.cas(cacheKey, cacheData, cas):
                break
    

  
