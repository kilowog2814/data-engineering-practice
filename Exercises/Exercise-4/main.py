import os
import pandas as pd
import json

root_folder = "Exercises\Exercise-4\data"

format_file = "*.json"

json_files = []

json_to_df = []


def main():
    for root, subroot_folders, files in os.walk(root_folder):
        for file in files:
            if file.endswith(".json"):
                json_files.append(os.path.join(root, file))

    for json_file in json_files:
        with open(json_file) as file:
            json_file = json.loads(file.read())

        df = pd.json_normalize(json_file)
        json_to_df.append(df)

    df = pd.concat(json_to_df)

    df.to_csv("retorno_exercise-4.csv", sep=";", index=False)


if __name__ == "__main__":
    main()
