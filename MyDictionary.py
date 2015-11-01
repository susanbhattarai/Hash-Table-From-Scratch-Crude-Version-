class Dictionary(object):
    
    def __init__(self):
        self.key = [None]
        self.value = [None]
        
    
    def Constructor(self, size):
        self.size = size
        self.key = self.key * size
        self.value = self.value * size
        
    
    def HashFunction(self, given_string, size):
        total = 0
        for pos in range(len(given_string)):
            # Using positional weighing on even indices 
            if pos % 2 == 0:
                total = total + (10**pos) * ord(given_string[pos])
            else:
                total = total + ord(given_string[pos])
        return total % size
    
    
    def Set(self,key,value):
        get_hash = self.HashFunction(key, self.size)
        
        if self.key[get_hash] == None:
            self.key[get_hash] = [key]
            self.value[get_hash] = [value]
            return "Success"
        
        else:
            if key in self.key[get_hash]:
                key_index = self.key[get_hash].index(key)
                temp = self.value[get_hash][key_index]
                self.value[get_hash][key_index]= value
                return "Success by deleting", temp

            else:
                self.key[get_hash].append(key)
                self.value[get_hash].append(value)
                return "Success by appending"


    def __setitem__(self, key, value):
        self.Set(key, value)


    def Get(self, key):
        get_hash = self.HashFunction(key, self.size)
        if self.key[get_hash] != None and key in self.key[get_hash]:
            key_index =  self.key[get_hash].index(key)
            return self.value[get_hash][key_index]
        
        return -1
        

    def __getitem__(self, key):
        return self.Get(key)


    def Delete(self, key):
        get_hash = self.HashFunction(key, self.size)
       
        if self.key[get_hash] != None and key in self.key[get_hash]:
            key_index = self.key[get_hash].index(key)
            temp = self.value[get_hash][key_index]
            self.key[get_hash][key_index] = None
            self.value[get_hash][key_index] = None
            return temp
        else:
            return "Key Not Found"
        

    def LoadFactor(self):
        total_items = 0
        for items in self.key:
            if items == None or items == [None]:
                total_items += 0
            else:
                total_items += len(items)
        return total_items / float(self.size)


        

    
