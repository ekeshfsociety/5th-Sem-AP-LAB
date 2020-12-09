class UniqueSubset:
    
    def setinput(self,s):
        return self.setsubset([],sorted(s))
    
    def setsubset(self,currentset,sorteds):
        if sorteds:
            return self.setsubset(currentset,sorteds[1:])+self.setsubset(currentset+[sorteds[0]],sorteds[1:])
        return [currentset]

uss=UniqueSubset()

print("Unique Subsets are:",uss.setinput([1,2,3,4,5]))