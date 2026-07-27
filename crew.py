# ============================================================
#  HACK THE HOOD - WEEK 8 CREW BOARD
#  One class. Everyone in the cohort adds one method to it.
#  Run this file with:  python3 crew.py
# ============================================================


class CrewMember:
    """One person in the Hack the Hood crew."""

    def __init__(self, name, city, skill):
        self.name = name
        self.city = city
        self.skill = skill

    def introduce(self):
        print(f"Hi, I'm {self.name} from {self.city}.")

    def show_skill(self):
        print(f"{self.name} is working on {self.skill}.")

    # ========================================================
    #  ADD YOUR METHOD BELOW THIS LINE
    #  Keep it inside the class.
    #  Line it up with show_skill above.
    # ========================================================

    # ========================================================
    #  ADD YOUR METHOD ABOVE THIS LINE
    # ========================================================
    def dream_project_edgar(self):
        print(f"{self.name} wants to build a Resume Keyword Scanner")

# ============================================================
#  THE FRONT DOOR
#  Everything under here runs when you type: python3 crew.py
# ============================================================
if __name__ == "__main__":

    print("=== HACK THE HOOD CREW BOARD ===")
    print()

    jordan = CrewMember("Jordan", "Oakland", "teaching Python")
    jordan.introduce()
    jordan.show_skill()
    print()

    edgar = CrewMember("Edgar", "Hayward", "learning python") 
    edgar.introduce()
    edgar.dream_project_edgar()
    print()

    # ========================================================
    #  ADD YOUR OBJECT AND YOUR METHOD CALL BELOW THIS LINE
    # ========================================================

    # ========================================================
    #  ADD YOUR OBJECT AND YOUR METHOD CALL ABOVE THIS LINE
    # ========================================================

    print("=== END OF BOARD ===")
