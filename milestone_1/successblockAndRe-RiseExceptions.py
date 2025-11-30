class User:
    def __init__(self, name, engagement):
        self.name = name
        self.engagement_metrics = engagement
        self.score = 0


    def __repr__(self):
        return f"User {self.name}"


def get_engaged_user(user):
    try:
        user.score = perform_calculation(user.engagement_metrics)
    except KeyError:
        print("Incorrect values provided to our calculation function.")
    finally:
        if user.score > 500:
            send_engagement_notification(user)

def perform_calculation(metrics):
    return metrics['clicks'] * 5 + metrics['hits'] * 2

def send_engagement_notification(user):
    print(f"Notification sent to {user}.")

my_user = User("Rolf", {'clicks': 61, 'hits': 100})
get_engaged_user(my_user)



#raise usar raise dentro do bloco de except não precisa do tipo do error
#finally sempre será executado
#Se tiver return dentro do finally ele sempre vence mesmo com return na função