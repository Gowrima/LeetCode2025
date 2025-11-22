class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        
        i, j, result = 0, 0, 0

        for i in range(len(players)):
            while j<len(trainers):
                #print ("i=", i, "j =", j)

                if players[i] <= trainers[j]:
                    result += 1
                    j += 1
                    break
                else:
                    j += 1

        return result