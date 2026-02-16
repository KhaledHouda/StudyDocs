import datetime
import string
import os
import glob
import argparse



class Exercise00:
    STUDENT_NAME = "Khaled Houda"

    @staticmethod
    def deadline(format):
        wantedDeadline = datetime.datetime(2023, 11, 15, 9, 0)
        return wantedDeadline.strftime(format)
    
    def __init__(self, bamboozle:str, *args):
        self.first17Letters = ""
        iterator = 17
        
        if len(bamboozle) < 17:
            iterator = len(bamboozle)
           
        for i in range(iterator):
            self.first17Letters += bamboozle[i]
        self.first17Letters += "..."     
    @property
    def txt(self):
        txt = ""
        txt += self.first17Letters
        return txt

    def format(self, mode:str):
        if mode == "order":
            return OrderNiggaFuckNiggas()
        if mode == 'dict':
            return DictFuckEpsteinNiggas()
        
    def listfiles(self, type = ""):
        if type != "":
            typeSpecifier = "**/*" + '.'+ type
        else:
            typeSpecifier = "**/*"

        yield glob.glob(typeSpecifier)

    
#ex7
    def collatz(self, xStart:int):
        xCurrent = xStart
        collatzList = []
        index = 1
        while xCurrent !=1:
            collatzList.append(xCurrent)

            if xCurrent %2 == 1:
                xCurrent = 3*xCurrent+1
            else:
                xCurrent //= 2
            index +=1

        return (collatzList , index )

#ex7 

#ex8
    def __call__(self, a,b,c):
        return "a = " + a + "\n" + "b = " + b + "\n" +  "c = " + c

    
#ex8




            
        
        
class OrderNiggaFuckNiggas:
    def format(self,  par1:str , par2:str, par3:str):
        orderedOutput = par3 + " - " + par2 + " - " + par1 + " epstein fuck niggas"
        return orderedOutput
        
class DictFuckEpsteinNiggas:
    def format(self, x:float , y:float):
        x= str(x)
        y= str(y)

        xTemp = ""
        yTemp = ""
        foundPointX = False
        foundPointY = False
        for i in range(len(x)):
            if x[i] == '.':
                foundPointX = True
            if i+1 == len(x):
                xTemp += "."
                xTemp += "0"
                break


            if foundPointX:
                xTemp += x[i]
                xTemp += x[i+1]
                break

            xTemp +=x[i]
            
        for i in range(len(y)):
            if y[i] == '.':
                foundPointY = True

            if foundPointY:
                yTemp += y[i]
                if (len(y)-1) -i >= 4:
                    yTemp += y[i+1]
                    yTemp += y[i+2]
                    yTemp += y[i+3]
                    yTemp += y[i+4]
                
                if (len(y)-1) -i == 3:
                    yTemp += y[i+1]
                    yTemp += y[i+2]
                    yTemp += y[i+3]
                    yTemp += "0"

                if (len(y)-1) -i == 2:
                    yTemp += y[i+1]
                    yTemp += y[i+2]                                        
                    yTemp += "00"
                
                if (len(y)-1) -i == 1:
                    yTemp += y[i+1]
                    yTemp += y[i+2]                                        
                    yTemp += "000"                
                
                break

            yTemp +=y[i]

    
        x = xTemp
        y = yTemp
        return "x ,y = (" + x + " , " + y + ")"             

    


    




ex = Exercise00("abcdefghijklmnopqrstuvwxyz")
print(ex.txt)
print( ex.format('order').format('baba', 'mama' , 'jido') )
print(ex.format('dict').format( 1234, 6877.8245454533 ))
for i in ex.listfiles():
    print(i)

print( ex("six sevem", "six seven", "addie") ) 



#10
parser = argparse.ArgumentParser(description= "ex00 khaled balalalalal nigga")
parser.add_argument("FILE", help="the input positional parameter")
parser.add_argument("-b", action="store_true" , default=False, help= "an optional boolean flag(Defaukt:false)" )
parser.add_argument("-f", "--float", type=float, default=0.0, help= "An optional parameter of type float (Default:0.0)." )
parser.add_argument("-i", "--INT",type=int, default=0, help= "An optional parameter of type float (Default:0)." )




parser.parse_args()
