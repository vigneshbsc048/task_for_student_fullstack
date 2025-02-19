

# from rest_framework import generics
# from rest_framework.response import Response
# from rest_framework import status
# from .models import Student
# from .serializers import StudentSerializer
# from .utils import validate_json, ValidationError


# # Validation configuration
# config = {
#     "name": "string min length is 10 mandatory",
#     "age": "number optional",
#     "data": {
#         "class": "string mandatory"
#     }
# }


# class StudentListCreateView(generics.ListCreateAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

#     def create(self, request, *args, **kwargs):
#         # Validate incoming JSON
#         try:
#             validate_json(request.data, config)
#         except ValidationError as e:
#             return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

#         # If validation passes, create the student
#         return super().create(request, *args, **kwargs)





###############################################################
############# working good, showing, and expcted error is working ,
#############"name must be at least 10 characters long."
#############"data.class is required."
################## but not working data.class is required error...... 
############################################################### 



# from rest_framework import generics
# from rest_framework.response import Response
# from rest_framework import status
# from .models import Student
# from .serializers import StudentSerializer
# from .utils import validate_json, ValidationError


# # Updated Validation configuration
# config = {
#     "name": "string min length is 10 mandatory",
#     "age": "number optional",
#     "grade": "string mandatory"
# }


# class StudentListCreateView(generics.ListCreateAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

#     def create(self, request, *args, **kwargs):
#         # Validate incoming JSON
#         try:
#             validate_json(request.data, config)
#         except ValidationError as e:
#             return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

#         # If validation passes, create the student
#         return super().create(request, *args, **kwargs)




###### /////// best solution for checking name, age, class, grade, and error is working good

from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import Student
from .serializers import StudentSerializer
from .utils import validate_json, ValidationError

# ✅ Corrected Validation Configuration (Include data.class)
config = {
    "name": "string min length is 10 mandatory",
    "age": "number optional",
    "grade": "string mandatory",
    "data": {
        "class": "string mandatory"  # ✅ Added this
    }
}

class StudentListCreateView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def create(self, request, *args, **kwargs):
        # Validate incoming JSON
        try:
            validate_json(request.data, config)
        except ValidationError as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

        # If validation passes, create the student
        return super().create(request, *args, **kwargs)
