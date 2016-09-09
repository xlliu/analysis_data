#!/usr/bin/env python
# -*-  coding:utf-8 -*-

"""
@version: 1.0.0
@author: xlliu
@contact: liu.xuelong@163.com
@site: https://github.com/xlliu
@software: PyCharm
@file: value_summany.py
@time: 2016/8/18 11:16
"""
import pandas as pd
from com.analysis.utils.err import ErrorCode
from com.analysis.core.base import Base

class VSummany(Base):

   def do_(self, *args):
       cid = args[1]
       sql = "select type from data_theme where cid = %s"
       sql11 = "select cid, title from data_theme where type = %s"
       sql2 = "select cid from data_theme where type = %s"
       sql3 = "select uuid,time from data_index_default where cid = %s"
       sql4 = "select %s from %s "
       sql5 = "select num_var, var from %s where cid=%s"
       
       data_result = pd.DataFrame()

       sql = sql % "'"+cid+"'"
       type_1 = pd.read_sql_query(sql, self._stata_engine_data_index).fillna(0).ix[0,0]
       
#       if type_1:
#           sql11 = sql11 % "'"+type_1+"'"
#           cids = pd.read_sql_query(sql11, self._stata_engine_data_index)
#           
#           index = []
#           for i,v in cids.iterrows():
#               data_result_chunk = pd.DataFrame()
#               sql3all_t = sql3 % "'"+v["cid"]+"'"
#               sql3all_t_result = pd.read_sql_query(sql3all_t, self._stata_engine_data_index)
#               for i, ir in sql3all_t_result.iterrows():
#                   sql4all_t = sql4 % tuple([cid ,"`"+ir["uuid"]+"`"])
#                   data_result_c = pd.read_sql_query(sql4all_t, self._stata_engine_data_base).rename(columns={cid: ir["time"]})
#                   data_result_chunk = pd.merge(data_result_chunk, data_result_c, how="right", left_index="index", right_index="index")
#               
#               data_result_chunk = data_result_chunk.apply(lambda x: x.value_counts(), axis=0)
#               index.extend([v["title"]]*len(data_result_chunk.index.to_series()))
#               #index = pd.MultiIndex.from_arrays([mindex, mindex2],names=["题目","答案"])
#               data_result= pd.concat([data_result, data_result_chunk], ignore_index=True)
#           ir = ["_".join([i,r]) for i,r in zip(index,[u"否", u"是"]*(len(index)/2))]
#           # ir = "_".join(zip(index,["否", "是"]*(len(index)/2)))
#           dindex = dict(zip(list(data_result.index),ir))
#           data_result = data_result.rename(index=dindex)
#           ds = data_result.sum(axis=0)
#           ds.name="合计"
#           data_result = data_result.append(ds)
#                  
#           return ErrorCode.SUCCESS, data_result.fillna(0).to_json()
#       else:
#           sql3all = sql3 % "'"+cid+"'"
#           index_result = pd.read_sql_query(sql3all, self._stata_engine_data_index)
#           sql5all = ""
#           for i, ir in index_result.iterrows():
#               sql4all = sql4 % tuple([cid ,"`"+ir["uuid"]+"`"])
#               sql5all = sql5 % tuple(["`"+ir["uuid"]+"`", "'"+cid.lower()+"lab'"])
#               
#               # updata column to time
#               data_result_c = pd.read_sql_query(sql4all, self._stata_engine_data_base).rename(columns={cid: ir["time"]})
#               data_result = pd.merge(data_result, data_result_c, how="right", left_index="index", right_index="index")
#               # data_result_with = data_result.T.sum(axis=1).T
#           data_result= data_result.apply(lambda x: x.value_counts(), axis=0)
#           
#           data_result_i = pd.read_sql_query(sql5all, self._stata_engine_data_options)
#           num_value2value = {}
#           num_value_list = []
#           value_list = []
#           for i, ir in data_result_i.iterrows():
#               num_value2value[ir["num_var"]] = ir["var"]
#               value_list.append(ir["var"])
#               num_value_list.append(ir["num_var"])
#           # data_result = data_result.T.rename(columns=num_value2value).T
#           dr1 = data_result.reindex(num_value_list)
#           dr2 = dr1.rename(index=num_value2value)
#           ds = dr2.sum(axis=0)
#           ds.name="合计"
#           data_result = dr2.append(ds)
#           
#           #return ErrorCode.SUCCESS, self.generator_view(data_result.fillna(0))
#           return ErrorCode.SUCCESS, data_result.fillna(0).to_json()
 
       try:
           sql3all = sql3 % "'"+cid+"'"
           index_result = pd.read_sql_query(sql3all, self._stata_engine_data_index)
           sql5all = ""
           for i, ir in index_result.iterrows():
               sql4all = sql4 % tuple([cid ,"`"+ir["uuid"]+"`"])
               sql5all = sql5 % tuple(["`"+ir["uuid"]+"`", "'"+cid.lower()+"lab'"])
               
               # updata column to time
               data_result_c = pd.read_sql_query(sql4all, self._stata_engine_data_base).rename(columns={cid: ir["time"]})
               data_result = pd.merge(data_result, data_result_c, how="right", left_index="index", right_index="index")
               # data_result_with = data_result.T.sum(axis=1).T
           data_result= data_result.apply(lambda x: x.value_counts(), axis=0)
           
           data_result_i = pd.read_sql_query(sql5all, self._stata_engine_data_options)
           num_value2value = {}
           num_value_list = []
           value_list = []
           for i, ir in data_result_i.iterrows():
               num_value2value[ir["num_var"]] = ir["var"]
               value_list.append(ir["var"])
               num_value_list.append(ir["num_var"])
           # data_result = data_result.T.rename(columns=num_value2value).T
           dr1 = data_result.reindex(num_value_list)
           dr2 = dr1.rename(index=num_value2value)
           ds = dr2.sum(axis=0)
           ds.name="合计"
           data_result = dr2.append(ds)
           
           #return ErrorCode.SUCCESS, self.generator_view(data_result.fillna(0))
           return ErrorCode.SUCCESS, data_result.fillna(0).to_json()
       except:
           sql11 = sql11 % "'"+type_1+"'"
           cids = pd.read_sql_query(sql11, self._stata_engine_data_index)

           index = []
           for i,v in cids.iterrows():
               data_result_chunk = pd.DataFrame()
               sql3all_t = sql3 % "'"+v["cid"]+"'"
               sql3all_t_result = pd.read_sql_query(sql3all_t, self._stata_engine_data_index)
               for i, ir in sql3all_t_result.iterrows():
                   sql4all_t = sql4 % tuple([cid ,"`"+ir["uuid"]+"`"])
                   data_result_c = pd.read_sql_query(sql4all_t, self._stata_engine_data_base).rename(columns={cid: ir["time"]})
                   data_result_chunk = pd.merge(data_result_chunk, data_result_c, how="right", left_index="index", right_index="index")

               data_result_chunk = data_result_chunk.apply(lambda x: x.value_counts(), axis=0)
               index.extend([v["title"]]*len(data_result_chunk.index.to_series()))
               #index = pd.MultiIndex.from_arrays([mindex, mindex2],names=["题目","答案"])
               data_result= pd.concat([data_result, data_result_chunk], ignore_index=True)
           ir = ["_".join([i,r]) for i,r in zip(index,[u"否", u"是"]*(len(index)/2))]
           # ir = "_".join(zip(index,["否", "是"]*(len(index)/2)))
           dindex = dict(zip(list(data_result.index),ir))
           data_result = data_result.rename(index=dindex)
           ds = data_result.sum(axis=0)
           ds.name="合计"
           data_result = data_result.append(ds)

           return ErrorCode.SUCCESS, data_result.fillna(0).to_json()
