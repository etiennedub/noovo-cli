from app import App
import sys

if __name__ == '__main__':
    a = App(sys.argv[1:])
    #a = App(["Un souper presque parfait", "-v", "-l"])
    rc = a.run()




