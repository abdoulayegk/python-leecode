class stack:
    def __init__(self):
        self.items = []

    def push(self, data):
        return self.items.append(data)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        if self.items == []:
            return True
        return False


def is_match(p1, p2):
    if p1 == '(' and p2 == ')':
        return True
    if p1 == '[' and p2 == ']':
        return True
    if p1 == '{' and p2 == '}':
        return True
    else:
        return False


class Solution:
    def is_valid(self, s):
        st = stack()
        is_balanced = True
        index = 0
        while index < len(s) and is_balanced:
            parent = s[index]
            if parent in '([{':
                st.push(parent)
            else:
                if st.is_empty():
                    is_balanced = False
                else:
                    top = st.pop()
                    if not is_match(top, parent):
                        is_balanced = False
            index += 1
        if st.is_empty() and is_balanced:
            return True
        return False


val = Solution()
print(val.is_valid('[]()'))
