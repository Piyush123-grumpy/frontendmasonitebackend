from masonite.controllers import Controller
from masonite.views import View
from masonite.response import Response


class UsersController(Controller):
    def index(self,response:Response):
        return response.json({
            'foo':'bar'
        })

