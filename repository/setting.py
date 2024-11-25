from py_directus import Directus
from dotenv import load_dotenv
import os
import asyncio
import sys
from typing import Optional

# เพิ่ม Root Project สำหรับ Import Schemas
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from schemas.setting import Setting

# โหลด environment variables
load_dotenv()
TOKEN_DIRECTUS = os.getenv("TOKEN_DIRECTUS")
HOST_DIRECTUS = os.getenv("HOST_DIRECTUS")

async def get_settings() -> Optional[Setting]:
    try:
        # เชื่อมต่อ Directus
        directus = await Directus(HOST_DIRECTUS, token=TOKEN_DIRECTUS)
        
        # ดึงข้อมูล settings
        response = await directus.collection('settings').read()
        
        # ดึงข้อมูลจาก response โดยใช้ item() หรือ item_as_dict()
        setting = response.item()  # หรือใช้ response.item_as_dict()
        
        print("\nข้อมูล Settings:")
        print(f"ID: {setting.get('id')}")
        print(f"Internal Gateway: {setting.get('internal_gateway')}")
        print(f"Internal Speedtest: {setting.get('internal_speedtest')}")
        print(f"External Gateway: {setting.get('external_gateway')}")
        print(f"Ping Count: {setting.get('ping_count')}")
        print(f"URL Check DNS: {setting.get('url_check_dns_resolver')}")
        
        return Setting(**setting)  # แปลง dict เป็น Setting object

    except Exception as e:
        print(f"เกิดข้อผิดพลาดในการเชื่อมต่อ Directus: {str(e)}")
        return None

async def main():
    setting = await get_settings()
    if setting:
        # ตัวอย่างการใช้งานข้อมูล
        print("\nการใช้งานข้อมูล:")
        print(f"Gateway ภายใน: {setting.internal_gateway}")
        print(f"จำนวน Ping: {setting.ping_count}")

if __name__ == "__main__":
    asyncio.run(main())