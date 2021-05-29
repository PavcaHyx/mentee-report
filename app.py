import json

from exceptions import InvalidPath
from mentee_report import MenteesReport


def main():
    base_path = r'C:\Users\pavli\OneDrive\Desktop\mentees_report'
    file_name = 'mentees_report_task.csv'
    delimiter = ','

    mentee_report = MenteesReport(base_path, file_name, delimiter)

    try:
        all_mentees = mentee_report.get_data()
        required_information = mentee_report.get_required_information(all_mentees)
    except InvalidPath as e:
        required_information = "Sorry, pasted path " + e.full_path + " is invalid."

    with open('result.json', 'w') as json_file:
        json.dump(required_information, json_file)


if __name__ == "__main__":
    main()
