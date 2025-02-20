class TrieNode:
    def __init__(self):
        self.isFile = False
        self.content = ""
        self.child = collections.defaultdict(TrieNode) # key:name,value:node

class FileSystem:

    def __init__(self):
        self.root = TrieNode()

    def ls(self, path: str) -> List[str]:
        path = path.split("/")
        cur = self.root
        
         # travese the path
        for p in path:
            if not p:
                continue
            cur = cur.child[p] # move into the next directory
        if cur.isFile: # If path is a file path, returns a list that only contains this file's name.
            return [path[-1]]
        return sorted(cur.child.keys())   

    def mkdir(self, path: str) -> None:
        path = path.split("/")[1:]
        cur = self.root
        
        for p in path:
            if p not in cur.child:
                cur.child[p] = TrieNode()  # ✅ Create directory node
            cur = cur.child[p]

    def addContentToFile(self, filePath: str, content: str) -> None:
        path = filePath.split("/")[1:]
        cur = self.root
        # get to the end of the path
        for p in path:
            if p not in cur.child:
                cur.child[p] = TrieNode()  # ✅ Ensure file node exists
            cur = cur.child[p]
            
        cur.isFile = True
        cur.content += content

    def readContentFromFile(self, filePath: str) -> str:
        cur = self.root
        path = filePath.split("/")[1:]

        
        for p in path:
            cur = cur.child[p]
        return cur.content
        


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)