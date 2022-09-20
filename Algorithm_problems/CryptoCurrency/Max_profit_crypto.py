'''
Author :Akuthota shiva kumar
email:atpshivakumar@gmail.com
'''

'''
Importing regex library for reading input
'''
import re

def readInputsPS1():
    '''
    This function is to read inputPS1 from the current working directory
    '''
    try :
        cryptodata=[]
        with open("inputPS1.txt",'r') as inpu:
            input_data=inpu.read().strip().split("\n")
            if("Type of Crypto coins:" in input_data[0]):
                coins=re.findall("\d+",input_data[0])[0]
            else:
                raise Exception("Types of crypto currency data does not exist in input")
            if("Maximum spend:" in input_data[1]):
                max_spend=re.findall("\d+",input_data[1])[0]
            else:
                raise Exception("Maximum spend does not exist in input")
            for each in input_data:
                #Creating list of lists for the input data to read from inputPS1.txt
                if "/" in each:
                    if(len(re.findall("/",each))==3):
                        cryptodata.append([each.split("/")[0],[int(number) for number in each.split("/")[1:]]])
                    else:
                        raise Exception("Input data is not correct")
        return coins,max_spend,cryptodata                    
                        
    except Exception as e:
        print(e)

def takeInput(elem):
    '''
    To sort elements based on input for output display
    '''
    return elem[5]
def takefourth(elem):
    '''
    To sort elements based on profit for algorithm
    '''
    return elem[4]

def AlgotofindMax(types,max_spend,data):
    '''
    This function to add the profit percentage to the array and 
    '''
    i=0
    for each in data:
        each.extend(each[1])
        each.remove(each[1])
        each.append(each[3]/each[2])
        each.append(i)
        i=i+1
    

    data=sorted(data,key=takefourth,reverse=True)
    profit=0
    for each in data:
        count=0
        for i in range(each[1]):
            if(max_spend>0 and max_spend>each[2]):
                max_spend=max_spend-each[2]
                count=count+1
                profit=profit+each[3]
            else:
                fraction=max_spend/each[2]
                max_spend=max_spend-fraction*each[2]
                count=count+fraction
                profit=profit+each[3]*fraction
                break
        each.append(count)

        
    return profit,data

def writeOutputPS1(profit,Output):
    fileout=open(r'outputPS1.txt','w');
    
    fileout.write("Max Profit:"+str(round(profit,7))+"\n")
    fileout.write("Quantity selection Ratio:\n")
    for each in Output:
        fileout.write(each[0]+":"+str(round(each[-1]/each[1],3))+"\n")                 
    fileout.write("Total Quantity of each coin sold:"+"\n")
    for each in Output:
        fileout.write(each[0]+":"+str(round(each[-1],3))+"\n")
def main():
    '''
    Main function to call all the other functions to read and write output according to the requirement.
    '''
    types,max_profit,data=readInputsPS1()
    profit,Output=AlgotofindMax(types,int(max_profit),data)
    Output=sorted(Output,key=takeInput)
    writeOutputPS1(profit,Output)

if __name__=="__main__":
    main()




