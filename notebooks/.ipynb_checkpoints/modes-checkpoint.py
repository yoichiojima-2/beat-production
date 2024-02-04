def lydian(key: int) -> list[int]:
    return [
        key,
        key + 2,
        key + 4,
        key + 6,
        key + 7,
        key + 9,
        key + 11
    ]

def ionian(key: int) -> list[int]:
    return [
        key,
        key + 2,
        key + 4,
        key + 5,
        key + 7,
        key + 9,
        key + 11
    ]

def mixolydian(key: int) -> list[int]:
    return [
        key,
        key + 2,
        key + 4,
        key + 5,
        key + 7,
        key + 9,
        key + 10
    ]

def dorian(key: int) -> list[int]:
    return [
        key,
        key + 2,
        key + 3,
        key + 5,
        key + 7,
        key + 9,
        key + 10
    ]


def aeolian(key: int) -> list[int]:
    return [
        key,
        key + 2,
        key + 3,
        key + 5,
        key + 7,
        key + 8,
        key + 10
    ]


def phrygian(key: int) -> list[int]:
    return [
        key,
        key + 1,
        key + 3,
        key + 5,
        key + 7,
        key + 8,
        key + 10
    ]

def locrian(key: int) -> list[int]:
    return [
        key,
        key + 1,
        key + 3,
        key + 5,
        key + 6,
        key + 8,
        key + 10
    ]