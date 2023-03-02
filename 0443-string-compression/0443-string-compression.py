class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0
        while i < len(chars):
            count = 0
            for char in chars[i:]:
                if char != chars[i]:
                    break
                count += 1
            if count != 1:
                list_appending = list(str(count))
                chars[i+1:i+count] = list_appending
                i += 1 + len(list_appending)
            else:
                i += 1
            
        return len(chars)
