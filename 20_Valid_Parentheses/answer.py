class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        head_list = ["(", "{", "["]
        dict_ = {
            "(": ")",
            "{": "}",
            "[": "]"
        }

        for sym in s:
            if sym in head_list:
                stack.append(dict_[sym])
            else:
                if not stack:
                    return False
                correct_tail = stack.pop()
                
                if correct_tail != sym:
                    return False
        if stack:
            return False
        return True