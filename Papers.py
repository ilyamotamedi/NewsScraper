# API for adding, removing, editing papers from JSON data...
import json

def openJSON(json_file):
  with open(json_file) as file:
    return json.load(file)

def overWriteJSON(json_file, data):
  with open(json_file, 'w') as file:
    json.dump(data, file)

def findPaper(json_file: str, name: str) -> dict:
  return openJSON(json_file)[name]

def addPaper(json_file: str, name: str, rss: str, link: str) -> None:
  data = openJSON(json_file)
  data.update({name: {"rss":rss, "link":link}})
  overWriteJSON(json_file, data)

def removePaper(json_file: str, name: str) -> None:
  data = openJSON(json_file)
  del data[name]
  overWriteJSON(json_file, data)

def updatePaper(json_file: str, name: str, rss: str, link: str) -> None:
  removePaper(json_file, name)
  addPaper(json_file, name, rss, link)
