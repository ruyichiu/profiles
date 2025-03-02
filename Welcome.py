def print_welcome():
    name = input("請輸入你的名字：")
    print(f"""
    ╔═══════════════════════════╗
    ║  歡迎來到 {name} 的GitHub！  ║
    ╚═══════════════════════════╝
    """)

if __name__ == "__main__":
    print_welcome()
