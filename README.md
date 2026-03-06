<div align="center">
  <img src="https://img.icons8.com/color/120/000000/the-sims.png" alt="The Sims Icon">
  <h1>The Sims Auto Cheats</h1>
  <p><b>เครื่องมือช่วยพิมพ์สูตรอัตโนมัติสำหรับเกม The Sims 1-4 / Automated Cheat Typing Tool for The Sims 1-4</b></p>

  <!-- Badges -->
  <p>
    <img alt="Python" src="https://img.shields.io/badge/python-3.x-blue.svg?logo=python&logoColor=white" />
    <img alt="Status" src="https://img.shields.io/badge/status-active-success.svg" />
    <img alt="License" src="https://img.shields.io/badge/license-MIT-green.svg" />
    <img alt="Platform" src="https://img.shields.io/badge/platform-Windows-lightgrey.svg?logo=windows" />
    <img alt="Version" src="https://img.shields.io/badge/version-1.0.0-red.svg?cacheSeconds=2592000" />
  </p>
</div>

---

## 🇹🇭 ภาษาไทย (Thai)

**The Sims Auto Cheats** คือโปรแกรมตัวช่วยสำหรับการเล่นเกม The Sims ภาค 1 ถึง 4 ที่พัฒนาด้วยภาษา Python โปรแกรมนี้จะช่วยให้คุณใช้งานสูตรโกงเกมต่างๆ (Cheats) ได้อย่างรวดเร็วและสะดวกสบาย โดยไม่ต้องพิมพ์เองซ้ำๆ เพียงแค่กดปุ่มคีย์ลัด (Hotkeys) โปรแกรมจะทำการพิมพ์สูตรให้คุณโดยอัตโนมัติ

**ผู้สร้าง (Creator):** TOPTUBBY  
**เวอร์ชัน (Version):** v1.0.0  

### ✨ คุณสมบัติหลัก (Features)
- 🎮 รองรับเกม The Sims ตั้งแต่ภาค 1 จนถึงภาค 4 (แยกโปรแกรมสำหรับแต่ละภาคอย่างชัดเจน)
- ⚡ ใช้งานง่ายผ่านระบบคีย์ลัด (เช่น `Ctrl+1`, `Ctrl+2` เป็นต้น)
- 🖥️ มีหน้าต่างเมนู (GUI) แสดงผลคีย์ลัดต่างๆ ให้ดูอย่างชัดเจน ไม่ต้องนั่งจำสูตร
- 💖 *พิเศษสำหรับ The Sims 4:* รองรับการพิมพ์สูตรปรับระดับค่าความสัมพันธ์ (Relationship) ผ่านคีย์ลัดได้ทันที

### 🚀 การติดตั้ง (Installation)

**วิธีที่ 1: สำหรับผู้ใช้งานทั่วไป (แนะนำ)**
คุณสามารถใช้งานได้ทันทีโดยไม่ต้องติดตั้งอะไรเพิ่มเติม เพียงเข้าไปที่โฟลเดอร์โปรเจคและเริ่มใช้งานไฟล์ `.exe` ได้เลย

