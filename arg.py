
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--echo", type=int, help="echo the string you use here")
args = parser.parse_args()

import time
for i in range(200):
    time.sleep(args.echo)
    print(args.echo)
    print('nonono')