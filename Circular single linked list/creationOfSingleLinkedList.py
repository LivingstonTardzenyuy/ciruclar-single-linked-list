
#defining our constructor class
class Node:
    def __init__(self,value=None):
        self.value=value
        self.next=None
#defining our circular linked list
class circularSingleLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None

    def __iter__(self):
        node=self.head
        while node:
            yield node
            node=node.next

    def insertion(self,value,location):
        nodeValue=Node(value)
        if self.head is None:
            self.head=nodeValue
            self.tail=nodeValue
            # print ("no linked list present")

        else:
            if location==0:
                nodeValue.next=self.head
                self.head=nodeValue

            elif location==1:
                nodeValue.next=None
                self.tail.next=nodeValue
                self.tail=nodeValue

            else:
                node=self.head
                index=0
                while index<location-1:
                    node=node.next
                    index+=1
                nodeAfter=node.next

                node.next=nodeValue
                nodeValue.next=nodeAfter

    def displayingValue(self):
        if self.head is None:
            print("no elements to print")
        else:
            nodevalue=self.head
            while nodevalue is not None:
                print(nodevalue.value)
                nodevalue=nodevalue.next

    def searchingValue(self,nodeValue):
        if self.head is None:
            print("no value found to display")

        else:
            # node=self.head
            while self.head is not None:
                if nodeValue==self.head.value:
                    return self.head.value
                else:
                    self.head=self.head.next
            return "node value is None"

    #deleting all elements in the linked list
    def deletion(self,location):
        if self.head==None:
            print("the linked list does not exist")

        else:
            if location==0:
                if self.head==self.tail:
                    self.head=None
                    self.tail=None
                else:
                    self.head=self.head.next

            elif location==1:
                if self.head==self.tail:
                    self.head=None
                    self.tail=None

                else:
                    nodevalue=self.head
                    index=0
                    while nodevalue is not None:
                        if nodevalue.next ==self.tail:
                            break
                        nodevalue=nodevalue.next

                        nodevalue.next=None
                        self.tail=nodevalue

csll=circularSingleLinkedList()
csll.insertion(2,0)
print([node.value for node in csll])
csll.insertion(5,1)
print([node.value for node in csll])
csll.insertion(4,0)
print([node.value for node in csll])
csll.insertion(9,1)
print([node.value for node in csll])
csll.insertion(10,2)
print([node.value for node in csll])
# csll.displayingValue()

print("searching function")
# csll.deletion(0)
csll.deletion(1)
print([node.value for node in csll])