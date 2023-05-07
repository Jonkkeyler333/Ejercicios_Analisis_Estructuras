from empty import Empty
class Pila:
    def __init__(self) -> None:
        self.data=[]
    
    def push(self,elemento)->None:
        """Add a element to the stack
        
        :param elemento: the element to add
        """
        self.data.append(elemento)

    def is_Empty(self)->bool:
        """Return True is the list is empty

        :return: the state of the stack(Empty?)
        :rtype: bool
        """
        return len(self.data)==0
    
    def pop(self):
        if self.is_Empty():
            raise Empty()
        else:
            return self.data.pop()
        
    def __len__(self)->int:
        """Return the len of the stack

        :return: the lent of the stack
        :rtype: int
        """
        return len(self.data)
    
    def top(self)->None:
        """Return (but do not remove) the element at the top of the stack
        return Raise Empty exception if the stack is empty
        """
        if self.is_Empty():
            raise Empty()
        
        

    
    
if __name__=='__main__':
    p1=Pila()
    p1.push('keyler')
    print(len(p1))
    print(p1.pop())
    p1.pop()
        
        
    