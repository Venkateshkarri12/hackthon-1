import csv
patients = {}

def add_patient():
    patient_id = input("Enter patient ID: ")
    if patient_id in patients:
        print("Patient ID already exists!\n")
        return
    name = input("Enter patient name: ")
    age = input("Enter patient age: ")
    gender = input("Enter patient gender: ")
    diagnosis = input("Enter diagnosis: ")

    patients[patient_id] = {
        "name": name,
        "age": int(age),
        "gender": gender,
        "diagnosis": diagnosis,
        "last_checkup_date": "today"     }
    print("Patient added successfully!\n")

def view_reports():
    if not patients:
        print("No patient data available.\n")
        return

    for patient_id, details in patients.items():
        print(f"ID: {patient_id}, Name: {details['name']}, Age: {details['age']}, Gender: {details['gender']}, "
              f"Diagnosis: {details['diagnosis']}, Last Checkup: {details['last_checkup_date']}\n")

def update_report():
    patient_id = input("Enter patient ID to update: ")

    if patient_id in patients:
        new_diagnosis = input("Enter new diagnosis: ")
        patients[patient_id]["diagnosis"] = new_diagnosis
        patients[patient_id]["last_checkup_date"] = "today"  
        print("Report updated successfully!\n")
    else:
        print("Patient ID not found.\n")

def delete_patient():
    patient_id = input("Enter patient ID to delete: ")

    if patient_id in patients:
        del patients[patient_id]
        print("Patient record deleted successfully!\n")
    else:
        print("Patient ID not found.\n")

def search_patient():
    search_key = input("Enter patient name or ID to search: ")
    found = False
    for patient_id, details in patients.items():
        if search_key.lower() in patient_id.lower() or search_key.lower() in details['name'].lower():
            print(f"ID: {patient_id}, Name: {details['name']}, Age: {details['age']}, Gender: {details['gender']}, "
                  f"Diagnosis: {details['diagnosis']}, Last Checkup: {details['last_checkup_date']}\n")
            found = True
    if not found:
        print("No matching patient found.\n")

def health_summary():
    if not patients:
        print("No patient data available.\n")
        return

    total_patients = len(patients)
    male_patients = len([p for p in patients.values() if p['gender'].lower() == 'male'])
    female_patients = len([p for p in patients.values() if p['gender'].lower() == 'female'])
    avg_age = sum(p['age'] for p in patients.values()) / total_patients
    diagnoses = [p['diagnosis'] for p in patients.values()]
    common_diagnosis = max(set(diagnoses), key=diagnoses.count)

    print(f"Total Patients: {total_patients}")
    print(f"Male Patients: {male_patients}")
    print(f"Female Patients: {female_patients}")
    print(f"Average Age: {avg_age:.2f}")
    print(f"Most Common Diagnosis: {common_diagnosis}\n")

def export_data():
    filename = input("Enter filename to export data (with .csv extension): ")
    try:
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['ID', 'Name', 'Age', 'Gender', 'Diagnosis', 'Last Checkup Date'])
            for patient_id, details in patients.items():
                writer.writerow([patient_id, details['name'], details['age'], details['gender'],
                                 details['diagnosis'], details['last_checkup_date']])
        print("Data exported successfully!\n")
    except Exception as e:
        print(f"An error occurred while exporting data: {e}\n")

def import_data():
    filename = input("Enter filename to import data from (with .csv extension): ")
    try:
        with open(filename, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                patients[row['ID']] = {
                    "name": row['Name'],
                    "age": int(row['Age']),
                    "gender": row['Gender'],
                    "diagnosis": row['Diagnosis'],
                    "last_checkup_date": row['Last Checkup Date']
                }
        print("Data imported successfully!\n")
    except Exception as e:
        print(f"An error occurred while importing data: {e}\n")

def advanced_search():
    print("Advanced Search Options:")
    print("1. Search by Age Range")
    print("2. Search by Gender")
    print("3. Search by Diagnosis")
    choice = input("Enter your choice: ")

    if choice == '1':
        min_age = int(input("Enter minimum age: "))
        max_age = int(input("Enter maximum age: "))
        for patient_id, details in patients.items():
            if min_age <= details['age'] <= max_age:
                print(f"ID: {patient_id}, Name: {details['name']}, Age: {details['age']}, "
                      f"Gender: {details['gender']}, Diagnosis: {details['diagnosis']}, "
                      f"Last Checkup: {details['last_checkup_date']}\n")

    elif choice == '2':
        gender = input("Enter gender (Male/Female): ")
        for patient_id, details in patients.items():
            if details['gender'].lower() == gender.lower():
                print(f"ID: {patient_id}, Name: {details['name']}, Age: {details['age']}, "
                      f"Gender: {details['gender']}, Diagnosis: {details['diagnosis']}, "
                      f"Last Checkup: {details['last_checkup_date']}\n")

    elif choice == '3':
        diagnosis = input("Enter diagnosis: ")
        for patient_id, details in patients.items():
            if diagnosis.lower() in details['diagnosis'].lower():
                print(f"ID: {patient_id}, Name: {details['name']}, Age: {details['age']}, "
                      f"Gender: {details['gender']}, Diagnosis: {details['diagnosis']}, "
                      f"Last Checkup: {details['last_checkup_date']}\n")

    else:
        print("Invalid choice! Please try again.\n")

def main():
    while True:
        print("1. Add Patient")
        print("2. View Reports")
        print("3. Update Report")
        print("4. Delete Patient")
        print("5. Search Patient")
        print("6. Advanced Search")
        print("7. Health Summary")
        print("8. Export Data")
        print("9. Import Data")
        print("10. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_patient()
        elif choice == '2':
            view_reports()
        elif choice == '3':
            update_report()
        elif choice == '4':
            delete_patient()
        elif choice == '5':
            search_patient()
        elif choice == '6':
            advanced_search()
        elif choice == '7':
            health_summary()
        elif choice == '8':
            export_data()
        elif choice == '9':
            import_data()
        elif choice == '10':
            print("Exiting the system.")
            break
        else:
            print("Invalid choice! Please try again.\n")

if __name__ == "__main__":
    main()

