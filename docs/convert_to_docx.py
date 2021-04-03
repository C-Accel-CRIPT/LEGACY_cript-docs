import subprocess
import time
## can't handle svg.


documents = [
    "Collections",
    "Data",
    "Data_Entry",
    "Experiments",
    "Groups",
    "Materials_O",
    "Materials_P",
    "Modules",
    "Polymers",
    "Process",
    "Publications",
    "README",
    "Sample",
    "Users",
    "Version_Control"
]

for doc in documents:
    subprocess.Popen([
        "pandoc",
        "-o",
        fr"C:\Users\nicep\Desktop\docs\{doc}.docx",
        fr"C:\Users\nicep\Desktop\Reseach_Post\Documents\Poly_Dat\cript-docs\docs\data-models\{doc}.md",
        r"--resource-path=C:\Users\nicep\Desktop\Reseach_Post\Documents\Poly_Dat\cript-docs\docs\img"
    ],
        shell=True, env={'PATH': r'C:\Users\nicep\AppData\Local\Pandoc'})

    time.sleep(3) # need to give time for processing
    print(f"completed: {doc}")


print("done")
