# Target Interface
class LibrarySystem:
    def load_resources(self):
        pass

    def use_resources(self):
        pass


# Legacy System
class LegacyArchive:
    def fetch_data(self):
        print("[LegacyArchive] Fetching archive data...")

    def display_data(self):
        print("[LegacyArchive] Displaying archive data...")


# Adapter
class ArchiveAdapter(LibrarySystem):
    def __init__(self, legacy_archive):
        self.legacy_archive = legacy_archive

    def load_resources(self):
        self.legacy_archive.fetch_data()

    def use_resources(self):
        self.legacy_archive.display_data()


# Client
class UniversityLibrary:
    def __init__(self, system):
        self.system = system

    def operate(self):
        print("[Library] Loading resources...")
        self.system.load_resources()

        print("[Library] Using resources...")
        self.system.use_resources()


# Run
if __name__ == "__main__":
    old_archive = LegacyArchive()
    adapter = ArchiveAdapter(old_archive)
    library = UniversityLibrary(adapter)

    library.operate()