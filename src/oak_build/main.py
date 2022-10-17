from sys import exit, argv

from oak_build.app import App

if __name__ == '__main__':
    exit(App(argv[1:]).run())
