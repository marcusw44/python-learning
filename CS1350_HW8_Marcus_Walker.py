"""
CS1350 - Exception Handling Assignment

1. Exception_Lecture1: practice_3_complete_pattern()
2. Exception_Lecture2: practice_2_custom_exceptions()
3. Exception_Lecture2: practice_3_complete_system()

"""

import os


def practice_3_complete_pattern():
    """
    Practice with try-except-else-finally.
    """
    print("\n" + "=" * 50)
    print("EXERCISE 3: Complete Exception Pattern")
    print("=" * 50)

    # TODO 1: File processor with complete error handling
    def process_file(filename):
        """
        Read a file, process its content, and ensure the file is closed.
        Return processed content or None.
        """
        file = None
        try:
            file = open(filename, "r", encoding="utf-8")
        except FileNotFoundError:
            print(f"File '{filename}' was not found.")
            return None
        except PermissionError:
            print(f"No permission to read '{filename}'.")
            return None
        except Exception as e:
            print(f"Unexpected error opening '{filename}': {e}")
            return None
        else:
            try:
                content = file.read()
                processed_content = content.upper().split()
                print(f"Successfully processed '{filename}'.")
                return processed_content
            except Exception as e:
                print(f"Error processing '{filename}': {e}")
                return None
        finally:
            if file is not None and not file.closed:
                file.close()
                print(f"Closed '{filename}'.")

    # Test with different scenarios
    test_files = ["exists.txt", "missing.txt", "/root/file"]
    for filename in test_files:
        result = process_file(filename)
        print(f"Processing '{filename}': {result}")

    # TODO 2: Resource manager
    class ResourceManager:
        def __init__(self, name):
            self.name = name
            self.resource = None

        def acquire(self):
            """Acquire resource - might fail."""
            if self.resource is not None:
                raise RuntimeError(f"{self.name} is already acquired.")
            if not self.name:
                raise RuntimeError("Resource name cannot be empty.")
            self.resource = f"{self.name} resource"
            print(f"Acquired {self.resource}.")

        def release(self):
            """Release resource - must always happen."""
            if self.resource is not None:
                print(f"Released {self.resource}.")
                self.resource = None

        def use(self):
            """Use resource - only if acquired."""
            if self.resource is None:
                raise RuntimeError(f"{self.name} has not been acquired.")
            print(f"Using {self.resource}.")

    # Test resource management with try-except-else-finally
    rm = ResourceManager("Database")
    try:
        rm.acquire()
        rm.use()
    except RuntimeError as e:
        print(f"Resource error: {e}")
    else:
        print("Resource was used successfully.")
    finally:
        rm.release()


