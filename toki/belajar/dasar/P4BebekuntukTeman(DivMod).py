# P4BebekuntukTeman(DivMod).py : program sederhana pembagian dan modulus.
# Ridhan Fadhilah, 10-12-2015

a, k = map(int, input().split())
jml  = str(a // k)                # pembagian
sisa = str(a % k)                 # modulus
print('masing-masing ' + jml)
print('bersisa ' + sisa)
