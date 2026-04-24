from abc import ABC, abstractmethod


# Target interface
class StudentPerformance(ABC):
    @abstractmethod
    def get_performance(self):
        pass


# ---------------- Legacy Systems ----------------

class GradingSystem:
    def get_grade(self):
        print("Getting grade from grading system...")
        return "A"


class EvaluationSystem:
    def fetch_marks(self):
        print("Getting marks from evaluation system...")
        return 85


# ---------------- Adapters ----------------

class GradingAdapter(StudentPerformance):
    def __init__(self, system):
        self.system = system

    def get_performance(self):
        grade = self.system.get_grade()
        return "Performance (Grade): " + grade


class EvaluationAdapter(StudentPerformance):
    def __init__(self, system):
        self.system = system

    def get_performance(self):
        marks = self.system.fetch_marks()
        return "Performance (Marks): " + str(marks)


# ---------------- Main System ----------------

class CollegeSystem:
    def __init__(self, performance):
        self.performance = performance

    def show(self):
        print("College System:", self.performance.get_performance())


# ---------------- Run ----------------

if __name__ == "__main__":
    grading_system = GradingSystem()
    evaluation_system = EvaluationSystem()

    grade_adapter = GradingAdapter(grading_system)
    marks_adapter = EvaluationAdapter(evaluation_system)

    print("Using grading system:")
    system1 = CollegeSystem(grade_adapter)
    system1.show()

    print("\nUsing evaluation system:")
    system2 = CollegeSystem(marks_adapter)
    system2.show()