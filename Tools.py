import json

def addPaper(json_file: str, name: str, rss: str, link: str) -> None:
  new_item = {name: {"rss":rss, "link":link}}
  
  with open(json_file) as file:
    data = json.load(file)
  
  data.update(new_item)
  with open(json_file, 'w') as file:
    json.dump(data, file)

def removePaper(json_file: str, name: str) -> None:
  