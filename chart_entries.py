import billboard
import sys
import json
import time
import datetime
import csv


class ChartData:

    def __init__(self, chart_name_list, start_date, end_date):

        self.chart_name_list = chart_name_list
        self.start_date = start_date
        self.end_date = end_date

    def parse_data(self,chart_data, chart_name):

        chart_data_dict = {}
        chart_data_dict['chart_name'] = chart_name
        chart_content_list = []
        for line in chart_data:
            chart_content = {}
            if chart_name == 'hot-100':
                chart_content['title'] = line.title
                chart_content['artist'] = line.artist
            else:
                chart_content['artist'] = line.artist
            chart_content_list.append(chart_content)
        chart_data_dict['data'] = chart_content_list
        return chart_data_dict  

    def csv_data(self, chart_data,chart_name):

        csv_list = []
        for line in chart_data:
            if chart_name == 'hot-100':
                line_string = [line.title , line.artist]
            else:
                line_string = [line.artist]
            csv_list.append(line_string)
        return csv_list

    def write_to_json_file(self,file_name, parsed_data):

        json_data = json.dumps(parsed_data, indent = 3)
        with open(file_name, "w") as f:
            f.write(json_data)

    def write_to_csv_file(self, file_name, chart_name, parsed_data):

        if chart_name == 'hot-100':
            file_titles = ['Title', 'Artist']
        else:
            file_titles = ['Artist']
        with open(file_name, 'w') as file:
            writer = csv.DictWriter(file, fieldnames = file_titles)
            writer.writeheader()    
            writer = csv.writer(file)
            writer.writerows(parsed_data)

    def get_data(self):

        st_dt = datetime.datetime.strptime(self.start_date, '%Y-%m-%d')
        ed_dt = datetime.datetime.strptime(self.end_date, '%Y-%m-%d')

        if st_dt > ed_dt:
            print("Start date should not be greater than end date")
            sys.exit()

        calculated_days = ed_dt - st_dt
        diff_days = calculated_days.days
        if diff_days > 30:
            print("Days should not exceed more than 30")
            sys.exit()

        for chart_name in self.chart_name_list:
            current_dt = st_dt
            for date in range(diff_days):
                formatted_dt = datetime.datetime.strftime(current_dt, '%Y-%m-%d')
                chart_data = billboard.ChartData(chart_name, formatted_dt)
                parsed_data = self.parse_data(chart_data,chart_name)
                file_name = '/var/www/msg/api/billboard-charts/source/' + chart_name + '_' + self.start_date + '_' + self.end_date + '_' + str(time.time()) + '.json'
                self.write_to_json_file(file_name, parsed_data)
                parsed_data_csv = self.csv_data(chart_data,chart_name)
                file_name = '/var/www/msg/api/billboard-charts/source/' + chart_name + '_' + self.start_date + '_' + self.end_date + '_' + str(time.time()) + '.csv'
                self.write_to_csv_file(file_name, chart_name, parsed_data_csv)
                current_dt = current_dt + datetime.timedelta(days=1)

if __name__ == '__main__':

    if len(sys.argv) != 4:
        print("Check your arguments")
        print("eg: python chart_entries.py <chart_name_list> <start_date> <end_date>")
        sys.exit()

    chart_name_list = sys.argv[1].split(',')
    start_date = sys.argv[2]
    end_date = sys.argv[3]
    chart_data_obj = ChartData(chart_name_list,start_date,end_date)
    chart_data_obj.get_data()
