from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from numpy import mean

# Create your views here.
from django.views.generic import DetailView, ListView, UpdateView

from blog.forms import WatchCreate, MaisonForm
from blog.models import Watch, Maison, Condition


@login_required()
def LikeView(request, pk):
    post = get_object_or_404(Watch, id=request.POST.get('post_id'))
    post.likes.add(request.user)
    return HttpResponseRedirect(reverse('blog:blogPostDetail', args=[str(pk)]))


class WatchDetail(DetailView):
    model = Watch
    template_name = 'blog/blogPost/detail.html'

    def get_context_daya(self, *args, **kwargs):
        context = super(WatchDetail, self).get_context_data(**kwargs)
        stuff = get_object_or_404(Watch, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()
        return context

class WatchList(ListView):
    model = Watch
    template_name = 'blog/blogPost/home_view.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Condition.objects.all()
        context = super(WatchList, self).get_context_data(**kwargs)
        context["cat_menu"] = cat_menu
        return context

    def get_queryset(self):
        result = super(WatchList, self).get_queryset()
        query = self.request.GET.get('order')
        if query:
            if query == 'maison' or query == 'model' or query == "owner":
                result = Watch.objects.all().order_by(query)
        else:
            result = Watch.objects.all()
        return result


class MaisonDetailView(DetailView):
    model = Maison
    template_name = 'blog/blogPost/maison_detail.html'


class MaisonListView(ListView):
    model = Maison
    template_name = 'blog/blogPost/maison_list.html'

def conditionListView(request):
    condition_watch_list = Condition.objects.all()
    return render(request, 'blog/blogPost/condition_list.html', {'condition_watch_list': condition_watch_list})

@login_required
def create_watch(request):
    if request.method == 'POST':
        form = WatchCreate(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('Watch-Hub-Home')
    else:
        form = WatchCreate()

    return render(request, 'blog/blogPost/insert_watch.html', {'form': form})


def watchSearch(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        watch_list = Watch.objects.filter(model__contains=searched)
        return render(request, 'blog/blogPost/watch_search.html', {'searched': searched, 'watch_list':watch_list})
    else:
        return render(request, 'blog/blogPost/watch_search.html', {})


def ConditionView(request, condition):
    condition_watch = Watch.objects.filter(condition=condition)
    return render(request, 'blog/blogPost/watch_list.html', {'condition':condition, 'condition_watch': condition_watch})

class UpdateWatch(UpdateView):
    model = Watch
    template_name = 'blog/blogPost/update_watch.html'
    fields = ['condition', 'price', 'photo']

    def get_context_data(self, *args, **kwargs):
        cat_menu = Condition.objects.all()
        context = super(UpdateWatch, self).get_context_data(**kwargs)
        context["cat_menu"] = cat_menu
        return context


@login_required
def maison_create(request):
    if request.method == 'POST':
        form = MaisonForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('<script type="text/javascript">window.close()</script>')
        else:
            form = MaisonForm()

        return render(request, 'blog/blogPost/maison_create.html', {'form': form})


def favorite_watch_view(request):
    list_like = []

    for watch in Watch.objects.all():
        if watch.likes.filter(username=request.user.username).exists():
            if watch not in list_like:
                list_like.append(watch)

    context = {
        'list_like': list_like
    }

    return render(request, 'blog/blogPost/favorite.html', context)


def watch_suggestion(request):
    sugg_watch = []
    maison_like = []
    watch_like = []
    w_price = 0
    watch_price = []

    # dai miei orologi preferiti inserisco agli orologi suggeriti anche quelli con prezzo simile
    w_price = mean([Watch.price for Watch in watch_like])

    #inserisco la maison di un orologio a cui hai messo mi piace e non è ancora salvata
    for watch in Watch.objects.all():
        if watch.likes.filter(username = request.user.username).exists():
            if watch.maison not in maison_like:
                maison_like.append(watch.maison)
                watch_like.append(watch.pk)
        if watch.maison in maison_like and watch.pk not in watch_like:
            sugg_watch.append(watch)
        if w_price + 500 > watch.price or watch.price < w_price - 500:
            watch_price.append(watch)


    context = {
        'sugg_watch':sugg_watch[:3],
        'watch_price':watch_price[:2]
    }

    return render(request, 'blog/blogPost/suggestion.html', context)
