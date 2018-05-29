from extract import extractInfo

def parseLinks(soup,url,baseUrl):
	if(url == baseUrl == 'http://doer.metastudio.org/phet/en/simulations.html'):
		return parseForPhet(soup,baseUrl)
	# Do different parsing if required
	# else:
		

def parseForPhet(soup,baseUrl):
	tags = soup.find_all('a',class_='simulation-link')
	return tags
	




	
	
