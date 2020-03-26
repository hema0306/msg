import pandas as pd
import sys
import json


class PandasData:

	def __init__(self, user_response):

		self.user_response = user_response

	def to_csv_data(self, user_response):
		df = pd.DataFrame(data = [user_response]).T
		print(df)
		result_data = df.to_csv('data.csv')
		return result_data

	# def to_json_data(self, data):
	# 	json_data = pd.DataFrame(data = [user_response]).T
	# 	print(json_data)
	# 	result_data = data.to_json('data.json')
	# 	return result_data

	def convert_json(self,user_response):
		convert_data = json.dumps(user_response, indent=1)
		with open('data.json', "w") as f:
			f.write(convert_data)

	def get_data(self, user_response):
		csv_data = self.to_csv_data(user_response)
		# json_data = self.to_json_data(user_response)
		json_file = self.convert_json(user_response)

if __name__ == '__main__':

	user_response = input("Enter the data: ")

	class_obj = PandasData(user_response)
	class_obj.get_data(user_response)
