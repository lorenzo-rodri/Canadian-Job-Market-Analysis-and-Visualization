import sys
import csv
import re
import numpy as np
import matplotlib.pyplot as plt

#
#   Group Members:
#   Lorenzo Rodriguez
#   Elliot Peracchia
#   Owen Pitcher-Bond
#

# Function to get match user input string to string name in file
def switchJob(Jobtype):
    match (Jobtype):
        case 1:
            return "Total, all occupations"
        case 2:
            return "Management occupations"
        case 3:
            return "Business, finance and administration occupations"
        case 4:
            return "Natural and applied sciences and related occupations"
        case 5:
            return "Health occupations"
        case 6:
            return "Occupations in education, law and social, community and government services"
        case 7:
            return "Occupations in art, culture, recreation and sport"
        case 8:
            return "Sales and service occupations"
        case 9:
            return "Trades, transport and equipment operators and related occupations"
        case 10:
            return "Natural resources, agriculture and related production occupations"
        case 11:
            return "Occupations in manufacturing and utilities"
        case 12:
            return "Unclassified occupations"
        case _:
            return "error"


# Function to get match user input string to string name in file
def switchEdu(Edulvl):
    match (Edulvl):
        case 1:
            return "Minimum level of education required, all levels"
        case 2:
            return "No minimum level of education required"
        case 3:
            return "High school diploma or equivalent"
        case 4:
            return "Non-university certificate or diploma"
        case 5:
            return "University certificate or diploma below bachelor's level"
        case 6:
            return "Bachelor's degree"
        case 7:
            return "University certificate, diploma or degree above the bachelor's level"
        case _:
            return "error"


# Function to remove extra formatting for numbers in datafiles
def remove_letter_grades(value):
    if isinstance(value, str):
        return re.sub(r"[A-F]$", "", value).strip()  # Removes any letter from A to F at the end
    return value


