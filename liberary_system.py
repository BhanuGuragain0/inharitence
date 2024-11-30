from time import sleep
from colorama import Fore, Style, init

# Initialize colorama for colored output
init(autoreset=True)

class LibraryMember:
    def __init__(self, name: str, student_id: str, section: str):
        self.name = name
        self.student_id = student_id
        self.section = section
        self.borrowed_books = []

    def manage_book(self, book_name: str, action: str):
        """
        Manage books (borrow/return) using a single method.
        
        Args:
            book_name (str): Name of the book.
            action (str): 'borrow' or 'return'.
        """
        if action == "borrow":
            self.borrowed_books.append(book_name)
            self._print_action(f"borrowed '{book_name}'", Fore.GREEN)
        elif action == "return":
            if book_name in self.borrowed_books:
                self.borrowed_books.remove(book_name)
                self._print_action(f"returned '{book_name}'", Fore.BLUE)
            else:
                self._print_action(f"has not borrowed '{book_name}'", Fore.RED, error=True)
        self._loading_animation(action.capitalize())

    def _print_action(self, action_message, color, error=False):
        """Print action message with the given color."""
        icon = "❌" if error else "✅" if "returned" in action_message else "📚"
        print(f"{color}\n{icon} {self.name} (ID: {self.student_id}, Section: {self.section}) {action_message}." + Style.RESET_ALL)

    @staticmethod
    def _loading_animation(action):
        """Display a loading animation."""
        print(Fore.YELLOW + f"{action} in progress...", end="")
        for _ in range(3):
            sleep(0.5)
            print(Fore.YELLOW + ".", end="")
        print("\n" + Fore.GREEN + f"{action} completed!" + Style.RESET_ALL)


class StudentMember(LibraryMember):
    def access_study_room(self):
        """Provide access to the study room."""
        print(Fore.MAGENTA + f"\n📖 Student {self.name} (ID: {self.student_id}, Section: {self.section}) is accessing the study room." + Style.RESET_ALL)
        self._loading_animation("Study room access")


# Example usage
if __name__ == "__main__":
    subjects = [
        "Programming and Algorithms",
        "Practical Pen-Testing",
        "Skills Development",
        "Programming Foundations",
        "Platforms and Operating Systems",
        "Digital Forensic Fundamentals",
        "Computer System & Networks",
        "Legal and Ethical Foundations in Cyber Security",
        "Introduction to Web Development and Database Systems",
        "The Security Professional",
        "Creative Thinking for Business",
        "Foundations of Cyber Security",
    ]

    print(Fore.LIGHTYELLOW_EX + "=== Generic Library Member Interaction ===" + Style.RESET_ALL)
    generic_member = LibraryMember("Aashish Panthi", "230364", "E35B")
    generic_member.manage_book(subjects[0], "borrow")
    generic_member.manage_book(subjects[0], "return")
    generic_member.manage_book("Nonexistent Subject", "return")

    print(Fore.LIGHTCYAN_EX + "\n=== Student Member Interaction ===" + Style.RESET_ALL)
    student_member = StudentMember("Bhanu Guragain", "230404", "E35B")
    student_member.manage_book(subjects[1], "borrow")
    student_member.manage_book(subjects[2], "borrow")
    student_member.manage_book(subjects[1], "return")
    student_member.access_study_room()
