

class References:
	def __init__(self):
		# 0-> Elementary, 1 -> Middle 2-> High 3 -> University
		self.gradeLevel = [False, False, False, False]
		self.name = ''

def extractInfo(url,baseUrl,soup):
	# Assuming there will be no info in the baseUrl
	if(url == baseUrl):
		return None
	if(baseUrl == 'http://doer.metastudio.org/phet/en/simulations.html'):
		return extractForPhet(soup)


def extractForPhet(soup):
	ref = References()
	ref.name = soup.find('title').string
	elem = soup.find('a',{'id': 'nav-location-nav-elementary-school'})
	if(elem and elem.span['class'] == [u'nml-link-label', u'selected']):
		ref.gradeLevel[0] = True
	middle = soup.find('a',{'id': 'nav-location-nav-middle-school'})
	if(middle and middle.span['class'] == [u'nml-link-label', u'selected'] ):
		ref.gradeLevel[1] = True
	high = soup.find('a',{'id': 'nav-location-nav-high-school'})
	if(high and high.span['class'] == [u'nml-link-label', u'selected']):
		ref.gradeLevel[2] = True
	university = soup.find('a',{'id': 'nav-location-nav-university'})	
	if(university and university.span['class'] == [u'nml-link-label', u'selected']):
		ref.gradeLevel[3] = True

	print ref.name + '\n'
	print ref.gradeLevel
	print '\n'
	return ref
	

