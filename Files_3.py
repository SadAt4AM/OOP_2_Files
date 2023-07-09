from pprint import pprint

file_list = ["1.txt","2.txt","3.txt"]
file_name = "4.txt"

class Fileread:

    def __init__(self,file_r):
        self.file_r = file_r


    def read_file(self):
        file_dict = {}
        for o_file in self.file_r:
            with open(o_file, 'r', encoding="utf-8") as f:
                text_1 = ''
                count = 0
                for r_file in f:
                    count += 1
                    text_1 += r_file
                file_dict[count] = o_file
        return file_dict


def write_file(dict_t,file_name):
    x = dict_t.items()
    sorted_dict = sorted(x, key=lambda y:y[0])
    z = dict(sorted_dict)
    with open(file_name, 'w', encoding="utf-8") as f:
        for k,v in z.items():
            f.write(v +'\n')
            f.write(str(k) + '\n')
            with open(v, 'r', encoding="utf-8") as file_obj:
                x = file_obj.readlines()
                text = ""
                for final_x in x:
                    text += final_x
            f.write(text + '\n')


text1 = Fileread(file_list)
x = text1.read_file()
pprint(x)
write_file(x,file_name)
