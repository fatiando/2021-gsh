"""
Use livereload to serve the talk slides for local inspection.
"""
from livereload import Server


server = Server()
server.watch("slide-contents.md")
server.watch("index.html")
server.watch("css")
server.watch("assets")
server.serve(root=".", port="8008", host="localhost", open_url_delay=1)
