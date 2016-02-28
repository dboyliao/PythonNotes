#!/usr/bin/env python

from selenium.webdriver import Firefox

driver = Firefox()
driver.get("http://10fastfingers.com/typing-test/english")

def get_words(driver):
	return driver.find_elements_by_xpath("//div[@id='words']//span")


def enter_keys(driver, words_list, limit):
	count = 0
	form = driver.find_element_by_xpath("//input[@id='inputfield']")
	for s in words_list:
		if s.text != u"" and count < limit:
			form.send_keys(s.text)
			form.send_keys(" ")
			count += 1
		else:
			break
words_list = get_words(driver)
enter_keys(driver, words_list, len(words_list))
driver.close()
