import tkinter as tk
import threading
import keyboard
import winsound

class theSimsCheatApp(tk.Tk):
    def __init__(self):
        super().__init__()

        # กำหนดขนาดหน้าต่าง
        self.geometry("300x300")
        self.title("The Sims 1 trainer")
        self.iconbitmap('sims1.ico')

        # สร้าง Label แสดงข้อความ
        self.bold_font = ("Arial", 15, "bold")
        self.label = tk.Label(self, text="The Sims 1 auto cheat", font=self.bold_font)
        self.label.pack(pady=0, padx=20, anchor='w')

        self.bold_font = ("Arial", 10, "bold")
        self.label = tk.Label(self, text="สูตรทั่วไป", font=self.bold_font)
        self.label.pack(pady=0, padx=20, anchor='w')
        
        self.label = tk.Label(self, text="เปิด Command Ctrl+Shift+C เพื่อใส่สูตร")
        self.label.pack(pady=0, padx=20, anchor='w')

        # สร้าง Label แสดงคำสั่ง
        commands = [
            ("Ctrl+0 --> เพิ่มเงิน 1,000"),
            ("Ctrl+1 --> เพิ่มเงิน 1,000 (ภาคเสริม)"),
            ("Ctrl+2 --> ย้ายสิ่งของได้ทุกอย่าง"),
            ("Ctrl+3 --> ปลดล็อกรางวัลอาชีพ"),
            ("Ctrl+4 --> ทำให้แถบความต้องการเต็ม"),
            ("Ctrl+5 --> ตั้งอายุของซิมส์ได้ตัวอื่นๆ ได้ เมื่อคลิกซิมส์นั้นๆ"),
            ("Ctrl+6 --> หยุดอายุของซิมส์"),
            ("Crtl+7 --> ทำให้น้ำล้อมรอบบ้าน"),
            ("Crtl+8 --> ซ่อมแซมวัตถุจำนวนมาก")
        ]
        for cmd in commands:
            self.label = tk.Label(self, text=cmd)
            self.label.pack(pady=0, padx=20, anchor='w')

        self.label = tk.Label(self, text="sims1_autocheats v1.0.0 by TOPTUBBY")
        self.label.pack(pady=10, padx=40, anchor='w')

        # เริ่มสร้าง binding สำหรับตรวจจับคีย์ลัด Ctrl+1 ถึง Ctrl+6 และ Ctrl+7
        self.bind_keyboard_shortcuts()

    def bind_keyboard_shortcuts(self):
        commands = {
            "Ctrl+0": "klapaucius",
            "Ctrl+1": "rosebud !;!;!;",
            "Ctrl+2": "moveObjects on",
            "Ctrl+3": "unlockCareerRewards",
            "Ctrl+4": "maxMotives",
            "Ctrl+5": "AgeSimsCheat on",
            "Ctrl+6": "aging on",
            "Ctrl+7": "water_tool",
            "Ctrl+8": "prepare_lot"
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
