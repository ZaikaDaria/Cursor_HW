class Profile:
    def __init__(self, name, last_name, phone_number, address, email, birthday, age, sex):
        self.name = name
        self.last_name = last_name
        self.phone_number = phone_number
        self.address = address
        self.email = email
        self.birthday = birthday
        self.age = age
        self.sex = sex
        self.profile_data = [self.name, self.last_name, self.phone_number, self.address,
                             self.email, self.birthday, self.age, self.sex]

        print(f"{self.name},your profile has been created successfully")

    def __str__(self):
        return f'This is your profile info: {self.profile_data}'

profile = Profile("Daria", "Zaika", "+380633333333",
                  "Kyiv, Bazhana street", "dashazaika@gmail.com",
                  "24.07.1990", "30", "female")
print(profile)
