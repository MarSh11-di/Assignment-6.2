import csv
def meters (distans:int):
   return int(distans*0.3048)
def feet (distans:int):
   return int(distans*0.3048)

def convert_units(file_data:str, name_unit:str):
   with open(file_data, "r") as file:
      readers = csv.DictReader(file)
      dist_list =[]
      for row in readers:
         if name_unit == "ft":
            if name_unit not in row["Distance"]:
               number = int(row["Distance"][:-1])
               convert_num = str(feet(number))+"ft"
               dist_list.append({"Date": row["Date"],"Distance":convert_num, "Reading":row['Reading']})
            else:
               dist_list.append({"Date": row["Date"],"Distance":row["Distance"], "Reading":row['Reading']})
         elif name_unit == "m":
            if name_unit not in row["Distance"]:
               number = int(row["Distance"][:-2])
               convert_num = str(meters(number))+"m"
               dist_list.append({"Date": row["Date"],"Distance":convert_num, "Reading":row['Reading']})
            else:
               dist_list.append({"Date": row["Date"],"Distance":row["Distance"], "Reading":row['Reading']})
   with open(file_data, "w", newline="") as file:
      header =["Date","Distance","Reading"]
      writer = csv.DictWriter(file, fieldnames=header)
      writer.writeheader()
      for row in dist_list:
         writer.writerow(row)
convert_units("data_temper_dist.csv", "m")