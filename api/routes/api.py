from masonite.routes import Route

ROUTES=[
    Route.get('/user','UsersController@index')
]