def main(argv):

    datafile = argv[1]  # datafile inputted on command line
    datafile2 = argv[2] # second datafile inputted on command line

    chosenyear = 0
    Jobtypestr = ""
    Edulvlstr = ""
    Jobtype = 0
    Edulvl = 0
    category = 0
    
	# Get user input for if user wants to look at wage data or vacancy data
    print("Which statistic to you want to search for?\n(1) Job Vacancy data in Canada\n(2) Wage data in Canada")
    while (category < 1 or category > 2):
        print("\nEnter your choice: ")
        category = input()
        if category.isdigit():
            category = int(category)
            if (category > 0 and category < 3):
                break
            else:
                print("\nEnter a number within the range.")
        else:
            print("\nEnter a numeric value.")
            category = 0
    


    # Get user input for job type
    print("\nWhat type of job?\n")
    print("(1) All Jobs\n(2) Management Occupations\n(3) Business and Finance")
    print("(4) Natural and applied Sciences\n(5) Health Occupations\n(6) Education/Law/Government Services")
    print("(7) Art/Culture/Sport and Recreation\n(8) Sales and service\n(9) Trades/Transport/Equipment Operation")
    print("(10) Agriculture and Environment\n(11) Manufacturing\n(12) Other")

    while (Jobtype <= 0 or Jobtype >= 12):
        print("\nEnter your choice: ")
        Jobtype = input()
        if Jobtype.isdigit():
            Jobtype = int(Jobtype)
            if (Jobtype < 13 and Jobtype > 0):
                break
            else:
                print("\nEnter a number within the range.")
        else:
            print("\nEnter a numeric value.")
            Jobtype = 0

    # Get user input for education level
    print("\nWhat level of education?\n")
    print("(1) All levels\n(2) No Education Required\n(3) Highschool Diploma")
    print("(4) Non University Certificate or diploma\n(5) University Certificate or diploma below Bachelors")
    print("(6) Bachelors Degree\n(7) University Certificate or degree above Bachelors")

    while (Edulvl <= 0 or Edulvl >= 8):
        print("\nEnter your choice: ")
        Edulvl = input()
        if Edulvl.isdigit():
            Edulvl = int(Edulvl)
            if (Edulvl < 8 and Edulvl > 0):
                break
            else:
                print("\nEnter a number within the range")
        else:
            print("\nEnter a numeric value.")
            Edulvl = 0

    # Get input for year
    print("\nWhat year do you want to see data for?")
    while (chosenyear <= 2014 or chosenyear >= 2024):
        print("\nEnter year: ")
        chosenyear = input()
        if chosenyear.isdigit():
            chosenyear = int(chosenyear)
            if (chosenyear < 2024 and chosenyear > 2014):
                break
            else:
                print("\nPlease enter a year between 2015 and 2023.")
        else:
            print("\nEnter a numeric value.")
            chosenyear = 0

    Jobtypestr = switchJob(Jobtype)

    Edulvlstr = switchEdu(Edulvl)

	# open for writing user input to file
    with open('output.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Job Type", "Education Level", "Year", "Vacancies", "Average Wage"]) # write file header

    # loop through each year
    for year in range (2015, 2024):

        # initialize math variables to 0 on each loop
        vacsum = 0
        wagesum = 0.0
        qnum = 0

        # open both of our data files
        with open(datafile, encoding="utf-8-sig") as df1, open(datafile2, encoding="utf-8-sig") as df2:
            datafile_read = csv.reader(df1)
            datafile_read2 = csv.reader(df2)

            for row in datafile_read:

                # Filter based on user input given for data file 1
                if (Jobtypestr == row[0]):
                    if (Edulvlstr == row[1]):
                        if (year == 2015):
                            for i in range(2,6):
                                if row[i] != ".." and row[i] != 'F' and row[i] != " ":
                                    vacsum = vacsum + int(remove_letter_grades(row[i]).replace(",", ""))
                        elif (year == 2016):
                            for i in range(6,10):
                                if row[i] != ".." and row[i] != 'F' and row[i] != " ":
                                    vacsum = vacsum + int(remove_letter_grades(row[i]).replace(",", ""))
                        elif (year == 2017):
                            for i in range(10,14):
                                if row[i] != ".." and row[i] != 'F' and row[i] != " ":
                                    vacsum = vacsum + int(remove_letter_grades(row[i]).replace(",", ""))
                        elif (year == 2018):
                            for i in range(14,18):
                                if row[i] != ".." and row[i] != 'F' and row[i] != " ":
                                    vacsum = vacsum + int(remove_letter_grades(row[i]).replace(",", ""))
                        elif (year == 2019):
                            for i in range(18,22):
                                if row[i] != ".." and row[i] != 'F' and row[i] != " ":
                                    vacsum = vacsum + int(remove_letter_grades(row[i]).replace(",", ""))
                        elif (year == 2020):
                            for i in range(22,26):
                                if row[i] != ".." and row[i] != 'F' and row[i] != " ":
                                    vacsum = vacsum + int(remove_letter_grades(row[i]).replace(",", ""))
                        elif (year == 2021):
                            for i in range(26,30):
                                if row[i] != ".." and row[i] != 'F' and row[i] != " ":
                                    vacsum = vacsum + int(remove_letter_grades(row[i]).replace(",", ""))
                        elif (year == 2022):
                            for i in range(30,34):
                                if row[i] != ".." and row[i] != 'F' and row[i] != " ":
                                    vacsum = vacsum + int(remove_letter_grades(row[i]).replace(",", ""))
                        elif (year == 2023):
                            for i in range(34,37):
                                if row[i] != ".." and row[i] != 'F' and row[i] != " ":
                                    vacsum = vacsum + int(remove_letter_grades(row[i]).replace(",", ""))



            for row in datafile_read2:

                # Filter based on user input given for data file 2
                if (Jobtypestr == row[0]):
                    if (Edulvlstr == row[1]):
                        if (year == 2015):
                            for i in range(2,6):
                                if row[i] != ".." and row[i] != 'F' and row[i] != " ":
                                    wagesum = wagesum + float(remove_letter_grades(row[i]).replace(",", ""))
                                    qnum += 1
                        elif (year == 2016):
                            for i in range(6,10):
                                if row[i] != ".." and row[i] != 'F' and row[i] != " ":
                                    wagesum = wagesum + float(remove_letter_grades(row[i]).replace(",", ""))
                                    qnum += 1
                        elif (year == 2017):
                            for i in range(10,14):
                                if row[i] != ".." and row[i] != 'F' and row[i] != " ":
                                    wagesum = wagesum + float(remove_letter_grades(row[i]).replace(",", ""))
                                    qnum += 1
                        elif (year == 2018):
                            for i in range(14,18):
                                if row[i] != ".." and row[i] != 'F' and row[i] != " ":
                                    wagesum = wagesum + float(remove_letter_grades(row[i]).replace(",", ""))
                                    qnum += 1
                        elif (year == 2019):
                            for i in range(18,22):
                                if row[i] != ".." and row[i] != 'F' and row[i] != " ":
                                    wagesum = wagesum + float(remove_letter_grades(row[i]).replace(",", ""))
                                    qnum += 1
                        elif (year == 2020):
                            for i in range(22,26):
                                if row[i] != ".." and row[i] != 'F' and row[i] != " ":
                                    wagesum = wagesum + float(remove_letter_grades(row[i]).replace(",", ""))
                                    qnum += 1
                        elif (year == 2021):
                            for i in range(26,30):
                                if row[i] != ".." and row[i] != 'F' and row[i] != " ":
                                    wagesum = wagesum + float(remove_letter_grades(row[i]).replace(",", ""))
                                    qnum += 1
                        elif (year == 2022):
                            for i in range(30,34):
                                if row[i] != ".." and row[i] != 'F' and row[i] != " ":
                                    wagesum = wagesum + float(remove_letter_grades(row[i]).replace(",", ""))
                                    qnum += 1
                        elif (year == 2023):
                            for i in range(34,37):
                                if row[i] != ".." and row[i] != 'F' and row[i] != " ":
                                    wagesum = wagesum + float(remove_letter_grades(row[i]).replace(",", ""))
                                    qnum += 1

            # if there are no quarters available, wagesum will be set to 0 to avoid div by 0 error
            if (qnum != 0):
                wagesum = wagesum / qnum
            else:
                wagesum = 0

            # set data row to the info on this year iteration
            data_row = [Jobtypestr, Edulvlstr, year, vacsum, wagesum]

			# write line to file at each iteration
            if (wagesum != 0):
                with open('output.csv', 'a', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow(data_row)

                # add data for this year to our exampledata array
                with open("output.csv","r") as i:
                    rawdata = list(csv.reader(i,delimiter = ","))

                exampledata = np.array([[float(row[2]), float(row[3]), float(row[4])] for row in rawdata[1:]], dtype=np.float64)
                xdata = exampledata[:,0]
                if category == 1:
                    ydata = exampledata[:,1]
                elif category == 2:
                    ydata = exampledata[:,2]



    # plot data to graph after all loops are done
    plt.figure(1, dpi=120)
    font = {'family' : 'normal',
        'weight' : 'bold',
        'size'   : 22}
    plt.title(f"{Jobtypestr}, {Edulvlstr}")
    plt.xlabel("Year")
    plt.ylabel("# of Vacancies" if category == 1 else "Wages ($)")
    if category == 1:
        plt.plot(xdata, ydata, label="vacancies over time", marker='o')
    if category == 2:
        plt.plot(xdata, ydata, label="wages over time", marker='o')

	# Highlight the point tha the user chose
    highlight_x = chosenyear
    if highlight_x in xdata:
        highlight_y = ydata[np.where(xdata == highlight_x)][0]
        plt.scatter(highlight_x, highlight_y, s=100, facecolor='red', zorder = 10, label="*Chosen Year*")
    else:
        print(f"Data for year {highlight_x} not found.")
        # Optionally, handle this case (e.g., set highlight_y to NaN or skip plotting)
        highlight_y = np.nan  # or you can choose to not plot it

    plt.legend()
    plt.grid(True)

    # print out data that user filtered by
    print("\n\n****************************************************\n")
    print(f"Showing data for: {Jobtypestr}, {Edulvlstr}, {highlight_x}\n")
    
    if (category == 1):
        print("Total number of vacancies: ")
        if np.isnan(highlight_y):
            print("No data for this year.")
        else:
            print(f"{highlight_y:.0f}")

    if (category == 2):
        print("Average wage: ")
        if np.isnan(highlight_y):
            print("No data for this year.")
        else:
            print(f"${highlight_y:.2f}/hour")

    print("\n****************************************************\n\n")

    plt.show()

main(sys.argv)