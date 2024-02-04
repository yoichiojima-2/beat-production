from dataclasses import dataclass

@dataclass
class Mode:
    key: int

    def build_notes(self, intervals: list[int]):
        notes: list[int] = []
        for i in intervals:
            notes.append(self.key + i)
        return notes

    def lydian(self) -> list[int]:
        return self.build_notes([0, 2, 4, 6, 7, 9, 11])

    def ionian(self) -> list[int]:
        return self.build_notes([0, 2, 4, 5, 7, 9, 11])
    
    def mixolydian(self) -> list[int]:
        return self.build_notes([0, 2, 4, 5, 7, 9, 10])
    
    def dorian(self) -> list[int]:
        return self.build_notes([0, 2, 3, 5, 7, 9, 10])
    
    def aeolian(self) -> list[int]:
        return self.build_notes([0, 2, 3, 5, 7, 8, 10])    
    
    def phrygian(self) -> list[int]:
        return self.build_notes([0, 1, 3, 5, 7, 8, 10])   

    def locrian(self) -> list[int]:
        return self.build_notes([0, 1, 3, 5, 6, 8, 10])