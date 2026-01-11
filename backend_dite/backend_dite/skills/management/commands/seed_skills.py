from django.core.management.base import BaseCommand
from skills.models import Skill



class Command(BaseCommand):
    help = "Seed vývojových dovedností 0–18 měsíců"

    def handle(self, *args, **kwargs):

        skills_data = [

        # 🟢 MOTORIKA
        {
            "name": "Zvedá hlavu na bříšku",
            "description": "Krátce zvedá a drží hlavu vleže na bříšku.",
            "min_age_months": 0,
            "max_age_months": 2,
            "category": "motor",
            "icon": "premium_photo-1668806642968-c6bebdab7c4c.avif",

        },
        {
            "name": "Opírá se o lokty",
            "description": "Na bříšku se opírá o lokty a drží hlavu stabilně.",
            "min_age_months": 2,
            "max_age_months": 4,
            "category": "motor",
            "icon": "tummy-time-for-baby.jpg"
        },
        {
            "name": "Otáčí se",
            "description": "Přetáčí se ze zad na bok a později na bříško.",
            "min_age_months": 3,
            "max_age_months": 6,
            "category": "motor",
            "icon": "9268448c-01fd-421c-b475-8e2714eb5768.png"
        },
        {
            "name": "Sedí s oporou",
            "description": "Sedí s podporou rodiče nebo polštáře.",
            "min_age_months": 5,
            "max_age_months": 9,
            "category": "motor",
            "icon": "Baby-Bottom-Shuffling-768x525.webp"
        },
        {
            "name": "Sedá si z polohy na čtyřech",
            "description": "Z polohy na čtyřech se samostatně posadí bez pomoci dospělého.",
            "min_age_months": 8,
            "max_age_months": 12,
            "category": "motor",
            "icon": "5be7817a-ca76-4f17-bedb-86b444e9c079-md.jpeg"
        },
        {
            "name": "Leze po čtyřech",
            "description": "Pohybuje se vpřed na dlaních a kolenou (klasické lezení).",
            "min_age_months": 7,
            "max_age_months": 11,
            "category": "motor",
            "icon": "pngtree-happy-baby-crawling-on-knees-child-photo-png-image_13775196.png"
        },
        {
            "name": "Sedí bez opory",
            "description": "Sedí stabilně bez podpory.",
            "min_age_months": 6,
            "max_age_months": 10,
            "category": "motor",
            "icon": "OIP (4).webp"
        },
        {
            "name": "Leze / plazí se",
            "description": "Pohybuje se lezením nebo plazením.",
            "min_age_months": 6,
            "max_age_months": 10,
            "category": "motor",
            "icon": "OIP (3).webp"
        },
        {
            "name": "Stojí u opory",
            "description": "Postaví se a stojí u nábytku.",
            "min_age_months": 8,
            "max_age_months": 12,
            "category": "motor",
            "icon": "51fvWhiy0QL._AC_SX466_.jpg"
        },
        {
            "name": "Chodí podél nábytku",
            "description": "Pohybuje se podél nábytku s oporou.",
            "min_age_months": 9,
            "max_age_months": 15,
            "category": "motor",
            "icon": "shutterstock_681367789.jpg"


        },
        {
            "name": "Chodí samostatně",
            "description": "Chodí bez opory, stabilita se postupně zlepšuje.",
            "min_age_months": 11,
            "max_age_months": 18,
            "category": "motor",
            "icon": "premium_photo-1668060124844-be33c27f9448.avif"
        },
        {
            "name": "Jízda na tříkolce",
            "description": "Ve 4 letech děti mohou jezdit na tříkolce a hrát pohybové hry s prvky týmových akcí.",
            "min_age_months": 48,
            "max_age_months": 54,
            "category": "motor",
            "icon": "637261c7aa204f4a34b063de_best-bikes-for-infants.jpeg"
        },

        # 🟣 ŘEČ
       {
            "name": "Stavění vět z 3-4 slov",
            "description": "Ve 3 letech děti začínají aktivně vytvářet věty ze 3-4 slov. Mohou klást jednoduché otázky, jako \"Co to je?\" nebo \"Kde je maminka?\".",
            "min_age_months": 36,
            "max_age_months": 48,
            "category": "speech",
            "icon": "rompecabezas-silueta-humana_1308-127027.avif"

        },
        {
            "name": "Používání složitějších vět",
            "description": "Ve 4 letech děti používají složitější věty a začínají formulovat své myšlenky složitějšími konstrukcemi. Aktivně rozšiřují svou slovní zásobu.",
            "min_age_months": 48,
            "max_age_months": 60,
            "category": "speech",
            "icon": "OIP.webp"
        },
        {
            "name": "Pochopení otázek s rozvinutými odpověďmi",
            "description": "Od 3 do 4,5 let děti začínají rozumět otázkám, které vyžadují rozvinutou odpověď, a mohou již recitovat básně, písničky a vyprávět příběhy.",
            "min_age_months": 36,
            "max_age_months": 54,
            "category": "speech",
            "icon": "1-18-theory-of-mind.jpg"
        },
        {
            "name": "Reaguje na zvuky",
            "description": "Otáčí hlavu ke zvuku, naslouchá.",
            "min_age_months": 0,
            "max_age_months": 3,
            "category": "speech",
            "icon": "1-18-theory-of-mind.jpg"
        },
        {
            "name": "Žvatlá",
            "description": "Opakuje slabiky (ba, da, ma).",
            "min_age_months": 4,
            "max_age_months": 10,
            "category": "speech",
            "icon": "OIP.webp"
        },
        {
            "name": "Říká první slova",
            "description": "Používá smysluplná slova (mama, tata, dej).",
            "min_age_months": 9,
            "max_age_months": 15,
            "category": "speech",
            "icon": "illustration-of-kids-background_29937-200.avif"
        },

        # 🔵 SOCIÁLNÍ
        {
            "name": "Usmívá se na rodiče",
            "description": "Sociální úsměv jako reakce na blízké.",
            "min_age_months": 1,
            "max_age_months": 3,
            "category": "social",
            "icon": "Physical-Development-3-6-Months-683x1024.png"
        },
        {
            "name": "Bojí se cizích lidí",
            "description": "Projevuje úzkost z cizích osob.",
            "min_age_months": 6,
            "max_age_months": 10,
            "category": "social",
            "icon": "9ce39f8b-2b6f-4b8e-ab62-7bbbe32dd6e5.png"
        },
        {
            "name": "Napodobuje dospělé",
            "description": "Napodobuje gesta a jednoduché činnosti.",
            "min_age_months": 9,
            "max_age_months": 15,
            "category": "social",
            "icon": "baby-boy-mother-play-together-28987471.webp"
        },
        {
            "name": "Hraje si s jinými dětmi",
            "description": "Ve 3 letech dítě začíná hrát s jinými dětmi a rozvíjí základní sociální dovednosti, učí se sdílet hračky.",
            "min_age_months": 36,
            "max_age_months": 48,
            "category": "social",
            "icon": "R.jpg"
        },
            #kognitivní
        {
            "name": "Chápání abstraktních pojmů",
            "description": "Od 3 do 4 let děti začínají chápat abstraktní pojmy jako čas, barvy a tvary. Mohou třídit věci podle kategorií.",
            "min_age_months": 36,
            "max_age_months": 48,
            "category": "cognitive",
            "icon": "rompecabezas-silueta-humana_1308-127027.avif"
        },
        {
            "name": "Chápání příčinných souvislostí",
            "description": "Ve 4,5 letech děti začínají chápat příčinné souvislosti a mohou provádět jednoduché experimenty, jako je řešení úkolů na sčítání a odčítání pomocí hraček.",
            "min_age_months": 54,
            "max_age_months": 66,
            "category": "cognitive",
            "icon": "pngtree-fine-motor-skill-clipart-boy-playing-with-toys-vector-cartoon-png-image_12163511.png"
        }

        ]

        # Перебираем каждый элемент в списке и создаем или обновляем записи в базе данных
        for skill in skills_data:
            skill_obj, created = Skill.objects.update_or_create(
                name=skill["name"],
                defaults=skill
            )

            if created:
                self.stdout.write(self.style.SUCCESS(f"✅ Skill '{skill_obj.name}' was created"))
            else:
                self.stdout.write(self.style.SUCCESS(f"🔄 Skill '{skill_obj.name}' was updated"))

        self.stdout.write(self.style.SUCCESS("✅ Vývojové dovednosti úspěšně vloženy"))