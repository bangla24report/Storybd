#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

def Google(url):
	#Google
	re1 = "http://googleads.g.doubleclick.net/aclk?sa=L&ai=CWEQH6Q73UqW9CMvMigfdiIGoB9rlksIEAAAQASAAUO7kr-b8_____wFgvwWCARdjYS1wdWItMDQ2NjU4MjEwOTU2NjUzMsgBBOACAKgDAaoEggFP0E-9agyjXkIfjOxmtpPE76hNCBn1in_meKMn53O-8ZFlbxWDgYdaVZQKJza8mIRXw22hWIVMAOJJzq-S6AipWHe9iVZCAAlcHj-gT2B33tD9a2oQrZ61S3-WFh_8T8RFUFnC_PRC35CTFbueQrUYjC-j6ncVXzt_IPXugo5vE-3x4AQBoAYV&num=0&sig=AOD64_2petJH0A9Zjj45GN117ocBukiroA&client=ca-pub-0466582109566532&adurl="+url
	re2 = "http://googleads.g.doubleclick.net/aclk?sa=L&ai=C-RHnNvn2Uom8LeTaigfjkIHICfLQnccEAAAQASAAUNTx5Pf4_____wFgvwWCARdjYS1wdWItMDQ2NjU4MjEwOTU2NjUzMsgBBOACAKgDAaoEhQFP0LHofgVzg8U9Bvwu2_hN9Ow0n2tBH9xjKtngqcF6hgGQpxV6QzMgNxx0_UawPG3-UD097GLLCirbVMl2QxQqa04U3cp4YFgV5dshYbzmqlVVfNn-NuunzLNab6ATE5BUwQ9bgXBOW_qEz8qgbwVOvUJrn1IzL-ymANaKsQLZ9POlkbIe4AQBoAYV&num=0&sig=AOD64_3a3m_P_9GRVFc6UIGvnornMcLMoQ&client=ca-pub-0466582109566532&adurl="+ url
	redirects =[re1,re2]
	guardar(redirects)
def Google2(url):	
	#Google2
	re3 = "https://www.google.com/accounts/ServiceLogin?continue=http://googleads.g.doubleclick.net/aclk?sa=L&ai=CtHoIVxn3UvjLOYGKiAeelIHIBfLQnccEAAAQASAAUNTx5Pf4_____wFgvwWCARdjYS1wdWItMDQ2NjU4MjEwOTU2NjUzMsgBBOACAKgDAaoE5AFP0NHr5cHwFmWgKNs6HNTPVk7TWSV-CDHX83dKdGSWJ2ADoZNIxUHZwjAODRyDY_7nVtpuqSLOTef4xzVxDQ2U22MNbGak33Ur7i2jDB8LdYt9TbC3ifsXmklY5jl3Zpq4_lP7wagVfjt0--tNPPGTR96NGbxgPvfHMq9ZsTXpjhc_lPlnyGjlWzF8yn437iaxhGRwYLt_CymifLO2YaJPkCm9nLpONtUM-mstUSpKQrP2VjjaZkbDtuK0naLLBV37aYEY4TzWQi8fQGN47z4XgpinBCna91zQayZjn2wxccDCl0zgBAGgBhU&num=0&sig=AOD64_3Qi4qG3CRVHRI5AHSkSGuL7HJqSA&client=ca-pub-0466582109566532&adurl="+ url +"/essaybeans/reflections/solitude.html"
	re4 = "https://accounts.google.com/accounts/SetSID?ssdc=1&sidt=*&continue=http://googleads.g.doubleclick.net/aclk?sa=L&ai=CtHoIVxn3UvjLOYGKiAeelIHIBfLQnccEAAAQASAAUNTx5Pf4_____wFgvwWCARdjYS1wdWItMDQ2NjU4MjEwOTU2NjUzMsgBBOACAKgDAaoE5AFP0NHr5cHwFmWgKNs6HNTPVk7TWSV-CDHX83dKdGSWJ2ADoZNIxUHZwjAODRyDY_7nVtpuqSLOTef4xzVxDQ2U22MNbGak33Ur7i2jDB8LdYt9TbC3ifsXmklY5jl3Zpq4_lP7wagVfjt0--tNPPGTR96NGbxgPvfHMq9ZsTXpjhc_lPlnyGjlWzF8yn437iaxhGRwYLt_CymifLO2YaJPkCm9nLpONtUM-mstUSpKQrP2VjjaZkbDtuK0naLLBV37aYEY4TzWQi8fQGN47z4XgpinBCna91zQayZjn2wxccDCl0zgBAGgBhU&num=0&sig=AOD64_3Qi4qG3CRVHRI5AHSkSGuL7HJqSA&client=ca-pub-0466582109566532&adurl=" + url
	redirects =[re3,re4]
	guardar(redirects)
