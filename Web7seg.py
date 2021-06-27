import webiopi

GPIO = webiopi.GPIO

LED1PIN = 21
LED2PIN = 22
LED3PIN = 23
LED4PIN = 24
LED5PIN = 25
LED6PIN = 26
LED7PIN = 27

def setup():
	GPIO.setFunction( LED1PIN, GPIO.OUT )
	GPIO.setFunction( LED2PIN, GPIO.OUT )
	GPIO.setFunction( LED3PIN, GPIO.OUT )
	GPIO.setFunction( LED4PIN, GPIO.OUT )
	GPIO.setFunction( LED5PIN, GPIO.OUT )
	GPIO.setFunction( LED6PIN, GPIO.OUT )
	GPIO.setFunction( LED7PIN, GPIO.OUT )

@webiopi.macro
def ChangeLedActive( led, active ):
	if 0 == int(led):
		GPIO.digitalWrite( LED1PIN, True )
		GPIO.digitalWrite( LED2PIN, True )
		GPIO.digitalWrite( LED3PIN, True )
		GPIO.digitalWrite( LED4PIN, True )
		GPIO.digitalWrite( LED5PIN, True )
		GPIO.digitalWrite( LED6PIN, True )
		GPIO.digitalWrite( LED7PIN, False )
	if 1 == int(led):
		GPIO.digitalWrite( LED1PIN, False )
		GPIO.digitalWrite( LED2PIN, True )
		GPIO.digitalWrite( LED3PIN, True )
		GPIO.digitalWrite( LED4PIN, False )
		GPIO.digitalWrite( LED5PIN, False )
		GPIO.digitalWrite( LED6PIN, False )
		GPIO.digitalWrite( LED7PIN, False )
	if 2 == int(led):
		GPIO.digitalWrite( LED1PIN, True )
		GPIO.digitalWrite( LED2PIN, True )
		GPIO.digitalWrite( LED3PIN, False )
		GPIO.digitalWrite( LED4PIN, True )
		GPIO.digitalWrite( LED5PIN, True )
		GPIO.digitalWrite( LED6PIN, False )
		GPIO.digitalWrite( LED7PIN, True )
	if 3 == int(led):
		GPIO.digitalWrite( LED1PIN, True )
		GPIO.digitalWrite( LED2PIN, True )
		GPIO.digitalWrite( LED3PIN, True )
		GPIO.digitalWrite( LED4PIN, True )
		GPIO.digitalWrite( LED5PIN, False )
		GPIO.digitalWrite( LED6PIN, False )
		GPIO.digitalWrite( LED7PIN, True )
	if 4 == int(led):
		GPIO.digitalWrite( LED1PIN, False )
		GPIO.digitalWrite( LED2PIN, True )
		GPIO.digitalWrite( LED3PIN, True )
		GPIO.digitalWrite( LED4PIN, False )
		GPIO.digitalWrite( LED5PIN, False )
		GPIO.digitalWrite( LED6PIN, True )
		GPIO.digitalWrite( LED7PIN, True )
	if 5 == int(led):
		GPIO.digitalWrite( LED1PIN, True )
		GPIO.digitalWrite( LED2PIN, False )
		GPIO.digitalWrite( LED3PIN, True )
		GPIO.digitalWrite( LED4PIN, True )
		GPIO.digitalWrite( LED5PIN, False )
		GPIO.digitalWrite( LED6PIN, True )
		GPIO.digitalWrite( LED7PIN, True )
	if 6 == int(led):
		GPIO.digitalWrite( LED1PIN, True )
		GPIO.digitalWrite( LED2PIN, False )
		GPIO.digitalWrite( LED3PIN, True )
		GPIO.digitalWrite( LED4PIN, True )
		GPIO.digitalWrite( LED5PIN, True )
		GPIO.digitalWrite( LED6PIN, True )
		GPIO.digitalWrite( LED7PIN, True )
	if 7 == int(led):
		GPIO.digitalWrite( LED1PIN, True )
		GPIO.digitalWrite( LED2PIN, True )
		GPIO.digitalWrite( LED3PIN, True )
		GPIO.digitalWrite( LED4PIN, False )
		GPIO.digitalWrite( LED5PIN, False )
		GPIO.digitalWrite( LED6PIN, False )
		GPIO.digitalWrite( LED7PIN, False )
	if 8 == int(led):
		GPIO.digitalWrite( LED1PIN, True )
		GPIO.digitalWrite( LED2PIN, True )
		GPIO.digitalWrite( LED3PIN, True )
		GPIO.digitalWrite( LED4PIN, True )
		GPIO.digitalWrite( LED5PIN, True )
		GPIO.digitalWrite( LED6PIN, True )
		GPIO.digitalWrite( LED7PIN, True )
	if 9 == int(led):
		GPIO.digitalWrite( LED1PIN, True )
		GPIO.digitalWrite( LED2PIN, True )
		GPIO.digitalWrite( LED3PIN, True )
		GPIO.digitalWrite( LED4PIN, True )
		GPIO.digitalWrite( LED5PIN, False )
		GPIO.digitalWrite( LED6PIN, True )
		GPIO.digitalWrite( LED7PIN, True )
