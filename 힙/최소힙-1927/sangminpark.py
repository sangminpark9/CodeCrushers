import sys

class heap:
    def __init__(self):
        self.arr= []

    def insert(self,data):
        self.arr.append(data)
        self._heapify_up(len(self.arr) - 1)
 
    def _heapify_up(self, current_idx):
        while current_idx > 0:
            parent_idx = (current_idx - 1) // 2
            if self.arr[parent_idx] <= self.arr[current_idx]:
                break
            self.arr[current_idx], self.arr[parent_idx] = self.arr[parent_idx], self.arr[current_idx]
            current_idx = parent_idx

    def delete(self):
        if len(self.arr) == 0: # 비어있는 경우
            return 0
        
        if len(self.arr) == 1:
            return self.arr.pop()
        
        output = self.arr[0]
        self.arr[0] = self.arr.pop()
        self._heapify_down(0)

        return output

    def _heapify_down(self, i):
        smallest = i
        left = 2 * i + 1
        right = 2 * i + 2
        
        if left < len(self.arr) and self.arr[left] < self.arr[smallest]:
            smallest = left
        
        if right < len(self.arr) and self.arr[right] < self.arr[smallest]:
            smallest = right
        
        if i != smallest:
            self.arr[i], self.arr[smallest] = self.arr[smallest], self.arr[i]
            self._heapify_down(smallest)
        

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    h = heap()
    for _ in range(n):
        x = int(sys.stdin.readline())
        if x == 0:
            print(h.delete())
        else:
            h.insert(x)
