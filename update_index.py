# %%
import glob
import os

from bs4 import BeautifulSoup as bs


# %%
def generate_tree(path, html=""):
    for dir in os.listdir("figs"):
        html += f"<h3>figs/{dir}</h3>"
        html += "<ul>"
        section_path = os.path.join("figs", dir)
        for year in os.listdir(section_path):
            html += f"<li><b>{year}</b><ul>"
            year_path = os.path.join(section_path, year)
            files = glob.glob(year_path + "/*")
            for file in sorted(files):
                html += f'<li><a href="{file}">{os.path.basename(file)}</a></li>'
            html += "</li></ul>"
        html += "</ul>"

    return html


soup = bs(generate_tree("."))
prettyHTML = soup.prettify()


with open("index.html", "w") as f:
    f.write(prettyHTML)

# %%
