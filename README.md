# SoC\_filelist\_duplicated\_check

[shaokaiheng/SoC\_filelist\_duplicated\_check (github.com)](https://github.com/shaokaiheng/SoC_filelist_duplicated_check "shaokaiheng/SoC_filelist_duplicated_check (github.com)")

# Before start

Step1:Set your python env

Step2:Change your filelist file path here in [main.py](http://main.py "main.py")

      file\_path='C:/Users/shaok/PycharmProjects/pythonProject/check\_filelist/filelist.f'

# Example

./example/filelist.f

./example/filelist\_hierarych1.f

./example/filelist\_hierarych2.f

## Hierarchy

filelist.f

   |-filelist\_hierarych1.f

      |-filelist\_hierarych2.f

# Result

```纯文本
Warning:    clk_gat    is duplicated in filelist: C:/Users/shaok/PycharmProjects/pythonProject/check_filelist/filelist_hierarych1.f
   Already used file in :/home/std_cell/verision1/clk_gat.v

Warning:    module_a12    is duplicated in filelist: C:/Users/shaok/PycharmProjects/pythonProject/check_filelist/filelist_hierarych_2.f
   Already used file in :/home/module_a/rtl/new/module_a12.v

Warning:    module_c2    is duplicated in filelist: C:/Users/shaok/PycharmProjects/pythonProject/check_filelist/filelist_hierarych_2.f
   Already used file in :/home/module_b/rtl/new/module_c2.v

Warning:    clk_gat    is duplicated in filelist: C:/Users/shaok/PycharmProjects/pythonProject/check_filelist/filelist_hierarych_2.f
   Already used file in :/home/std_cell/verision1/clk_gat.v


Process finished with exit code 0
```

# Advice

In Project env, Linux env var could be used like

setenv PROJECT\_ROOT=/home/project/username/xxx/

```纯文本
import os
str=os.environ.get('PROJECT_ROOT')
print(str)
```

```纯文本
/home/project/username/xxx/
```

> 📌Flexibility to modify your own scripts
