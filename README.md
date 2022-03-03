# hadoop-Post-Sale-Automobile-Report

<div align="center">


This is a practice project in python to set up a map reduce job with simple methods and test the local Hadoop setup.

The goal is to write a MapReduce program to produce a report of the total number of accidents per make and year of the car

</div>

## Running the code


Clone the repository with git bash (or download from GitHub):

```bash
git clone https://github.com/shaizamzaheer/bankapp.git

hadoop jar /usr/local/hadoop/contrib/streaming/hadoop-*streaming*.jar \
-file autoinc_mapper1.py -mapper autoinc_mapper1.py \
-file autoinc_reducer1.py -reducer autoinc_reducer1.py \
-input input/data.csv -output output/all_accidents
hadoop jar /usr/local/hadoop/contrib/streaming/hadoop-*streaming*.jar \
-file autoinc_mapper2.py -mapper autoinc_mapper2.py \
-file autoinc_reducer2.py -reducer autoinc_reducer2.py \
-input output/all_accidents -output output/make_year_count

```



## 🛡 License

[![License](https://img.shields.io/badge/license-MIT-green)](./LICENSE)

This project is licensed under the terms of the `MIT` license.