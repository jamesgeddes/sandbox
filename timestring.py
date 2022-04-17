from datetime import datetime
import csv

in_file = "datetest.csv"
out_file = "out.csv"

out_row = ["Date", "Metric"]

with open(out_file, "w", newline="") as csv_out:
    writer = csv.writer(csv_out)
    with open(in_file, "r", newline="") as csv_in:
        reader = csv.reader(csv_in, delimiter=",", quotechar='"')
        print(reader)
        writer.writerow(out_row)
        out_row = []
        for row in enumerate(reader):
            datetime_out = ""
            if row[0] == 0:
                pass
            else:
                for item in row[1]:
                    try:
                        datetime_out = datetime.strptime(item, "%m-%d-%Y").strftime("%B %d, %Y")
                        out_row.append(datetime_out)

                    except TypeError:
                        print("Type error")
                        out_row.append(item)

                    except ValueError:
                        print("Value error")
                        out_row.append(item)
            if out_row:
                writer.writerow(out_row)
