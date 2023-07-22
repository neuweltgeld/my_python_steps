class student:
    
    num_of_students = 0
    
    def __init__(self, first, last, age, lecture):
        self.first = first
        self.last = last
        self.age = age
        self.lecture = lecture
        student.num_of_students += 1 # __init__ çalıştığında sayıya 1 ekler
    
    def output(self):
        return f"{self.first} {self.last} isimli öğrenci {self.age} yaşında ve {self.lecture} dersini alıyor."
    
    @classmethod
    def import_(cls,str_):
        first,last,age,lecture = str_.split("-")
        return cls(first,last,age,lecture)

student1 = student("geralt", "of rivia", 300, "mutasyon")
student2 = student("ciri", "başbelası", 20, "hayat bilgisi")

# dışardan gelen veriyi classmethod ile split edip kullandık.
student3 = student.import_("vezemir-dede-500-tarih") 

print(f"toplam {student.num_of_students} öğrenci var.")

print(student1.output()) # otomatik self ataması
print(student.output(student2)) # direk class çağırırsan argümanı kendin yaz.
print(student.output(student3))
