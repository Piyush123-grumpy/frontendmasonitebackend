from masonite.controllers import Controller
from masonite.views import View
from masonite.request import Request
from app.models.Blog import Blog


class BlogController(Controller):


    def __init__(self,view:View,request:Request):
        self.view=view
        self.request=request

    def show(self):
        return Blog.all()
    
    def addBlog(self):
        data=self.request.only('author','title','text')
        Blog.create(data)
        return Blog.all()
    
    def putData(self):
        data=self.request.param('id')

        data2=self.request.only('author','title','text')

        blog=Blog.where('id', data)
        blog.update(data2)
        return {}
    
    def deleteData(self):
        data=self.request.param('id')
        blog=Blog.where('id', data).delete()
        return data