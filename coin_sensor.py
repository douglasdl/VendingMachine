class CoinSensor():
    def __init__(self):
        self._value = 0

    @property
    def value(self):
        value = self._value
        #self._value = 0
        return value    

    @value.setter
    def value(self, value):
        if value == 10 or value == 50 or value == 100 or value == 500:  
            self._value = value
            return value
        else:
            self._value = 0
            print("Invalid coin")
            return self._value
            

def main():
    print("CoinSensor Module")
    cs = CoinSensor()
    cs.value = int(input("コインを入れてください："))

    print(cs.value)
    


if __name__ == '__main__':
    main()