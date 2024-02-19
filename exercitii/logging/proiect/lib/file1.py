import logging
lg = logging.getLogger("lproj."+__name__)

lg.debug("Incarcare modul")

def func1():
    print("f1")
    x = 1
    lg.debug("func1")
    lg.debug("func1 %s %s", x, 100)
