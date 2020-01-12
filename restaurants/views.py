from django.shortcuts import render

def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):

    context = { 
    	"my_list" : [
    		{"restaurant_name": "Tampopo",
    		"food_type" : "Ramen"},
    		
    		{"restaurant_name": "Tatami",
    		"food_type": "Japanese"},
    		
    		{"restaurant_name": "St Almakan",
    		"food_type": "Street asian"}
    	]

    }
    return render(request, 'list.html', context)


def restaurant_detail(request):

    context = {
    	"my_object":
    		{"restaurant_name": "Tampopo",
    		"food_type" : "Ramen"}

    }
    return render(request, 'detail.html', context)
