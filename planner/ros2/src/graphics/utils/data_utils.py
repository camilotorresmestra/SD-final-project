import gspread
import datetime
import csv
import os

class GSheetReader():
    def __init__(self):
        # Change to load with g_auth
        self._auth_filename = '/workspace/planner/creds/caramel-logic-295802-ca4ef81bcc62.json'
        self.gc = gspread.service_account(filename=self._auth_filename)
        self.worksheetName = "SD_final_project"
        self.wks = self.gc.open(self.worksheetName).sheet1
        self.index = 2
    # id (different than routine_id), date, time, routine_id, total_distance, total_time
    def write_row(self,routine_id, total_distance, total_time):
        now = datetime.now()
        self.wks.update_cell(self.index,1,self.index)
        self.wks.update_cell(self.index,2,str(now.date()))
        self.wks.update_cell(self.index,3,str(now.time()))
        self.wks.update_cell(self.index,4,routine_id)
        self.wks.update_cell(self.index,5,total_distance)
        self.wks.update_cell(self.index,6,total_time)
        self.index += 1

    def download_sheet(self):
        filename = self.worksheetName + '.csv'
        with open(filename, 'w') as f:
            writer = csv.writer(f)
            writer.writerows(self.wks.get_all_values())

def main():
    # Create a GSheetReader instance and download the file to the defined folder
    GSheetReader().download_sheet()

if __name__ == "__main__":
    main()
