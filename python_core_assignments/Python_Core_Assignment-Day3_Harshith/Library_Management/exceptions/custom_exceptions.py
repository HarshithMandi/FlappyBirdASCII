class LibraryError(Exception):
    pass


class BookNotFoundError(LibraryError):
    pass


class BookAlreadyBorrowedError(LibraryError):
    pass


class MemberNotFoundError(LibraryError):
    pass


class BookNotBorrowedByMemberError(LibraryError):
    pass


class DataFileNotFoundError(LibraryError):
    pass
