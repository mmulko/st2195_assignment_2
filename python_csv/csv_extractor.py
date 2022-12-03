"""Importing required libraries"""
import io
import pandas as pd
import requests
from bs4 import BeautifulSoup

"""Getting page as html"""
cars_html = requests.get("https://en.wikipedia.org/wiki/Comma-separated_values").text

"""Extracting required chunk of text"""
souped_cars = BeautifulSoup(cars_html, "html.parser")
cars_data = souped_cars.find_all('pre')
cars_csv_as_string = cars_data[10].get_text()

"""Transforming [string] into [io.StringIO] for mutability"""
cars_csv_as_str_io = io.StringIO(cars_csv_as_string)

"""Transorming data into CSV format and creating CSV file"""
cars_df = pd.read_csv(cars_csv_as_str_io, sep=",")
cars_df.to_csv("python_csv/cars.csv", index=False, header=True)

"""Checking the result"""
print(pd.read_csv("python_csv/cars.csv"))