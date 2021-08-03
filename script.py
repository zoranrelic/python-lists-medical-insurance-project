names = ["Mohamed", "Sara", "Xia", "Paul", "Valentina", "Jide", "Aaron", "Emily", "Nikita", "Paul"]
insurance_costs = [13262.0, 4816.0, 6839.0, 5054.0, 14724.0, 5360.0, 7640.0, 6072.0, 2750.0, 12064.0]

# Dodana Priscilla
names.append("Priscilla")
insurance_costs.append(8320.0)

medical_records = list(zip(insurance_costs, names))
num_medical_records = len(medical_records)
print(medical_records)

print("\nThere are " + str(num_medical_records) + " medical records.")

first_medical_record = medical_records[0]

cheapest_three = sorted(medical_records)

occurences_paul = names.count("Paul")

#prvi entry

print("\nHere is the first medical record: " + str(first_medical_record))

#sortirano po cijeni osiguranja

print("\nHere are the medical records sorted by insurance cost: " + str(sorted(medical_records)))

#tri najjeftinija osiguranja

print("\nHere are the three cheapest insurance costs in our medical records: " + str(cheapest_three[0:3]))

#tri najskuplja

print("\nHere are the three expensive insurance costs in our medical records: " + str(cheapest_three[-3:]))

#koliko je dupliciranih po imenu Paul

print("\nThere are " + str(occurences_paul) + " individuals with the name Paul in our medical records.")
