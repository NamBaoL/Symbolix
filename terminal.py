import sys, main, os
from termcolor import *

if len(sys.argv) == 1 or sys.argv[1:][0] == 'run':
  os.system('cls' if os.name == 'nt' else 'clear')
  print(colored('Symbolix Editor v0.1.0', 'light_blue', attrs=['bold']) + colored(' [made by @ErikTheParrot]', 'light_blue'))
  print(colored('-> enter quit to quit\n', 'cyan'))
  while True:
    code = input('> ')
    if code == 'quit':
      break
    main.run([code])