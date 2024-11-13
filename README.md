This is the latest version of the website implementation and deployment of CUHK Advanced Wireless System Groups.

Last updated on September 5, 2024.

To modify and update this website, it is recommended to clone all content locally and modify and update it locally on github.

There are many old versions of md type files in this folder that are outdated and will not be used. At present, the content about research and fite is directly integrated into an html text, and does not share the common js format with others.

It should also be noted that the content of the "htdocs" folder updated on the ie server is compiled differently from the way it is on this repository. The content on htdocs is almost directly run by a separate html page, and the maintainer can further view and compare it on the ie server. But in general, the content is written in the same way.

When running and testing this website locally, the following instructions are appropriate: git pull origin master; bundle exec jekyll serve. It is also necessary to run the backend script app.py, because some functions of this website require network port response and listening to use.
