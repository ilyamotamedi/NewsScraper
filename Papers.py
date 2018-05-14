# API for adding, removing, editing papers from JSON data...
import json

def findPaper(json_file: str, name: str) -> dict:
  with open(json_file) as file:
    data = json.load(file)
  return data[name]

def addPaper(json_file: str, name: str, rss: str, link: str) -> None:
  new_item = {name: {"rss":rss, "link":link}}
  
  with open(json_file) as file:
    data = json.load(file)
  
  data.update(new_item)
  with open(json_file, 'w') as file:
    json.dump(data, file)

def removePaper(json_file: str, name: str) -> None:
  with open(json_file) as file:
    data = json.load(file)

  del data[name]
  with open(json_file, 'w') as file:
    json.dump(data, file)

def updatePaper(json_file: str, name: str, rss: str, link: str) -> None:
  removePaper(json_file, name)
  addPaper(json_file, name, rss, link)
