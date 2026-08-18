import datetime
import os
# Για να ανοίξει το .txt αρχείο
from fpdf import FPDF, XPos, YPos


# 1: Materials Data Base
# Cost: € / unit 
# Carbon : kg CO2 / unit

print('Welcome to Carbon Calculator!')
materials_data = {
    '1': {
            'name' : 'Σκυρόδεμα C25/30',
            'unit' : 'm3',
            'cost_per_unit' : 105.0,
            'carbon_per_unit' : 310.0,
    },

    '2': {
            'name' : 'Σκυρόδεμα C30/37 (Eco-Cement)',
            'unit' : 'm3',
            'cost_per_unit' : 120.0,
            'carbon_per_unit' : 220.0,
    },
    '3': {
            'name' : 'Χάλυβας B500C (Πρωτογενής)',
            'unit' : 'kg',
            'cost_per_unit' : 1.10,
            'carbon_per_unit' : 1.90,
    },

    '4' : {
        "name": "Τσιμεντοκονία (Επίχρισμα)",
        "cost_per_unit": 12.0,
        "carbon_per_unit": 18.0,
        "unit": "m2",
    },
    "5": {
        "name": "Ξυλεία Καλουπιών",
        "cost_per_unit": 220.0,
        "carbon_per_unit": 110.0,
        "unit": "m3",
    },
    "6": {
        "name": "Διογκωμένη Πολυστερίνη (EPS 100)",
        "cost_per_unit": 65.0,
        "carbon_per_unit": 75.0,
        "unit": "m3",
    },
    "7": {
        "name": "Πετροβάμβακας 50mm",
        "cost_per_unit": 8.50,
        "carbon_per_unit": 4.20,
        "unit": "m2",
    },
    "8": {
        "name": "Άσφαλτος",
        "cost_per_unit": 18.0,
        "carbon_per_unit": 22.0,
        "unit": "m2",
    },

    "9": {
        "name": "Γυψοσανίδες Standard 12.5mm",
        "cost_per_unit": 5.20,
        "carbon_per_unit": 2.80,
        "unit": "m2",
    },
    "10": {
        "name": "Κουφώματα Αλουμινίου (με Διπλά Τζάμια)",
        "cost_per_unit": 280.0,
        "carbon_per_unit": 45.0,
        "unit": "m2",
    }

}

#2 List for storing user's pereferences

project_materials = []

def display_menu():
    '''Εμφανίζει τα διαθέσιμα υλικά.'''
    print('\n=== ΔΙΑΘΕΣΙΜΑ ΥΛΙΚΑ ===')
    for key, item in materials_data.items():
        print(f'{key}. {item['name']} ({item['cost_per_unit']} EUR / {item['unit']}, {item['carbon_per_unit']}kg CO2/ {item['unit']})')

def add_material():
    '''Προσθέτει ένα υλικό στο έργο του χρήστη'''
    display_menu()
    choice = input('\n Επιλέξτε αριθμό υλικού (1-10) ή ''0'' για ολοκλήρωση: ').strip()

    if choice == '0':
        return choice


    if choice in materials_data:
        selected = materials_data[choice]
        try: 
            quantity = float(input(f'Εισάγετε ποσότητα σε {selected['unit']}: '))

            if quantity <= 0:
                print('Η ποσότητα πρέπει να είναι θετικός αριθμός.')
                return choice

            # Υπολογισμοί για το συγκεκριμένο υλικό
            item_cost = quantity * selected['cost_per_unit']
            item_carbon = quantity * selected['carbon_per_unit']

            found = False
            for entry in project_materials:
                if entry["name"] == selected["name"]:
                    entry["quantity"] += quantity
                    entry["total_cost"] += item_cost
                    entry["total_carbon"] += item_carbon
                    found = True
                    break

            if not found:
                materials_entry = {
                    'name': selected['name'],
                    'quantity' : quantity,
                    'unit' : selected['unit'],
                    'total_cost' : item_cost,
                    'total_carbon' : item_carbon 
                }

                project_materials.append(materials_entry)
            print(f'Προστέθηκε : {selected['name']} | {quantity} {selected['unit']} | Κόστος¨{item_cost:.2f} EUR | CO2: {item_carbon:.2f} kg')
        except ValueError:
            print('Λάθος καταχώρηση. Παρακαλώ εισάγετε αριθμό.')
    else:
        print('Μη έγκυρη επιλογή υλικού.')

    return choice

