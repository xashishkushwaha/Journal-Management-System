import datetime
import time
import sys
import csv

#--------------Main ID and Password and Initail Trascact ID--------------

mainId = "aaa"
mainPassword = "754"
filename = "journalentry.csv"
file = open(filename, "a")
file.close

#----------------------------------------------------------------------------

def processing(): # processing
    print("\nProcessing..")
    for i in range(1,5):
        print(f"{'.'*i}{25*i}%")
        time.sleep(0.2)
    print("\n")

def login(userId, Password): # Login page where user can login with Id and Password
    Login = False
    if userId == mainId:
        if Password == mainPassword:                     
            processing()
            print("Login Success")
            Login = True
            return Login
    time.sleep(0.5)
    print("Invalid login ID or password")
    return Login

def forgotIdPassword(mobileNumer): # Use to Forgot Passowrd
    if mobileNumer == 7777777777:
        print(f"ID         {mainId}\nPasssword  {mainPassword}")
    else:
        print("Wrong Mobile Number")

def dateAndTime(date = None, time = None): # Gives current date and time
    if date == "current" and time == "current":
        date = datetime.datetime.now().strftime("%d/%m/%y")
        # time = datetime.datetime.now().strftime("%X")
        date_time = (f"{date}")
        return date_time
  
def checkDateFormat(Date): # Check Date and Time Format entered by the user
    checkDate = False
    try:
        while checkDate == False:
            if len(Date) == 8:
                if "/" in Date:
                    splitDate = Date.split("/")
                    for i in splitDate:
                        if i.isnumeric():
                            if len(i) == 2:
                                checkDate = True
                                return checkDate
            if checkDate == False:
                print("Invalid Date Format")
                return checkDate
    except:
        return checkDate
  
def generateTransactionId(): # Generate Unique transaction ID for all Transaction Automatically
    global TransactionID;
    TransactionID = "1000000000";
    with open(filename, "r") as csvfile:
        csvfilereader = csv.DictReader(csvfile)
        listcsvfilereader = (list(csvfilereader))
        if listcsvfilereader == []:
            pass
        else:
            for row in listcsvfilereader:
                rowID = int(row["TRANSACTION ID"])
                TransactionID = int(TransactionID)
                if rowID > TransactionID or rowID == TransactionID:
                    TransactionID = rowID + 1
        return str(TransactionID) 
    
def mainHeading(): # Gives main heading or Project Name
    print("".center(108,'-'))
    print("Journal Management System".center(108,' '))
    print("".center(108,'-'))

def tittleHeading():  # Gives tittle heading of the Journal Entry
    F = "%15s %16s %35s %10s %11s %11s"
    print("-"*108)
    print(F % ("DATE","TRANSACTION ID","PARTICULARS","L.F","DEBIT","CREDIT"))
    print("-"*108)

def addData(list=[]): # Add Data in file
    tittleHeading = ["DATE","TRANSACTION ID","PARTICULARS","L.F","DEBIT","CREDIT"]
    try:
        with open(filename,'r') as csvfile:
            csvFIleReader = csv.DictReader(csvfile)
            
            for rows in csvFIleReader:
                if rows == []:
                    pass
                else:
                    list.append(rows)
    except:
        pass
    
    with open(filename, "w") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=tittleHeading)
        writer.writeheader()
        writer.writerows(list)
        return True

def displayData(date = True): # Display Data
    display = False
    try:
        with open(filename,'r') as csvfile:
            csvFIleReader = csv.reader(csvfile)
            tittleheading = next(csvFIleReader)
            for rows in csvFIleReader:
                if rows == []:
                    pass
                    
                else:
                    if date == True:
                        F = "%15s %16s %35s %10s %11s %11s"
                        print(F % tuple(rows))
                        display = True  
                        
                    else:
                        if date == rows[0]:
                            F = "%15s %16s %35s %10s %11s %11s"
                            print(F % tuple(rows))
                            display = True  

            if display == True:
                pass
            else:
                print("\tNot Data Found")
                
    except Exception as e:
        print(e)
        print("No Data Found")

