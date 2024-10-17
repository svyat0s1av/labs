class circle:
    def __init__(self,radius):
        self.radius=radius
    def get_radius(self):
        return (self.radius)
    def set_radius(self,new_radius):
        self.radius=new_radius
krug=circle(5)
print(krug.get_radius())
krug.set_radius(10)
print(krug.get_radius())