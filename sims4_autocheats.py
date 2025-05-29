import tkinter as tk
import threading
import keyboard
import winsound

class theSimsCheatApp(tk.Tk):
    def __init__(self):
        super().__init__()

        # กำหนดขนาดหน้าต่าง
        self.geometry("300x500")
        self.title("The Sims 4 trainer")
        self.iconbitmap('sims4.ico')

        # สร้าง Label แสดงข้อความ
        self.bold_font = ("Arial", 15, "bold")
        self.label = tk.Label(self, text="The Sims 4 auto cheat", font=self.bold_font)
        self.label.pack(pady=0, padx=20, anchor='w')

        self.bold_font = ("Arial", 10, "bold")
        self.label = tk.Label(self, text="สูตรทั่วไป", font=self.bold_font)
        self.label.pack(pady=0, padx=20, anchor='w')
        
        self.label = tk.Label(self, text="เปิด Command Ctrl+Shift+C เพื่อใส่สูตร")
        self.label.pack(pady=0, padx=20, anchor='w')

        # สร้าง Label แสดงคำสั่ง
        commands = [
            ("Ctrl+0 --> เปิดสูตร"),
            ("Ctrl+1 --> ความต้องการเต็ม"),
            ("Ctrl+2 --> ปรับแต่งซิมส์"),
            ("Ctrl+3 --> เพิ่มเงิน 50000"),
            ("Ctrl+4 --> จ่ายบิลล์อัตโนมัติ"),
            ("Ctrl+5 --> ทำให้อยู่ฟรี"),
            ("Ctrl+6 --> เลื่อนขั้นอาชีพ")
        ]
        for cmd in commands:
            self.label = tk.Label(self, text=cmd)
            self.label.pack(pady=0, padx=20, anchor='w')

        # สร้าง Label สำหรับการปรับค่าความสัมพันธ์
        self.bold_font = ("Arial", 10, "bold")
        self.label = tk.Label(self, text="สูตรปรับค่าความสัมพันธ์ ความรัก/สังคม", font=self.bold_font)
        self.label.pack(pady=0, padx=20, anchor='w')

        labels_entries = [
            ("ชื่อซิมส์ นามสกุลซิมส์:", "entry1"),
            ("ชื่อซิมส์เป้าหมาย นามสกุลซิมส์เป้าหมาย:", "entry2")
        ]
        for label_text, entry_name in labels_entries:
            self.label = tk.Label(self, text=label_text)
            self.label.pack(pady=0, padx=40, anchor='w')
            setattr(self, entry_name, tk.Entry(self, width=20))
            getattr(self, entry_name).pack(pady=0, padx=40, anchor='w')

        # สร้าง Label สำหรับคำสั่งการปรับค่าความสัมพันธ์
        commands_relationship = [
            ("Ctrl+7 --> ทำให้ความรักเป็นบวก"),
            ("Ctrl+8 --> ทำให้ความสัมพันธ์เป็นบวก"),
            ("Ctrl+9 --> ทำให้ความสัมพันธ์เป็นลบ"),
            ("Ctrl+. --> ทำให้ความรักเป็นลบ"),
            ("Alt+0 --> ทำให้ความรักกับสัตรเป็นบวก"),
            ("Alt+1 --> ทำให้ความรักกับสัตรเป็นลบ"),
            ("Alt+2 --> รู้จักทุกคน")
        ]
        for cmd in commands_relationship:
            self.label = tk.Label(self, text=cmd)
            self.label.pack(pady=0, padx=20, anchor='w')

        self.label = tk.Label(self, text="sims4_autocheats v1.0.0 by TOPTUBBY")
        self.label.pack(pady=10, padx=40, anchor='w')

        # เริ่มสร้าง binding สำหรับตรวจจับคีย์ลัด Ctrl+1 ถึง Ctrl+6 และ Ctrl+7
        self.bind_keyboard_shortcuts()

    def bind_keyboard_shortcuts(self):
        commands = {
            "Ctrl+0": "testingcheats true",
            "Ctrl+1": "sims.fill_all_commodities",
            "Ctrl+2": "cas.fulleditmode",
            "Ctrl+3": "motherlode",
            "Ctrl+4": "households.autopay_bills",
            "Ctrl+5": "FreeRealEstate on",
            "Ctrl+6": "careers.promote",
            "Ctrl+7": self.friendshipPlus,
            "Ctrl+8": self.romancePlus,
            "Ctrl+9": self.friendshipMinus,
            "Ctrl+.": self.romanceMinus,
            "Alt+0": self.petPlus,
            "Alt+1": self.petMinus,
            "Alt+2": "relationship.introduce_sim_to_all_others"
        }

        for key, cmd in commands.items():
            if callable(cmd):
                keyboard.add_hotkey(key, cmd)
            else:
                keyboard.add_hotkey(key, lambda cmd=cmd: self.auto_type(cmd))

    def friendshipPlus(self):
        self.handle_relationship("100 LTR_Friendship_Main")
    
    def romancePlus(self):
        self.handle_relationship("100 LTR_Romance_Main")

    def friendshipMinus(self):
        self.handle_relationship("-100 LTR_Friendship_Main")

    def romanceMinus(self):
        self.handle_relationship("-100 LTR_Romance_Main")  

    def petPlus(self):
        self.handle_relationship("100 LTR_SimToPet_Friendship_Main")  

    def petMinus(self):
        self.handle_relationship("-100 LTR_SimToPet_Friendship_Main")

    def handle_relationship(self, value):
        # รับข้อความจาก Entry widgets
        text1 = self.entry1.get()
        text2 = self.entry2.get()
        
        # ตรวจสอบว่าไม่มีตัวเลข hotkey ติดมาด้วย
        if any(char.isdigit() for char in text1) or any(char.isdigit() for char in text2):
            return
        
        # ใช้ keyboard ในการพิมพ์ข้อความ
        keyboard.write(f"modifyrelationship {text1} {text2} {value}")

    def auto_type(self, text):
        # ตรวจสอบว่าไม่มีตัวเลข hotkey ติดมาด้วย
        if any(char.isdigit() for char in text):
            return
        
        # ใช้ keyboard ในการพิมพ์ข้อความ
        keyboard.write(text)

if __name__ == "__main__":
    app = theSimsCheatApp()
    app.mainloop()
