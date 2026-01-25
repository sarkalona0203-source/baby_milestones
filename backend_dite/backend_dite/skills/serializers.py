from rest_framework import serializers
from .models import Skill


class SkillSerializer(serializers.ModelSerializer):
    age_range = serializers.SerializerMethodField()

    class Meta:
        model = Skill
        fields = [
            "id",
            "name",
            "description",
            "icon",
            "min_age_months",
            "max_age_months",
            "age_range",
        ]

    def get_age_range(self, obj):
        if not self.context.get("show_status"):
            return None

        if obj.max_age_months:
            return f"{obj.min_age_months}–{obj.max_age_months} měsíců"

        return f"od {obj.min_age_months} měsíců"

    def get_nutrition_tips(self, obj):
        age = self.context.get("age")
        if age is None:
            return []

        guides = NutritionGuide.objects.filter(
            min_age_months__lte=age,
            max_age_months__gte=age
        )

        return [
            {
                "title": g.title,
                "text": g.text,
                "type": g.type,
            }
            for g in guides
        ]