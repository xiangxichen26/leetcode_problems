class Solution:
    def minimumPushes(self, word: str) -> int:
        # count the frequency of each characters in the word
        letter_counts = {chr(i): 0 for i in range(ord('a'), ord('z') + 1)}
        for i in word:
            letter_counts[i] = letter_counts.get(i) + 1

        # sorted the frequency of each characters
        letter_counts = dict(sorted(letter_counts.items(), key=lambda item: item[1], reverse=True))
        
        # assign letter to the key pad and count the push times
        ans = 0
        count = 0 
        time = 1
        for j in letter_counts:
            if letter_counts[j] == 0:
                break
            else:
                count += 1
                ans =  ans + letter_counts[j] * time
                if count == 8:
                    time += 1
                    count = 0 
        return ans
