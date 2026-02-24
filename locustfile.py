
from locust import HttpUser, task, between

class ReactAppUser(HttpUser):
    wait_time = between(1, 3) # Users wait 1-3 seconds between clicks

    @task
    def load_homepage(self):
        self.client.get("/")
