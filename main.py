import os
import pygame

from coin import Coin


class VendingMachine:
    def __init__(self):
        self.coin = Coin()
        self.frontDoorIsClosed = True
        self.insertingAmount = 0
        self.mostExpensive = 200

        self.stock = [0, 0, 0, 0, 0, 0, 0, 0]
        self.coins10 = 0
        self.coins50 = 0
        self.coins100 = 0
        self.coins500 = 0
        self.salesAmount = 0
        self.cashAmount = 0
        #pygame.init()
        #pygame.display.set_caption("Robot Car Simulator")
        width = 400
        height = 400
        #win = pygame.display.set_mode((width, height))
        #clock = pygame.time.Clock()
        ticks = 1000
        exit = False
        x = 200
        y = 200
        w = 20
        h = 20
        direction = "Forward"
        print("New Vending Machine")
    

    def underOperation(self):
        print("営業中")

    def setSaleAmount(self, sale):
        self.salesAmount = self.salesAmount + sale

    def coinCheck(self, coins):
        self.coins = self.coins + coins


    def openFrontDoor(self):
        self.frontDoorIsOpen = True
        print("Opening Front Door")

    def closeFrontDoor(self):
        self.frontDoorIsOpen = True
        print("Closing Front Door")

    def setInsertingAmount(self):
        self.insertingAmount = self.insertingAmount + self.coin

    def insertCoin(self, coin):
        self.setInsertingAmount(coin)
        print(self.insertingAmount)

    def buyProduct(self, product):
        pass

    def setCashAmount(self, coin):    
        if coin == 10:  
            self.coins10 = self.coins10 + 1
        elif coin == 50:  
            self.coins50 = self.coins50 + 1
        elif coin == 100:  
            self.coins100 = self.coins100 + 1
        elif coin == 500:  
            self.coins500 = self.coins500 + 1
        else: 
            print("Invalid coin")
        
        self.showCoins()
    
    def showCoins(self):
        print("COINS:")
        print(" 10円", self.coins10)
        print(" 50円", self.coins50)
        print("100円", self.coins100)
        print("500円", self.coins500)   




def main():
    eco = VendingMachine()
    eco.underOperation()
    while (eco.frontDoorIsClosed and eco.insertingAmount < eco.mostExpensive):
        eco.insertingAmount = eco.coin._total
    
    print("商品を選択してください。")
    #M1.openFrontDoor()
    #M1.closeFrontDoor()
    #M1.insertCoin(100)
    #M1.insertCoin(100)
    #M1.buyProduct("Calpis")


if __name__ == '__main__':
    main()    