**วิธีที่ 2: สำหรับนักพัฒนา (รันผ่าน Python)**
หากต้องการแก้ไขโค้ดหรือรันด้วยตัวเอง คุณสามารถติดตั้งตามขั้นตอนดังนี้:
1. ติดตั้ง [Python](https://www.python.org/downloads/) ลงในเครื่องคอมพิวเตอร์ของคุณ
2. คัดลอกโปรเจคนี้มาไว้ในเครื่อง
3. ติดตั้งไลบรารีที่จำเป็นผ่าน Command Prompt / Terminal:
   ```bash
   pip install keyboard
   ```
   *(หมายเหตุ: ไลบรารี `tkinter` แและ `winsound` มีมาให้พร้อมกับ Python บน Windows แล้ว)*

### 🎮 การใช้งาน (Usage)
1. เปิดโปรแกรม `sims[1-4]_autocheats.exe` หรือรันสคริปต์ภาคที่คุณต้องการเล่น เช่น `python sims4_autocheats.py`
2. เข้าเกม The Sims
3. ในเกมกดปุ่ม **Ctrl+Shift+C** เพื่อเปิดช่องใส่สูตร (Command panel)
4. กดคีย์ลัดตามที่แสดงบนหน้าต่างโปรแกรม (เช่น `Ctrl+1`) โปรแกรมจะทำการพิมพ์สูตรให้โดยอัตโนมัติ

### 💡 คำแนะนำและข้อควรระวัง (Recommendations)
- ⚠️ **Run as Administrator:** การใช้งานไลบรารีของ Python อย่าง `keyboard` เพื่อส่งคำสั่งเข้าเกม อาจต้องใช้สิทธิ์ของระบบปฏิบัติการ หากกดคีย์ลัดแล้วไม่ทำงาน ให้คลิกขวาที่ไฟล์ `.exe` หรือตัวรันโค้ดแล้วเลือก **"Run as administrator"** (เรียกใช้ในฐานะผู้ดูแล)
- 🇺🇸 **ภาษาของคีย์บอร์ด:** แนะนำให้ตรวจสอบให้แน่ใจว่าภาษาของคีย์บอร์ดบนคอมพิวเตอร์ของคุณถูกตั้งค่าเป็น **"ภาษาอังกฤษ (EN)"** ก่อนกดสูตร เพื่อป้องกันการพิมพ์สูตรออกมาเป็นภาษาไทย
- 🚫 **ซ้อนทับคีย์ลัด (Hotkey Overlap):** ในขณะที่รันโปรแกรมอยู่ หากใช้คีย์ลัดที่ตรงกันในการใช้อื่นๆ (เช่นพิมพ์งาน) อาจทำให้โปรแกรมทำงานได้ แนะนำให้ปิดโปรแกรมเมื่อไม่ได้เล่นเกมแล้ว

---

## 🇬🇧 English

**The Sims Auto Cheats** is an automated tool developed in Python for The Sims 1 through 4. It significantly enhances your gameplay experience by allowing you to quickly and effortlessly apply game cheat codes without typing them manually. Simply press the predefined hotkeys, and the program will automatically type the desired cheats into the game's console for you.

**Creator:** TOPTUBBY  
**Version:** v1.0.0  

### ✨ Features
- 🎮 Supports The Sims 1, 2, 3, and 4 (dedicated programs included for each specific game).
- ⚡ Efficient cheat activation via simple hotkeys (e.g., `Ctrl+1`, `Ctrl+2`).
- 🖥️ Straightforward GUI that visibly lists all available hotkeys so you don't have to memorize them.
- 💖 *Exclusive to The Sims 4:* Features an advanced relationship modifier allowing quick targeted adjustments to romance/friendship meters.

### 🚀 Installation

**Method 1: For General Users (Recommended)**
There is no installation required. You can simply open the project folder and run the provided compiled `.exe` files out of the box.

**Method 2: For Developers (Running via Python)**
If you wish to modify the script or run it directly through Python:
1. Install [Python](https://www.python.org/downloads/) on your computer.
2. Clone or download this project format.
3. Install required library dependencies using Command Prompt / Terminal:
   ```bash
   pip install keyboard
   ```
   *(Note: The `tkinter` and `winsound` libraries are built-in with Windows Python installations)*

### 🎮 Usage
1. Run the respective executor (e.g., `sims[1-4]_autocheats.exe`) or the python script corresponding to your game (e.g., `python sims4_autocheats.py`).
2. Launch your game (The Sims 1, 2, 3, or 4).
3. In-game, press **Ctrl+Shift+C** to open the cheat console line.
4. Press the hotkey shown on the tool's interface (e.g., `Ctrl+1`). The cheat code will be typed out automatically.

### 💡 Recommendations & Tips
- ⚠️ **Run as Administrator:** In some environments, the `keyboard` module may require administrator privileges to pass keystrokes into games. If hotkeys don't seem to work, right-click on the script or `.exe` and select **"Run as administrator"**.
- 🇺🇸 **Keyboard Layout:** Ensure your system keyboard language is set to **English** while using the hotkeys. Otherwise, the tool might type out cheat codes using another language's layout or special characters.
- 🚫 **Hotkey Disabling:** When you are done playing, remember to shut down the app. Running it continuously in the background may interfere with normal typing or other applications mapped to the same hotkeys.

---

<div align="center">
  <p>Made with ❤️ by <b>TOPTUBBY</b></p>
</div>
