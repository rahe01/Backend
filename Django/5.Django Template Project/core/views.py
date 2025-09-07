from django.shortcuts import render

# Create your views here.


def home(req):
    dishes = [
        {
            "name": "Paneer Butter Masala",
            "description": "Creamy and rich, with a delightful blend of spices, perfect with naan or rice.",
            "image": "core/images/img1.png",
            "price": 180
        },
        {
            "name": "Chicken Biryani",
            "description": "Aromatic basmati rice cooked with tender chicken and special spices.",
            "image": "core/images/img3.png",
            "price": 220
        },
        {
            "name": "Veg Hakka Noodles",
            "description": "Stir fried noodles with fresh vegetables and sauces.",
            "image": "core/images/img2.png",
            "price": 150
        },
    ]
    return render(req, 'core/home.html' ,{"dishes": dishes})


def menu(request):
    dishes = [
        {
            "name": "Paneer Butter Masala",
            "description": "Creamy and rich, with a delightful blend of spices, perfect with naan or rice.",
            "image": "core/images/img1.png",
            "price": 180
        },
        {
            "name": "Chicken Biryani",
            "description": "Aromatic basmati rice cooked with tender chicken and special spices.",
            "image": "core/images/img2.png",
            "price": 220
        },
        {
            "name": "Veg Hakka Noodles",
            "description": "Stir fried noodles with fresh vegetables and sauces.",
            "image": "core/images/img3.png",
            "price": 150
        },
    ]
    return render(request, 'core/menu.html', {"dishes": dishes})

def tracking(req):
    return render(req, 'core/tracking.html')


def reservation(req):

    return render(req, 'core/reservation.html')

def contact(req):

    return render(req, 'core/contact.html')