from datetime import date, datetime
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import PersonSerializer, CommonSerializer, ServerSerializer
from .models import Common
from calc.fiscalcode import fc
import platform

class PersonView(APIView):
    def post(self, request):
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            born = data['date']
            today = date.today()
            age = today.year - born.year - ((today.month, today.day) < (born.month, born.day))
            data_datetime = datetime.strptime(str(born), "%Y-%m-%d")
            birth_date = data_datetime.strftime("%d/%m/%Y")
            result = f"Name: {data['name']}, Surname: {data['surname']}, Birth date: {data['date']}, City: {data['city']}, Sex: {data['sex']}"
            f_code = fc(data['name'], data['surname'], birth_date, data['city'], data['sex'])
            return Response({'result': result, 'age': age, 'fiscal_code': f_code})
        return Response(serializer.errors, status=400)

class CommonsView(APIView):
    def get(self, request):
        commons = Common.objects.all()
        serializer = CommonSerializer(commons, many=True)
        return Response(serializer.data)

class CommonsViewDetail(APIView):
    def get(self, request, code):
        common = Common.objects.get(common_code=code)
        serializer = CommonSerializer(common)
        return Response(serializer.data)

class ServerView(APIView):
    def get(self, request):
        server = platform.node()
        return Response(server)