def Google3(url):	
	#Google3
	re5 = "http://cm.g.doubleclick.net/pixel?google_nid=rfi&google_cm&google_sc&google_hm=Njk4NjIwODk1OTI4NzkxMzM3&forward="+ url
	re6 = "http://cm.g.doubleclick.net/pixel?google_nid=rfi&google_cm&google_sc&google_hm=Njk4NjIwODk1ODY0NDM1NzM2&forward="+ url
	redirects =[re5,re6]
	guardar(redirects)
def Google4(url):	
	#Google4
	re7 = "https://www.google.com/accounts/Logout?service=wise&continue=http://googleads.g.doubleclick.ne/aclk?sa=L&ai=CtHoIVxn3UvjLOYGKiAeelIHIBfLQnccEAAAQASAAUNTx5Pf4_____wFgvwWCARdjYS1wdWItMDQ2NjU4MjEwOTU2NjUzMsgBBOACAKgDAaoE5AFP0NHr5cHwFmWgKNs6HNTPVk7TWSV-CDHX83dKdGSWJ2ADoZNIxUHZwjAODRyDY_7nVtpuqSLOTef4xzVxDQ2U22MNbGak33Ur7i2jDB8LdYt9TbC3ifsXmklY5jl3Zpq4_lP7wagVfjt0--tNPPGTR96NGbxgPvfHMq9ZsTXpjhc_lPlnyGjlWzF8yn437iaxhGRwYLt_CymifLO2YaJPkCm9nLpONtUM-mstUSpKQrP2VjjaZkbDtuK0naLLBV37aYEY4TzWQi8fQGN47z4XgpinBCna91zQayZjn2wxccDCl0zgBAGgBhU&num=0&sig=AOD64_3Qi4qG3CRVHRI5AHSkSGuL7HJqSA&client=ca-pub-0466582109566532&adurl="+ url
	redirects =[re7]
	guardar(redirects)
def Ebay(url):	
	#Ebay
	re8 = "http://rover.ebay.com/rover/1/711-67261-24966-0/2?mtid=691&kwid=1&crlp=1_263602&itemid=370825182102&mpre=http://googleads.g.doubleclick.net/aclk?sa=L&ai=CÑRHnNvn2Uom8LeTaigfjkIHICfLQnccEAAAQASAAUNTx5Pf4_____wFgvwWCARdjYS1wdWItMDQ2NjU4MjEwOTU2NjUzMsgBBOACAKgDAaoEhQFP0LHofgVzg8U9Bvwu2_hN9Ow0n2tBH9xjKtngqcF6hgGQpxV6QzMgNxx0_UawPG3-UD097GLLCirbVMl2QxQqa04U3cp4YFgV5dshYbzmqlVVfNn-NuunzLNab6ATE5BUwQ9bgXBOW_qEz8qgbwVOvUJrn1IzL-ymANaKsQLZ9POlkbIe4AQBoAYV&num=0&sig=AOD64_3a3m_P_9GRVFc6UIGvnornMcLMoQ&client=ca-pub-0466582109566532&adurl=" + url
	redirects =[re8]
	guardar(redirects)
