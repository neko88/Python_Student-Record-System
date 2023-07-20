class Update:
    def displayUpdate(self, setting:bool, name, obj, update):
        if setting is True:
            print(f"\n..[Update: {name}] {obj} has been successfully updated to: {update}")
        else:
            print(f"No changes for {name} made.")
