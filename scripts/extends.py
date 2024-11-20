# Author: Sebastian Schiller-Stoff
# Description: File allows to define certain function to manipulate the SSR process
# e.g. to filter out certain digital-objects or to load digital-objects from a different source


#
#
# # Use cases
# # - Add objects to the list
# def modify_object_data(digital_objects):
#     """
#     Custom function allows to modify digital objects data in memory.
#     :param digital_objects: list of digital objects
#     :return: list of digital objects
#     """
#
#     filtered = []
#
#     for digital_object in  digital_objects:
#         # print(digital_object.db)
#         if digital_object.db["baseMetadata"]["title"] == 'Alexei Jopich':
#             filtered.append(digital_object)
#             pass
#         else:
#             pass
#
#
#     return filtered
#
#
# # Completely rewrite what objects are being loaded
# def load_digital_objects():
#     """
#     Custom function allows to build digital objects in memory.
#     :return: list of digital objects
#     """
#
#     return []