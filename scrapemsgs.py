from bs4 import BeautifulSoup
import argparse
import os
import csv
import json

class Error(Exception):
	pass

class ArgError(Error):
	def __init__(self, message):
		self.message = message

class Scraper():
    def __init__(self, files, user, save, rewrite, verbose):
        self.files = files
        self.user = user
        self.soups = []
        self.v = verbose
        self.rewrite = rewrite
        for file in files:
            self.printv("reading file")
            self.soups.append(BeautifulSoup(open(file), "html.parser"))
        self.readFiles()
    
    def printv(self, text):
        if self.v:
            print(text)

    def readFiles(self):
        if not os.path.exists("rawoutput.csv") or self.rewrite:
            self.printv("processing html files")
            self.messages = []
            fileno = 0
            for soup in self.soups:
                self.printv("reading " + self.files[fileno])
                # Intensive computation
                # May fail if a message div doesn't have a span child...
                rawdivs = soup.find_all(lambda div: div.has_attr('data-sigil') and div.has_attr('data-store') and div['data-sigil']=='message-text')
                for div in rawdivs:
                    info = json.loads(div['data-store'].replace('&quot;', '"'))
                    if(len(div.span.contents) > 0):
                        self.printv(div.span.contents[0])
                        self.messages.append([info['author'], info['timestamp'], div.span.contents[0]])
                fileno += 1
                with open("rawoutput.csv", "w") as f:
                    writer = csv.writer(f)
                    for message in self.messages:
                        writer.writerow(message)
        else:
            with open("rawoutput.csv", "w") as f:
                reader = csv.reader(f)
                self.messages = list(reader)
                

    def save(self, file):
        print("Unimplemented")
            
        
def main():
    parser = argparse.ArgumentParser(description='File name')

    parser.add_argument('-save', action = 'store_true', help='save to this file name')
    parser.add_argument('-files', nargs='+', type=str, help="html files to scrape", required=True)
    parser.add_argument('-user', default = "100002257667676", type = str, help='user name for flex')
    parser.add_argument('-rewrite', action = 'store_true', help='rewrites messages csv with raw html files')
    parser.add_argument('-v', action = 'store_true', help='enable verbose mode')

    args = parser.parse_args()		

    scraper = Scraper(args.files, args.user, args.save, args.rewrite, args.v)

    if(args.save):
        scraper.save("output.csv")

main()
