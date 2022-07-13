import time
import  pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_show_my_pets():
   # Вводим email
   element = WebDriverWait(pytest.driver, 10).until(
      EC.presence_of_element_located((By.ID, "email"))
   )
   pytest.driver.find_element_by_id('email').send_keys('shalimov@it-limon.ru')
   # Вводим пароль
   element = WebDriverWait(pytest.driver, 10).until(
      EC.presence_of_element_located((By.ID, "pass"))
   )
   pytest.driver.find_element_by_id('pass').send_keys('Bn3s6wp9')
   # Нажимаем на кнопку входа в аккаунт
   pytest.driver.find_element_by_css_selector('button[type="submit"]').click()
   # Проверяем, что мы оказались на главной странице пользователя
   element = WebDriverWait(pytest.driver, 10).until(
      EC.text_to_be_present_in_element((By.TAG_NAME,"h1"),"PetFriends")
   )
   assert pytest.driver.find_element_by_tag_name('h1').text == "PetFriends"


def test_pets_images_names():
   images = pytest.driver.find_elements_by_css_selector('.card-deck .card-img-top')
   names = pytest.driver.find_elements_by_css_selector('.card-deck .card-img-top')
   descriptions = pytest.driver.find_elements_by_css_selector('.card-deck .card-img-top')

   for i in range(len(names)):
      pytest.driver.implicitly_wait(10)
      assert images[i].get_attribute('src') != ''
      assert names[i].text != ''
      assert descriptions[i].text != ''
      assert ', ' in descriptions[i]
      parts = descriptions[i].text.split(", ")
      assert len(parts[0]) > 0
      assert len(parts[1]) > 0