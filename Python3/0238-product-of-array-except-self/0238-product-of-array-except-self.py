class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        postfix = []

        product = 1
        for i in range(len(nums)):
            product *= nums[i]
            prefix.append(product)

        product = 1
        for j in range(len(nums) - 1, 0, -1):
            product *= nums[j]
            postfix.insert(0, product)
        postfix.append(1)

        l = []
        for i in range(len(nums)):
            prfx = prefix[i - 1] if i > 0 else 1
            n = prfx * postfix[i]
            l.append(n)
        return l