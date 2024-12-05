class car:
    def open(self):
        print("door")
        self._acc()
    def _acc(self):
        print("speed increse")
my_car =  car()
my_car._acc()