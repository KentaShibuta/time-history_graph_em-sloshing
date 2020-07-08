import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors
import matplotlib.font_manager as fon

#-----preferences-------
del fon.weight_dict['roman']
matplotlib.font_manager._rebuild()

plt.rcParams['font.family'] = 'Times New Roman' #全体のフォントを設定
plt.rcParams["mathtext.fontset"] = "stix" # これを入れておくと，斜体にするときれいになる．

plt.figure(figsize=(12,6))

plt.rcParams["font.size"] = 16

file_name = "result_data/20200606_cul1_53_interface.csv"
file_name_2 = "result_data/20200614_cul3_54_interface.csv"
file_name_3 = "result_data/20200614_cul2_53_interface.csv"
file_name_4 = "result_data/20200614_cul1_53_interface.csv"

num_lines = 0
num_lines =len(open(file_name).readlines())
print(num_lines)

# 1 file setting
df = pd.read_csv(file_name, header=None)
df_1 = pd.DataFrame(df)
df_1.columns = ['time', 'real_left', 'real_right', 'left', 'right']
print(df_1)

# 2 file setting
df_2 = pd.read_csv(file_name_2, header=None)
df_2 = pd.DataFrame(df_2)
df_2.columns = ['time', 'real_left', 'real_right', 'left', 'right']
print(df_2)

# 3 file setting
df_3 = pd.read_csv(file_name_3, header=None)
df_3 = pd.DataFrame(df_3)
df_3.columns = ['time', 'real_left', 'real_right', 'left', 'right']
print(df_3)

# 4 file setting
df_4 = pd.read_csv(file_name_4, header=None)
df_4 = pd.DataFrame(df_4)
df_4.columns = ['time', 'real_left', 'real_right', 'left', 'right']
print(df_4)

plt.xlabel('time [s]')
plt.ylabel('Interface_hight [m] (on the right wall)')

#gla_1
plt.plot(df_1['time'], df_1['right'], label = "Bx=0 T", linestyle = "dotted")
plt.plot(df_2['time'], df_2['right'], label = "Bx=0.01 T", linestyle = "dashed")
plt.plot(df_3['time'], df_3['right'], label = "Bx=0.02 T", linestyle = "dashdot")
plt.plot(df_4['time'], df_4['right'], label = "Bx=0.03 T", linestyle = "solid")

plt.gca().yaxis.set_tick_params(which='both', direction='in',bottom=True, top=True, left=True, right=True)
plt.gca().xaxis.set_tick_params(which='both', direction='in',bottom=True, top=True, left=True, right=True)
plt.xlim(15, 50)
plt.ylim(-0.075, 0.15)

plt.legend(bbox_to_anchor=(1, 1), loc='upper right', borderaxespad=0.5,labelspacing=0.1,fontsize=14)

#plt.savefig("./fig.png", format = 'png', dpi=1000)
plt.savefig("./displament_right-wall.png",format = 'png')
plt.show()