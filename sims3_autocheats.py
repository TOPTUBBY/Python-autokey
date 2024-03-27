import tkinter as tk
import threading
import keyboard
import winsound

class theSimsCheatApp(tk.Tk):
    def __init__(self):
        super().__init__()

        # กำหนดขนาดหน้าต่าง
        self.geometry("300x340")
        self.title("The Sims 3 trainer")
        self.iconbitmap('sims3.ico')

        # สร้าง Label แสดงข้อความ
        self.bold_font = ("Arial", 15, "bold")
        self.label = tk.Label(self, text="The Sims 3 auto cheat", font=self.bold_font)
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
            ("Ctrl+2 --> บ้านและที่ดินฟรี"),
            ("Ctrl+3 --> ปลดล็อกเสื้อผ้าในเกม"),
            ("Ctrl+4 --> ทำให้หลอดความต้องการเต็มแบบไม่ลดลงอีก"),
            ("Ctrl+5 --> ทำให้ซิมส์ที่เล่นอยู่ รู้จักซิมส์ทั้งหมู่บ้าน"),
            ("Ctrl+6 --> เลือกอาชีพให้ซิมส์"),
            ("Crtl+7 --> เปลี่ยนนิสัยซิมส์ที่เล่นอยู่"),
            ("Ctrl+8 --> เพิ่มระดับความสัมพันธ์กับซิมส์"),
            ("Ctrl+9 --> รีเซ็ตซิมส์ให้กลับสถานะเริ่มต้น"),
            ("Ctrl+. --> เปิดสูตร")
        ]
        for cmd in commands:
            self.label = tk.Label(self, text=cmd)
            self.label.pack(pady=0, padx=20, anchor='w')

        self.label = tk.Label(self, text="sims3_autocheats v1.0.0 by TOPTUBBY")
        self.label.pack(pady=10, padx=40, anchor='w')

        # เริ่มสร้าง binding สำหรับตรวจจับคีย์ลัด Ctrl+1 ถึง Ctrl+6 และ Ctrl+7
        self.bind_keyboard_shortcuts()

    def bind_keyboard_shortcuts(self):
        commands = {
            "Ctrl+0": "kaching",
            "Ctrl+1": "motherlode",
            "Ctrl+2": "Freerealestate",
            "Ctrl+3": "unlockOutfits on",
            "Ctrl+4": "Make Needs Static",
            "Ctrl+5": "Make Me Know Everyone",
            "Ctrl+6": "Set Career",
            "Ctrl+7": "Modify Traits for Active Sim",
            "Ctrl+8": "Make Friends For Me",
            "Ctrl+9": "resetSim",
            "Ctrl+.": "testingcheatsenabled true"
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
