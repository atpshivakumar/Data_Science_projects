'''
Author :Akuthota shiva kumar
email:atpshivakumar@gmail.com
'''


import os
class DrugNode:
    '''
    This class has all the function to create edit or update the drug nodes which are given as a input from the input files and Prompt file
    '''
    #creating of drug node
    def __init__(self, Uid, availCount):
        '''
        This function is used to initialize the Node with Unique id and quantiy of medicine
        :param Uid: unique id of the Medicine
        :param availCount: quantity of medicine
        '''
        self.left=None
        self.right=None
        self.Uid = Uid
        self.avCount = availCount
        self.chkoutCtr = 1
    def readDrugList(self,Uid, availCount):
        '''
        Creating of new node and assigning to left or right according to availability
        :param Uid: Unique id of the medicine
        :param availCount: quantity of medicine
        :return: Nothing
        '''
        if(self.left is None):
            self.left = DrugNode(Uid, availCount)
            foo.flag=0

        elif(self.right is None):
            self.right = DrugNode(Uid, availCount)
            foo.flag=1

        else:
            if (foo.flag):
                self.right.readDrugList(Uid, availCount)

            else:
                self.left.readDrugList(Uid, availCount)

    def checkDrugStatus(self,Uid):
        '''
        #checking the status of the unique id of drug
        :param Uid: Unique id for which we need to check the status
        :return: Nothing
        '''

        print("------------- checkDrugStatus:"+str(Uid)+" ---------------")
        Status=ifNodeExists(self,Uid)#checking wheather node exist or not
        if(not(Status)):
            print("Drug id "+str(Uid)+" does not exist")
        else:
            Nodein = NodeinTree(self, Uid)#getting the node
            if Nodein.avCount==0: #checking available count
                print("All units of drug id"+str(Uid)+" xx have been sold")
            elif Nodein.chkoutCtr%2==0:
                print("Drug id "+str(Uid)+ " entered "+ str(Nodein.chkoutCtr)+" times into the system. Its last status was ‘buy’ and currently have "+str(Nodein.avCount)+" units available")
            else:
                print("Drug id " +str(Uid) + " entered " + str(Nodein.chkoutCtr) + " times into the system. Its last status was ‘sell’ and currently have " + str(Nodein.avCount) + " units available")
        print("-----------------------------------------------\n")

    def _updateDrugList(self, Nodein, Uid, availCount):
        '''
        updating the drug data in the Binary tree according to the input
        :param Nodein: It is the node in the tree in which we need to update the quantity of the medicine
        :param Uid: Unique id of medicine
        :param availCount: Quantity to be incremented or decremented according to requirement
        :return: Nothing
        '''
        if(Nodein):
            Nodein.chkoutCtr = Nodein.chkoutCtr + 1
            if (Nodein.chkoutCtr % 2 == 0): #checking counter is odd or even to find sell or buy order
                if(availCount>Nodein.avCount):
                    print("Quantity of Drug Id "+str(Uid)+" available is "+str(Nodein.avCount)+" but asked is "+str(availCount)+"\n")
                else:
                    Nodein.avCount = Nodein.avCount - availCount
            else:
                Nodein.avCount = Nodein.avCount + availCount

        
    def printDrugInventory(self):
        '''
        function to print all nodes in the Binary tree
        :return: Nothing
        '''
        print("------------- printDrugInventory ---------------")
        #counting number of nodes
        def count_nodes(data):
            if data is None:
                return 0
            return 1 + count_nodes(data.left) + count_nodes(data.right)
        Total_nodes=count_nodes(self)
        print("Total number of medicines entered in the inventory: "+str(Total_nodes))
        Uidlist=[]
        def PrintTree(node):
            if(node.left):
                PrintTree(node.left)
            Uidlist.append(str(node.Uid)+","+str(node.avCount))
            if(node.right):
                PrintTree(node.right)

        PrintTree(self)
        for i in range(0, len(Uidlist) - 1):
            for j in range(i + 1, len(Uidlist)):
                if (int(Uidlist[i].split(",")[0]) > int(Uidlist[j].split(",")[0])):
                    temp = Uidlist[i]
                    Uidlist[i] = Uidlist[j]
                    Uidlist[j] = temp
        for each in Uidlist:
            print(each)
        print("-----------------------------------------------\n")
    def printStockOut(self):
        '''
        #function to print the drug unique ids which are out of stock
        :return: Nothing
        '''

        print("------------- printStockOut ---------------")
        print("The following medicines are out of stock:\n")
        list = []
        def ListofUidOutStock(node):
            if(node==None):
                return 0
            if (node.avCount == 0):
                list.append(node.Uid)
            ListofUidOutStock(node.left)
            ListofUidOutStock(node.right)

            return list
        data=ListofUidOutStock(self)
        for each in data:
            print(each)
            
        if(len(data)==0):
            print("All medicines are in stock")
        print("-----------------------------------------------\n")
    def highDemandDrugs(self,status, frequency):
        '''
        #function to print the drugs which are in high demand
        :param status: It is one of the inputs says sell or buy
        :param frequency: times the medicine is sold or bought
        :return:
        '''

        print('Drugs with '+status+' entries more than '+str(frequency)+' times are:')
        list = []

        def highDim(node,status,frequency):
            if (node == None):
                return 0
            if (node.chkoutCtr!=0):
                if(status=='sell'):
                    if frequency<int(node.chkoutCtr/2):
                        list.append(str(node.Uid)+" "+str(node.chkoutCtr))
                if(status=='buy'):
                    if frequency <int(node.chkoutCtr/2)+1:
                        list.append(str(node.Uid) + " " + str(node.chkoutCtr))
            highDim(node.left,status,frequency)
            highDim(node.right,status,frequency)

            return list
        highdata=highDim(self,status,frequency)
        for each in highdata:
            print(each)
        print("-----------------------------------------------\n")

    def supplyShortage(self,minunits):
        '''
        function to print the drugs which are less than minimum quantity
        :param minunits:
        :return:
        '''
        print("------------- supplyShortage: "+str(minunits)+" ---------------")
        list = []

        def Supplyshort(node,minunits):
            if (node == None):
                return 0
            if (node.avCount <= minunits):
                list.append(str(node.Uid)+" "+str(node.avCount))
            Supplyshort(node.left,minunits)
            Supplyshort(node.right,minunits)
            return list
        supplyshor=Supplyshort(self,minunits)
        for each in supplyshor:
            print(each)
        if(len(supplyshor)==0):
            print("Quantity of all medicines is morethan"+str(minunits)+"\n")
        print("-----------------------------------------------\n")

