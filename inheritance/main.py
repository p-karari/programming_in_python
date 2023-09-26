#inheritance

from chef import chef
from chinese_chef import chinese_chef

chef1 = chef()
chinesechef = chinese_chef()
chef1.makes_chicken()
chef1.makes_special_dish()
print("Chinese")
chinesechef.makes_chicken()
chinesechef.makes_special_dish()
chinesechef.makes_fried_rice()
chinesechef.makes_tea()