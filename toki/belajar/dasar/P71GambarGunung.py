# P71GambarGunung.py : program utk menggambar pola gunung dari input integer.
# Ridhan Fadhilah, 16-10-2023

num = int(input())

def count(x):
    memo = [] # memoization
    for i in range(1,x+1): # change recursive with simple looping with memoization
      print("*" * i)
      memo.append(i)
      for j in range(0, len(memo)-1):
        print("*" * memo[j])
        memo.append(memo[j])

if (__name__ == "__main__"):
    count(num)