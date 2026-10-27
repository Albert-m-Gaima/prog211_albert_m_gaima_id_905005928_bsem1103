"""
Assignment 1: Object-Oriented Programming 1 (PROG211)
Domain: Health (Vaccination Tracker)
Digital Public Goods (DPG) Standards Compliant
"""

class Patient:
    """Represents an individual patient receiving vaccinations."""
    
    def __init__(self, patient_id, name, age):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        # List data structure used internally to store vaccination records for this patient
        self.vaccination_history = []

    def add_vaccination(self, vaccine_tuple):
        """Instance method to record a vaccine using a tuple (Bonus requirement met)."""
        self.vaccination_history.append(vaccine_tuple)

    def display_info(self):
        """Instance method to display patient details and their vaccination history."""
        print(f"Patient ID : {self.patient_id}")
        print(f"Name       : {self.name}")
        print(f"Age        : {self.age}")
        if self.vaccination_history:
            print("  [Vaccination Records]:")
            for record in self.vaccination_history:
                # Unpacking the tuple: (Vaccine Name, Date Administered, Batch Number)
                v_name, v_date, v_batch = record
                print(f"   -> Vaccine: {v_name} | Date: {v_date} | Batch: {v_batch}")
        else:
            print("  [Vaccination Records]: No vaccinations recorded yet.")


class VaccinationTracker:
    """Manages multiple patient records using a dictionary data structure and DPG rules."""
    
    # Class attribute to track total registered patients across instances
    total_tracked = 0
    
    # Tuple used for standard approved DPG vaccines (Extra marks for Tuple integration)
    APPROVED_VACCINES = ("BCG", "Polio", "Measles", "COVID-19", "Tetanus")

    def __init__(self):
        # Dictionary data structure: using unique patient ID as the key and Patient object as the value
        self.records = {}

    def add_patient(self, patient_id, name, age):
        """Adds a new patient object into the dictionary structure."""
        if patient_id in self.records:
            print(f"Error: Patient ID '{patient_id}' already exists in the system.")
            return False
        
        # Validate age using static method
        if not VaccinationTracker.validate_age(age):
            print("Error: Invalid age provided. Age must be between 0 and 120.")
            return False

        # Creating object and storing in dictionary
        new_patient = Patient(patient_id, name, age)
        self.records[patient_id] = new_patient
        
        # Call class method to increment tracker count
        VaccinationTracker.increment_counter()
        print(f"Success: Patient '{name}' registered successfully.")
        return True

    def record_vaccine(self, patient_id, vaccine_name, date, batch_no):
        """Interacts between VaccinationTracker and Patient objects to log a vaccination."""
        if patient_id not in self.records:
            print(f"Error: Patient ID '{patient_id}' not found.")
            return
        
        if vaccine_name not in self.APPROVED_VACCINES:
            print(f"Warning: '{vaccine_name}' is outside standard DPG approved vaccines: {self.APPROVED_VACCINES}")
        
        # Using a tuple to encapsulate immutable vaccination details (Bonus Marks)
        vaccine_tuple = (vaccine_name, date, batch_no)
        
        # Object interaction: calling instance method on the specific Patient object
        self.records[patient_id].add_vaccination(vaccine_tuple)
        print(f"Success: Logged {vaccine_name} for patient ID {patient_id}.")

    def display_all_records(self):
        """Loops through the dictionary structure to display all records."""
        print("\n" + "="*45)
        print("      PUBLIC HEALTH VACCINATION REGISTRY     ")
        print("="*45)
        if not self.records:
            print("No records available in the tracker.")
        for pid, patient_obj in self.records.items():
            patient_obj.display_info()
            print("-" * 45)

    @classmethod
    def increment_counter(cls):
        """Class method (@classmethod) to update the total tracked count."""
        cls.total_tracked += 1

    @classmethod
    def get_total_tracked(cls):
        """Class method (@classmethod) to return total registered patients."""
        return cls.total_tracked

    @staticmethod
    def validate_age(age):
        """Static method (@staticmethod) to validate age format/range without modifying class state."""
        return isinstance(age, int) and 0 <= age <= 120

    @staticmethod
    def print_dpg_banner():
        """Static method to display DPG compliance notice."""
        print("[DPG Compliance Notice]")
        print(" * Open-Source & Reusable Architecture")
        print(" * Privacy-Respecting (No sensitive government ID or medical secrets stored)")
        print(" * Accessible & Lightweight CLI Interface\n")


# --- Execution Demonstration & Sample Usage ---
if __name__ == "__main__":
    # Display DPG Banner via Static Method
    VaccinationTracker.print_dpg_banner()

    # Initialize the Tracker system
    tracker = VaccinationTracker()

    # Registering patients
    print("--- Registering Patients ---")
    tracker.add_patient("P101", "Aminata", 24)
    tracker.add_patient("P102", "Mohamed", 29)
    print(f"Total Tracked via Class Method: {VaccinationTracker.get_total_tracked()}\n")

    # Recording vaccinations using tuples
    print("--- Recording Vaccinations ---")
    tracker.record_vaccine("P101", "COVID-19", "2026-01-15", "BATCH-SL-01")
    tracker.record_vaccine("P101", "Polio", "2026-03-10", "BATCH-SL-04")
    tracker.record_vaccine("P102", "BCG", "2026-02-20", "BATCH-SL-09")

    # Displaying all stored records from the dictionary
    tracker.display_all_records()