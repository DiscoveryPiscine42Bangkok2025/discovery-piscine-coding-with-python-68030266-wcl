import sys

def main():
    if len(sys.argv) != 2:
        return
    text = sys.argv[1]
    for ch in text:
        if ch == 'z':
            print("z")