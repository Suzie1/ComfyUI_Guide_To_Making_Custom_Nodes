from .nodes.tutorial_nodes import *

NODE_CLASS_MAPPINGS = { 
    "Print Hello World": PrintHelloWorld,
    "Concatenate Hello World": ConcatenateHelloWorld,
    "Hello World Overlay Text": HelloWorld,
    }
    
print("\033[34mComfyUI Tutorial Nodes: \033[92mLoaded\033[0m")
