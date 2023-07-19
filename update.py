class Update:
    def displayUpdate(self, setting:bool, objectName, objectData, updateData):
        if setting is True:
            print(f"The {objectData} for {objectName}, has been successfully updated to: {updateData}")
        else:
            print(f"No changes for {objectName} made.")
        return