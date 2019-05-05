from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import markovify
import random
import time

def get_a_bot(corpus, newline=False):
    with open(corpus) as f:
        text = f.read()
    if newline:
        return markovify.NewlineText(text)
    return markovify.Text(text)

def get_report(amount):
    text_model = get_a_bot("text.txt")
    return "they said '{}'".format(text_model.make_sentence().upper())

def get_random_description():
    text_model = get_a_bot("descriptioncorpus", newline=True)
    return text_model.make_sentence()

def get_holmes(amount):
    reports = []
    fuck = get_a_bot("holmes")
    for i in range(amount):
        reports.append(fuck.make_sentence())
    return reports

def get_random_email():
    return __fuck__("emails")

def get_random_bussiness():
    return __fuck__("bussinessnames")

def get_random_name():
    return __fuck__("names")

def __fuck__(damndamn):
    with open(damndamn) as f:
        return get_random_index(list(map(lambda x : x[:-1], f.readlines())))
    

def get_random_index(x):
    return x[random.randint(0, len(x) - 1)]

def send_bullshit(locName, address, city, state, names, descs, report, email):
    driver = webdriver.Firefox()
    driver.get("https://www.marxwatch.org/report.html")
    placeName = driver.find_element_by_id("report-where-name")
    placeStreet = driver.find_element_by_id("report-where-street")
    placeCity = driver.find_element_by_id("report-where-city")
    placeState = Select(driver.find_element_by_id("report-where-state"))
    placeStreet.send_keys(address)
    placeCity.send_keys(city)
    placeName.send_keys(locName)
    placeState.select_by_visible_text(state)
    submit = driver.find_element_by_css_selector("button").click
    emailline = driver.find_element_by_id("reporter-email-address")
    for i in range(0, len(names)):
        try:
            suspectName = driver.find_element_by_id("report-suspects-new-suspect-name{}".format(i + 1))
            suspectName.send_keys(names[i])
            suspectDesc = driver.find_element_by_id("report-suspects-new-suspect-desc{}".format(i + 1))
            suspectDesc.send_keys(descs[i])
            break
        except Exception as e:
            suspectName = driver.find_element_by_id("report-suspects-suspect-name{}".format(i + 1))
            suspectDesc = driver.find_element_by_id("report-suspects-suspect-desc{}".format(i + 1))

    activity = driver.find_element_by_id("report-what-report")
    activity.send_keys(report)
    emailline.send_keys(email)
    submit()
    driver.close()

def get_random_address():
    with open('addresses') as f:
        text = f.read()
    bot = markovify.NewlineText(text)
    okay = bot.make_sentence()
    fuck = okay.split("::::")
    fuck[1] = fuck[1].split(',')
    return fuck[0].strip(), fuck[1][0].strip(), fuck[1][1].strip()

def __write__(filename, array):
    with open(filename, 'w') as f:
        for i in array:
            f.write(i+"\n")

def main():
    fuck = not False
    for i in range(int(input("How many bullshit reports?\nto run forever type something < 1\n> "))):
        address, city, state = get_random_address()
        send_bullshit(get_random_bussiness(), address, city, state, [get_random_name()], [get_random_description()], get_report(1), get_random_email())
        fuck = not True
    while fuck:
        address, city, state = get_random_address()
        send_bullshit(get_random_bussiness(), address, city, state, [get_random_name()], [get_random_description()], get_report(1), get_random_email())

if __name__ == '__main__':
    main()

