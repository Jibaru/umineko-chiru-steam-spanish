import tkinter as tk
import sys


class Editor:
    def __init__(self, widget: tk.Text) -> None:
        self.widget = widget

    def setContentLines(self, lines: list):
        self.widget.delete("1.0", tk.END)
        for line in lines:
            self.widget.insert(tk.END, line)


class App:
    def __init__(self) -> None:
        self.window = tk.Tk()
        self.window.title("Editor de archivo")
        self.window.geometry("900x500")

    def makeFrame(self) -> tk.Frame:
        frame = tk.Frame(self.window)
        frame.pack()

        return frame

    def makeStringVar(self, lines: list) -> tk.StringVar:
        linesStringVar = tk.StringVar(self.window)
        linesStringVar.set(lines)

        return linesStringVar

    def makeEditor(self, master: tk.Widget) -> Editor:
        widget = tk.Text(master, width=250, height=20)
        widget.pack()

        editor = Editor(widget)

        return editor

    def makeButton(self, master: tk.Widget, callback) -> tk.Button:
        button = tk.Button(
            self.window,
            text="Guardar cambios",
            command=callback
        )
        button.pack(side=tk.TOP)

        return button

    def loop(self) -> None:
        self.window.mainloop()


class FileReader:
    def __init__(self) -> None:
        self.filename = "0.utf"
        self.lines = []

    def read(self):
        with open(self.filename, "r") as f:
            self.lines = f.readlines()

        return self.lines

    def writeFiltered(self, filteredChanges: dict):
        for index in filteredChanges:
            if self.lines[index] != filteredChanges[index]:
                self.lines[index] = filteredChanges[index]

        with open(self.filename, "w") as f:
            f.writelines(self.lines)


def filterOnlyLangEn(lines: list, until: int = 7073, to: int = -1):
    filteredLines = []

    to = len(lines) if to == -1 else to

    for i in range(until, to):
        if "langen^" in lines[i] or "langen!" in lines[i] or "langen@" in lines[i]:
            if (
                "langen!sd\\" == lines[i].strip() or
                "langen!sd@" == lines[i].strip() or
                'langen^"............"^\\' == lines[i].strip() or
                "langen!d300/" == lines[i].strip()
            ):
                continue
            filteredLines.append(str(i) + '===' + lines[i][6:])

    print("Total filtradas:", len(filteredLines))

    return filteredLines


def save(reader: FileReader, filteredList: list, editor: Editor):
    i = 2.0

    elements = {}

    while i <= len(filteredList):
        line = editor.widget.get(str(i - 1.0), str(i))
        vals = line.split('===')
        if len(vals) == 1:
            print(vals, i)
            i += 1
            continue

        index, line = vals

        elements[int(index)] = "langen" + line
        i += 1

    reader.writeFiltered(elements)


def main():
    if len(sys.argv) < 3:
        print("Proporcionar línea desde y hasta")
        return

    until, to = [int(i) for i in sys.argv[1:]]
    print(f"Líneas: {until} - {to}")

    reader = FileReader()
    filteredLines = filterOnlyLangEn(reader.read(), until, to)

    app = App()
    frame = app.makeFrame()

    editor = app.makeEditor(frame)
    editor.setContentLines(filteredLines)

    app.makeButton(frame, lambda: save(reader, filteredLines, editor))
    app.loop()


if __name__ == "__main__":
    main()
