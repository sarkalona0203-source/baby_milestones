from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Skill, NutritionGuide
from .serializers import SkillSerializer


class SkillListView(APIView):
    def get(self, request):
        age_input = request.GET.get("age")
        age_months = self.convert_to_months(age_input)

        if age_months is None:
            return Response(
                {"error": "Nesprávný věk. Zadejte prosím věk dítěte v měsících."},
                status=400
            )

        show_status = age_months >= 18

        if age_months < 18:
            skills = Skill.objects.filter(
                min_age_months__lte=age_months
            ).order_by("min_age_months")
        else:
            min_m, max_m = self.get_age_range(age_months)
            skills = Skill.objects.filter(
                min_age_months__lte=max_m,
                max_age_months__gte=min_m
            ).order_by("min_age_months")

        nutrition_guides = NutritionGuide.objects.filter(
            min_age_months__lte=age_months,
            max_age_months__gte=age_months
        )

        serializer = SkillSerializer(
            skills,
            many=True,
            context={
                "age": age_months,
                "show_status": show_status,
                "nutrition_guides": nutrition_guides,
            }
        )

        return Response({
            "age": age_months,
            "nutrition": [
                {
                    "title": g.title,
                    "text": g.text,
                    "type": g.type,
                }
                for g in nutrition_guides
            ],
            "skills": serializer.data
        })

    def convert_to_months(self, value):
        if value and value.isdigit():
            age = int(value)
            if 0 <= age <= 72:
                return age
        return None

    def get_age_range(self, age_months):
        start = (age_months // 6) * 6
        end = start + 6
        return start, end