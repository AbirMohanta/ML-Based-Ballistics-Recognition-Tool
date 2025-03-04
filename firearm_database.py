class FirearmDatabase:
    def __init__(self):
        # Dictionary mapping calibers to compatible firearms
        self.firearm_data = {
            ".223": {
                "rifles": [
                    {
                        "name": "AR-15",
                        "type": "Semi-Automatic Rifle",
                        "manufacturer": "Various",
                        "effective_range": "600 yards",
                        "description": "Popular modern sporting rifle, standard NATO caliber",
                        "common_use": "Sport shooting, hunting, tactical",
                        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/AR15_A3_Tactical_Carbine_pic1.jpg/1200px-AR15_A3_Tactical_Carbine_pic1.jpg"
                    },
                    {
                        "name": "Ruger Mini-14",
                        "type": "Semi-Automatic Rifle",
                        "manufacturer": "Ruger",
                        "effective_range": "500 yards",
                        "description": "Ranch rifle popular for varmint hunting",
                        "common_use": "Ranch use, hunting",
                        "image_url": "https://ruger.com/products/mini14RanchRifle/images/5816.jpg"
                    }
                ]
            },
            ".308": {
                "rifles": [
                    {
                        "name": "Remington 700",
                        "type": "Bolt Action Rifle",
                        "manufacturer": "Remington",
                        "effective_range": "800 yards",
                        "description": "Popular hunting rifle, also used by military/police",
                        "common_use": "Hunting, precision shooting",
                        "image_url": "https://www.remarms.com/assets/700-bdl.jpg"
                    },
                    {
                        "name": "M24 Sniper Weapon System",
                        "type": "Precision Rifle",
                        "manufacturer": "Remington",
                        "effective_range": "800+ yards",
                        "description": "Military sniper rifle system",
                        "common_use": "Military, precision shooting",
                        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f2/M24_Sniper_Weapon_System.jpg/1200px-M24_Sniper_Weapon_System.jpg"
                    }
                ]
            },
            ".30-06": {
                "rifles": [
                    {
                        "name": "M1 Garand",
                        "type": "Semi-Automatic Rifle",
                        "manufacturer": "Springfield Armory",
                        "effective_range": "600 yards",
                        "description": "Historic military rifle, WWII standard issue",
                        "common_use": "Historical collecting, competition",
                        "image_url": "https://upload.wikimedia.org/wikipedia/commons/9/9e/M1_Garand_rifle_-_USA_-_30-06_-_Arm%C3%A9museum.jpg"
                    }
                ]
            },
            ".338": {
                "rifles": [
                    {
                        "name": "Accuracy International AXMC",
                        "type": "Precision Rifle",
                        "manufacturer": "Accuracy International",
                        "effective_range": "1500 yards",
                        "description": "Professional long-range precision rifle",
                        "common_use": "Military, long-range shooting",
                        "image_url": "https://accuracyinternational.com/wp-content/uploads/2019/03/AXMC_Main_Image.jpg"
                    }
                ]
            },
            ".50": {
                "rifles": [
                    {
                        "name": "Barrett M82",
                        "type": "Semi-Automatic Anti-Materiel Rifle",
                        "manufacturer": "Barrett",
                        "effective_range": "2000 yards",
                        "description": "Heavy anti-materiel rifle",
                        "common_use": "Military, long-range shooting",
                        "image_url": "https://barrett.net/wp-content/uploads/2020/04/M82A1_1.jpg"
                    }
                ]
            }
        }
        
        # Additional ballistic performance data
        self.ballistic_data = {
            ".223": {
                "optimal_twist_rate": "1:7 - 1:9",
                "typical_use_range": "0-600 yards",
                "common_bullet_weights": "45-77 grains",
                "recommended_barrel_length": "16-20 inches",
                "typical_applications": [
                    "Varmint hunting",
                    "Target shooting",
                    "Competition",
                    "Home defense"
                ]
            },
            ".308": {
                "optimal_twist_rate": "1:10 - 1:12",
                "typical_use_range": "0-1000 yards",
                "common_bullet_weights": "150-180 grains",
                "recommended_barrel_length": "18-24 inches",
                "typical_applications": [
                    "Big game hunting",
                    "Long range shooting",
                    "Tactical applications",
                    "Competition"
                ]
            }
            # Add more calibers as needed
        }
    
    def get_compatible_firearms(self, caliber):
        """Get list of firearms compatible with given caliber"""
        return self.firearm_data.get(caliber, {"rifles": []})["rifles"]
    
    def get_ballistic_data(self, caliber):
        """Get ballistic performance data for given caliber"""
        return self.ballistic_data.get(caliber, {})
    
    def get_firearm_details(self, caliber, firearm_name):
        """Get detailed information about specific firearm"""
        firearms = self.get_compatible_firearms(caliber)
        for firearm in firearms:
            if firearm["name"] == firearm_name:
                return firearm
        return None 