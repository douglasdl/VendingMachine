from coin_sensor import CoinSensor

class Coin():
    def __init__(self):
        self._total = 0
        self._coinsensor = CoinSensor()

    @property
    def total(self):
        return self._total

    @property
    def coinsensor(self):
        return self._coinsensor

    def calc_total(self):
        if self._coinsensor.value > 0:
            pass
        self._total += self._coinsensor.value
        print("投入金額：", self._total)   
        return self._total 


def main():
    print("Coin Module")
    c = Coin()
    c._coinsensor.value = int(input("コインを入れてください："))
    #print(c.coinsensor.value)

    print(c.calc_total())


if __name__ == '__main__':
    main()