from masonite.routes import Route
from masonite.authentication import Auth
from masonite.api import Api

ROUTES = [
    
    Route.get("/", "WelcomeController@show"),
          Route.get("/all", "BlogController@show"),
          Route.post("/add", "BlogController@addBlog"),

        Route.put("/put/@id", "BlogController@putData"),
        Route.delete("/delete/@id", "BlogController@deleteData")
          
        ]+ Api.routes(auth_route="/api/auth", reauth_route="/api/reauth")