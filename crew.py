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
    #What I want to build
    def dream_project_qiansen(self):
        print(f"{self.name} wants to make a game.")
    #  Keep it inside the class.
    #  Line it up with show_skill above.
    # ========================================================

    # ========================================================
    #  ADD YOUR METHOD ABOVE THIS LINE
    # ========================================================


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

    # ========================================================
    #  ADD YOUR OBJECT AND YOUR METHOD CALL BELOW THIS LINE
    # ========================================================
    qiansen = CrewMember("Qiansen", "Oakland", "learning classes")
    qiansen.introduce()
    qiansen.dream_project_qiansen()
    print()
    # ========================================================
    #  ADD YOUR OBJECT AND YOUR METHOD CALL ABOVE THIS LINE
    # ========================================================

    print("=== END OF BOARD ===")
