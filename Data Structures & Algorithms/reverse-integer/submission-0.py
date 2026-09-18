class Solution:
    def reverse(self, x: int) -> int:
        string_int = str(x)
        reverse_int = 0
        if string_int[0] == '-':
            reverse_int = int('-' + string_int[:0:-1])
        else:
            reverse_int = int(string_int[::-1])
        if -2**31 <= reverse_int <= 2**31 - 1:
            return reverse_int
        return 0
        