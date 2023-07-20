from constants import WarningId, ErrorId, Grade


class Problem:

    def displayWarning(self, warningId:WarningId, obj:str, oldData):
        if warningId == WarningId.WARNING_1:
            print(f"\n[!! WARNING: {WarningId.WARNING_1.value}] There is already an existing record for {obj}: {oldData}")

### Overwrite Question:
        val = input("Would you like to overwrite it? [yes/no]")
        if val.lower() == "yes":
            return True
        else:
            return False


    def displayError(self, errorId:ErrorId, obj=None):
        if obj is None:
            obj = "object"
        if errorId == ErrorId.ERROR_1:
                print(f"\n[! ERROR: {ErrorId.ERROR_1.value}] No such {obj} in the system.")

        elif errorId == ErrorId.ERROR_2:
                print(f"\n[! ERROR: {ErrorId.ERROR_2.value}] Invalid input to: {obj}.")
        else:
            return

