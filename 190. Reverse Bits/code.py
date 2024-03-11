class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        binary = format(n,'b')
        binary = binary.zfill(32)
        reverse = str(binary)[::-1]
        return int(str(reverse), 2)

if __name__ == "__main__":
    a = Solution()
    n = 43261596
    print(a.reverseBits(n))  