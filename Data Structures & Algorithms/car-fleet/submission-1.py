class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        no_cars = len(position)
        time_pos = []
        stack = []
        fleet = 0

        for i in range(no_cars):
            time = (target-position[i])/speed[i]
            time_pos.append((time,position[i]))
        
        sorted_time_pos = sorted(time_pos, key=lambda x: x[1],reverse = True)
    
        for i in range(no_cars):
            if not stack:
                stack.append(sorted_time_pos[i][0])
                fleet +=1
            else:
                if sorted_time_pos[i][0]<=stack[-1]:
                    continue
                else:
                    stack.append(sorted_time_pos[i][0])
                    fleet +=1
        return fleet

        

