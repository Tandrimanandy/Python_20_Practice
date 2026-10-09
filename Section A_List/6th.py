'''
Question 6: Hospital Patient Queue
A hospital maintains a list of patients waiting for consultation.
 Write a function that removes the first patient after consultation, adds a new patient to the queue, and displays the updated queue.
'''

def update_queue(queue, new_patient):
    if queue:
        served = queue.pop(0)
        print(f"Consultation completed for: {served}")
    queue.append(new_patient)
    print(f"Added to queue: {new_patient}")

    print("Updated queue:")
    for position, patient in enumerate(queue, start=1):
        print(f"  {position}. {patient}")

patients = ["Tandrima", "Rudra", "Sudipa", "Drubo"]
update_queue(patients, input("Enter the name :"))
print()
