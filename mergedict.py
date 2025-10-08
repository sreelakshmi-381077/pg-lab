contacts1 = {
    "Anu": "9847304752",
    "Teena":"9947128793"
}
contacts2 = {
    "Anu": "9847128793",
    "Teena":"8765432561"
}
print("contacts1:",contacts1)
print("contacts2:",contacts2)
merged_contacts=contacts1.copy()
merged_contacts.update(contacts2)
print("Merged contacts:")
print(merged_contacts)