#%%
class Car:
    def __init__(self, color, speed, n_wheels): 
        super().__init__(color, speed) 
        self.n_wheels = n_wheels 
    def do_something(self):
        super().do_something()
        print('obiekt Car coś robi!')
        
car = Car("red", 250, 4)
print(car.color)
# %%
