from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render
from .models import City, Device, Info
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import DeviceSerializer, CitySerializer, InfoSerializer
from rest_framework import status
from rest_framework.parsers import JSONParser
import csv

def download(request):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="data.csv"'
    all_info = Info.objects.all()
    writer = csv.writer(response)
    writer.writerow([all_info])
    return response

def graph(request):
	all_info = Device.objects.all()
	return render (request, 'graph.html', {'all_info' : all_info})

def graph2(request):
	all_info = Info.objects.all()
	print (all_info)
	return render (request, 'graph2.html', {'all_info' : all_info})


def data(request):
	all_info = Info.objects.all()
	return render (request, 'data.html', {'all_info' : all_info})

def index(request):
	all_Cities = City.objects.all()
	return render(request, 'index', {'all_Cities' : all_Cities})

def detail_city(request, city_id):
	try:
		city = City.objects.get(pk = city_id)
	except City.DoesNotExist:
		raise Http404("There is no such city")
	return render(request, 'detail.html', {'city' : city})

def detail_city_inside(request, city_id, device_id):
	try:
		device_list = Info.objects.all()
		device_name = Device.objects.get(pk = device_id)
	except City.DoesNotExist:
		raise Http404("There is no any info")
	return render(request, 'detail2.html', {'device_name' : device_name, 'device_list' : device_list})

class CityList(APIView):
		def get(self, request):
			city = City.objects.all()
			serializer = CitySerializer(city, many=True)
			return Response(serializer.data)

		def post(self):
			pass


class DeviceList(APIView):
	def get(self, request):
		device = Device.objects.all()
		serializer = DeviceSerializer(device, many=True)
		return Response(serializer.data)

	def post(self, request):
		data1 = JSONParser().parse(request)
		serializer = DeviceSerializer(data=data1)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class InfoList(APIView):
	def get(self, request):
		sensor = Info.objects.all()
		serializer = InfoSerializer(sensor, many=True)
		return Response(serializer.data)

	def post(self, request):
		sensor = JSONParser().parse(request)
		serializer = DeviceSerializer(data=sensor)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)