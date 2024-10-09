절댓값 힙import sys

class heap:
    def __init__(self):
        self.heap = []
    
    def insert(self, data):
        self.heap.append(data)
        # 맨 마지막에 넣고 heapify up 실행
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, current_idx):
        while current_idx > 0: # root노드면 종료
            parent_idx = (current_idx - 1) // 2
            if abs(self.heap[parent_idx]) < abs(self.heap[current_idx]):
                break
            elif abs(self.heap[parent_idx]) == abs(self.heap[current_idx]):
                if self.heap[parent_idx] < self.heap[current_idx]:
                    break
            self.heap[parent_idx], self.heap[current_idx] = self.heap[current_idx], self.heap[parent_idx]
            current_idx = parent_idx
    
    def delete(self):
        if not self.heap:
            return 0
        if len(self.heap) == 1:
            return self.heap.pop()
        
        output = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)

        return output

    def _heapify_down(self,i):
        smallest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < len(self.heap) and abs(self.heap[smallest]) >= abs(self.heap[left]):
            if abs(self.heap[smallest]) == abs(self.heap[left]):
                if self.heap[smallest] > self.heap[left]:
                    smallest = left
            else:
                smallest = left
        if right < len(self.heap) and abs(self.heap[smallest]) >= abs(self.heap[right]):
            if abs(self.heap[smallest]) == abs(self.heap[right]):
                if self.heap[smallest] > self.heap[right]:
                    smallest = right
            else:
                smallest = right
        if smallest != i:
            self.heap[smallest], self.heap[i] = self.heap[i], self.heap[smallest]
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
