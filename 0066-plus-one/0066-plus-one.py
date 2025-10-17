class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        j = len(digits)-1
        carry = 0

        while j >= 0:
            if digits[j] < 9:
                digits[j] += 1
                return digits
            
            tmp_res = digits[j]+1
            carry = tmp_res//10
            tmp_res = tmp_res%10

            digits[j] = tmp_res

            if j == 0:
                digits.append(carry)
                carry = 0

            j -= 1

        return digits[::-1]
                
            
