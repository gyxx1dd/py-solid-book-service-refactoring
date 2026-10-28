from abc import ABC, abstractmethod

from app.book import Book


class Command(ABC):
    @abstractmethod
    def execute(self, book: Book, method_type: str) -> None | str:
        pass


class Display(Command):
    def execute(self, book: Book, method_type: str) -> None:
        book.display(method_type)


class Print(Command):
    def execute(self, book: Book, method_type: str) -> None:
        book.print_book(method_type)


class Serialize(Command):
    def execute(self, book: Book, method_type: str) -> None:
        book.serialize(method_type)
