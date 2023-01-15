#!/usr/bin/python3
''' Module has a class BaseCache that inherits from
base model class BaseCaching '''

from base_caching import BaseCaching


class BasicCache(BaseCaching):
  ''' Uses put and get functions '''

  def put(self, key, item):
    ''' Adds item to the cache '''
    if key and item:
      self.cache_data[key] = item

  def get(self, key):
    ''' Returns a value from the cache by key '''
    if key:
      return self.cache_data.get(key)
    
    ''' If no key, returns none '''
    if key is None or not key:
      return None 