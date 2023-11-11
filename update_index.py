# %%
import os

from pathlib import Path
import glob


# %%
def generate_tree(path, html=""):
    for dir in os.listdir("figs"):
        html += f"<h3>figs/{dir}</h3>"
        html += "<ul>"
        files = glob.glob(os.path.join("figs", dir) + '/*')
        files = sorted(files, key=os.path.getctime)
        for file in files:
            html += f'<li><a href="{file}">{os.path.basename(file)}</a></li>'
        html += "</ul>"

    return html


# %%
with open("index.html", "w") as f:
    f.write(generate_tree("."))
# %%
