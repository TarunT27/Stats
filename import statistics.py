import statistics

class DataAnalyzer:
    def __init__(self, data):
        self.data = data

    def get_summary(self):
        return {
            "mean": self.calculate_mean(),
            "median": self.calculate_median(),
            "variance": self.calculate_variance(),
            "standard_deviation": self.calculate_standard_deviation(),
        }

    def calculate_mean(self):
        return sum(self.data) / len(self.data)

    def calculate_median(self):
        return statistics.median(self.data)

    def calculate_variance(self):
        return statistics.variance(self.data)

    def calculate_standard_deviation(self):
        return statistics.stdev(self.data)

# Example usage
data = [10, 20, 30, 40, 50, 60, 70, 80, 90]
analyzer = DataAnalyzer(data)
summary = analyzer.get_summary()

print("Data Summary:")
for key, value in summary.items():
    print(f"{key.capitalize()}: {value:.2f}")
