import PySimpleGUI as sg
from zipfile import ZipFile

# user zip file



#  the Gui
sg.theme("DarkSlateBlue4")

layout = [
    [sg.Text("FILE PATH", size=(15,1)), sg.InputText(key="FILE PATH"), sg.FileBrowse(file_types=(("Zip Files", "*.zip"),))],
    [sg.Button('Extract'),sg.Exit()]
]

window = sg.Window('Mazen for Extracting files',layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "Exit":
        break
    elif event == "Extract":
        fileName = values["FILE PATH"].strip('"')

        with ZipFile(fileName, "r") as Zip:
            extracted_files = Zip.namelist()
            sg.popup("Files extracted:\n" + "\n".join(extracted_files))

            Zip.extractall()
        sg.popup("Extraction completed")
    else:
        sg.popup("please enter the file path")




window.close()