def nytimes(url):	
	#nytimes
	re9 = "http://www.nytimes.com/adx/bin/adx_click.html?type=goto&opzn&page=www.nytimes.com/pages/nyregion/index.html&pos=SFMiddle&sn2=8dfce1f6/9926f9b3&sn1=bbba504f/c0de9221&camp=CouplesResorts_1918341&ad=NYRegionSF_Feb_300x250-B5732328.10663001&goto=http://ad.doubleclick.net/ddm/clk/279541164;106630011;s?"+ url +"?-inclusive.php?utm_source=nyt&utm_medium=display&utm_content=clicktracker&utm_campaign=300x250_ExpectMore_NYT_NYRegion"
	redirects =[re9]
	guardar(redirects)
def GoogleLogout(url): 	
	#Google Redirect&logout
	re10 = "https://www.google.com/accounts/Logout?service=wise&continue=http://googleads.g.doubleclick.net/aclk?sa=L&ai=CtHoIVxn3UvjLOYGKiAeelIHIBfLQnccEAAAQASAAUNTx5Pf4_____wFgvwWCARdjYS1wdWItMDQ2NjU4MjEwOTU2NjUzMsgBBOACAKgDAaoE5AFP0NHr5cHwFmWgKNs6HNTPVk7TWSV-CDHX83dKdGSWJ2ADoZNIxUHZwjAODRyDY_7nVtpuqSLOTef4xzVxDQ2U22MNbGak33Ur7i2jDB8LdYt9TbC3ifsXmklY5jl3Zpq4_lP7wagVfjt0--tNPPGTR96NGbxgPvfHMq9ZsTXpjhc_lPlnyGjlWzF8yn437iaxhGRwYLt_CymifLO2YaJPkCm9nLpONtUM-mstUSpKQrP2VjjaZkbDtuK0naLLBV37aYEY4TzWQi8fQGN47z4XgpinBCna91zQayZjn2wxccDCl0zgBAGgBhU&num=0&sig=AOD64_3Qi4qG3CRVHRI5AHSkSGuL7HJqSA&client=ca-pub-0466582109566532&adurl="+url
	redirects =[re10]
	guardar(redirects)
def Lucky(url):	
	#"I'm Feeling Lucky"
	re11 = "https://www.google.com/#&q="+ url +"&btnI=denoqa"
	redirects =[re11]
	guardar(redirects)

def guardar(item):
	g1 = open("urls.txt",'w')
	for redirect in item:
		g1.write(redirect +"\n")
	print "Done"   	

if __name__ == "__main__":
	
	d1 = raw_input("""
	 _________________________________________________________
	|                                                         |
	| Redirect NOW                                            |
	| Select one Redirect:                                    |
	|         1- Google: 2 redirects                          | 
	|         2- Google2: 2 redirects                         |
	|         3- Google3: 2 redirects                         |
	|         4- Google4: 1 redirect                          |
	|         5- GoogleLogout: 1 redirect + logout google     |
	|         6- Ebay: 1 redirect                             |
	|         7- nytimes: 1 redirect                          |
	|         8- Lucky: 1 redirect                            | 
	|_________________________________________________________|

Write redirect number: """)

	if d1 == "1":
		d2 = raw_input("Write url: ")
		Google(d2)
	elif d1 == "2":	
		d2 = raw_input("Write url: ")
		Google2(d2)
	elif d1 == "3":
		d2 = raw_input("Write url: ")
		Google3(d2)
	elif d1 == "4":
		d2 = raw_input("Write url: ")
		Google4(d2)
	elif d1 == "5":
		d2 = raw_input("Write url: ")
		GoogleLogout(d2)
	elif d1 == "6":
		d2 = raw_input("Write url: ")
		Ebay(d2)
	elif d1 == "7":
		d2 = raw_input("Write url: ")
		nytimes(d2)
	elif d1 == "8":
		d2 = raw_input("Write url: ")
		Lucky(d2)
	else: 
		print "That's imposible"			 	
