#!/usr/bin/python3
import sys
import pandas as pd

def main(PATH):
	'''
	Convert a Bitwarden password.csv to a Dashlane password.csv

		Usage:
			converter.py /Path/To/bitwarden_export.csv

		Args:
			PATH: Path of the bitwarden_export.csv file

		Returns:
			A dashlane_password.csv file in the Dashlane format

	!! Be carefull to delete all .csv file after usage !!
	'''
	try:
		data = pd.read_csv(PATH)
	except:
		print('something bad occured')
		return


	try:
		data = data[data.type == 'login']
	except:
		print('something bad occured')
		return

	try:
		data = data.drop(['folder','favorite','type','notes','fields','login_totp','reprompt'], axis=1)
	except:
		print('something bad occured')
		return

	data = data.rename(columns= {'login_uri':'url','login_username':'username','login_password':'password'})

	data.to_csv('dashlane_password.csv',index=False)
	print('done')

if __name__ == '__main__':
	try:
		PATH = str(sys.argv[1])
		print(PATH)
		if PATH[-4:] == '.csv':
			main(PATH)
	except:
		print(main.__doc__)
		pass



