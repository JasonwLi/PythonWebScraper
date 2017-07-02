import csv
import datetime

def clean_csv(test):
    input1 = '/home/jason/Desktop/test.csv'
    save = '/home/jason/Desktop/solutions.csv'
    state = '/home/jason/Desktop/state_abbreviations.csv'
    with open(input1, 'rb') as f_in, open(save, 'wb') as f_out, open(state, 'rb') as state:
        ## input and output
        reader = csv.reader(f_in)
        readerS = csv.reader(state)
        writer = csv.writer(f_out)
        
        ## parse csv in to a list
        lines = [r for r in reader]
        state_names = {rows[0]:rows[1] for rows in readerS}
        for l in lines:
            for i in range(len(l)):
                ## convert State abbrv to full name
                if i == 5:
                    l[i] = state_names.get(l[i])
                ## clean up bio field for each entry removing spacing chars
                if i == 8:
                    l[i] = l[i].strip(' \t\n\r')
                    l[i] = " ".join(l[i].split())
                    continue
                ## setting time to standard format, adding new start_date descriptiong field
                if i == 10:
                    is_valid = False
                    for f in ['%m/%d/%Y', '%B %d, %Y', '%Y-%m-%d']:
                        try:
                            new_date = datetime.datetime.strptime(l[i], f).strftime("%Y-%m-%d")
                            l[i] = new_date
                            is_valid = True
                        except Exception, e:
                            pass
                    if is_valid == False:
                        l.append(l[i])
                        l[i] = " "
        ## adding new field names
        lines[0][5] = "state"
        lines[0][10] = "start_date"
        lines[0][11] = "start_date_description"
        ##print lines
        writer.writerows(lines)
        
if __name__ == "__main__":
    clean_csv()
                
        


        
