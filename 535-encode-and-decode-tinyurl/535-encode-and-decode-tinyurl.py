class Codec:    
    
    def __init__(self):
        self.a = {}
        self.c = 0

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """        
        self.c += 1
        self.a[self.c] = longUrl        
        return str(self.c)                

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.a[int(shortUrl)]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))