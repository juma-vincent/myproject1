from django.shortcuts import render,get_object_or_404,redirect
from django.db.models import Count
from .models import Artefact
from .forms import CommentForm


def favourite_artefact(request, id):
    artefact = get_object_or_404(Artefact, id=id)
    if artefact.favourite.filter(id=request.user.id).exists():
       artefact.favourite.remove(request.user) 
    else:
        artefact.favourite.add(request.user) 
    return redirect(artefact)
    # return render(request, 'collection/favourite_artefact_list.html')

def favourite_artefact_list(request):
    user = request.user   
    favourite_artefacts = user.favourites.all()
    context = {'favourite_artefacts': favourite_artefacts }
    return render(request, 'collection/favourite_artefact_list.html', context) 

def home(request):

    artefacts = Artefact.objects.all()
    
    return render(request,'collection/home.html',{'artefacts': artefacts})

def artefact_detail(request, id):

    artefact = get_object_or_404(Artefact, pk=id)
    is_favourite = False
    if artefact.favourite.filter(id=request.user.id).exists():
        is_favourite = True

    total_comments = artefact.comments.count()
    comments = artefact.comments.all()

    if request.method =='POST':

        comment_form = CommentForm(request.POST)

        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.artefact = artefact
            new_comment.save()

            return redirect(artefact)
    else:
        comment_form = CommentForm()


    return render(request, 'collection/artefact_detail.html', {'artefact':artefact,
                                                                'is_favourite': is_favourite,
                                                               'comments':comments,
                                                               'total_comments':total_comments,
                                                               'comment_form' : comment_form
                                                               })
