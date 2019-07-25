# P14While(BeoBacot).py : program utk terus menampilkan input.
# Ridhan Fadhilah, 11-12-2015

while True:
    try:
        print(input())
    except(EOFError): # ctrl + D
        break
