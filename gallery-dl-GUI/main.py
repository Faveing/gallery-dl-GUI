import logging
import window
from configWindow import configWindow
def main():
    configWindowApp= configWindow(argv=[])
    app = window.GUI(configWindow = configWindowApp)

if __name__ == "__main__":
    main()