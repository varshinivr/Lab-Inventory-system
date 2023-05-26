class TreeNode :
    def __init__(self, data,q,name) :
        self.data = data
        self.q=q
        self.name=name
        self.left = None
        self.right = None
        self.parent = None
        
class SplayTree :
    def __init__(self) :
        self.root = None
    def zig(self, node) :
        parent = node.parent
        parent.left = node.right
        if (node.right != None) :
            node.right.parent = parent
        node.right = parent
        node.parent = parent.parent
        parent.parent = node
    def zag(self, node) :
        parent = node.parent
        parent.right = node.left
        if (parent.right != None) :
            parent.right.parent = parent
        node.left = parent
        node.parent = parent.parent
        parent.parent = node
    def zigZig(self, node) :
        parent = node.parent
        grandParent = node.parent.parent
        parent.left = node.right
        if (node.right != None) :
            node.right.parent = parent
        node.right = parent
        parent.parent = node
        grandParent.left = parent.right
        if (parent.right != None) :
            parent.right.parent = grandParent
        parent.right = grandParent
        node.parent = grandParent.parent
        if (grandParent.parent != None) :
            if (grandParent.parent.left != None and
                grandParent.parent.left == grandParent) :
                grandParent.parent.left = node
            else :
                grandParent.parent.right = node
        grandParent.parent = parent
    def zagZag(self, node) :
        parent = node.parent
        grandParent = node.parent.parent
        parent.right = node.left
        if (node.left != None) :
            node.left.parent = parent
        node.left = parent
        node.parent = grandParent.parent
        if (grandParent.parent != None) :
            if (grandParent.parent.left != None and
                grandParent.parent.left == grandParent) :
                grandParent.parent.left = node
            else :
                grandParent.parent.right = node
        parent.parent = node
        grandParent.right = parent.left
        if (parent.left != None) :
            parent.left.parent = grandParent
        parent.left = grandParent
        grandParent.parent = parent
    def zagZig(self, node) :
        parent = node.parent
        grandParent = node.parent.parent
        parent.left = node.right
        if (node.right != None) :
            node.right.parent = parent
        grandParent.right = node
        node.parent = grandParent
        node.right = parent
        parent.parent = node
    def zigZag(self, node) :
        parent = node.parent
        grandParent = node.parent.parent
        parent.right = node.left
        if (node.left != None) :
            node.left.parent = parent
        grandParent.left = node
        node.parent = grandParent
        node.left = parent
        parent.parent = node
    def applyRotation(self, node) :
        if (node.parent != None) :
            if (node.parent.left != None and
                node.parent.left == node and
                node.parent.parent == None) :
                self.zig(node)
            elif (node.parent.right != None and
                  node.parent.right == node and
                  node.parent.parent == None) :
                self.zag(node)
            elif (node.parent.left != None and
                  node.parent.left == node and
                  node.parent.parent.left != None and
                  node.parent.parent.left == node.parent) :
                self.zigZig(node)
            elif (node.parent.right != None and
                  node.parent.right == node and
                  node.parent.parent.right != None and
                  node.parent.parent.right == node.parent) :
                self.zagZag(node)
            elif (node.parent.right != None and
                  node.parent.right == node and
                  node.parent.parent != None and
                  node.parent.parent.left != None and
                  node.parent.parent.left == node.parent) :
                self.zigZag(node)
            elif (node.parent.left != None and
                  node.parent.left == node and
                  node.parent.parent != None and
                  node.parent.parent.right != None and
                  node.parent.parent.right == node.parent) :
                self.zagZig(node)
            else :
                return
            self.applyRotation(node)
    def insertNode(self, data,q,name) :
        node = TreeNode(data,q,name)
        temp = None
        if (self.root == None) :
            self.root = node
        else :
            temp = self.root
            while (temp != None) :
                if (data > temp.data) :
                    if (temp.right == None) :
                        temp.right = node
                        node.parent = temp
                        temp = None
                    else :
                        temp = temp.right
                else :
                    if (temp.left == None) :
                        temp.left = node
                        node.parent = temp
                        temp = None
                    else :
                        temp = temp.left
            self.applyRotation(node)
        self.root = node
    def inOrder(self, node) :
        if (node != None) :
            self.inOrder(node.left)
            print(str(node.name),end ="  ")
            self.inOrder(node.right)
    def printTree(self) :
        if (self.root == None) :
            print("\n Empty Tree")
        else :
            print("\n Inorder :")
            self.inOrder(self.root)
            print()
    def deleteNode(self, value) :
        if (self.root != None) :
            node = self.root
            rightChild = None
            leftChild = None
            while (node != None and node.data != value) :
                if (value > node.data) :
                    node = node.right
                else :
                    node = node.left
            if (node != None) :
                print("\n Before delete node [" +
                      str(value) + "] :", end ="")
                self.printTree()
                self.applyRotation(node)
                self.root = node
                if (node.left == None) :
                    self.root = node.right
                elif (node.right == None) :
                    self.root = node.left
                else :
                    if (node.left != None) :
                        node.left.parent = None
                    if (node.right != None) :
                        node.right.parent = None
                    rightChild = node.right
                    leftChild = node.left
                    self.root = None
                    node.right = None
                    node.left = None
                    node = leftChild
                    while (node.right != None) :
                        node = node.right
                    self.applyRotation(node)
                    node.right = rightChild
                    rightChild.parent = node
                    self.root = node
                print("\n After delete node [" +
                      str(value) + "] :", end ="")
                self.printTree()
            else :
                print("\nDelete node " +
                      str(value) + " are not exist")
            if (self.root != None) :
                self.root.parent = None


