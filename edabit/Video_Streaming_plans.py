class BasicPlan:
    can_stream = True
    can_download = True
    num_of_devices = 1
    has_SD = True
    has_HD = False
    has_UHD = False
    price = '8.99'

class StardandPlan(BasicPlan):
    has_HD = True
    num_of_devices = 2
    price = '12.99'

class PremiumPlan(StardandPlan):
    has_UHD = True
    num_of_devices = 4
    price = '15.99'

p1 = StardandPlan()
print(p1.price)