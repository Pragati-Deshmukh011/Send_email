class Node:
    def __init__(self,value):
        self.data= value
        self.next= None
class linkedlist:
    def __init__(self): #empty ll  head=None
        self.head= None
        self.n=0
    def __len__(self):
        return self.n
    def insert_head(self,value):
        new_node=Node(value)
        new_node.next=self.head
        self.head=new_node
        self.n=self.n+1
    def __str__(self):
        curr=self.head
        res=''
        while curr!=None:
            res = res+str(curr.data)+'->'
            curr = curr.next
        return res[:-2]
    def append(self, value):
        new_node = Node(value)
        if self.head==None:
            self.head=new_node
            self.n=self.n+1
            return

        curr=self.head
        while curr.next!=None:
            curr = curr.next
        curr.next=new_node
        self.n=self.n+1
    def insertafter(self,after, value):
        new_node=Node(value)
        curr= self.head
        while curr!=None:
            if curr.data==after:
                break
            curr = curr.next
        if curr!=None:
            new_node.next=curr.next
            curr.next=new_node
        else:
            return 'Item not found'
    def clear(self):
        self.head=None
        self.n=0
    def del_head(self):
        if self.head==None:
            return 'empty LL'
        self.head= self.head.next
        self.n=self.n-1
    def del_tail(self):
        if self.head==None:
            return 'empty'
        curr = self.head
        if curr.next==None:
            return self.del_head()

        #curr=self.head
        while curr.next.next!=None:
            curr=curr.next
        curr.next=None
        self.n = self.n - 1
    def remove_value(self,value):
        if self.head==None:
            return 'empty ll'
        if self.head.data==value:
            return self.del_head()
        curr=self.head
        while curr.next!=None:
            if curr.next.data==value:
                break
            curr= curr.next
            #2cases
            if curr.next==None:
                return 'Not found'
            else:
                curr.next=curr.next.next
    def search(self,item):
        curr=self.head
        ind=0
        while curr!=None:
            if curr.data == item:
                return ind
            curr= curr.next
            ind+=1
        return 'not found'
    def __getitem__(self, index):
        curr=self.head1
        pos=0
        while curr!=None:
            if pos==index:
                return curr.data
            curr=curr.next
            pos+=1
        return 'index error'
    def replace_max(self,value):
        curr=self.head
        max=curr
        while curr!=None:
            if curr.data>max.data:
                max=curr
            curr = curr.next
        max.data= value
    def sum_odd_nodes(self):
        temp = self.head
        count=0
        result =0
        while temp!=None:
            if count%2!=0:
                result = result+temp.data
            count+=1
            temp=temp.next
        return (result)

    def reverse(self):
        prev_N= None
        curr_N = self.head

        while curr_N!=None:
            next_N = curr_N.next
            curr_N.next = prev_N
            prev_N= curr_N
            curr_N= next_N
        self.head = prev_N

    def change_sent(self):
        temp=self.head
        while temp!=None:
            if temp.data=='*' or temp.data=='/':
                temp.data=' '
                if temp.next.data=='*' or temp.next.data=='/':
                    temp.next.next,data= temp.next.next.data.upper()
                    temp.next=temp.next.next
        temp= temp.next




L=linkedlist()
L.insert_head(1)
L.insert_head(2)
L.insert_head(3)
L.insert_head(4)
#L.replace_max(6)
#L.sum_odd_nodes()
L.reverse()
print(L)