project_info = {}


def get_project_info():
    """Ζητάει τα βασικά στοιχεία του έργου από τον χρήστη"""
    print("=" * 50)
    print("      ΕΙΣΑΓΩΓΗ ΣΤΟΙΧΕΙΩΝ ΝΕΟΥ ΕΡΓΟΥ      ")
    print("=" * 50)

    project_info["title"] = (
        input("Όνομα / Τίτλος Έργου: ").strip() or "Ανώνυμο Έργο"
    )
    project_info["owner"] = (
        input("Κύριος του Έργου (Πελάτης): ").strip() or "Μη ορισμένος"
    )
    project_info["engineer"] = (
        input("Μηχανικός / Μελετητής: ").strip() or "Μη ορισμένος"
    )
    project_info["location"] = (
        input("Τοποθεσία Έργου: ").strip() or "Μη ορισμένη"
    )

    # Προσθήκη επιφάνειας κτιρίου σε τ.μ.
    while True:
        try:
            area_input = input("Συνολική Επιφάνεια Κτιρίου (m²): ").strip()
            area = float(area_input)
            if area > 0:
                project_info["area"] = area
                break
            print("❌ Η επιφάνεια πρέπει να είναι θετικός αριθμός.")
        except ValueError:
            print("❌ Παρακαλώ εισάγετε έγκυρο αριθμό.")

    date_input = input("Ημερομηνία (Enter για σημερινή): ").strip()
    if not date_input:
        project_info["date"] = datetime.datetime.now().strftime("%d/%m/%Y")
    else:
        project_info["date"] = date_input

    print("\n✅ Τα στοιχεία του έργου καταχωρήθηκαν!\n")



