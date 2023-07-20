from constants import WarningId, ErrorId

class Problem:

    def displayWarning(self, warningId:WarningId,obj:str):
        if warningId == WarningId.WARNING_1:
            print(f"[!! WARNING: {WarningId.WARNING_1.value}] There is already an existing record for {obj}.")

### Overwrite Question:
        val = input("Would you like to overwrite it? [yes/no]")
        if val.lower() == "yes":
            return True
        else:
            return False


    def displayError(self, errorId:ErrorId, obj):
        if errorId == ErrorId.ERROR_1:
                print(f"[! ERROR: {ErrorId.ERROR_1.value}] No such {obj} in the system.")

        elif errorId == ErrorId.ERROR_2:
                print(f"[! ERROR: {ErrorId.ERROR_2}] Invalid input to: {obj}.")
        else:
            return

