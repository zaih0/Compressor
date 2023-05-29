import os
import heapq

class HuffmanCoding:
    def __init__(self, path):
        self.path = path
        self.heap = []
        self.codes = {}


    class HeapNode:
        def __init__(self, char, freq):
            self.char = char
            self.freq = freq
            self.left = None
            self.right = None


        def __lt__(self, other):
            return self.freq < other.freq

        def __eq__(self, other):
            if (other == None):
                return False
            if(not isnstance(other, HeapNode)):
                return False
            return self.freq == other.freq

    def make_frequency_dict(text):
        frequency = {}
        for character in text:
            if not character in frequency:
                frequency[character] = o
            frequency[character] += 1
        return frequency


    def make_heap(self, frequency):
        for key in frequency:
            node = self.HeapNode(key, frequency[key]
            heapq.heappush(self.heap, node)
    
    def merge_codes(self):
         while(len(self.heap)>1):
         node1 = heapq.heappop(self.heap)
         node2 = heapq.heappop(self.heap)

         merged = self.HeapNode(None, node1.freq + node2.freq)
         merged.left = node1
         merged.right = node2

         heapq.heappush(self.heap, merged)

    def make_codes_helper(self, node, current_code):
        if(node == None):
            return

        if(node.char != None):
            self.codes[node.char] = current_code
        

        self.make_code_helper(node.left, current_code + "0")
        self.make_code_helper(node.left, current_code + "1")

    def make_codes(self):
        root = heapq.heappop(self.heap)
        current_code = ""
        self.make_code_helper(root, current_code)

    def get_encoded_text(self, text):
        #replace character with code and return

    def pad_encoded_text(self, encoded_text):
        #pad encoded text and return

    def get_byte_array(self, padded_encoded_text):
        #convert bits into bytes. Return byte array


    def compress(self):
        filename, file_extension = os.path.splitext(self.path)
        output.path = filename + ".bin"

        with open(self.path, 'r') as file
        open(output_path, 'wb') as output:
            text = file.read()
            text = text.rstrip()

            frequency = make_frequency_dict(text)

            self.make_heap(frequency)
            self.merge_codes()
            self.make_codes()

            encoded_text = get_encoded_text(text)
            padded_encoded_text = pad_encoded_text(encoded_text)

            b = self.get_byte_array(padded_encoded_text)
            output.write(bytes(b))
        print("Compressed")
        return output_path