def generate_report():
    """Δημιουργία και εξαγωγή αναφοράς σε PDF"""
    pdf = FPDF()
    pdf.add_page()

    font_path = "C:\\Windows\\Fonts\\arial.ttf"
    if os.path.exists(font_path):
        pdf.add_font("ArialGreek", "", font_path)
        pdf.set_font("ArialGreek", size=11)
    else:
        pdf.set_font("Helvetica", size=11)

    # 1. ΤΙΤΛΟΣ
    pdf.set_font_size(16)
    pdf.cell(
        0,
        10,
        "ΤΕΛΙΚΗ ΑΝΑΦΟΡΑ ΕΡΓΟΥ - EMBODIED CARBON & COST",
        new_x=XPos.LMARGIN,
        new_y=YPos.NEXT,
        align="C",
    )
    pdf.ln(5)

    # 2. ΣΤΟΙΧΕΙΑ ΕΡΓΟΥ (Περιλαμβάνει πλέον και τα m²)
    pdf.set_font_size(12)
    pdf.cell(
        0,
        8,
        "--- Γενικά Στοιχεία Έργου ---",
        new_x=XPos.LMARGIN,
        new_y=YPos.NEXT,
    )
    pdf.set_font_size(10)
    pdf.cell(
        0,
        6,
        f"Τίτλος Έργου: {project_info.get('title')}",
        new_x=XPos.LMARGIN,
        new_y=YPos.NEXT,
    )
    pdf.cell(
        0,
        6,
        f"Κύριος του Έργου: {project_info.get('owner')}",
        new_x=XPos.LMARGIN,
        new_y=YPos.NEXT,
    )
    pdf.cell(
        0,
        6,
        f"Μελετητής: {project_info.get('engineer')}",
        new_x=XPos.LMARGIN,
        new_y=YPos.NEXT,
    )
    pdf.cell(
        0,
        6,
        f"Τοποθεσία: {project_info.get('location')}",
        new_x=XPos.LMARGIN,
        new_y=YPos.NEXT,
    )
    pdf.cell(
        0,
        6,
        f"Επιφάνεια Κτιρίου: {project_info.get('area'):,.2f} m²",
        new_x=XPos.LMARGIN,
        new_y=YPos.NEXT,
    )
    pdf.cell(
        0,
        6,
        f"Ημερομηνία: {project_info.get('date')}",
        new_x=XPos.LMARGIN,
        new_y=YPos.NEXT,
    )
    pdf.ln(5)

    # 3. ΒΑΣΗ ΔΕΔΟΜΕΝΩΝ ΥΛΙΚΩΝ
    pdf.set_font_size(12)
    pdf.cell(
        0,
        8,
        "--- Βάση Δεδομένων Υλικών & Προδιαγραφών ---",
        new_x=XPos.LMARGIN,
        new_y=YPos.NEXT,
    )
    pdf.set_font_size(9)
    for key, item in materials_data.items():
        line = f"{key:>2}. {item['name']} | {item['cost_per_unit']:.2f} EUR/{item['unit']} | {item['carbon_per_unit']:.2f} kg CO2/{item['unit']}"
        pdf.cell(0, 5, line, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.ln(5)

    # 4. ΠΙΝΑΚΑΣ ΕΠΙΛΕΓΜΕΝΩΝ ΥΛΙΚΩΝ & ECO-SCORE
    pdf.set_font_size(12)
    pdf.cell(
        0,
        8,
        "--- Αναλυτικός Πίνακας Επιλεγμένων Υλικών Έργου ---",
        new_x=XPos.LMARGIN,
        new_y=YPos.NEXT,
    )
    pdf.set_font_size(10)

    if not project_materials:
        pdf.cell(
            0,
            6,
            "Δεν καταχωρήθηκε κανένα υλικό.",
            new_x=XPos.LMARGIN,
            new_y=YPos.NEXT,
        )
    else:
        total_cost = 0.0
        total_carbon = 0.0

        for entry in project_materials:
            line = f"• {entry['name']}: {entry['quantity']} {entry['unit']} | Κόστος: {entry['total_cost']:.2f} EUR | CO2: {entry['total_carbon']:.2f} kg"
            pdf.cell(0, 6, line, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
            total_cost += entry["total_cost"]
            total_carbon += entry["total_carbon"]

        # Υπολογισμός Eco-Score
        area = project_info.get("area", 1)
        carbon_per_sqm, eco_rating = calculate_eco_score(total_carbon, area)

        pdf.ln(4)
        pdf.set_font_size(11)
        pdf.cell(
            0,
            7,
            f"ΣΥΝΟΛΙΚΟ ΚΟΣΤΟΣ: {total_cost:,.2f} EUR ({total_cost/area:.2f} EUR/m²)",
            new_x=XPos.LMARGIN,
            new_y=YPos.NEXT,
        )
        pdf.cell(
            0,
            7,
            f"ΣΥΝΟΛΙΚΟ CO2: {total_carbon:,.2f} kg ({total_carbon/1000:.2f} τόνοι)",
            new_x=XPos.LMARGIN,
            new_y=YPos.NEXT,
        )
        pdf.cell(
            0,
            7,
            f"ΕΝΤΑΣΗ ΑΝΘΡΑΚΑ: {carbon_per_sqm:.2f} kg CO2/m²",
            new_x=XPos.LMARGIN,
            new_y=YPos.NEXT,
        )
        pdf.cell(
            0,
            7,
            f"ECO-SCORE ΚΤΙΡΙΟΥ: {eco_rating}",
            new_x=XPos.LMARGIN,
            new_y=YPos.NEXT,
        )

    filename = "project_report.pdf"
    pdf.output(filename)
    print(f"\n📄 Η αναφορά PDF δημιουργήθηκε: '{filename}'")
    os.startfile(filename)

def calculate_eco_score(total_carbon, building_area):
    """Υπολογίζει την περιβαλλοντική κατηγορία βάσει kg CO2/m²"""
    if building_area <= 0:
        return 0, "N/A"

    carbon_per_sqm = total_carbon / building_area

    if carbon_per_sqm < 150:
        rating = "A+ (Πολύ χαμηλό αποτύπωμα / Sustainable)"
    elif carbon_per_sqm < 300:
        rating = "A (Χαμηλό αποτύπωμα)"
    elif carbon_per_sqm < 500:
        rating = "B (Τυπική Κατασκευή)"
    else:
        rating = "C (Υψηλό Αποτύπωμα Άνθρακα)"

    return carbon_per_sqm, rating

get_project_info()

while True:
    user_choice = add_material()
    if user_choice == '0':
        break
   
generate_report()




