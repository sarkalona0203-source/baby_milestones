from rest_framework import serializers
from .models import Skill, NutritionGuide


class SkillSerializer(serializers.ModelSerializer):
    status = serializers.SerializerMethodField()
    support_text = serializers.SerializerMethodField()
    age_range = serializers.SerializerMethodField()
    nutrition_tips = serializers.SerializerMethodField()

    class Meta:
        model = Skill
        fields = [
            'id',
            'name',
            'description',
            'min_age_months',
            'max_age_months',
            'age_range',
            'status',
            'support_text',
            'icon',
            'nutrition_tips',
        ]

    def get_age_range(self, obj):
        return f"{obj.min_age_months}–{obj.max_age_months} měsíců"

    def get_status(self, obj):
        show_status = self.context.get("show_status", False)
        age = self.context.get("age")

        if not show_status or age is None:
            return None

        if age < obj.min_age_months:
            return "🔵 Ještě před vámi"
        elif age > obj.max_age_months:
            return "🟡 Mimo obvyklé rozpětí"
        else:
            return "🟢 V normě"

    def get_support_text(self, obj):
        show_status = self.context.get("show_status", False)
        age = self.context.get("age")

        if not show_status or age is None:
            return None

        if age < obj.min_age_months:
            return "Každé dítě má vlastní tempo. Brzy přijde čas na tento krok."
        elif age > obj.max_age_months:
            return "Možná stojí za to poradit se s pediatrem, ale neznamená to problém."
        else:
            return "Každé dítě má vlastní tempo. Ještě máte čas."

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