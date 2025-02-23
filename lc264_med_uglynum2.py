class Solution:
    def nthUglyNumber(self, n: int) -> int:
        # got this question from the heap / pq series
        # not sure if i would have tried solving w heap otherwise

        uglies = [1]
        seen = {1}
        i = 0
        while i < n-1:
            cur = heappop(uglies)
            # create products w 2,3,5 as prime factors
            products = [cur*2, cur*3, cur*5]
            for product in products:
                if product not in seen:
                    heappush(uglies, product)
                    seen.add(product)
            i += 1
        return uglies[0]

        