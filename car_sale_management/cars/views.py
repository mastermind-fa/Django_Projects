from django.views.generic import ListView, DetailView, CreateView
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Car, Brand, Order, Comment
from .forms import UserRegistrationForm, UserProfileForm, CommentForm
from . import forms
# Home Page and Car Listings


from django.shortcuts import render
from cars.models import Car
from brands.models import Brand
def home(request, brand_slug = None): # initially dhore nicchi je brand_slug None thakbe karon hocche user first time home page e asle se normal page dekhbe, se filter korte chaile brand te click korlei sei brand er slug ta capture korbo ar seta tokhn ar None thakbe na
    
    data = Car.objects.all() # sob post gula ke niye aslam
    if brand_slug is not None: # ekhn brand slug jodi None na hoy tar mane sekhane value ache
        brand = Brand.objects.get(slug = brand_slug) # slug je field model e likhechilam seta = amader brand slug kore dilam taile ekhn kon brand er slug sei brand object peye jabo
        data = Car.objects.filter(brand = brand) # post er brand te brand object bosiye filter korlam, ager data er sathe overright hoye jabe
    brands = Brand.objects.all() # sob brand dekhabo
    return render(request, 'home.html', {'data' : data, 'brand' : brands})
# Car Detail and Comments
class CarDetailView(DetailView):
    model = Car
    template_name = 'car_detail.html'
    context_object_name = 'car'

    def post(self, request, *args, **kwargs):
        car = self.get_object()
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.car = car
            comment.save()
            messages.success(request, "Comment added successfully!")
        return redirect('car-detail', pk=car.id)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        car = self.object # post model er object ekhane store korlam
        comments = car.comments.all()
        comment_form = forms.CommentForm()
        
        context['comments'] = comments
        context['comment_form'] = comment_form
        return context


# User Registration
class UserRegistrationView(CreateView):
    form_class = UserRegistrationForm
    template_name = 'register.html'

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        user.save()
        login(self.request, user)
        return redirect('home')


@login_required
def profile_view(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully!")
            return redirect('profile')
    else:
        form = UserProfileForm(instance=request.user)
    orders = Order.objects.filter(user=request.user)
    return render(request, 'profile.html', {'form': form, 'orders': orders})


@login_required
def buy_car(request, pk):
    car = get_object_or_404(Car, pk=pk)  # Fetch car by primary key
    if car.quantity > 0:
        car.quantity -= 1
        car.save()
        # Create the order with quantity and total_price
        Order.objects.create(
            user=request.user, 
            car=car, 
            quantity=1,  # Set quantity explicitly
            total_price=car.price  # Calculate total price
        )
        messages.success(request, "Car purchased successfully!")
    else:
        messages.error(request, "Sorry, this car is out of stock.")
    return redirect('car-detail', pk=pk)

    
