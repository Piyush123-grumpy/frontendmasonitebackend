"""UserTableSeeder Seeder."""
from masoniteorm.seeds import Seeder
from masonite.facades.Hash import Hash

from app.models.User import User


class UserTableSeeder(Seeder):
    def run(self):
        """Run the database seeds."""
        User.create(
            {
                "name": "abc",
                "email": "abc@abc.com",
                "password": "abc",
                "phone": "+123456789",
            }
        )
