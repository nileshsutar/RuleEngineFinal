from django.shortcuts import render


from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import status

from models import Rule
from serializers import RuleSerializer

# Create your views here.

class RuleViewSet(viewsets.ModelViewSet):
	queryset = Rule.objects.all()
	serializer_class = RuleSerializer
	parser_classes = (MultiPartParser, FormParser,)
	
	def list(self, request, format=None):
		serializer = self.serializer_class(self.queryset, many=True)
		return Response(serializer.data)
	
	def create(self, request, format=None):
		datafile = request.FILES.get('datafile')
		if not datafile:
			return Response(status=404)
		#request.data.pop("datafile")
		serializer = RuleSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			filelocation = serializer.instance.datafile.path
			serializer.instance.filelocation=filelocation
			serializer.instance.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

		
class RuleDetail(APIView):
	"""
	Retrive, update or delete a rule instance.
	"""

	def get_object(self, pk):
		try:
			return Rule.objects.filter(pk=pk)
		except Rule.DoesNotExist:
			return Http404

	def get(self, request, pk, format=None):
		rule = get_object(pk)
		serializer = RuleSerializer(rule)
		return Response(serializer.data)

	def put(self, request, pk, format=None):
		import pdb;pdb.set_trace()
		rule = get_object(pk)
		serializer = RuleSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			filelocation = serializer.instance.datafile.path
			serializer.instance.filelocation=filelocation
			serializer.instance.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	
	def delete(self, request, pk, format=None):
		rule = get_object(pk)
		rule.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)
