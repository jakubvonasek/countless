import conf

def parse_data(data):
  dictionary = {}
  lines = data.split('\n')
  for line in lines:
    if line.strip() != '':
      key, value = line.split(',')
      dictionary[key.strip()] = int(value.strip())
  return dictionary
  
def load_statistics():
  file_path = conf.datafile
  try:
    with open(file_path, 'r') as file:
      data = file.read()
      dick = parse_data(data)
      return dick
  except FileNotFoundError:
    print(f"Datafile '{file_path}' not found.")
    return None
  except IOError:
    print(f"Error reading file '{file_path}'.")
    return None
  
def save_statistics(text):
  file_path = conf.datafile
  try:
    with open(file_path, 'w') as file:
      file.write(text)
      # print(f"Data saved to file: '{file_path}'.")
  except FileNotFoundError:
    print(f"Datafile '{file_path}' not found.")
    return None
  except IOError:
    print(f"Error reading file '{file_path}'.")
    return None