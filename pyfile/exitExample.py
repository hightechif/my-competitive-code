import sys

while True:
  print 'Type exit to exit.'
  respone = raw_input()
  if respone == 'exit':
    sys.exit()

  print 'You typed ' + respone + '.\n'
