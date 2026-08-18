class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        visited = set()
        
        def open_rooms(i: int): 
            if i in visited:
                return
            else:
                visited.add(i)
            
            for key in rooms[i]:
                open_rooms(key)


        open_rooms(0)

        return len(rooms) == len(visited)
