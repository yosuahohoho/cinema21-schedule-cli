# Cineplex 21 ver 1.1

import urllib2
from bs4 import BeautifulSoup
import time



def download(url, user_agent='lilstallion', num_retries=2):
	
	headers = {'User-agent': user_agent}
	request = urllib2.Request(url, headers=headers)
	try:
		html = urllib2.urlopen(request).read()
	except urllib2.URLError as e:
		print 'Download Error:', e.reason
		html = None
		if num_retries > 0:
			if hasattr(e, 'code') and 500 <= e.code < 600:
				# retry 5XX HTTP errors
				return download(url, user_agent, num_retries-1)
		
	return html
	
def retrieve_data_XXI():
	data = soup.find("div", {"class":"col-m_462"}).findAll("div")
	theater = data[0].get_text()
	info = data[1].get_text()
	
	print theater
	print info
	print
	
	html = soup.find("div", {"id":"makan"}).findAll("tr", {"class":["light", "dark"]})
	
	for tag in html:
		# Retrieve image url
		a = tag.find_all('a')
		img = a[0].find('img').get('src')
		
		print img
		
		# Retrieve film titles
		a = tag.find_all('a')
		titles = a[1].get_text()
		print titles
		
		# Retrieve film schedules
		div = tag.find_all('div')
		td = tag.find_all('td')

		if div:
			schedules = div[0].get_text()
		else:
			schedules = td[1].get_text()
			
		print schedules
		print
		time.sleep(1)
		
def retrieve_night_show():
	html = soup.find("div", {"id":"makan"}).find_next_sibling('div', {'id':'makan'}).findAll("tr", {"class":["light", "dark"]})
	
	if html:
	    for tag in html:
		    # Retrieve image url
		    a = tag.find_all('a')
		    img = a[0].find('img').get('src')
		
		    print img
		
		    # Retrieve film titles
		    a = tag.find_all('a')
		    titles = a[1].get_text()
		    print titles
		
		    # Retrieve film schedules
		    div = tag.find_all('div')
		    td = tag.find_all('td')

		    if div:
			    schedules = div[0].get_text()
		    else:
			    schedules = td[1].get_text()
			
		    print schedules
		    print
	else:
		print "Tidak ada jadwal lewat dari pukul 22.00"


# URL data	
cinema21_url = {
				"tangcity": "http://www.21cineplex.com/theater/bioskop-tang-city-xxi,363,TGRTACI.htm",
				"balekota": "http://www.21cineplex.com/theater/bioskop-bale-kota-xxi,341,TGRBAKO.htm",
				"livingworld": "http://www.21cineplex.com/theater/bioskop-living-world-xxi,309,TGRLIWO.htm",
				"alamsutera": "http://www.21cineplex.com/theater/bioskop-alam-sutera-xxi,327,TGRALSU.htm",
				"supermallkarawaci": "http://www.21cineplex.com/theater/bioskop-supermal-karawaci-xxi,122,TGRKARA.htm",
				"smsserpong": "http://www.21cineplex.com/theater/bioskop-summarecon-mal-serpong-xxi,256,TGRSERO.htm",
				"aeon": "http://www.21cineplex.com/theater/bioskop-aeon-mall-bsd-city-xxi,378,TGRAEBS.htm",
				"cbdciledug": "http://www.21cineplex.com/theater/bioskop-cbd-ciledug-xxi,291,TGRCBCI.htm",
				}
				
# Display XXI Theaters in Tangerang
print "Theater XXI yang tersedia di Kota Tangerang:"
print
print " Balekota	Living World	Supermall Karawaci	AEON"
print " Tangcity	Alam Sutera	SMS Serpong		CBD Ciledug"
print
print "Type 'quit' to quit"
print "#######################################"

# Get time
day = time.strftime("%a", time.gmtime())
print day

# Main Loop
while True:
	print
	user_input = raw_input("Enter Theater Name: ")
	formated_input = user_input.lower().replace(" ", "")
	if user_input.lower() == 'quit':
		break
	elif formated_input in cinema21_url:
		url = cinema21_url[formated_input]
		theater = '%s XXI  %s' % (user_input.title(), time)
		print theater
		print
		
		# Main program
		html = download(url)
		soup = BeautifulSoup(html, 'html.parser')
		retrieve_data_XXI()
		
		if day == 'sat' or day == 'sun':
			retrieve_night_show()
		
		print "#######################################"
	else:
		print "Theater yang anda cari tidak ditemukan, mohon lihat daftar theater yang tersedia di atas .."
		continue
	


