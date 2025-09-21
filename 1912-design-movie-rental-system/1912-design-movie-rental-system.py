class MovieRentingSystem:

    def __init__(self, n: int, entries: List[List[int]]):
        self.price_map = {}  # (shop, movie) -> price
        self.available = defaultdict(SortedList)  # movie -> SortedList[(price, shop)]
        self.rented = SortedList()  # SortedList[(price, shop, movie)]
        
        for shop, movie, price in entries:
            self.price_map[(shop, movie)] = price
            self.available[movie].add((price, shop))          

    def search(self, movie: int) -> List[int]:
        return [shop for price, shop in self.available[movie][:5]]       

    def rent(self, shop: int, movie: int) -> None:
        price = self.price_map[(shop, movie)]
        self.available[movie].remove((price, shop))
        self.rented.add((price, shop, movie))       

    def drop(self, shop: int, movie: int) -> None:
        price = self.price_map[(shop, movie)]
        self.rented.remove((price, shop, movie))
        self.available[movie].add((price, shop))      

    def report(self) -> List[List[int]]:
        return [[shop, movie] for price, shop, movie in self.rented[:5]]        

# Your MovieRentingSystem object will be instantiated and called as such:
# obj = MovieRentingSystem(n, entries)
# param_1 = obj.search(movie)
# obj.rent(shop,movie)
# obj.drop(shop,movie)
# param_4 = obj.report()