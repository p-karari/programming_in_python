class Car_details:
    def __init__(self, brand_name, model_name, horse_power):
        self.brand_name = brand_name
        self.model_name = model_name
        self.horse_power = horse_power
   

    def is_a_race_car(self):
        if self.horse_power >= 600:
            return True