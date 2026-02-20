class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        a=[]
        for m in range(1,n+1):
            if m % 15 == 0:
                a.append("FizzBuzz")
            elif m % 3 == 0:
                a.append("Fizz")
            elif m % 5 == 0:
                a.append("Buzz")
            else:
                a.append(f"{m}")
        return a
