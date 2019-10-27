#!/usr/bin/python3
from webpage import webpage
from parser import instaparse

url = input("Enter an instagram profile: ")
if __name__ == "__main__":
    page = webpage(url)
    p = instaparse(page)
    page.tostring()
