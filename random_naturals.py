#! /usr/bin/env python
"Emit a random natural note at specified tempo."

import random
import sys
import time

notes = ["A", "B", "C", "D", "E", "F", "G"]

if __name__ == "__main__":
    if len(sys.argv) > 1:
        tempo = int(sys.argv[1])
    else:
        tempo = 60

    while True:
        print(random.choice(notes))
        time.sleep(60. / tempo)
