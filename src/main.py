import time
import io_operations as io
import conf as conf
import statistics_obj as statss

def main():

  print("Type h for help, s to show stats and q to quit.")
  dick = statss.Statistics(io.load_statistics())

  print("current stats:")
  dick.print()
  statistics = []
  
  while True:
    dick.save()
    command = input("Enter a command: ")
    
    if command == "s":
      dick.print()
    elif command == "q":
      dick.save()
      break
    elif command == "":
      print("Usage: <task>")
    elif command == "d":
      task = input("Type task to delete:")
      dick.delete(task)
    elif command == "h":
      print("Type s to show stats,\nd <task> to delete task,\nrst <task> to reset timer on task and\nq to quit.")
      break
    else:
      start_time = time.time()
      
      try:
        while(input("Press Enter to stop: ") != ""):
          pass
        end_time = time.time()
        elapsed_time = end_time - start_time
        dick.add(command, elapsed_time)
        
        print(f"{command} completed in {elapsed_time} seconds.")
      except KeyboardInterrupt:
        print("Task interrupted.")
        break

if __name__ == "__main__":
  main()