# Η κλάση αυτή περιγράφει τον χρήστη
class User:
    def __init__(self, name: str, email: str, password: str, our_spend_activities: int, our_spend_hobbies: int ):
        self.name = name
        self.email = email
        self.password = password
        self.our_spend_activities = our_spend_activities
        self.our_spend_hobbies = our_spend_hobbies

    #Για πιο εύκολη εκτύπωση
    def __str__(self)->str:
        return (f"User Name: {self.name},email: {self.email},Password: {self.password}, "
                f"hour for activity: {self.our_spend_activities},hour for hobbies: {self.our_spend_hobbies} ")

