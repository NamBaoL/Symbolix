import sys, main
from termcolor import *

if len(sys.argv) == 1 or sys.argv[1:][0] == 'run':
  print(colored("Symbolix Editor 0.1.0", 'light_blue', attrs=['bold']) + colored(' [made by @ErikTheParrot]\n', 'light_blue'))
  while True:
    main.run([input("> ")])