import csv
import os

from exceptions import InvalidPath


class MenteesReport:
    def __init__(self, base_path, file_name, delimiter):
        self._base_path = base_path
        self._file_name = file_name
        self._delimiter = delimiter

    def get_data(self,):
        full_path = os.path.join(self._base_path, self._file_name)
        try:
            with open(full_path, encoding="utf8") as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=self._delimiter)
                all_mentees = []
                for row, data in enumerate(csv_reader):
                    if row >= 1:
                        full_name = data[1] + ' ' + data[2]
                        length_full_name = len(full_name)
                        language = data[3]
                        all_mentees.append([length_full_name, full_name, language])
        except IOError as e:
            raise InvalidPath(full_path) from e

        return all_mentees

    def get_required_information(self, all_mentees):
        """
        :type all_mentees: list[lst,lst,..]
        :rtype: dict
        """
        all_mentees.sort()
        languages = set()
        mentees_count, length_names_sum = 0, 0
        shortest_name = all_mentees[0]
        longest_name = all_mentees[-1]
        shortest_names, longest_names = [], []

        for mentee in all_mentees:
            languages.add(mentee[-1])
            length_names_sum += mentee[0]
            mentees_count += 1
            if mentee[0] == shortest_name[0]:
                shortest_names.extend([mentee[1]])
            if mentee[0] == longest_name[0]:
                longest_names.extend([mentee[1]])

        return {
            "mentees_count": mentees_count,
            "set_languages": list(languages),
            "average_lenght_of_name":  round(length_names_sum/mentees_count, 1),
            "shortest_names": shortest_names,
            "longest_names": longest_names,
        }
