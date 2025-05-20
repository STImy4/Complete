import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC


def auth_website(url):
    # Настройка драйвера Chrome
    service = Service(ChromeDriverManager().install())
    
    # Настройка параметров Chrome
    chrome_options = webdriver.ChromeOptions()
    
    driver = webdriver.Chrome(service=service, options=chrome_options) #запуск двоих настроенных драйверов
    
    try:
        # Открываем указанный URL
        driver.get(url)
        
        # Подождем, пока страница загрузится
        driver.implicitly_wait(10)  # Ждем до 10 секунд

        #получаем заголовок страницы
        print("Заголовок страницы:", driver.title)
        
        # присваиваем заголовок
        page_title = driver.title

        # Проверка, содержит ли заголовок слово "Example"
        if "Example" in page_title:
            print(f"Заголовок страницы содержит слово 'Example': {page_title}")
        else:
            print(f"Заголовок страницы не содержит слово Example: {page_title}")
        
        
        
        # выполнение задачи
        try:
            driver.implicitly_wait(10)
            
            # Клик по элементу по css селектору
            driver.find_element(By.CSS_SELECTOR, "body > div > p:nth-child(3) > a").click()
            
            current = driver.current_url
            
            print(f"{current}")
            
            attempts = 0
            
            while attempts < 3:
                
                if current == "https://www.iana.org/help/example-domains":
                    print("Перенаправление успешно на:", current)
                    attempts += 4
                else:
                    print("Перенаправление не произошло. Текущий URL:", current)
                    attempts += 1
                    print(f"Попытка: {attempts}")
                    
            print("Переход выполнен успешно.")
            
            input("Нажми на любую кнопку чтоб завершить работу драйвера...")
            
            close_browser(driver)
            
            return driver  # Возвращаем драйвер для дальнейшего использования
        except:
            print("Ошибка")
            
            close_browser(driver)
            
            return None  # Неуспешный вход
        
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        
        close_browser(driver)
        
        return None # Неуспешный запуск


def close_browser(driver):
    if driver:
        driver.quit()  # Закрываем драйвер
        
        print("Браузер закрыт.")
        
        
if __name__ == "__main__":
    try:
        url = "https://example.com/"
        
        auth_website(url)
    finally:
        input("Нажми на любую кнопку чтоб завершить программу.")