import tkinter as tk
import threading
import keyboard
import winsound

class theSimsCheatApp(tk.Tk):
    def __init__(self):
        super().__init__()

        # กำหนดขนาดหน้าต่าง
        self.geometry("300x360")
        self.title("The Sims 2 trainer")
        self.iconbitmap('sims2.ico')

        # สร้าง Label แสดงข้อความ
        self.bold_font = ("Arial", 15, "bold")
        self.label = tk.Label(self, text="The Sims 2 auto cheat", font=self.bold_font)
        self.label.pack(pady=0, padx=20, anchor='w')

        self.bold_font = ("Arial", 10, "bold")
        self.label = tk.Label(self, text="สูตรทั่วไป", font=self.bold_font)
        self.label.pack(pady=0, padx=20, anchor='w')
        
        self.label = tk.Label(self, text="เปิด Command Ctrl+Shift+C เพื่อใส่สูตร")
        self.label.pack(pady=0, padx=20, anchor='w')

        # สร้าง Label แสดงคำสั่ง
        commands = [
            ("Ctrl+0 --> เพิ่มเงิน 1,000"),
            ("Ctrl+1 --> เพิ่มเงิน 50,000"),
            ("Ctrl+2 --> หยุดอายุของซิมส์"),
            ("Ctrl+3 --> ทำให้แถบความต้องการเต็ม"),
            ("Ctrl+4 --> ย้ายสิ่งของได้ทุกอย่าง"),
            ("Ctrl+5 --> ลบซิมส์ในแมพออกทั้งหมด"),
            ("Ctrl+6 --> เชิญซิมส์อื่นๆ มาร่วมงานปาร์ตี้ได้มากขึ้น 1-8"),
            ("Crtl+7 --> ลบเพื่อนบ้านออกจากละแวกบ้าน"),
            ("Crtl+8 --> ปลดล็อครางวัลแห่งชีวิต"),
            ("Crtl+9 --> ปรับแต้มแรงบรรดาลใจระดับ 1-5"),
            ("Ctrl+. --> เปิดสูตร"),
            ("Alt+0 --> หยุดการถดถอยของซิมส์ ทั้งหมด"),
        ]
        for cmd in commands:
            self.label = tk.Label(self, text=cmd)
            self.label.pack(pady=0, padx=20, anchor='w')

        self.label = tk.Label(self, text="sims2_autocheats v1.0.0 by TOPTUBBY")
        self.label.pack(pady=10, padx=40, anchor='w')

        # เริ่มสร้าง binding สำหรับตรวจจับคีย์ลัด Ctrl+1 ถึง Ctrl+6 และ Ctrl+7
        self.bind_keyboard_shortcuts()

    def bind_keyboard_shortcuts(self):
        commands = {
            "Ctrl+0": "kaching",
            "Ctrl+1": "motherlode",
            "Ctrl+2": "aging off",
            "Ctrl+3": "maxMotives",
            "Ctrl+4": "moveobjects on",
            "Ctrl+5": "deleteAllCharacters",
            "Ctrl+6": "intProp maxNumOfVisitingSims #",
            "Ctrl+7": "False",
            "Ctrl+8": "unlockCareerRewards",
            "Ctrl+9": "aspirationLevel #",
            "Ctrl+.": "boolProp testingCheatsEnabled true",
            "Alt+0": "lockAspiration on"

        }

        for key, cmd in commands.items():
            if callable(cmd):
                keyboard.add_hotkey(key, cmd)
            else:
                keyboard.add_hotkey(key, lambda cmd=cmd: self.auto_type(cmd))

    def auto_type(self, text):
        # ตรวจสอบว่าไม่มีตัวเลข hotkey ติดมาด้วย
        if any(char.isdigit() for char in text):
            return
        
        # ใช้ keyboard ในการพิมพ์ข้อความ
        keyboard.write(text)

if __name__ == "__main__":
    app = theSimsCheatApp()
    app.mainloop()
