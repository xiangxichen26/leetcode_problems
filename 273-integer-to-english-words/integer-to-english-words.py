class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"

        self.ones_map = {
            1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five",
            6: "Six", 7: "Seven", 8: "Eight", 9: "Nine", 10: "Ten",
            11: "Eleven", 12: "Twelve", 13: "Thirteen", 14: "Fourteen",
            15: "Fifteen", 16: "Sixteen", 17: "Seventeen", 18: "Eighteen",
            19: "Nineteen"
        }

        self.tens_map = {
            2: "Twenty", 3: "Thirty", 4: "Forty", 5: "Fifty",
            6: "Sixty", 7: "Seventy", 8: "Eighty", 9: "Ninety"
        }

        self.suffixes = [
            "", "Thousand", "Million", "Billion",
            "Trillion", "Quadrillion", "Quintillion",
            "Sextillion", "Septillion", "Octillion",
            "Nonillion", "Decillion"
        ]

        words = self.convert_number_to_words(num)
        return ' '.join(words)

    def convert_number_to_words(self, num: int) -> list:
        words = []
        count = 0
        
        while num:
            temp = num % 1000
            num //= 1000

            if temp != 0:
                sub_words = self.convert_chunk(temp)
                if self.suffixes[count]:
                    sub_words.append(self.suffixes[count])
                words = sub_words + words

            count += 1
        
        return words

    def convert_chunk(self, num: int) -> list:
        sub_words = []
        
        if num >= 100:
            sub_words.append(self.ones_map[num // 100])
            sub_words.append("Hundred")
            num %= 100
        
        if num >= 20:
            sub_words.append(self.tens_map[num // 10])
            if num % 10:
                sub_words.append(self.ones_map[num % 10])
        elif num > 0:
            sub_words.append(self.ones_map[num])
        
        return sub_words