def debitCreditSum(): # Total Debit And Credit
    try:
        with open(filename, "r") as csvfile:
            csvfilereader = csv.DictReader(csvfile)
            csvfilereader = list(csvfilereader)

            debitcount = 0
            creditcount = 0
            
            for row in csvfilereader:
                debit = row["DEBIT"]
                credit = row["CREDIT"]
                if debit == "-":
                    debit = 0
                if credit == "-":
                    credit = 0
                    
                debitcount += int(debit)
                creditcount += int(credit)
            print("\n")
            print(f"Total Debit  - {debitcount}".ljust(10))
            print(f"Total Credit - {creditcount}".ljust(10))
    except:
        print("\nData Not Found")

def checkTransactionId(TransactionId): # Check Transaction ID
    with open(filename, "r") as csvfile:
        
        csvfilereader = csv.DictReader(csvfile)
        csvfilereader = list(csvfilereader)

        for row in csvfilereader:
            if str(row["TRANSACTION ID"]) == TransactionId:
                return True

def checkDate(date): # Check Date
    with open(filename, "r") as csvfile:
        
        csvfilereader = csv.DictReader(csvfile)
        csvfilereader = list(csvfilereader)

        for row in csvfilereader:
            if (row["DATE"]) == date:
                return True
        
def deleteData(data="all"): # Delete all data or selected data
    try:
        if data == "all":
            csvfile = open(filename, "w")
            csvfile.close()
            return True
        else:
            with open(filename, "r") as csvfile:
                csvfilereader = csv.DictReader(csvfile)
                listcsvfile = list(csvfilereader)
                for index, row in enumerate(listcsvfile):
                    if len(str(row["TRANSACTION ID"])) == 10:
                        if str(row["TRANSACTION ID"]) == data:
                            listcsvfile.pop(index)

                    
                csvfile = open(filename, "w")
                csvfile.close()
                addData(listcsvfile)
                return True
    except:
        print("No Data Found")
        
def updateData(ID, newDate, reason, ledgerFolio, debitamount, creditamount): # Update the data
    with open(filename, "r") as csvfile:
        
        csvfilereader = csv.DictReader(csvfile)
        listcsvfile = list(csvfilereader)
        updatedlistcsvfile = []
        
        for index, row in enumerate(listcsvfile):
            if len(str(row["TRANSACTION ID"])) == 10:
                if str(row["TRANSACTION ID"]) == ID:
                    
                    if newDate == "":
                        pass
                    else:
                        row["DATE"] = newDate
                        
                    if reason == "":
                        pass
                    else:
                        row["PARTICULARS"] = reason
                        
                    if ledgerFolio == "":
                        pass
                    else:
                        row["L.F"] = ledgerFolio
                        
                    if debitamount == "-":
                        pass
                    else:
                        row["DEBIT"] = debitamount
                        row["CREDIT"] = "-"
                        
                    if creditamount == "-":
                        pass
                    else:
                        row["CREDIT"] = creditamount
                        row["DEBIT"] = "-"
                        
                    
                    updatedlistcsvfile.append(row)
                else:
                    updatedlistcsvfile.append(row)
                
        csvfile = open(filename, "w")
        csvfile.close()
        addData(updatedlistcsvfile)
        return True

