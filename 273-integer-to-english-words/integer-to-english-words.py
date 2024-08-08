class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        ones_map = {
            1:"One",
            2:"Two",
            3:"Three",
            4:"Four",
            5:"Five",
            6:"Six",
            7:"Seven",
            8:"Eight",
            9:"Nine",
            10:"Ten",
            11:"Eleven",
            12:"Twelve",
            13:"Thirteen",
            14:"Fourteen",
            15:"Fifteen",
            16:"Sixteen",
            17:"Seventeen",
            18:"Eighteen",
            19:"Nineteen"
        }

        tens_map = {
            2:"Twenty",
            3:"Thirty",
            4:"Forty",
            5:"Fifty",
            6:"Sixty",
            7:"Seventy",
            8:"Eighty",
            9:"Ninety"
        }
        
        suffixes = {
            0:"", 
            1:"Thousand",
            2:"Million",
            3:"Billion",
            4:"Trillion",
            5:"Quadrillion", 
            6:"Quintillion",
            7:"Sextillion",
            8:"Septillion", 
            9:"Octillion", 
            10:"Nonillion",
            11:"Decillion"
        }
        
        words = []
        count = 0 
        
        while num:
            temp = num % 1000
            num = num // 1000

            if temp == 0:
                count += 1
                continue
            
            sub_words = []
            x = temp % 100
            if x > 19:
                if x % 10:
                    sub_words.insert(0,ones_map[x % 10])
                sub_words.insert(0,tens_map[x // 10])
            elif x != 0:
                sub_words.insert(0,ones_map[temp % 100])
            
            if temp // 100:
                sub_words.insert(0, "Hundred")
                sub_words.insert(0, ones_map[temp // 100])
            
            if count:
                sub_words.append(suffixes[count])
            
            words = sub_words + words
            count += 1

        
        return ' '.join(words)

            

