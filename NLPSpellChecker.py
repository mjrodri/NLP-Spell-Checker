import re
import tkinter as tk
from tkinter.scrolledtext import ScrolledText

import nltk
from nltk.corpus import words
 
nltk.download("words")

class SpellingChecker():

    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("800x600")
        
        self.text = ScrolledText(self.root, font=("Arial", 14))
        self.text.bind("<KeyRelease>", self.check)  # Fix: added closing angle bracket
        self.text.pack()
        
        self.old_spaces = 0
        
        self.root.mainloop()
        
    def check(self, event):
        content = self.text.get("1.0", tk.END)  # Fix: changed "1,0" to "1.0"
        space_count = content.count(" ") 
        
        for tag in self.text.tag_names():
            self.text.tag_delete(tag)
            
        if space_count != self.old_spaces:  
            self.old_spaces = space_count
            for word in content.split(" "):
                if re.sub(r"[^\w]", "", word.lower()) not in words.words():
                    position = content.find(word)
                    end_position = position + len(word)
                    self.text.tag_add(word, f"1.{position}", f"1.{end_position}")  # Fix: changed add to tag_add
                    self.text.tag_config(word, foreground="red")                  
                
SpellingChecker()
