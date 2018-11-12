# Global-Virome-Project

- removeGaps/removeGaps.py is a useful tool that takes in a sequence alignment and remove any column with a gap in it. This will reduce the size of the alignemnt and improve performance for later sequence processing steps.

- log/dataFrameGen.py generates a dataframe that count how many of each host is in each ecotype. It takes in an ecotype log (.txt) and a spreadsheet(.xlsx) that contains mapping information of accession id, host, and countr.

- log/logGen.py adds host and country information into original log which only contains accession id. It takes in an ecotype log (.txt) and a spreadsheet(.xlsx) that contains mapping information of accession id, host, and countr.

- log/ecotypeUtils.py contains support functions for logGen.py and dataFrameGen.py.

- dependency: pip install pandas
              pip install xlsxrd

