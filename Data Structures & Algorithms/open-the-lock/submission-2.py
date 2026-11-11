class Solution:
    
    def openLock(self, deadends: List[str], target: str) -> int:
        visited = {}
        bfs = [["0000",0]]
        while bfs:
            current,turns = bfs.pop(0)
            if current in deadends:continue 
            if current in visited and visited[current]<=turns:
                continue
            visited[current] = turns
            if current == target:continue
            
            for i in range(len(current)):
                temp = list(current)
                if temp[i]=="0":
                    temp[i] = "1"
                    bfs.append(["".join(temp),turns+1])
                    temp[i]="9"
                    bfs.append(["".join(temp),turns+1])
                elif temp[i]=="9":
                    temp[i] = "0"
                    bfs.append(["".join(temp),turns+1])
                    temp[i]="8"
                    bfs.append(["".join(temp),turns+1])
                else:
                    
                    temp[i] = str(int(current[i])+1)
                    bfs.append(["".join(temp),turns+1])
                    temp[i]=str(int(current[i])-1)
                    bfs.append(["".join(temp),turns+1])
                
        return visited.get(target,-1)
                