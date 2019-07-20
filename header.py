class Header():
    def __init__(self):
        self.score = 0000
        self.lives = 2
        self.time = 200

    def printheader(self):
        print("")
        print("TIME LEFT : " + str(self.time))
        print("YOUR SCORE IS : " + str(self.score) +"\t\t      LIFE REMAINING  : " + str(self.lives))
 
    def timer(self):
        if self.time == 0:
            print("Your Score is: "+str(self.score))
            print("GAME OVER !! Your Time Is UP :( My Time Is Now!!)")

            quit()
        else:
            self.time -= 1
    def end(self,level,q):
        if self.lives != 0 and q == -1:
            self.score += self.time
        if level > 2:
            print("Congrats, You completed both levels")
            print("Your score is :"+str(self.score))
            self.score = 0
            quit()
        elif level == 2:
            print("GAME OVER!!")
            print("Your score is :"+str(self.score))
            self.score = 0
            quit() 
        else:
            print("GAME OVER!!")
            print("Your Score is: "+str(self.score)) 
            self.score = 0 
                  
header = Header()            
