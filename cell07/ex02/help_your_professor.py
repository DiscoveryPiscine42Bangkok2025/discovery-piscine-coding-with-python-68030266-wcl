def average(grades):
    return sum(grades.value()) / len(grades)

class_B = {
    "p:1",
    "o:2",
    "p:8",
    "x:9"
}

class_C ={
    "f:18",
    "a:12",
    "n:15",
    "t:17"
}

print(f"Average for class B {average(class_B)}.")
print(f"Average for class C {average(class_C)}.")