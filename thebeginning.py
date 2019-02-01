from selenium import webdriver
import pandas as pd
robot = webdriver.Chrome()
robot.get("https://github.com/collections/machine-learning")
OSSList = robot.find_elements_by_xpath("//h1[@class='h3 lh-condensed']")
csvOSSList = {}
for proj in OSSList:
 proj_name = proj.text # Project name
 proj_url = proj.find_elements_by_xpath("a")[0].get_attribute('href') # Project URL
 csvOSSList[proj_name] = proj_url

robot.close()
project_df = pd.DataFrame.from_dict(csvOSSList, orient = 'index')
project_df.to_csv('csvOSSList.csv')
