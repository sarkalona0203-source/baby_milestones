from django.core.management.base import BaseCommand
from skills.models import NutritionGuide


class Command(BaseCommand):
    help = "Seed výživových doporučení pro děti 0–12 měsíců"

    def handle(self, *args, **kwargs):

        nutrition_data = [

            # 0–4 měsíce
            {
                "min_age_months": 0,
                "max_age_months": 4,
                "title": "Mateřské mléko nebo umělá výživa",
                "text": "Dítě by mělo být výhradně kojeno nebo krmeno umělou výživou. Pevná strava ani příkrmy se zatím nedoporučují.",
                "type": "feeding"
            },

            # 5–6 měsíců – začátek příkrmů
            {
                "min_age_months": 5,
                "max_age_months": 6,
                "title": "Začátek příkrmů",
                "text": "Od 5.–6. měsíce lze začít s příkrmy. Nejvhodnější jsou hladká zeleninová pyré bez soli a cukru. Příkrm je doplňkem, hlavní výživou zůstává mléko.",
                "type": "feeding"
            },
            {
                "min_age_months": 6,
                "max_age_months": 6,
                "title": "Množství příkrmu",
                "text": "V 6 měsících dítě obvykle sní přibližně 50–150 g příkrmu denně. Zbytek denního příjmu tvoří mateřské mléko nebo umělá výživa.",
                "type": "feeding"
            },

            # 7–8 měsíců
            {
                "min_age_months": 7,
                "max_age_months": 8,
                "title": "Hutnější konzistence",
                "text": "Postupně lze zvyšovat hustotu příkrmů. Dítě se učí pracovat s lžičkou a novými chutěmi.",
                "type": "feeding"
            },

            # kousky
            {
                "min_age_months": 8,
                "max_age_months": 10,
                "title": "Kousky v jídle",
                "text": "Od 8. měsíce lze postupně zavádět měkké kousky jídla. Dítě se učí kousat a žvýkat. Kousky musí být dobře měkké a malé.",
                "type": "feeding"
            },

            # těstoviny
            {
                "min_age_months": 8,
                "max_age_months": 12,
                "title": "Těstoviny",
                "text": "Malé těstoviny lze podávat přibližně od 8–9 měsíců. Musí být dobře uvařené, bez soli a omáček, ideálně rozmačkané nebo velmi měkké.",
                "type": "warning"
            },

            # varování – med
            {
                "min_age_months": 0,
                "max_age_months": 12,
                "title": "Pozor na med",
                "text": "Med se nesmí podávat dětem do 1 roku kvůli riziku dětského botulismu.",
                "type": "warning"
            },

            # varování – houby, mléko
            {
                "min_age_months": 0,
                "max_age_months": 12,
                "title": "Nevhodné potraviny",
                "text": "Nevhodné jsou houby, celé ořechy, sůl, cukr a kravské mléko jako nápoj. Kravské mléko lze používat pouze v malém množství při vaření.",
                "type": "warning"
            },
            # 12–15 měsíců
            {
                "min_age_months": 12,
                "max_age_months": 15,
                "title": "Přechod na běžnou stravu",
                "text": "Dítě jí měkkou běžnou stravu rodičů. Doporučeno 3 jídla denně + mléko dle potřeby. Porce cca 200–250 g jídla.",
                "type": "feeding"
            },
            # 15–18 měsíců
            {
                "min_age_months": 15,
                "max_age_months": 18,
                "title": "Postupné zvyšování porcí",
                "text": "Dítě jí téměř běžnou stravu, kousky musí být měkké a malé. Doporučeno 3–4 jídla denně + mléko dle potřeby. Porce cca 250–300 g jídla.",
                "type": "feeding"
            },            # varování – tvrdé ořechy a syrová vejce
            {
                "min_age_months": 0,
                "max_age_months": 18,
                "title": "Pozor na některé potraviny",
                "text": "Tvrdé ořechy a syrová vejce nejsou vhodné do 18 měsíců. Vždy dávejte měkké a bezpečné varianty.",
                "type": "warning"
            }
        ]

        for item in nutrition_data:
            obj, created = NutritionGuide.objects.update_or_create(
                title=item["title"],
                defaults=item
            )

            if created:
                self.stdout.write(self.style.SUCCESS(f"✅ {obj.title} vytvořeno"))
            else:
                self.stdout.write(self.style.SUCCESS(f"🔄 {obj.title} aktualizováno"))

        self.stdout.write(self.style.SUCCESS("✅ Výživová doporučení úspěšně vložena"))