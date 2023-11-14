# script flow:
# 1.open filelist read lines
# 2.delete blank lines,Comment line
# 3.if line is -f xxx .f ,Iterate 1,2,3
# 4.else if line is .v file && not in the list ,filename into a list
#                               else  print 'Warning' & the filelist dir
def extract_between_slash_and_dot_v(input_string):
    dot_v_index = input_string.find('.v')

    if dot_v_index != -1:
        # 从找到的索引 dot_v_index 往前找到最近的一个 '/'
        slash_index = input_string.rfind('/', 0, dot_v_index)

        if slash_index != -1:
            result = input_string[slash_index + 1:dot_v_index]
            return result

    return None

module_lst_glb=[]
module_dir_glb=[]

def iterate_filelist_check(file_path):
    global module_lst_glb,module_dir_glb
    current_file_path = file_path
    with open(file_path, 'r') as file:
        lines = file.readlines()
    non_blank_lines = [line.strip() for line in lines if line.strip() and not line.strip().startswith("//")]
    for l in  non_blank_lines:
        if(l.endswith('.f')):
            new_file_path = l.replace('-f','').replace(' ','')
            iterate_filelist_check(new_file_path)
        elif(l.endswith('.v') or l.endswith('.sv')):
            module_name = extract_between_slash_and_dot_v(l)
            if module_name not in module_lst_glb:
                module_lst_glb.append(module_name)
                module_dir_glb.append(l)
            elif(l not in module_dir_glb):
                print('Warning:    '+module_name+'    is duplicated in filelist: '+current_file_path)
                search_pattern=module_name+'.v'
                for item in module_dir_glb:
                    if item.endswith(search_pattern):
                        print('\t Already used file in :'+item+'\n')


