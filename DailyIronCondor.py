from kivy.config import Config
Config.set('kivy', 'keyboard_mode', 'systemanddock')
Config.set('graphics', 'width', '300')
Config.set('graphics', 'height', '600')
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
import sys
import json
import logging
import datetime
import statistics
from time import sleep
from dateutil import parser
from datetime import datetime
from alice_blue import *
from nsepython import * 

from kivy.uix.image import Image
from kivy.uix.image import AsyncImage
from kivy.config import Config  
# 0 being off 1 being on as in true / false
# you can use 0 or 1 && True or False
#Config.set('graphics', 'resizable', True)
#Config.set('graphics', 'width', '200')
#Config.set('graphics', 'height', '500') 

class MainApp(App):
	def build(self):
		self.title = "Let Money Earn's Daily IC"
		self.image="http://3.bp.blogspot.com/-ruWtVjCLxME/W3GjsF3750I/AAAAAAAAGBQ/GlsSCEfvJGwIwEIpm--ADSG8d3ElOIRmgCK4BGAYYCw/s1600/logo2.png"
		self.img = AsyncImage(source =self.image)
		self.img.allow_stretch = True
		self.img.keep_ratio = True
		self.img.size_hint_x = 1
		self.img.size_hint_y = .15
		self.img.pos = (2, 1)
		self.img.opacity = 1
		
		self.username = '180970'
		self.password = 'cgpb35621'
		self.twoFA =  'pune'
		self.app_id =  'qhdk1iuZ22'
		self.api_secret =  'Apx9BBmlaZyOVtXU0La4rcFLsaPHOSrSrKibtW1OEJexQpZTvgo2LgxE0Vm8bx0M'
		self.StartTime=1930
		self.Index='BANKNIFTY'
		self.LotSize=25
		self.TargetOptionPrice=30
		self.TargetOptionBuyPrice=5
		self.Lot=2
		self.SL=2
		
		
		self.PutToShort=0
		self.PutToLong=0
		self.CallToShort=0
		self.CallToLong=0
		self.PeStrike=0
		self.CeStrike=0
		
		main_layout = BoxLayout(orientation="vertical")
		main_layout.add_widget(self.img)
		self.solution = TextInput(
            multiline=False, readonly=True, halign="left", font_size=12,
			background_color= "#AED581",
			
			
        )
		main_layout.add_widget(self.solution)	
		self.socket_opened = False
		self.alice = None
		self.units = 0
		btn = Button(text ="Let's Trade!",
                   font_size ="10sp",
                   background_color =(1, 1, 1, 1),
                   color =(1, 1, 1, 1),
                   size =(12, 12),
                   size_hint =(1, .2),
                   pos =(300, 250))
 
        # bind() use to bind the button to function LogintoAliceBlue
		btn.bind(on_press = self.Daily_Short_straddle)
		main_layout.add_widget(btn)
		access_token = AliceBlue.login_and_get_access_token(username = self.username, password = self.password, twoFA = self.twoFA,
															redirect_url='https://ant.aliceblueonline.com/plugin/callback',
															app_id = self.app_id,
															api_secret = self.api_secret)
															
		self.alice = AliceBlue(username = self.username, password = self.password, access_token = access_token)			
		self.socket_opened = False			
		self.solution.text= self.solution.text+"Wellcome to Let Money Earn's Daily IC	"+str(time.time())+'\n'
		self.solution.text= self.solution.text+"--------------------------------'"+'\n'
		self.solution.text= self.solution.text+"'Logged In to AliceBlue!'"+'\n'
		self.solution.text= self.solution.text+"NIFTY tarding at :"+str(nse_quote_ltp('NIFTY'))+'\n'
		self.solution.text= self.solution.text+"BANKNIFTY tarding at :"+str(nse_quote_ltp('BANKNIFTY'))+'\n'
		
		return main_layout
		
		
	def LogintoAliceBlue(self, event):
		Daily_Short_straddle()
		
		 
	def running_status():
		
		todays_date=datetime.date.today().strftime('%d-%b-%Y')

		if(str(nse_holidays('trading')).find(todays_date))>0 :
			print('Chill!!!! Today is holidays ...')
			sys.exit()

		if(datetime.date.today().strftime("%A")=='Sunday'):
			print('Chill!!!! it is Sunday...')
			sys.exit()
			
		if(datetime.date.today().strftime("%A")=='Saturday'):
			print('Chill!!!! it is Saturday...')
			sys.exit()
		
		start_now=datetime.datetime.now().replace(hour=9, minute=15, second=0, microsecond=0)
		end_now=datetime.datetime.now().replace(hour=15, minute=30, second=0, microsecond=0)
		if start_now<datetime.datetime.now()<end_now:
			print('Welcome : Let Money Earn!')
		else:
			print('Market is closed...')
			sys.exit()

	
	def SampleCode():
		print(alice.get_daywise_positions()) # get daywise positions
		bn_call = alice.get_instrument_for_fno(symbol = 'BANKNIFTY', expiry_date=datetime.date(2019, 6, 27), is_fut=False, strike=30000, is_CE = True)
		bn_put = alice.get_instrument_for_fno(symbol = 'BANKNIFTY', expiry_date=datetime.date(2019, 6, 27), is_fut=False, strike=30000, is_CE = False)
		print(nse_quote_ltp("BANKNIFTY","09-Sep-2021","PE",35000))
		print(nse_quote_ltp("BANKNIFTY",currentExpiryDate.replace(" ", "-"),"PE",35000))
		#print(alice.get_instrument_by_token('NFO','53907'))		
		#print(alice.get_instrument_by_token('NFO','37764'))
		#print(alice.get_instrument_by_symbol('NFO', 'NIFTY 09 SEP2021 17500.0 CE'))
		#print(alice.get_instrument_by_symbol('NFO', 'BANKNIFTY 09 SEP21 39500.0 CE'))	
		#print(alice.get_instrument_by_symbol('NFO', 'BANKNIFTY OCT 32800.0 PE'))
		print(
		   alice.place_order(transaction_type = TransactionType.Buy,
							 instrument = alice.get_instrument_by_symbol('NSE', 'INFY'),
							 quantity = 1,
							 order_type = OrderType.StopLossMarket,
							 product_type = ProductType.Delivery,
							 price = 8.0,
							 trigger_price = 8.0,
							 stop_loss = None,
							 square_off = None,
							 trailing_sl = None,
							 is_amo = False)
		)

	#Get the Index Level
	#Get ATM Level
	#Login to AliceBlue
	#Sell CE/PE
	#Put SL
	#Change the SL in while Loop

	def Daily_Short_straddle(self, event):
		self.solution.text= self.solution.text+"Getting Strikes to Trade"+"\n"
		Index=self.Index
		Lot=self.Lot
		LotSize=self.LotSize
		TargetOptionPrice=self.TargetOptionPrice
		TargetOptionBuyPrice=self.TargetOptionBuyPrice
		PeStrike=0
		CeStrike=0
		payload=nse_optionchain_scrapper(Index)
		currentExpiry,dte=nse_expirydetails(payload,0)
		self.solution.text= self.solution.text+str(currentExpiry)+"\n"
		currentExpiryDate=currentExpiry.strftime("%d")+" "+currentExpiry.strftime("%b")+" "+str(int(currentExpiry.strftime("%Y")))
		
		currentExpiry=currentExpiry.strftime("%d")+" "+currentExpiry.strftime("%b")+str(int(int(currentExpiry.strftime("%Y")) - round(int(currentExpiry.strftime("%Y"))/1000,0)*1000))
		self.solution.text= self.solution.text+("We Will Trade for :"+ currentExpiryDate)+"\n"
		payload=nse_optionchain_scrapper('BANKNIFTY')
		
		
		for x in range(30):
			x = round(nse_quote_ltp(Index)/100, 0)*100-x*100
			PEltp=nse_optionchain_ltp(payload,x,"PE",0,"sell")
			PeStrike=PeStrike+1
			if PEltp>TargetOptionPrice:
				self.PutToShort=x
			else:
				break
		self.solution.text= self.solution.text+"Put Strike To Short : "+str(self.PutToShort)+ "	LTP:"+str(PEltp)+"\n"
		for x in range(30):
			x = round(nse_quote_ltp(Index)/100, 0)*100+x*100
			PEltp=nse_optionchain_ltp(payload,x,"CE",0,"sell")
			CeStrike=CeStrike+1
			if PEltp>TargetOptionPrice:
				self.CallToShort=x
			else:
				break
		self.solution.text= self.solution.text+"Call Strike To Short : "+str(self.CallToShort)+ "	LTP:"+str(PEltp)+"\n"
		for x in range(PeStrike-1,50):
			x = round(nse_quote_ltp(Index)/100, 0)*100-x*100
			PEltp=nse_optionchain_ltp(payload,x,"PE",0,"sell")
			if PEltp<TargetOptionBuyPrice:
				self.PutToLong=x
				break
		self.solution.text= self.solution.text+"Put Strike To Long : "+str(self.PutToLong)+ "	LTP:"+str(PEltp)+"\n"		
		for x in range(CeStrike-1,50):
			x = round(nse_quote_ltp(Index)/100, 0)*100+x*100
			PEltp=nse_optionchain_ltp(payload,x,"CE",0,"sell")
			if PEltp<TargetOptionBuyPrice:
				self.CallToLong=x
				break	
		self.solution.text= self.solution.text+"Call Strike To Long : "+str(self.CallToLong)+ "	LTP:"+str(PEltp)+"\n"						
		start_time = time.time()
		self.solution.text= self.solution.text+('Placing Buy Order for Call '+str(self.CallToLong)+' CE')+"\n"
		self.alice.place_order(transaction_type=TransactionType.Buy,
								instrument=self.alice.get_instrument_by_symbol('NFO', Index+' '+currentExpiry.upper()+' '+str(self.CallToLong)+' CE'),
								quantity=Lot*LotSize,
								order_type=OrderType.Market,
								product_type=ProductType.Intraday,
								price=0.0,
								trigger_price=None,
								stop_loss=None,
								square_off=None,
								trailing_sl=None,
								is_amo=False)
		self.solution.text= self.solution.text+('Placing Buy Order for PUT '+str(self.PutToLong)+' PE')+"\n"
		self.alice.place_order(transaction_type = TransactionType.Buy,
								instrument = self.alice.get_instrument_by_symbol('NFO', Index+' '+currentExpiry.upper()+' '+str(self.PutToLong)+' PE'),
								quantity = Lot*LotSize,
								order_type=OrderType.Market,
								product_type=ProductType.Intraday,
								price=0.0,
								trigger_price=None,
								stop_loss=None,
								square_off=None,
								trailing_sl=None,
								is_amo=False)
		self.solution.text= self.solution.text+('Placing SELL Order for CALL '+str(self.CallToShort)+' CE')+"\n"						
		self.alice.place_order(transaction_type=TransactionType.Sell,
								instrument=self.alice.get_instrument_by_symbol('NFO', Index+' '+currentExpiry.upper()+' '+str(self.CallToShort)+' CE'),
								quantity=Lot*LotSize,
								order_type=OrderType.Market,
								product_type=ProductType.Intraday,
								price=0.0,
								trigger_price=None,
								stop_loss=None,
								square_off=None,
								trailing_sl=None,
								is_amo=False)
		self.solution.text= self.solution.text+('Placing SELL Order for PUT '+str(self.PutToShort)+' PE')+"\n"
		self.alice.place_order(transaction_type = TransactionType.Sell,
								instrument = self.alice.get_instrument_by_symbol('NFO', Index+' '+currentExpiry.upper()+' '+str(self.PutToShort)+' PE'),
								quantity = Lot*LotSize,
								order_type=OrderType.Market,
								product_type=ProductType.Intraday,
								price=0.0,
								trigger_price=None,
								stop_loss=None,
								square_off=None,
								trailing_sl=None,
								is_amo=False)
		#alice.subscribe(index_call,index_put, LiveFeedType.COMPACT)
		self.solution.text= self.solution.text+('Placing SLM Order for CALL '+str(self.CallToShort)+' CE')+"\n"
		self.alice.place_order(transaction_type = TransactionType.Buy,
						instrument = self.alice.get_instrument_by_symbol('NFO', Index+' '+currentExpiry.upper()+' '+str(self.CallToShort)+' CE'),
						quantity = LotSize*Lot,
						order_type = OrderType.StopLossMarket,
						product_type = ProductType.Delivery,
						price = round(nse_quote_ltp(Index,currentExpiryDate.replace(" ", "-"),"CE",self.CallToShort)*SL/0.05,0)*0.05,
						trigger_price = round(nse_quote_ltp(Index,currentExpiryDate.replace(" ", "-"),"CE",self.CallToShort)*SL/0.05,0)*0.05,
						stop_loss = None,square_off = None,trailing_sl = None, is_amo = False)
		self.solution.text= self.solution.text+('Placing SLM Order for PUT '+str(self.PutToShort)+' PE')+"\n"
		self.alice.place_order(transaction_type =  TransactionType.Buy,
						instrument = self.alice.get_instrument_by_symbol('NFO', Index+' '+currentExpiry.upper()+' '+str(self.PutToShort)+' PE'),
						quantity = Lot*LotSize,
						order_type = OrderType.StopLossMarket,
						product_type = ProductType.Delivery,
						price = round(nse_quote_ltp(Index,currentExpiryDate.replace(" ", "-"),"PE",self.PutToShort)*SL/0.05,0)*0.05,
						trigger_price = round(nse_quote_ltp(Index,currentExpiryDate.replace(" ", "-"),"PE",self.PutToShort)*SL/0.05,0)*0.05,
						stop_loss = None,square_off = None,trailing_sl = None, is_amo = False)
		self.solution.text= self.solution.text+("Time Taken--- %s seconds ---" % (time.time() - start_time))+"\n"

if __name__ == "__main__":
	
    app = MainApp()
    app.run()
