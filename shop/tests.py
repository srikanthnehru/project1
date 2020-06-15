from django.test import TestCase
import os
import pathlib
import unittest

from selenium import webdriver


# Create your tests here.

url = "http://google.co.in"

driver = webdriver.Chrome(executable_path="E:\Automation\Phython\MyPrograms\Django\Projects\project1\shop\drivers\chromedriver.exe")
driver.get(url)