def readInputPS1file():
    '''
    this function is to read input ps1 file and create nodes in the tree accordingly
    :return: this function returns the Tree created by reading inputPS1 file
    
    '''
    if(os.path.isfile('inputPS1.txt')):
        with open('inputPS1.txt','r') as druginput:
            data=druginput.read().split("\n")
            rootnode=DrugNode(int(data[0].split(",")[0]),int(data[0].split(",")[1]))
            for ele in range(1,len(data)):
                if data[ele] != '':
                    Status=ifNodeExists(rootnode,int(data[ele].split(",")[0]))
                    Nodein=NodeinTree(rootnode,int(data[ele].split(",")[0]))
                    if Status:
                        Nodein.chkoutCtr = Nodein.chkoutCtr + 1
                        if(Nodein.chkoutCtr%2==0):
                            Nodein.avCount=Nodein.avCount-int(data[ele].split(",")[1])
                        else:
                            Nodein.avCount = Nodein.avCount + int(data[ele].split(",")[1])
                    else:
                        rootnode.readDrugList(int(data[ele].split(",")[0]),int(data[ele].split(",")[1]))
        return rootnode
    else:
        print("InputPS1.txt file doesnot exist")
def readpromptsPS1file(rootnode):
    '''
    This function is used to read PromptsPS1file from the current working directory
    :param rootnode: Root node is parameter to this function which is required to update or change the data in the Tree
    :return: Nothing
    '''
    # this function is used to read prompts ps2.txt file and run the commands accordingly
    if(os.path.isfile('promptsPS1.txt')):
        with open('promptsPS1.txt','r') as prompts:
            promptsdata=prompts.read().split("\n")
            try :
                for each in promptsdata:
                    if(each!=""):
                        if(each.split()[0] == 'printDrugInventory'):
                            rootnode.printDrugInventory()
                        elif(each.split()[0] == 'printStockOut'):
                            rootnode.printStockOut()
                        elif(each.split()[0] == 'updateDrugList:'):
                            inputs=each.split(":")[1].split(",")
                            Status=ifNodeExists(rootnode,int(inputs[0]))
                            Node = NodeinTree(rootnode, int(inputs[0]))
                            if(Status):
                                rootnode._updateDrugList(Node,int(inputs[0]), int(inputs[1]))
                            else:
                                rootnode.readDrugList(int(inputs[0]), int(inputs[1]))
                        elif(each.split()[0] == 'checkDrugStatus:'):
                            rootnode.checkDrugStatus(int(each.split(":")[1]))
                        elif(each.split()[0] == 'freqDemand:'):
                            rootnode.highDemandDrugs(each.split()[1].strip(","),int(each.split()[2]))
                        elif(each.split()[0] == 'supplyShortage:'):
                            rootnode.supplyShortage(int(each.split()[1]))
            except:
                print("Input in the prompts PS1 is not correct ,update the input and run Again")
    else:
        print("PromptsPS1.txt file does not exist in the current working directory")
def foo():
    foo.flag=1
foo.flag = 0
def ifNodeExists(node, key):
    '''
    this function is used to check if the node is present in the tree or not
    :param node: Root of the tree where the key has to be searched
    :param key: the Unique id which has to be checked in Tree
    :return: True or False
    '''
    if (node == None):
        return False
    if (node.Uid == key):
        return True
    res1 = ifNodeExists(node.left, key)
    if res1:
        return True
    res2 = ifNodeExists(node.right, key)
    return res2
def NodeinTree(node,Uid):
    '''
    Function to find if node is present in the tree or not
    :param node: Root node as parameter
    :param Uid: Unique id to be searched in the Tree
    :return: Node if it is matched with Unique id else None
    '''
    if(node==None):
        return None
    if(node.Uid==Uid):
        return node
    res1 = NodeinTree(node.left, Uid)
    if(res1):
        return res1
    res2 = NodeinTree(node.right, Uid)
    return res2
root=readInputPS1file()
readpromptsPS1file(root)