# from selenium import webdriver
# from selenium.webdriver.common.by import By
# # Set up WebDriver (change the path to your webdriver executable)
# try:
#     options=webdriver.EdgeOptions()
#     options.add_argument("headless")
#     driver = webdriver.Edge(options=options)

# # Navigate to the quiz page
#     driver.get('https://www.welovequizzes.com/multiple-choice-quiz-questions-and-answers/')

# # Find and extract questions and options
#     questions = driver.find_elements(By.XPATH,'//*[@id="post-1721"]/div[1]/div/div[1]/h3[1]')  # Replace 'question' with the actual class name or selector
#     options = driver.find_elements(By.XPATH,'//*[@id="post-1721"]/div[1]/div/div[1]/p[9]')  # Replace 'option' with the actual class name or selector

#     question_text = questions[0].text
#     print(f"Question {question_text}")

# except KeyboardInterrupt:
#     driver.quit()


# from selenium import webdriver
# from selenium.webdriver.common.by import By
# options= webdriver.ChromeOptions()
# options.add_argument("headless")
# driver=webdriver.Chrome(options=options)
# driver.get('https://www.welovequizzes.com/multiple-choice-quiz-questions-and-answers/')
# que = driver.find_elements(By.XPATH ,'//*[@id="post-1721"]/div[1]/div/div[1]/h3[1]')
# ans = driver.find_elements(By.XPATH , '//*[@id="post-1721"]/div[1]/div/div[1]/p[4]')
# ans1 = driver.find_elements(By.XPATH , '//*[@id="post-1721"]/div[1]/div/div[1]/p[5]')
# ans2 = driver.find_elements(By.XPATH , '//*[@id="post-1721"]/div[1]/div/div[1]/p[6]')
# ans3 = driver.find_elements(By.XPATH , '//*[@id="post-1721"]/div[1]/div/div[1]/p[7]')
# txt = que[0].text
# txt2 = ans[0].text
# txt3 = ans1[0].text
# txt4 = ans2[0].text
# txt5 = ans3[0].text
# print(f"q.n 1 : {txt}")
# print(f"options  {txt2}")
# print(f"options  {txt3}")
# print(f"options  {txt4}")
# print(f"options  {txt5}")
# ins = input("select a,b,c or d options ")
# a = ins.upper()
# match a:
#     case "A":
#         print("correct answer Pacific ocean")
#     case _  : 
#         print("your options is wrong")
# que = driver.find_elements(By.XPATH ,'//*[@id="post-1721"]/div[1]/div/div[1]/h3[2]')
# ans = driver.find_elements(By.XPATH , '//*[@id="post-1721"]/div[1]/div/div[1]/p[8]')
# ans1 = driver.find_elements(By.XPATH , '//*[@id="post-1721"]/div[1]/div/div[1]/p[9]')
# ans2 = driver.find_elements(By.XPATH , '//*[@id="post-1721"]/div[1]/div/div[1]/p[10]')
# ans3 = driver.find_elements(By.XPATH , '//*[@id="post-1721"]/div[1]/div/div[1]/p[11]')
# txt = que[0].text
# txt2 = ans[0].text
# txt3 = ans1[0].text
# txt4 = ans2[0].text
# txt5 = ans3[0].text
# print(f"q.n 1 : {txt}")
# print(f"options  {txt2}")
# print(f"options  {txt3}")
# print(f"options  {txt4}")
# print(f"options  {txt5}")
# ins = input("select a,b,c or d options ")
# a = ins.upper()
# match a:
#     case "C":
#         print("correct answer A flow of electorns")
#     case _  : 
#         print("your options is wrong")