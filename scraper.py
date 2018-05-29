import urllib2
from bs4 import BeautifulSoup
from parser import parseLinks
from extract import extractInfo

def scrap(baseUrl):

	traverseList = []
	base = baseUrl
	traverseList.insert(0,base)
	limit = 40
	count = 0

	while(traverseList):

		url = traverseList.pop()
		# print url
		if(not url):
			continue

		try:
			response = urllib2.urlopen(url)
		except urllib2.URLError:
			print 'URLError with URL ' + url + '\n'
			continue 

		try:
			webContent = response.read()
		except:
			continue

		soup = BeautifulSoup(webContent,'html.parser')
		aRefs = parseLinks(soup,url,baseUrl)
		info =	extractInfo(url,baseUrl,soup)

		if(not aRefs):
			continue

		# Add more pages to visit here.
		for tag in aRefs:
			# print tag['href']
			# print '\n'

			try:
				traverseList.append('http://doer.metastudio.org/phet/en/'+tag['href'])
			except KeyError:
				print 'href tag does not exist'

		print 'Checked url ' + url
		count += 1

	print 'Successfully completed scraping base url' + base + '\n'


def appendProtocol(url):
	if(url[0:4] == 'http' or url[0:5] == 'https'):
		return ''
	else:
		return 'http:'
