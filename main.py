#!/usr/bin/python3
from webpage import webpage
from parser import instaparse

if __name__ == "__main__":
    page = webpage("https://www.instagram.com/mariekondo/")
    p = instaparse(page)
    page.tostring()
