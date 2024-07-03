import csv
import os
def read_csv_to_dictionary(filename):
    with open(filename,'r+', encoding='utf-8-sig') as file:
        csv_reader = csv.DictReader(file, delimiter=';')
        data = []
        for row in csv_reader:
            name = row['fullname']
            num = row['num']
            mail = row['mail']
            fname = row['name']
            lname = row['surname']
            position = row['position']
            row = {'fullname': name, 'num': num, 'mail': mail, 'fname': fname, 'lname': lname, 'position': position}
            data.append(row)
    return data

def find_user(login):
    global row
    for row in data:
        if login in row["mail"]:
            return row
            
class Person:
    def __init__(self, row):
            self.name = row['fullname'].strip()
            self.num = row['num'].strip()
            self.mail = row['mail'].strip()
            self.fname = row['fname'].strip()
            self.lname = row['lname'].strip()
            self.position = row['position'].strip()
   #footer_folder_path
    def footer_generate(self):
        with open("template/footer_template.html", 'r',encoding='utf-8') as temp_footer:
            with open("footer\%s%s_example_com (%s).htm"%(self.fname.lower()[0:1],self.lname.lower(),self.mail), 'w',encoding='utf-8') as new_footer:
                for line in temp_footer:

                    if line.strip() == '{uname}':
                        new_footer.writelines(self.name)

                    elif line.strip() == '{num}':
                        if self.num == '' or self.num == '-':
                            new_footer.writelines('')
                        else:
                            new_footer.writelines(f"<tr width='297' height='15'><td width='20' height='15' nowrap='nowrap'><img width='15' height='15' src='data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAA8AAAAPCAYAAAA71pVKAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAGdSURBVDhPbZPLK0RhGMbPEBmXcomQXGqIcivZKBYuC2IxK4qVpZWUhaV/wMqwFoWSS+OSkhRpmrJSkhBlgzRGTCKX3zPOOZ2Dp37znPO97/udc973G4/h0Hl6ru5boBuaIQdu4QiWfM/3+7gtu5jCTGwKamEF1uERiqEBRmAP+tjkE/8pNguDcAKjBJ+07pT5VjNQDU3kvFrF01giDMMHvBH8wv+I3Dksjbjfw4122gb5O2xADfSTsIW7RH4qdgqtCfx0wSqJEVxN0tv0wgKJXtwl8mLYIgyoWM1QI6Qw1MMlRKEQ/tMuNKo4A5SoXR+wAExCBfcXPD0fKhV3SA31qvgOyrQiUTCGJcFyfMEw1iDEBkGwRqvxRVSswbdpxSE/xEg+xicgG/QJPSB1QFjdVuAMSnjqiyKWiA1iQ1AK19AJKXCga2vOWViU4vjJ+S3iRZg21uznIUTuOO4WicnmpUus+2AHNEI12T6eVZi+R/NVZ3VoDuEG8qAddOZ19gPW5+mby3HNTadpFq5ADamDAtDh0b9qkyJtZsowvgH7mYfSG3FCqgAAAABJRU5ErkJggg=='></td><td width='277' height='15' nowrap='nowrap'><span style='font-family:arial;color:black;text-align:left;font-size:13px;line-height: 15px;'><a href='tel:{self.num}'>{self.num}</a></span></td></tr>")
                       
                    elif line.strip() == '{mail}':
                            new_footer.writelines(f'<td width="277" height="15" nowrap="nowrap"><span style="font-family:arial;color:black;text-align:left;font-size:13px;line-height: 15px;"><a href="{self.mail}">{self.mail}</a></span></td>')
                    
                    elif line.strip() == '{pos}':
                            new_footer.writelines(self.position)
                    else:
                        new_footer.write(line)
            new_footer.close()
        temp_footer.close()
        
data = read_csv_to_dictionary('data.txt')

#desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
#footer_folder_path = os.path.join(desktop_path, 'footer')

#if not os.path.exists(footer_folder_path):
#    os.makedirs(footer_folder_path)

size = len(data)
for i in range(0,size):
    row = data[i]
    user = Person(row)
    user.footer_generate()
