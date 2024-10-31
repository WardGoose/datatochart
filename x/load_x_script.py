from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import time

user_id = {
    'moodengeth' : 'moodengctoeth',
    'moodengsol' : 'moodengsol'
}

def load_x_data():
    # ChromeDriver를 자동 설치 및 설정
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # 브라우저 창을 열지 않고 실행
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    # 크롬드라이버 경로 설정
    chrome_driver_path = '/usr/bin/chromedriver'
    service = Service(chrome_driver_path)
    # 드라이버 시작
    driver = webdriver.Chrome(service=service, options=options)
    
    try:
        for filename, name in user_id.items():
            # 웹 페이지로 이동
            driver.get(f'https://x.com/{name}')
        try:
            # 명시적 대기: body 요소가 로드될 때까지 최대 10초간 대기
            WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#react-root > div > div > div.css-175oi2r.r-1f2l425.r-13qz1uu.r-417010.r-18u37iz > main > div > div > div > div.css-175oi2r.r-kemksi.r-1kqtdi0.r-1ua6aaf.r-th6na.r-1phboty.r-16y2uox.r-184en5c.r-1abdc3e.r-1lg4w6u.r-f8sm7e.r-13qz1uu.r-1ye8kvj > div > div:nth-child(3) > div > div > div:nth-child(1) > div > div.css-175oi2r.r-13awgt0.r-18u37iz.r-1w6e6rj > div:nth-child(2) > a > span.css-1jxf684.r-bcqeeo.r-1ttztb7.r-qvutc0.r-poiln3.r-1b43r93.r-1cwl3u0.r-b88u0q > span")))
        
            # 페이지의 body 요소에서 IP 텍스트 추출
            followers_info = driver.find_element(By.CSS_SELECTOR, "#react-root > div > div > div.css-175oi2r.r-1f2l425.r-13qz1uu.r-417010.r-18u37iz > main > div > div > div > div.css-175oi2r.r-kemksi.r-1kqtdi0.r-1ua6aaf.r-th6na.r-1phboty.r-16y2uox.r-184en5c.r-1abdc3e.r-1lg4w6u.r-f8sm7e.r-13qz1uu.r-1ye8kvj > div > div:nth-child(3) > div > div > div:nth-child(1) > div > div.css-175oi2r.r-13awgt0.r-18u37iz.r-1w6e6rj > div:nth-child(2) > a > span.css-1jxf684.r-bcqeeo.r-1ttztb7.r-qvutc0.r-poiln3.r-1b43r93.r-1cwl3u0.r-b88u0q > span").text.strip()

            # 현재 시간 정보를 가져와 'YYYY-MM-DD HH:MM' 형식으로 저장
            current_time = datetime.now().strftime('%Y-%m-%d %H:%M')
            
            # 결과를 'YYYY-MM-DD HH:MM result' 형식으로 저장
            result = f"{current_time} {followers_info.replace(',','')}\n"
        
            # 결과를 파일에 저장
            with open(f'x/data/{filename}.txt', 'a', encoding='utf-8') as f:
                f.write(result)

            time.sleep(2)
        except:
            # 현재 시간 정보를 가져와 'YYYY-MM-DD HH:MM' 형식으로 저장
            current_time = datetime.now().strftime('%Y-%m-%d %H:%M')
            result = f"{current_time} 0\n"
            with open(f'x/data/{filename}.txt', 'a', encoding='utf-8') as f:
                f.write(result)
            time.sleep(2)
    finally:
        # 브라우저 닫기
        driver.quit()

if __name__ == "__main__":
    load_x_data()
