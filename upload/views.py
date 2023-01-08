from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import DataQualityCheck, Upload
from .serializers import  DataQualityCheckSerializer, UploadSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db import connection

class uploadView(APIView):
    def get(self,request):
        uploads=Upload.objects.all()
        uploadserializer=UploadSerializer(uploads,many=True)
        return Response(uploadserializer.data)

    def post(self,request):
        insert_serializer=UploadSerializer(data=request.data)
        if insert_serializer.is_valid():
            insert_serializer.save()
            cursor = connection.cursor()
            ret = cursor.callproc("proc_schema_data",())
            cursor.close()
            return Response(insert_serializer.data)
        
        else:
            Response(insert_serializer.errors)

class UploadLayerView(APIView):
    def get(self,request,pk):
        get_uploaded_data=Upload.objects.get(pk=pk)
        get_uploaded_serializer=UploadSerializer(get_uploaded_data)
        return Response(get_uploaded_serializer.data)

    def put(self,request,pk):
        get_uploaded_data=Upload.objects.get(pk=pk)
        update_serializer=UploadSerializer(get_uploaded_data,data=request.data)
        if update_serializer.is_valid():
            update_serializer.save()
            return Response(update_serializer.data)
        else:
            return Response(update_serializer.errors)

class dataQualityCheck(APIView):
    def get(self,request):
        dataQuality=DataQualityCheck.objects.all()
        dataQualitySerializer=DataQualityCheckSerializer(dataQuality,many=True)
        return Response(dataQualitySerializer.data)

    def post(self,request):
        dataQuality_serializer=DataQualityCheckSerializer(data=request.data)
        if dataQuality_serializer.is_valid():
            dataQuality_serializer.save()
            return Response(dataQuality_serializer.data)
        
        else:
            Response(dataQuality_serializer.errors)

class getSchemaStructure(APIView):
    def get(self,request):
        cur = connection.cursor()
        sql = "select column_name  from SPOTLIGHT.information_schema.columns where table_schema = 'BRONZE_LAYER' and table_name ='"+self.request.query_params.get('table_name')+"'"
        cur.execute(sql)
        records = cur.fetchall()
        return Response(records)

class getSchemaData(APIView):
    def get(self,request):
        cur = connection.cursor()
        # sql = "select "+self.request.query_params.get('columns_name') +"  from '"+self.request.query_params.get('table_name')+"'"
        sql = "select "+self.request.query_params.get('columns_name') +"  from SPOTLIGHT.BRONZE_LAYER.BRONZE_LAYER"
        cur.execute(sql)
        records = cur.fetchall()
        return Response(records)