if __name__ == '__main__':

    while True:
        
        print("LOGIN".center(108,"-"))
        print("'F' to forgot ID and Password")
        id = (input("Enter Your Username - ".rjust(60," "))).lower()
        password = (input("Enter Your Password - ".rjust(60," ")).lower())
        
        if id == "f" or password == 'f': # Forgot Id and Password
            mobileNumber = int(input("Enter your Mobile Number - "))
            forgotIdPassword(mobileNumber)
        
        elif login(id, password): # Login Page
            time.sleep(0.4)
            mainHeading()
            time.sleep(0.4)
            
            while True:
                print("\n")
                listMainmenu = ["1. Add Data", "2. Display Data", "3. Remove Data", "4. Update Data", "5. Total Debit/Credit", "6. Exit"]
                print("MAINMENU".center(108, " "))
                for i in listMainmenu:
                    print(" "*46,i)
                    time.sleep(0.1)
                userInput = input("➤ Type Here : ")
                time.sleep(0.2)
                
                if userInput =="1": # Add Data
                    checkDate = False
                    Ledger = False
                    debitCreditEntry = False
                    reasonEntry = False
                    
                    listAllData = []
                    dictSingleData = {"DATE":"", "TRANSACTION ID":"","PARTICULARS":"","L.F":"","DEBIT":"","CREDIT":""} # Takes the SIngle Tranaction Data
                    
                    dataAdded = False
                    while checkDate == False: #Check Date and time
                        current = (input(("Do you want to add current Date and Time (Y/N) - ")).upper())
                        if current == "Y":
                            dictSingleData["DATE"] = dateAndTime("current", "current")
                            checkDate = True
                        elif current == "N":
                            date = input("Enter the date of the Transaction in (DD/MM/YY) - ")
                            checkDate = checkDateFormat(date)
                            if checkDate == True:
                                dictSingleData["DATE"] = date
                        else:
                            pass
                        
                        if checkDate == True:
                            dictSingleData["TRANSACTION ID"] = generateTransactionId() # Generate Transaction ID
                        
                    while reasonEntry == False: # Reason for Transaction
                        print("\n")
                        time.sleep(0.3)
                        reason = (input("Enter the Reason for this Transaction - \n(i.e- Paid to Anshika, Paid at Shopping Mall, Received Salary, 'Auto Debit SBI Bank' etc.\n➤ "))
                        if len(reason) < 34:
                            # reason = str(correctText(reason))
                            dictSingleData["PARTICULARS"] = (reason.title()).strip()
                            reasonEntry = True
                        else:
                            print("`Reason Should Less Than 34 Character`")
                    
                    while Ledger == False: # Ledger Folio
                        time.sleep(0.3)
                        print("\nLedger Folio -")
                        listLedgerFolio = ["Cash","Cheque","ATM","Auto","Fees","Online"]
                        for i in range(len(listLedgerFolio)):
                            time.sleep(0.1)
                            print(f"{i+1}. {listLedgerFolio[i]}")
                        try:
                            ledgerFolio = int(input("➤ "))
                            dictSingleData["L.F"] = listLedgerFolio[ledgerFolio-1]
                            Ledger = True
                        except:
                            print("Invalid Entry")
                    
                    while debitCreditEntry == False: # Credit And Debit Entry
                        time.sleep(0.3)
                        debitCredit = (input("\nDebit or Credit (D/C)- ")).lower()
                        if debitCredit == "d": # Debit
                            amount = (int(input("Enter the Debit amount in Rupees (i.e 100000, 23312, 25000)\n➤ Amount Rs. ")))
                            dictSingleData["DEBIT"] = amount
                            dictSingleData["CREDIT"] = "-"
                            debitCreditEntry = True
                            listAllData.append(dictSingleData)
                            
                            
                        elif debitCredit == "c": # Credit
                            amount = (int(input("Enter the Credit amount in Rupees (i.e 100000, 23312, 25000)\n➤ Amount Rs. ")))
                            dictSingleData["CREDIT"] = amount
                            dictSingleData["DEBIT"] = "-"
                            debitCreditEntry = True
                            listAllData.append(dictSingleData)
                            
                            
                        else:
                            print("Invalid Entry")
                        
                        if debitCreditEntry == True:
                            dataadded = addData(listAllData)
                            if dataadded == True:
                                print("--> DATA ADDED")

                elif userInput == "2": # Display all the stored data
                    displayalldata = (input("Do you want to see all the data (Y/N) - ")).lower()

                    if displayalldata == "y":
                        processing()
                        tittleHeading()
                        displayData()
                        
                    elif displayalldata == "n":
                        while True:
                            date = input("Enter the specific date in (DD/MM/YY) - ")
                            print(date)
                            try:
                                processing()
                                tittleHeading()
                                displayData(date)
                                break
                            except:
                                print("Invalid Date")
                                
                    else:
                        print("Invalid Input")

                elif userInput == "3": # Delete Data
                    deleted = False
                    while True:
                        print("\n")
                        listMainmenu = ["1. Delete All Data", "2. Delete Specific Data","3. Back"]
                        print("MAINMENU".center(108, " "))
                        
                        for i in listMainmenu:
                            print(" "*46,i)
                        userInput = input("➤ Type Here : ")
                        time.sleep(0.3)
                        if userInput == "1":
                            deleted = deleteData()
                            if deleted == True:
                                print("--Data Deleted--")
                            break
                        
                        elif userInput == "2":
                            while True:
                                TransactionID = input("Enter the Transaction ID - ")
                                if len(TransactionID) == 10:
                                    if TransactionID.isnumeric():
                                        if checkTransactionId(TransactionID):
                                            
                                            deleted = deleteData(TransactionID)
                                            if deleted == True:
                                                print("--Data Deleted--")
                                            break
                                        else:
                                            print("Invalid Transaction ID")
                                if TransactionID == "3":
                                    break
                                else:
                                    print("Invalid Transaction ID")
                                    
                        elif userInput == "3":
                            break
                        else:
                            print("Invalid Input")
                   
                elif userInput == "4": # Update Data
                    print("|| To Update Data, Type the Data and Enter ||".center(108," "))
                    print("|| You Cannot Change Unique Transaction ID ||".center(108, " "))
                    print(f"||{' '*17}3. Back{' '*17}||".center(108, " "))
                    print("\n")
                    
                    
                    checkDate = False
                    reasonEntry = False
                    Ledger = False
                    debitCreditEntry = False
                    
                    while True: # Check Transaction ID
                        TransactionID = input("Enter the Transaction ID - ")
                        if len(TransactionID) == 10 and TransactionID.isnumeric() and checkTransactionId(TransactionID):
                            while checkDate == False : #Update Date
                                newDate = input("Enter the Transaction date in (DD/MM/YY) - ")
                                checkDate = checkDateFormat(newDate)
                                if checkDate== True:
                                    break
                                
                            while reasonEntry == False: # Update Reason for Transaction
                                time.sleep(0.3)
                                reason = (input("Enter the Reason for this Transaction - \n")).title()
                                if len(reason) < 34:
                                    # reason = str(correctText(reason))
                                    reasonEntry = True
                                else:
                                    print("`Reason Should Less Than 34 Character`")
                                                
                            while Ledger == False: # Ledger Folio
                                time.sleep(0.3)
                                print("Ledger Folio - \n")
                                listLedgerFolio = ["Cash","Cheque","ATM","Auto","Fees","Online"]
                                for i in range(len(listLedgerFolio)):
                                    time.sleep(0.1)
                                    print(f"{i+1}. {listLedgerFolio[i]}")
                                try:
                                    ledgerFolio = int(input("➤ "))
                                    Ledger = True
                                    ledgerFolio = listLedgerFolio[ledgerFolio-1]
                                except:
                                    print("Invalid Entry")
                                                
                            while debitCreditEntry == False: # Credit And Debit Entry
                                time.sleep(0.3)
                                debitCredit = (input("Debit or Credit (D/C)- ")).lower()
                                if debitCredit == "d": # Debit
                                    debitamount = (int(input("Enter the Debit amount in Rupees\n➤Amount Rs. ")))
                                    creditamount = "-"
                                    debitCreditEntry = True
                                    
                                elif debitCredit == "c": # Credit
                                    creditamount = (int(input("Enter the Credit amount in Rupees\n➤ Amount Rs. ")))
                                    debitamount = "-"
                                    debitCreditEntry = True
                                    
                                else:
                                    print("Invalid Entry")
                                                
                            
                            if updateData(TransactionID, newDate, reason, ledgerFolio, debitamount, creditamount) == True:
                                print("--> DATA UPDATED");
                                break
                                                            
                        elif TransactionID == "3":
                            break
                        else:
                            print("Invalid Transaction ID - 1")
                
                elif userInput == "5": # Debit Credit Sum
                    debitCreditSum()            
                    
                elif userInput == "6": # Exit
                    sys.exit()