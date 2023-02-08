import argparse
import csv
import re
import sys
import urllib.request
from urllib.request import urlopen
# other imports go here

url = 'http://s3.amazonaws.com/cuny-is211-spring2015/weblog.csv'

def downloadData(url):
    """Downloads the data"""
    with urllib.request.urlopen(url) as response:
        response = response.read().decode('utf-8')
    return response

def processData(file):
    with open(sys.argv[1], 'rt') as f:
        reader = csv.reader(f)

#search for hits that are an image file
file = downloadData(url)
reader = csv.reader(file.splitlines(), delimiter=',')
heading = next(reader, None)
hits = 0
image_hits = 0
for line in reader:
    filename = line[0]
    hits += 1
    if re.search(r"(\.jpeg|\.gif|\.PNG)$", str(filename)):
        image_hits += 1
percentage = (image_hits / hits) * 100

print("Image requests account for {:.1f}% of all requests".format(percentage))

#determine the most popular browser
file = downloadData(url)
reader = csv.reader(file.splitlines(), delimiter=',')
heading = next(reader, None)
browser_counts = {"Firefox": 0, "Chrome": 0, "Internet Explorer": 0, "Safari": 0}
for line in reader:
    browser = line[2]
    if re.search(r"Firefox", str(browser)):
        browser_counts["Firefox"] += 1
    if re.search(r"Chrome", str(browser)):
        browser_counts["Chrome"] += 1
    if re.search(r"MSIE", str(browser)):
        browser_counts["Internet Explorer"] += 1
    if re.search(r"Safari", str(browser)):
        browser_counts["Safari"] += 1

most_popular = max(browser_counts, key=browser_counts.get)
print(most_popular, "is the most popular browser")

def main(url):
    print(f"Running main with URL = {url}...")


if __name__ == "__main__":
    """Main entry point"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", help="URL to the datafile", type=str, required=True)
    args = parser.parse_args()
    main(args.url)
    
