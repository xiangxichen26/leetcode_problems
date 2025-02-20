from collections import OrderedDict

class LFUCache:

    def __init__(self, capacity: int):
        self.freqToKeys = {} # frequency -> OrderedDict({key: None})
        self.keyToVal = {} # key -> value
        self.keyToFreq = {} # key -> frequency
        self.cap = capacity
        self.size = 0
        self.minFreq = 0

    def get(self, key: int) -> int:
        if key not in self.keyToVal:
            return -1
        self.increaseFreq(key)
        return self.keyToVal[key]

    def put(self, key: int, value: int) -> None:
        if self.cap == 0:  
            return

        if key in self.keyToVal:
            # update val
            self.keyToVal[key] = value
            # increse the frequency
            self.increaseFreq(key)
            return
        
        # the cap is full
        if self.size >= self.cap:
            # remove the least frequentlt used
            self.removeMinFreqKey()
            
        # put the key,value
        self.addKeyValue(key,value)
    
    def increaseFreq(self, key:int) -> None:
        cur_freq = self.keyToFreq[key]
        self.keyToFreq[key]  = cur_freq + 1

        # remove the key from the list of original freq
        del self.freqToKeys[cur_freq][key]

        if not self.freqToKeys[cur_freq]: # 如果当前 freq 为空，删除该 freq
            del self.freqToKeys[cur_freq]
            if cur_freq == self.minFreq: # 如果 minFreq 被移除，则增加 minFreq
                self.minFreq += 1

        # add the key to the list of 
        if cur_freq + 1 not in self.freqToKeys:
            self.freqToKeys[cur_freq + 1] = OrderedDict()
        self.freqToKeys[cur_freq + 1][key] = None

    def removeMinFreqKey(self) -> None:
        if self.minFreq not in self.freqToKeys:
            return 

        minFreqKeys = self.freqToKeys[self.minFreq]
        deletedKey, _ = minFreqKeys.popitem(last=False)  # 删除最早插入的 key

        if not minFreqKeys:
            del self.freqToKeys[self.minFreq]

        del self.keyToVal[deletedKey]
        del self.keyToFreq[deletedKey]

        self.size -= 1

    def addKeyValue(self, key:int, value:int) -> None:
        self.keyToVal[key] = value
        self.keyToFreq[key] = 1

        if 1 not in self.freqToKeys:
            self.freqToKeys[1] = OrderedDict()
        self.freqToKeys[1][key] = None

        self.minFreq = 1
        self.size += 1
       


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)