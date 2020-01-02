# -*- coding: utf-8 -*-
"""

"""
import pandas as pd

def load_excel(path, sheets = 2): 
    '''
    当Excel表有多个sheet时的处理.
    
    path: string类, 给出文件路径名
    sheets: int类, 给出sheet的个数
    
    返回 DataFrame 类
    
    PS: 提供的数据中非第一个sheet是没有column名的
    '''
    if sheets == 1:
        file = pd.read_excel(path)
    else:
        file = pd.read_excel(path, sheet_name = None, header = None) # 读取所有sheet
        file = pd.concat(file) # 拼接
        file.columns = list(file.iloc[0]) # 设定好 columns
        file = file.drop(index=file.index[0])      
    return file

def time_order(path_r, path_s, sheets=2):
    '''
    把每个参数从表中摘出来, 并且按照时间排好顺序
    
    contribution from 杜智辉
    path_r: string类 文件读取路径
    path_s: string类 文件存放路径
    sheets: int类 给出sheet的个数
    
    无返回
    '''
    df = load_excel(path_r, sheets)
    # 层次化索引
    split_sort = df.set_index(['采集项名称', '业务处理时间']).sort_index(level=['采集项名称', '业务处理时间'])
    
    # 写数据
    writer = pd.ExcelWriter(path_s)
    for value in split_sort.index.levels[0]:
        split_sort.loc[value].reset_index().to_excel(writer, sheet_name=value, index=False)
    writer.save()
    

if __name__ == '__main__':
    #　该程序运行需要很长时间
    path_r = [r'./origin/西昌2#高炉采集数据表_高炉本体(炉顶,炉喉,炉身,炉腹).xlsx',
              r'./origin/西昌2#高炉采集数据表_高炉本体(炉缸1).xlsx',
              r'./origin/西昌2#高炉采集数据表_高炉本体(炉缸2).xlsx',
              r'./origin/西昌2#高炉采集数据表_高炉本体(炉缸3).xlsx',
              r'./origin/西昌2#高炉采集数据表_高炉本体(炉缸4).xlsx',
              r'./origin/西昌2#高炉采集数据表_喷吹系统.xlsx',
              r'./origin/西昌2#高炉采集数据表_上料系统.xlsx',
              r'./origin/西昌2#高炉采集数据表_送风系统.xlsx',
              r'./origin/西昌2#高炉采集数据表_渣铁系统.xlsx',
              r'./origin/上料实绩表.xlsx']
    
    path_s = [r'./report/new西昌2#高炉采集数据表_高炉本体(炉顶,炉喉,炉身,炉腹).xlsx',
              r'./report/new西昌2#高炉采集数据表_高炉本体(炉缸1).xlsx',
              r'./report/new西昌2#高炉采集数据表_高炉本体(炉缸2).xlsx',
              r'./report/new西昌2#高炉采集数据表_高炉本体(炉缸3).xlsx',
              r'./report/new西昌2#高炉采集数据表_高炉本体(炉缸4).xlsx',
              r'./report/new西昌2#高炉采集数据表_喷吹系统.xlsx',
              r'./report/new西昌2#高炉采集数据表_上料系统.xlsx',
              r'./report/new西昌2#高炉采集数据表_送风系统.xlsx',
              r'./report/new西昌2#高炉采集数据表_渣铁系统.xlsx',
              r'./report/new上料实绩表.xlsx']

    for i in range(len(path_r)):
         time_order(path_r[i], path_s[i])

