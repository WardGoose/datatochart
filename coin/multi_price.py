# API : dexscreener

# Moodeng
# ethereum
# 0x28561b8a2360f463011c16b6cc0b0cbef8dbbcad

# Shiba inu
# ethereum
# 0x95ad61b0a150d79219dcf64e1e6cc01f0b64c4ce

import requests
import json
from datetime import datetime

# tokenAddresses = "0x28561b8a2360f463011c16b6cc0b0cbef8dbbcad,0x95ad61b0a150d79219dcf64e1e6cc01f0b64c4ce"

API_URLS = {
    'moodengeth': f"0x28561b8a2360f463011c16b6cc0b0cbef8dbbcad",
    'moodengsol': f'ED5nyyWEzpPPiWimP8vYm7sD7TD3LAt3Q3gRTWHzPJBY'
}

for filename, token in API_URLS.items():
    response = requests.get(
        f"https://api.dexscreener.com/latest/dex/tokens/{token}",
        headers={},
    )
    data = response.json()

    current_time = datetime.now().strftime('%Y-%m-%d %H:%M')
    
    # MarketCap
    with open(f'coin/data/{filename}cap.txt', 'a', encoding='utf-8') as file:
        # json.dump(data, file, ensure_ascii=False, indent=4) # json 전체내용 저장
        if filename == 'moodengeth':
            data1 = data['pairs']
            for i in data1:
                result = i['labels']
                if 'v3' in result:
                    result = f"{current_time} {i.get('marketCap', 'N/A')}\n"
                    file.write(result)

                    # print(f"Symbol: {i['baseToken']['symbol']}, Price: {i.get('priceUsd', 'N/A')}, MarketCap: , MarketCap: ${i.get('marketCap', 'N/A')}") # 단순 결과 출력
        elif filename == 'moodengsol':
            data1 = data['pairs'][0]
            result = f"{current_time} {data1.get('marketCap', 'N/A')}\n"
            file.write(result)


    with open(f'coin/data/{filename}.txt', 'a', encoding='utf-8') as file:
        # json.dump(data, file, ensure_ascii=False, indent=4) # json 전체내용 저장
        if filename == 'moodengeth':
            data1 = data['pairs']
            for i in data1:
                result = i['labels']
                cap = i['marketCap']
                if 'v3' in result:  # v3가 있는지 확인 , json 내용엔 v2 도 있음
                    result = f"{current_time} {i.get('priceUsd', 'N/A')}\n"
                    file.write(result)

                    # print(f"Symbol: {i['baseToken']['symbol']}, Price: {i.get('priceUsd', 'N/A')}") # 단순 결과 출력

        elif filename == 'moodengsol':
            data1 = data['pairs'][0]
            cap = f"{current_time} {data1.get('marketCap', 'N/A')}\n"
            result = f"{current_time} {data1.get('priceUsd', 'N/A')}\n"
            file.write(result)

            # print(f"Symbol: {data1['baseToken']['symbol']}, Price: {data1.get('priceUsd', 'N/A')}") # 단순 결과 출력

    

