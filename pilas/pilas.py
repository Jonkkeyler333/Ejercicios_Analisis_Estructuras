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
        """Remove and return the top element from the stack

        :raises Empty: if the stack is empty , return a Excepcion
        :return: return the top element from the stack
        """
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
        else:
            return self.data[-1]
    
    def clear(self)->None:
        """Remove all the elements of the stack
        """
        self.data=[]
        
    def __str__(self) -> str:
        return(str(self.data))
        
# if __name__=='__main__':
#     p1=Pila()
#     p1.push('keyler')
#     p1.push('andrea')
#     p1.push(20)
#     print(p1.is_Empty())
#     print(len(p1))
#     print(p1.top())
#     print(p1.pop())
#     print(p1.top())
#     print(p1)
#     print(p1.pop())
#     print(p1,p1.clear(),p1)
        
    