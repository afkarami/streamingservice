from multiprocessing import Value


class User:
    
    # Data user
    data_user = {
        1: ["Rosy", "Basic Plan", 12, 'rosy-123'],
        2: ["Rany", "Standard Plan", 12, 'rany-123'],
        3: ["Airin", "Premium Plan", 12, 'airin-123'],
        4: ["Fahmi", "Basic Plan", 6, 'fahmi-123'],
        5: ["Ahmad", "Standard Plan", 2, 'fahmi-123'],
        6: ["Karami", "Premium Plan", 4, 'karami-123']
    }

    # Data Plan
    list_plan = ("Basic Plan", "Standard Plan", "Premium Plan")
    list_benefit = [
        [True, True, True, "Bisa Stream"],
        [True, True, True, "Bisa Download"],
        [True, True, True, "Kualitas SD"],
        [False, True, True, "Kualitas HD"],
        [False, False, True, "Kualitas UHD"],
        [1, 2, 4, "Number of Devices"],
        ["3rd party Movie only", "Basic Plan Content + Sports", "Basic Plan + Standard Plan + PacFlix Original Series", "Jenis Konten"],
        [120_000, 160_000, 200_000]
        ]
    headers = ["Basic Plan", "Standard Plan", "Premium Plan"]

    # akses user
    def __init__(self, username):
        self.username = username
        self.current_plan = None
        self.duration_plan = None
        self.kode_referral = None

        for key, value in self.data_user.items():
            if value[0] == self.username:
                self.current_plan = value [1]
                self.duration_plan = value [2]
                self.kode_referral = value [3]
                break
