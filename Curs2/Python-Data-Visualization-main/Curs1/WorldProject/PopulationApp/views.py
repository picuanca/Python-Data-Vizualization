from django.shortcuts import render
import matplotlib.pyplot as plt
# Create your views here.
from io import BytesIO
import base64
import matplotlib

matplotlib.use("svg")

def all_countries_view(request):
	context = {}
	return render(request, 'all_countries.html', context)


def create_image(countries = ["China", "India", "Brazil"], population = [1411, 1378, 213]):	
	
	fig, axes = plt.subplots()
	axes.pie(population, labels=countries);

	buffer = BytesIO()
	fig.savefig(buffer, format="png")
	buffer.seek(0)
	image_png = buffer.getvalue()
	buffer.close()

	return base64.b64encode(image_png).decode("utf-8")

suprafete = {
    'Bangladesh': 147570,
    'Brazil': 8515770,
    'China': 9562910,
    'India': 3287263,
    'Indonesia': 1904569,
    'Mexic': 1972550,
    'Nigeria': 923768,
    'Pakistan': 881913,
    'Russia': 17098242,
    'United States': 9831510
}

populatii = {
	'Bangladesh': 170,
	'Brazil': 213,    
	'China': 1411,    
	'India': 1378,    
	'Indonesia': 271,
	'Mexico': 126,
	'Nigeria': 211,
	'Pakistan': 225,
	'Russia': 146,
	'United States': 331
}


def choose_countries_view(request):
	countries = ['Bangladesh', 'Brazil', 'China', 'India', 'Indonesia', 'Mexico', 'Nigeria', 'Pakistan', 'Russia', 'United States']
	population =  [170, 213, 1411, 1378, 271, 126, 211, 225, 146, 331]


	result_image = '10_tari.png'
	base64_image = None
	tari = None
	measure = "tari"

	if request.method == "POST":
		print("parametri:", request.POST.keys())
		tari = request.POST.keys()
		print("tarile primite:", tari)

		measure = request.POST.get("measure", "tari")
		if measure == "tari":
			measured_data = populatii
		elif measure == "suprafete":
			measured_data = suprafete

		tari = [t for t in tari if t in countries]
		locuitori = [measured_data[t] for t in tari]		

		base64_image = create_image(tari, locuitori)
	

	context = {
		"countries": countries,
		"result_image": result_image,
		"base64_image":base64_image,
		'tari': tari,
		'measure': measure
	}
	return render(request, 'choose_countries.html', context)
