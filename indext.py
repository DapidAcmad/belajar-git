import os
import sys

# Fungsi untuk mencetak teks berwarna di terminal
def print_colored_banner():
    # Menggunakan kode warna ANSI Escape Sequences
    GREEN = "\033[92m"
    CYAN = "\033[96m"
    YELLOW = "\033[93m"
    RESET = "\033[0m"
    BOLD = "\033[1m"

    # Membersihkan layar terminal saat program dijalankan
    os.system('cls' if os.name == 'nt' else 'clear')

    print(f"{GREEN}{BOLD}" + "="*60 + f"{RESET}")
    print(f"{CYAN}{BOLD}          WELCOME TO DAVID AHMAD KURNIAWAN'S REPO!          {RESET}")
    print(f"{GREEN}{BOLD}" + "="*60 + f"{RESET}\n")

    print(f"{YELLOW}Status  :{RESET} Vocational School Student & Software Development Learner")
    print(f"{YELLOW}Stack   :{RESET} Python, C++, HTML, PHP, & Git")
    print(f"{YELLOW}Motto   :{RESET} Code, Commit, Conquer! 🚀\n")

    print(f"{GREEN}" + "-"*60 + f"{RESET}")
    print(f"{CYAN} Terima kasih sudah berkunjung ke repository saya!{RESET}")
    print(f"{GREEN}" + "-"*60 + f"{RESET}\n")

if __name__ == "__main__":
    print_colored_banner()
