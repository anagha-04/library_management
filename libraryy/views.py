from django.shortcuts import render,redirect

from libraryy.models import LibraryModel

from django.views.generic import View

# Create your views here.
class Add_books_view(View):

    def get(self,request):

        return render(request,"add_book.html")
    
    def post(self,request):

        print(request.POST)

        LibraryModel.objects.create(title = request.POST.get("title"),
                                    author = request.POST.get("author"),
                                    category = request.POST.get("category"))
        
        return render(request,"add_book.html")
    
class Book_list_view(View):

    def get(self,request):

        books_data = LibraryModel.objects.all()

        return render(request,"book_list.html",{"books_data":books_data})
    
class Books_update_view(View):

    def get(self,request,**kwargs):

        id = kwargs.get("pk")

        books = LibraryModel.objects.get(id=id)

        return render(request,"update.html",{"books":books})
    
    def post(self,request,**kwargs):

        id = kwargs.get("pk")

        books = LibraryModel.objects.get(id=id)

        print(request.POST)

        books.title = request.POST.get("title")

        books.author = request.POST.get("author")

        books.category = request.POST.get("category")

        books.save()

        return render(request,"update.html")
    
class Books_delete_view(View):

    def get(self,request,**kwargs):

        id = kwargs.get("pk")

        books_delete=LibraryModel.objects.get(id=id)

        books_delete.delete()

        return redirect("list")
    




