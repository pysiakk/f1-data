import glob
import os


# %%
def generate_tree(path, html=""):
    for dir in os.listdir("figs"):
        html += f"<h3>figs/{dir}</h3>"
        html += "<ul>"
        section_path = os.path.join("figs", dir)
        for year in os.listdir(section_path):
            html += "<li><ul>"
            year_path = os.path.join(section_path, year)
            files = glob.glob(year_path + "/*")
            files = sorted(files, key=os.path.getctime)
            for file in files:
                html += f'<li><a href="{file}">{os.path.basename(file)}</a></li>'
            html += "</li></ul>"
        html += "</ul>"

    return html


with open("index.html", "w") as f:
    f.write(generate_tree("."))
