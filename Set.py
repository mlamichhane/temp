# Implementation of the Set ADT container using a Python list.
class Set :
    # Creates an empty set instance.
    def __init__(self):
        self._theElements = list()

    # Returns the number of items in the set.
    def __len__(self):
        return len(self._theElements)

    # Determines if an element is in the set.
    def __contains__(self, element):
        return element in self._theElements
    
    # Adds a new unique element to the set.
    def add(self, element):
        if element not in self:
            self._theElements.append(element)
    
    # Removes an element from the set.
    def remove(self, element):
        assert element in self, "The element must be in the set."
        self._theElements.remove(element)
    
    # Determines if two sets are equal.
    def __eq__(self, setB):
        if len(self) != len(setB):
            return False
        else :
            return self.isSubsetOf(setB)

    # Determines if this set is a subset of setB.
    def isSubsetOf(self, setB):
        for element in self:
            if element not in setB:
                return False
        return True

    # Creates a new set from the union of this set and setB.
    def union(self, setB):
        newSet = Set()
        newSet._theElements.extend(self._theElements)
        for element in setB:
            if element not in self:
                newSet._theElements.append(element)
        return newSet

    # Creates a new set from the intersection: self set and setB.
    def interset(self, setB):
        newSet = Set()
        for element in self._theElements:
            if setB.__contains__(element):
                newSet.add(element)
        return newSet
        # pass  # Function logic to be added later

    # Creates a new set from the difference: self set and setB.
    def difference(self, setB):
        newSet = Set()
        for element in self._theElements:
            if not setB.__contains__(element):
                newSet.add(element)
        return(newSet)
        # pass  # Function logic to be added later

    # Returns an iterator for traversing the list of items.
    def __iter__(self):
        return iter(self._theElements)
    
#Example usages
if __name__ == "__main__":
    smith = Set()
    smith.add("CSCI-112")
    smith.add("MATH-121")
    smith.add("HIST-340")
    smith.add("ECON-101")
   
    roberts = Set()
    roberts.add("POL-101")
    roberts.add("ANTH-230")
    roberts.add("CSCI-112")
    roberts.add("ECON-101")

    if smith == roberts :
        print( "Smith and Roberts are taking the same courses." )
    else :
        sameCourses = smith.interset(roberts)
        if sameCourses.__len__() == 0:
            print( "Smith and Roberts are not taking any of the same courses." )
        else :
            print( "Smith and Roberts are taking some of the same courses:" )
            for course in sameCourses:
                print(course)