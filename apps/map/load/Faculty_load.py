from apps.map.models import Campus, Building, Faculty
import csv
import django
django.setup()


faculty_path = 'C:/Users/wecox1088/Desktop/UNGMap_Data/Faculty/All_Faculty.csv'
f = open(faculty_path, 'r')
reader = csv.reader(f, delimiter=',', quotechar='"')
data = [line for line in reader]
f.close()
for line in data[1:]:
    campus, building, name, title, office_num, phone_num, email, department = line
    campus = Campus.objects.filter(pk=campus).first()
    building = Building.objects.filter(pk=building).first()

    faculty = Faculty(campus=campus, building=building, name=name, title=title, office_num=office_num,
                      phone_num=phone_num, email=email, department=department)
    faculty.save()
print "Done"