# Copyright 2019 Cloudera, Inc.
# Not to be reproduced or shared without prior written consent from Cloudera.


import processlog as pl


if __name__ == "__main__":
    """This program displays the state of radios and temp from a log file

    Parameters
    ----------
    file_location (argv[1]): which file to read
    which_record (argv[2]): the line that contains the record we want
    """

    # Set the variables
    file_location = sys.argv[1]
    which_record = int(sys.argv[2])

    # Open file and get the n-th line
    with open(file_location, 'r') as log_file:
        lines = log_file.readlines()

    # Get the record and values
    record = lines[which_record]
    values = pl.get_state_temp(record)

    # Display the state and temp
    pl.display_state_temp(values[0], values[1], values[2])