class chemical:
    def __init__(self,chem_no,chem_name):
        self.chem_no=chem_no
        self.chem_name=chem_name
    def get_chemno(self):
        return self.chem_no
    def get_chemname(self):
        return self.chem_name

class inventory:

    def __init__(self):
        self.possible=[[1, 1, 0, 0, 1],
                       [1, 1, 0, 0, 1], 
                       [0, 0, 1, 1, 0], 
                       [0, 0, 1, 1, 1], 
                       [1, 1, 0, 1, 1]]
        self.name=[["K2","KMnO4","Nil","Nil","KCl"],
                   ["KMnO4","(MnO4)2","Nil","Nil","MnO4Cl"],
                   ["Nil","Nil","S4","SO","Nil"],
                   ["Nil","Nil","SO","O2","ClO"],
                   ["KCl","MnO4Cl","Nil","ClO","Cl2"]]
        self.chemical=[chemical(1,"K"),chemical(2,"MnO4"),chemical(3,"S"),chemical(4,"O"),chemical(5,"Cl")]
    
    def find(self,x):
        for i in self.chemical:
            if(i.get_chemname()==x):
                y=i.get_chemno()
                return y
        print("\n\tElement not present !")
        return False
    
    def add_edge(self,x,y):
        self.possible[x][y]=1
        self.name[x][y]=self.chemical[x].get_chemname()+self.chemical[y].get_chemname()

    def delete_edge(self,x,y):
        self.possible[x-1][y-1]=0
    
    def check(self,x,y):
        if(self.possible[x-1][y-1]==1):
            print("\n\tExists !")
            return self.name[x-1][y-1]
        else:
            print("\n\tDoes not Exist !")
            return -1

def edge_add():
    x=input("\n\tElement : ")
    y=input("\tElement : ")
    k=a.find(x)
    l=a.find(y)
    a.add_edge(k-1,l-1)
    print("\n\tEdge added !")
    xmenu(x)

def edge_delete():
    x=input("\n\tElement : ")
    y=input("\tElement : ")
    k=a.find(x)
    l=a.find(y)
    a.delete_edge(k-1,l-1)
    print("\n\tEdge deleted !")
    xmenu(x)
input
def create_compound():
    x=1
    print("\n\tCREATE COMPOUND")
    while(x==1):
        k=input("\n\tElement : ")
        l=input("\tElement : ")
        x=a.find(k)
        if(x==False):
            return 
        if(x==-1):
            print("\n\tElement not present !")
        y=a.find(l)
        if(y==-1):
            print("\n\tElement not present !")
        m=a.check(x,y)
        if(m==-1):
            print("\n\tNot possible !")
        else:
            b.insertNode(0,5,m)
            b.printTree()
            x=int(input("\n\tEnter 1 to continue, Choice : "))
    xmenu(x)

def xmenu(x):
    while(x==1):
        print("\n\t")
        print("\n\t1 - Add Edge")
        print("\t2 - Delete Edge")
        print("\t3 - Create Compund")
        print("\t4 - Exit")
        choice=int(input("\n\tEnter choice : "))
        if(choice==1):
            edge_add()       
        elif(choice==2):
            edge_delete()            
        elif(choice==3):
            create_compound()
        elif(choice==4):
            x=0
            return    

def start():
    print("\n\tLAB INVENTORY\n")
    login_id=int(input("\t1 - Teacher\n\t2 - Student\n\tChoice : "))
    if(login_id==1):
        id=(input("\n\tEnter ID : "))
        c.login(id)
    elif(login_id==2):
        id=input("\n\tEnter ID : ")
        d.login(id)

class teacher:
    def __init__(self,teacher_id,teacher_name):
        self.teacher_id=teacher_id
        self.teacher_name=teacher_name
    def login(self,x):
        if x in tea:
            print("\n\tLogin successful !")
            xmenu(1)            
        else:
            print("\n\tInvalid input !")

b=SplayTree()
a=inventory()

def view_splay(x):
    b.printTree()
    tmenu(x)

def create_compound1(x):
    teacher.createcompund()
    tmenu(x)

def view_graph(x):
    print("\n")
    for i in a.possible:
        print("\t",i)
    tmenu(x)

def tmenu(x):
    print("\n\tMENU")
    print("\n\t1 - View splay tree")
    print("\t2 - View graph")
    print("\t3 - Combine compounds")
    print("\t4 - Exit")
    choice=int(input("\n\tCHoice : "))
    if(choice==1):
        view_splay(x)       
    elif(choice==2):
        view_graph(x)            
    elif(choice==3):
        create_compound()
    elif(choice==4):
        x=0
        return 

class student:
    def __init__(self,student_id,student_name):
        self.student_id=student_id
        self.student_name=student_name
    
    def login(self,x):
        if x in stud:
            print("\n\tLogin successful ! ")
            tmenu(1)
        else:
            print("\n\tInvalid input ! ")

tea=["Anu","Mona","Raji","Aditi","Priya"]
stud=["Shyam","Seenu","Venkat","Ramesh","Suresh"]
flag=0
c=teacher("Mona",101)
d=student("Mona",1)

a=inventory()
b=SplayTree()