
#求1-100之间的和

if __name__ == '__main__':
    def forsum():
        sum=0
        for i in range(1,101):
            sum+=i
        print(sum)
        return sum
    forsum()
if __name__ == '__main__':
    def whilesum():
        sum=0
        i=1
        while i <=100:
            sum+=i
            i+=1
        print(sum)
        return sum
    whilesum()