def practice_2_custom_exceptions():
    """
    Practice creating and using custom exceptions.
    """
    print("\n" + "=" * 50)
    print("EXERCISE 5: Custom Exceptions")
    print("=" * 50)

    # TODO 1: Create custom exceptions
    class GameError(Exception):
        """Base class for game exceptions."""
        pass

    class InvalidMoveError(GameError):
        """Invalid game move."""

        def __init__(self, position, reason):
            self.position = position
            self.reason = reason
            super().__init__(f"Invalid move at {position}: {reason}")

    class GameOverError(GameError):
        """Game has ended."""

        def __init__(self, winner):
            self.winner = winner
            if winner:
                message = f"Game is over. Winner: {winner}"
            else:
                message = "Game is over. The game was a draw."
            super().__init__(message)

    # TODO 2: Use custom exceptions
    class TicTacToe:
        def __init__(self):
            self.board = [[" " for _ in range(3)] for _ in range(3)]
            self.current_player = "X"
            self.game_over = False
            self.winner = None

        def make_move(self, row, col):
            if self.game_over:
                raise GameOverError(self.winner)

            if not isinstance(row, int) or not isinstance(col, int):
                raise InvalidMoveError((row, col), "Row and column must be integers.")

            if not (0 <= row < 3 and 0 <= col < 3):
                raise InvalidMoveError((row, col), "Position is out of bounds.")

            if self.board[row][col] != " ":
                raise InvalidMoveError((row, col), "Position is already taken.")

            self.board[row][col] = self.current_player

            # Check rows, columns, and diagonals for a winner.
            lines = (
                self.board
                + [[self.board[r][c] for r in range(3)] for c in range(3)]
                + [[self.board[i][i] for i in range(3)]]
                + [[self.board[i][2 - i] for i in range(3)]]
            )
            for line in lines:
                if line[0] != " " and line[0] == line[1] == line[2]:
                    self.game_over = True
                    self.winner = self.current_player
                    return

            # A full board with no winner is a draw.
            if all(cell != " " for board_row in self.board for cell in board_row):
                self.game_over = True
                self.winner = None
                return

            self.current_player = "O" if self.current_player == "X" else "X"

    # Test the game
    game = TicTacToe()
    test_moves = [
        (0, 0),  # Valid
        (0, 0),  # Already taken
        (5, 5),  # Out of bounds
    ]

    for row, col in test_moves:
        try:
            game.make_move(row, col)
            print(f"Move ({row}, {col}) successful")
        except InvalidMoveError as e:
            print(f"Invalid move: {e}")
        except GameOverError as e:
            print(f"Game over: {e}")


def practice_3_complete_system():
    """
    Build a complete error handling system.
    """
    print("\n" + "=" * 50)
    print("EXERCISE 6: Complete Error Handler")
    print("=" * 50)

    # TODO: Build a file processing system with proper error handling
    class FileProcessor:
        def __init__(self):
            self.processed_files = []
            self.failed_files = []

        def process_file(self, filename):
            """
            Process a single file with complete error handling.
            """
            file = None
            try:
                file = open(filename, "r", encoding="utf-8")
            except FileNotFoundError as e:
                print(f"File not found: {filename} ({e})")
                self.failed_files.append({"filename": filename, "error": str(e)})
                return None
            except PermissionError as e:
                print(f"Permission denied: {filename} ({e})")
                self.failed_files.append({"filename": filename, "error": str(e)})
                return None
            except Exception as e:
                print(f"Unexpected error opening {filename}: {e}")
                self.failed_files.append({"filename": filename, "error": str(e)})
                return None
            else:
                try:
                    content = file.read()
                    # Processing here means successfully reading the file.
                    self.processed_files.append(filename)
                    print(f"Successfully processed: {filename}")
                    return content
                except Exception as e:
                    print(f"Error processing {filename}: {e}")
                    self.failed_files.append({"filename": filename, "error": str(e)})
                    return None
            finally:
                if file is not None and not file.closed:
                    file.close()

        def process_directory(self, directory):
            """
            Process all files in a directory, collecting errors.
            """
            try:
                filenames = os.listdir(directory)
            except (FileNotFoundError, PermissionError, NotADirectoryError) as e:
                self.failed_files.append({"filename": directory, "error": str(e)})
                print(f"Could not access directory '{directory}': {e}")
                return

            for filename in filenames:
                full_path = os.path.join(directory, filename)
                if os.path.isfile(full_path):
                    self.process_file(full_path)

        def get_report(self):
            """
            Return a summary of processing.
            """
            return {
                "processed_count": len(self.processed_files),
                "failed_count": len(self.failed_files),
                "processed_files": self.processed_files.copy(),
                "failed_files": self.failed_files.copy(),
            }

    # Test the processor
    processor = FileProcessor()
    test_files = [
        "valid.txt",
        "missing.txt",
        "/root/restricted.txt",
    ]

    for filename in test_files:
        processor.process_file(filename)

    report = processor.get_report()
    print(f"Report: {report}")


if __name__ == "__main__":
    practice_3_complete_pattern()
    practice_2_custom_exceptions()
    practice_3_complete_system()
