class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        # Avoid recalculation
        memoize: Dict[int, bool] = {}
    
        def checkWord(index: int) -> bool:
            if index in memoize:
                return memoize[index]

            if index >= len(s):
                return True

            currIndex = index
            currStr = ""

            while currIndex < len(s):
                currStr += s[currIndex]

                # use the word in the dictionary
                if currStr in wordDict and checkWord(currIndex + 1):
                    memoize[index] = True
                    return True

                # dont use the word in the dictionary - continue adding to currIndex
                currIndex += 1
            
            memoize[index] = currStr in wordDict
            return memoize[index]

        return checkWord(0)
                
            


