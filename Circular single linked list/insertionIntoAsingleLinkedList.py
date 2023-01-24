
#creation of constructor
class Node:
    def __init__(self,value=None):
        self.value=value
        self.next=None

#creation of our class
class circularSingleLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None

    def __iter__(self):
        node=self.head

        while node:
            yield node
            node = node.next
            if node==self.tail.next:
                break


    #insertion into single linked list
    def insertion(self,value,location):
        nodeValue=Node(value)
        if self.head is None:
            self.head=nodeValue
            self.tail=nodeValue

        else:
            if location==0:
                nodeValue.next=self.head
                self.head=nodeValue
                self.tail.next=nodeValue

            elif location==1:
                nodeValue.next=self.tail.next
                self.tail.next=nodeValue
                self.tail=nodeValue

            else:
                node=self.head
                index=0
                while index<location-1:
                    node=node.next
                    index+=1
                nodeNodenext=node.next

                node.next=nodeValue
                nodeValue.next=nodeNodenext

        return "successfully inserted"

    #traversing a single linked list
    def traversing(self):
        if self.head is None:
            print("the circular single linked list does not exist")
        else:
            nodevalue=self.head
            while nodevalue.next is not None:
                print(nodevalue.value)
                nodevalue=nodevalue.next

                #we include this portion because the last node points to the physical address of the last node
                if nodevalue==self.tail.next:
                    break

            return "node value is Null"

    #searching for a node in a circular linked list
    def searching(self,nodevalue):
        if self.head is None:
            print("the linked list is empty")

        else:
            node=self.head
            while node is not None:
                if node.value==nodevalue:
                    print (node.value)
                node=node.next
                if node==self.tail.next:
                    return "the node does not exist"
    #deleting a node
    def deleting(self,location):
        if self.head is None:
            return "no element found to delete"

        else:
            nodevalue = self.head
            if location==0:
                if self.head==self.tail:
                    self.head=None
                    self.tail=None
                    nodevalue.next=None

                else:
                    self.head=self.head.next
                    self.tail.next=self.head

            elif location==1:
                if self.head==self.tail:
                    self.head=None
                    self.tail=None
                    nodevalue.next=None

                else:
                    # index=0
                    while nodevalue is not None:
                        if nodevalue.next==self.tail:
                            break
                        nodevalue=nodevalue.next
                    nodevalue.next=self.head
                    self.tail=nodevalue

            else:
                index=0
                while index<location-1:
                    nodevalue=nodevalue.next
                    index+=1
                nodeNodenext=nodevalue.next

                nodevalue=nodevalue.next
                nodevalue.next=nodeNodenext.next

    #deleting the entire single linked list
    def deleteAll(self):
        if self.head is None:
            return "no nodes found to delete"
        else:
            node=self.head
            self.head=None
            self.tail=None
            node=None
circularSLL=circularSingleLinkedList()
circularSLL.insertion(2,0)
circularSLL.insertion(5,1)
circularSLL.insertion(7,0)
circularSLL.insertion(9,1)
circularSLL.insertion(10,2)
print([node.value for node in circularSLL])

# circularSLL.traversing()
print("searching")
# circularSLL.searching(10)
# print([node.value for node in circularSLL])
circularSLL.deleting(0)
circularSLL.deleting(2)
circularSLL.deleting(1)
print([node.value for node in circularSLL])
circularSLL.deleteAll()
print("deleting everything")
