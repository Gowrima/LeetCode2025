class Solution:
    def convertDateToBinary(self, date: str) -> str:
        date_ = date.split('-')
        result = ''

        for i in range(len(date_)):
            # convert date_[i] to binary
            res = ''

            cur = int(date_[i])

            while cur > 0:
                res += str(cur%2)
                cur = cur//2
            
            result += res[::-1]
            result += '-'
        
        return result[:-1]

