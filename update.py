class Update:
    def displayUpdate(self, setting:bool, name, obj, update):
        if setting is True:
            print(f"The {obj} for {name}, has been successfully updated to: {update}")
        else:
            print(f"No changes for {name} made.")