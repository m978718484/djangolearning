#coding=utf-8
import xlrd,pyExcelerator
import os
import sqlite3


path='in'#文件夹名
db_path = 'test.db'


def print_xls(path,leave_date):
    data = xlrd.open_workbook(path)   
    table=data.sheets()[0]#打开excel的第几个sheet
    start_point = []
    end_point = []
     
    for r in xrange(table.nrows):
        for c in xrange(table.ncols):
            value = table.cell(r,c).value
            if value == u'下车人数合计':
                start_point.append((r,c))
            if value ==u'上车人数合计':
                end_point.append((r,c))
    #print start_point
    #print end_point        
    start_length = len(start_point)
    end_length = len(end_point)
    if start_length != end_length:
        print 'error format excel'
    else:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        train = ''
        ws_r_index = 1
        ws_r_index1 = 1
        for i in range(start_length):
            for r in range(start_point[i][0]+2,end_point[i][0]):
                ws_c_index = 0
                train = table.cell(start_point[i][0]-1,0).value.encode('utf-8') 
                train = train.split()[0]          
                ws_r_index += 1

            for r_up in range(end_point[i][1]+2,start_point[i][1]):
                #站点
                station = table.cell(start_point[i][0],r_up).value
                #开车时间
                leaved_time = table.cell(start_point[i][0]+1,r_up).value
                leaved_time = leaved_time if leaved_time is not None and leaved_time != '' else 'N/A'
                #上车人数
                up_man = table.cell(end_point[i][0],r_up).value
                up_man = up_man if up_man is not None and up_man != '' else 0
                ws_r_index1 += 1

                cursor.execute("insert into railway_passenger_flow_forecast values (?,?,?,?,?,?,?)",(leave_date,train,station,leaved_time,'',up_man,''))

        ws_r_index = 1
        for i in range(start_length):
            for r in range(start_point[i][0]+2,end_point[i][0]):
                ws_c_index = 0
                #车次
                train = table.cell(start_point[i][0]-1,0).value.encode('utf-8')
                train = train.split()[0]
                #下车站点
                station = table.cell(r,0).value
                #到站时间
                arrived_time = table.cell(r,1).value
                arrived_time = arrived_time if arrived_time is not None and arrived_time != '' else 'N/A'
                #下车人数
                down_man = table.cell(r,start_point[i][1]).value
                down_man = down_man if down_man is not None and down_man != '' else 0
               
                ws_r_index += 1
                cursor.execute("insert into railway_passenger_flow_forecast values (?,?,?,?,?,?,?)",(leave_date,train,station,'',arrived_time,'',down_man))

        conn.commit()
        cursor.close()
        conn.close()    
                         
if __name__=='__main__':
    if not os.path.exists(db_path):
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute('CREATE TABLE "railway_passenger_flow_forecast" ("leave_date" VARCHAR(20), "train" VARCHAR(20), "station" VARCHAR(20), "leave_time" VARCHAR(10), "arrived_time" VARCHAR(10), "up_man" INTEGER, "down_man" INTEGER)')
        conn.commit()
        cursor.close()
        conn.close()

    for root, dirs, files in os.walk( path ):
        for fn in files:
            print_xls( '%s\\%s'%(root,fn),fn.replace('.xls','') )
