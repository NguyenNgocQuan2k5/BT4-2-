class Stack:
    def __init__(self):
        self.data = [] 
    
    def push(self, item):
        if isinstance(item, str):
            self.data.append(item) 
        else:
            raise ValueError("Chỉ cho phép chuỗi")
    
    def pop(self):
        if not self.is_empty():
            return self.data.pop()  
            raise IndexError("Không thể pop từ ngăn xếp trống")
    
    def peek(self):
        if not self.is_empty():
            return self.data[-1] 
        else:
            raise IndexError("Không thể peek từ ngăn xếp trống")
    
    def is_empty(self):
        return len(self.data) == 0 
    
    def __str__(self):
        return f"Stack({self.data})" 