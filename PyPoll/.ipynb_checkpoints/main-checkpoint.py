{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "e0401358",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "23.04854332167558\n"
     ]
    }
   ],
   "source": [
    "import csv\n",
    "csvpath = os.path.join(\".\" , \"Resources\", \"election_data.csv\")\n",
    "with open(csvpath, encoding='UTF-8') as csvfile:\n",
    "    csv_reader = csv.reader(csvfile, delimiter= \",\")\n",
    "    row_count = 0\n",
    "    CCS_count = 0\n",
    "    DD_count = 0\n",
    "    RAD_count = 0\n",
    "    next(csv_reader)\n",
    "    for row in csv_reader :\n",
    "        count = row_count + 1\n",
    "        row_count = count\n",
    "        vote_count = row_count\n",
    "        if row[2] == \"Charles Casper Stockham\":\n",
    "            CCS_count = CCS_count + 1\n",
    "        elif row[2] == \"Diana DeGette\":\n",
    "            DD_count = DD_count + 1\n",
    "        elif row[2] == \"Raymon Anthony Doane\":\n",
    "            RAD_count = RAD_count + 1\n",
    "CCS_percentage = (CCS_count/row_count)*100\n",
    "DD_percentage = (DD_count/row_count)*100\n",
    "RAD_percentage = (RAD_count/row_count)*100\n",
    "print(CCS_percentage)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7d5644cb",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
