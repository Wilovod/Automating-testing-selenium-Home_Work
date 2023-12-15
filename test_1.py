import pytest
import yaml
import time

with open('./testdata.yaml', encoding='utf-8') as f:
    testdata = yaml.safe_load(f)


def test_step_1(site, select_input_login, select_input_password, select_input_button, select_error):
    input1 = site.find_element('xpath', select_input_login)
    input1.send_keys('test')
    input2 = site.find_element('xpath', select_input_password)
    input2.send_keys('test')
    btn = site.find_element('css', select_input_button)
    btn.click()
    err_label = site.find_element('xpath', select_error)
    assert err_label.text == '401'


def test_step_2(site, select_input_login, select_input_password, select_input_button, select_hello_user):
    input1 = site.find_element('xpath', select_input_login)
    input1.send_keys(testdata['login'])
    input2 = site.find_element('xpath', select_input_password)
    input2.send_keys(testdata['password'])
    btn = site.find_element('css', select_input_button)
    btn.click()
    answer = site.find_element('xpath', select_hello_user)
    assert answer.text == f'Hello, {testdata["login"]}'


def test_step_3(site, select_input_login, select_input_password, select_input_button, new_post, select_post_title,
                select_post_description, select_button_save, select_post_ok):
    input1 = site.find_element('xpath', select_input_login)  # Ввод логина при регистрации
    input1.send_keys(testdata['login'])
    input2 = site.find_element('xpath', select_input_password)  # Ввод пароля при регистрации
    input2.send_keys(testdata['password'])
    btn = site.find_element('css', select_input_button)  # Клик по кнопке входна на сайт
    btn.click()

    time.sleep(2)

    click_1 = site.find_element('xpath', new_post)  # Создание поста
    click_1.click()
    post_1 = site.find_element('xpath', select_post_title)  # Ввод названия поста
    post_1.send_keys(testdata['title'])
    post_2 = site.find_element('xpath', select_post_description)  # Ввод описания поста
    post_2.send_keys(testdata['description'])
    click_2 = site.find_element('css', select_button_save)  # Клик по кнопке создания поста
    click_2.click()

    time.sleep(4)

    post_ok = site.find_element('xpath', select_post_ok) # Проверка на наличие заголовка поста
    assert post_ok.text == f'{testdata["title"]}'

