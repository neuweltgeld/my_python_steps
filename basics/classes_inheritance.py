class worker:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
        
    def fullname(self):
        return f"{self.first}, {self.last}"
    
    def output(self):
        print(f" name : {self.first} \n lastname : {self.last} \n age : {self.age}")
        
class admin(worker):
    def __init__(self, first, last, age, position): # yeni argümanı tanımla "position"
        super().__init__(first, last, age) # workerdan firs,last,age çek
        self.position = position # ekleme yap

class manager(worker):
    def __init__(self, first, last, age, position, workers = None): # worker listesi tanımla
        super().__init__(first, last, age)
        self.position = position
        if workers is None:
            workers = []
        else:
            self.workers = workers

    def add_worker(self, workera):
        if workera not in self.workers:
            self.workers.append(workera)
            
    def remover_worker(self, workera):
        if workera in self.workers:
            self.workers.remove(workera)
            
    def worker_output(self):
        for workera in self.workers:
            print(">>>>", workera.fullname())
            
worker_1 = worker("ciri", "başbelası", 20)
worker_2 = worker("jaskier", "dandelion", 30)
admin_1 = admin("geralt", "of rivia", 300, "admin")
manager_1 = manager("vezemir", "dede", 500, "manager", [worker_1,worker_2])
  
manager_1.worker_output()
