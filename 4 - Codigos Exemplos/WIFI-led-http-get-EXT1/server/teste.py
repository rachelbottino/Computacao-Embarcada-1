#!/usr/bin/env python

import json

def run():
    with open('LED.json', 'r') as f:
      data = json.load(f)
    print("LED está {}".format(data['LED']))

if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
