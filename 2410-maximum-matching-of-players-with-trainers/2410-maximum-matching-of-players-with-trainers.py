class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        
        i, j, result = 0, 0, 0

        for i in range(len(players)):
            while j<len(trainers):
                
                if players[i] <= trainers[j]:
                    result += 1
                    j += 1
                    break
                j += 1

        return result