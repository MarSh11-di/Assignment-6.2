import csv
from convertor import temperature as temp

def rider_file(file_str:str, target_temp:str):
   with open(file_str,"r") as file:
      readers = csv.DictReader(file)
      temp_list =[]
      for row in readers:
         if target_temp not in row['Reading']:
            number = int(row['Reading'][:-3])
            if target_temp == "C":
               converted_temp = str(temp.conver_to_celsius(number))+"Â°C"
            elif target_temp == "F":
               converted_temp = str(temp.convert_to_fahrenheit(number))+"Â°F"
            else:
               print("Target temperature is incorrect")
               break
            temp_list.append({"Date": row["Date"], 'Reading':converted_temp})
         else:
            temp_list.append({"Date": row["Date"], 'Reading':row["Reading"]})    
   with open(file_str, "w", newline="") as file:
      header =["Date","Reading"]
      writer = csv.DictWriter(file, fieldnames=header)
      writer.writeheader()
      for row in temp_list:
         writer.writerow(row)
rider_file("data_temper.csv","C")   

