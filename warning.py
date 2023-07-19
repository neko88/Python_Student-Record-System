from enum import Enum

class Warning:
    def displayWarning(self, warningId:str, object):
        print("Warning: ")
        if warningId == "w001":
            print(f"[w001] There is already an existing record for {object}.")
        else:
            return

        val = input("Would you like to overwrite it? [yes/no]")
        if val == "yes" or "Yes":
            return True
        if val == "no" or "No":
            return False

    def displayError(self, errorId:str, object):
        print("Error: ")
        if errorId == "e001":
                print(f"[e001] No such {object} in the system.")
        elif "e002":
                print(f"[e002] Invalid input to: {object}.")
        else:
            return

