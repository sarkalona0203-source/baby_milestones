from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Skill
from .serializers import SkillSerializer


class SkillListView(APIView):
    def get(self, request):
        age_input = request.GET.get("age", "")
        age_months = self.convert_to_months(age_input)

        if age_months is None:
            return Response(
                {"error": "Nesprávný věk. Zadejte prosím datum narození dítěte."},
                status=400
            )

        # 🔹 ДО 18 МЕСЯЦЕВ — просто актуальные навыки
        if age_months < 18:
            # Берём все навыки, где max_age_months <= 18 или min_age_months <= возраст ребёнка
            skills = Skill.objects.filter(
                min_age_months__lte=age_months
            ).order_by('min_age_months')  # сортировка по возрасту
            show_status = True  # чтобы выводились диапазон и поддержка

        # 🔹 ПОСЛЕ 18 МЕСЯЦЕВ — группировка + статус
        else:
            min_m, max_m = self.get_age_range(age_months)
            skills = Skill.objects.filter(
                min_age_months__lte=max_m,
                max_age_months__gte=min_m
            )
            show_status = True

        serializer = SkillSerializer(
            skills,
            many=True,
            context={
                "age": age_months,
                "show_status": show_status
            }
        )
        return Response(serializer.data)

    def convert_to_months(self, age_input):
        if age_input.isdigit():
            return int(age_input)
        return None

    def get_age_range(self, age_months):
        start = (age_months // 6) * 6
        end = start + 6
        return start, end
