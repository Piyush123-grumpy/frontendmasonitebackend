"""A WelcomeController Module."""
from masonite.views import View
from masonite.controllers import Controller
from app.models.User import User

class WelcomeController(Controller):
    """WelcomeController Controller Class."""

    def show(self, view: View):
        
        return  User.all()
